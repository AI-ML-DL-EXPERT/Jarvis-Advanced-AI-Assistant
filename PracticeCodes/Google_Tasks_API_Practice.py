# import pickle
#
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# import pickle
#
# from pprint import pprint
#
# CLIENT_SECRET_FILE = "client_secret_tasks_api.json"
#
# scopes = ["https://www.googleapis.com/auth/tasks"]
#
# flow = InstalledAppFlow.from_client_secrets_file(
#     CLIENT_SECRET_FILE, scopes=scopes
# )
#
# # Initial authorization (if refresh token is not available or needs refresh)
# try:
#     with open("token.pickle", "rb") as token:
#         credentials = pickle.load(token)
#     credentials.refresh(Request())  # Refresh token if it exists
# except (FileNotFoundError, pickle.PickleError):
#     credentials = flow.run_local_server(port=0)
#     with open("token.pickle", "wb") as token:
#         pickle.dump(credentials, token)
#
# tasks = build("tasks", "v1", credentials=credentials)
#
# # Print task lists
# # pprint(tasks.tasklists().list().execute())
# # pprint(tasks.tasks().list(tasklist= "N0RQVFJXVXNHY3NmSkdERg").execute())
#
#
# # Creating the Dictionary of all the task lists
# tasksListsTitleID_Dict = {}
#
# # Fetching all the task lists
# for tasklist in tasks.tasklists().list().execute()["items"]:
#     try:
#         tasksListsTitleID_Dict[tasklist["title"]] = tasklist["id"]
#
#     except KeyError:
#         print(tasklist["title"] + "is not a valid task list title or it is this tasklist is already present in the "
#                                   "tasks list")
#
# pprint(tasksListsTitleID_Dict)
#
# # taskListName = input("Task list name: ")
# # # Creating New Task List
# # new_task_list = {
# #     "title": taskListName
# # }
# #
# #
# # # Checking if the task list is already present in the tasks list
# # if taskListName in tasksListsTitleID_Dict.keys():
# #     print(taskListName + " is already present in the tasks list")
# #
# # else:
# #     inserted_task_list = tasks.tasklists().insert(body=new_task_list).execute()
# #     pprint(inserted_task_list)
#
# # print(tasks.task lists().get(tasklist= "Jarvis AI Assistant Tasks"))
#
#
# # Creating the Dictionary of all the tasks of a task lists
# tasksTitleID_Dict = {}
#
# # Fetching all the task lists
# for tasklist in tasks.tasks().list(tasklist=tasksListsTitleID_Dict["Jarvis AI Assistant Tasks"]).execute()["items"]:
#     try:
#         tasksTitleID_Dict[tasklist["title"]] = tasklist["id"]
#
#     except KeyError:
#         print(tasklist["title"] + "is not a valid task list title or it is this tasklist is already present in the "
#                                   "tasks list")
#
# pprint(tasksTitleID_Dict)
#
# taskTitleName = input("Task Title: ")
# # Creating New Task List
# new_task_list = {
#     "title": taskTitleName
# }
#
#
# # Checking if the task list is already present in the task list
# if taskTitleName in tasksListsTitleID_Dict.keys():
#     print(taskTitleName + "is already present in the tasks list")
#
# else: inserted_task_title = tasks.tasks().insert(body=new_task_list, tasklist= tasksListsTitleID_Dict["Jarvis AI
# Assistant Tasks"]).execute() pprint(inserted_task_title)
#
#
# # Inserting Tasks to an existing tasks list
#
# newTaskTitle = input("Enter the Task Title: ")
# newTask = {
#     "title": newTaskTitle,
# }
#
#  Optimizing it
# ----------------------------------------------------------------------------------------------------------------------
#


from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
from pprint import pprint


def get_credentials(client_secret_file="client_secret_tasks_api.json",
                    scopes=["https://www.googleapis.com/auth/tasks"]):
    """
  Retrieves credentials from a pickle file or prompts for authorization.

  Args:
      client_secret_file (str, optional): Path to the client secret file. Default to "client_secret_tasks_api.json".
      scopes (list, optional): List of OAuth scopes required for access. Default to ["https://www.googleapis.com/auth/tasks"].

  Returns:
      object: Google API Client credentials object.
  """

    try:
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)
        credentials.refresh(Request())
        return credentials
    except (FileNotFoundError, pickle.PickleError):
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secret_file, scopes=scopes
        )
        credentials = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)
        return credentials


def get_service(credentials):
    """
  Builds the Tasks service object using the provided credentials.

  Args:
      credentials (object): Google API Client credentials object.

  Returns:
      object: Tasks service object.
  """

    return build("tasks", "v1", credentials=credentials)


def get_task_lists(service):
    """
  Retrieves a list of task lists and their IDs.

  Args:
      service (object): Tasks service object.

  Returns:
      dict: Dictionary mapping task list titles to their IDs.
  """

    task_lists = service.tasklists().list().execute()["items"]
    tasks_dict = {task_list["title"]: task_list["id"] for task_list in task_lists}
    return tasks_dict


def add_new_tasklist(service, title, **existing_tasklists):
    """
  Creates a new task list with the specified title.

  Args:
      service (object): Tasks service object.
      title (str): Title for the new task list.

  Returns:
      dict: Information about the created task list.
  """

    try:
        if title in existing_tasklists.keys():
            print(f"Task list with title {title} already exists.")
            return None
        else:
            new_task_list = {"title": title}
            inserted_task_list = service.tasklists().insert(body=new_task_list).execute()
            return inserted_task_list

    except Exception as e:
        print(e)


def add_new_task(service, tasklist_id, title, due_date=None):
    """
  Adds a new task to the specified task list.

  Args:
      service (object): Tasks service object.
      tasklist_id (str): ID of the target task list.
      title (str): Title for the new task.
      due_date (str, optional): Due date in ISO 8601 format (YYYY-MM-DDTHH:mm:ss.sssZ). Defaults to None.

  Returns:
      dict: Information about the created task.
  """

    new_task = {"title": title}
    if due_date:
        new_task["due"] = due_date
    inserted_task = service.tasks().insert(tasklist=tasklist_id, body=new_task).execute()
    return inserted_task


def get_tasks(service, tasklist_id):
    """
  Retrieves all tasks within the specified task list.

  Args:
      service (object): Tasks service object.
      tasklist_id (str): ID of the target task list.

  Returns:
      list: List of dictionaries containing task information.
  """

    tasks = service.tasks().list(tasklist=tasklist_id).execute()["items"]
    return tasks


def task_mark_as_done(service, task_id, tasklist_id):
    """
  Marks the specified task as completed.

  Args:
      service (object): Tasks service object.
      Task_id (str): ID of the task to mark done.
  """

    task_patch = {"status": "completed"}
    service.tasks().patch(task=task_id, body=task_patch, tasklist=tasklist_id).execute()
    print(f"Task reverted: {task_id}")


def task_mark_as_not_done(service, task_id, tasklist_id):
    """
  Marks the specified task as not completed (needsAction).

  Args:
      service (object): Tasks service object.
      task_id (str): ID of the task to mark as not done.
  """

    task_patch = {"status": "uncompleted"}
    service.tasks().patch(task=task_id, body=task_patch, tasklist=tasklist_id).execute()


def show_tasks(service, tasklist_id):
    """
  Prints the titles of all tasks within the specified task list.

  Args:
      service (object): Tasks service object.
      tasklist_id (str): ID of the target task list.
  """

    tasks = get_tasks(service, tasklist_id)
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(f"- {task['title']}")
    else:
        print("No tasks found in this list.")


credentials = get_credentials()
tasks = get_service(credentials)

# new_task_list = add_new_tasklist(tasks, "New Task List")
# print(new_task_list)

task_lists = get_task_lists(tasks)
pprint(task_lists)

# add_new_task(tasks, task_lists["Jarvis AI Assistant Tasks"], "NO Swimming Today")

show_tasks(tasks, task_lists["Jarvis AI Assistant Tasks"])

# pprint(get_tasks(tasks, task_lists["Jarvis AI Assistant Tasks"]))

task_mark_as_done(tasks, "bXhqYXhSSGhVODRKU1NvXw", task_lists["Jarvis AI Assistant Tasks"])

task_mark_as_not_done(tasks, "bXhqYXhSSGhVODRKU1NvXw", task_lists["Jarvis AI Assistant Tasks"])

new_tasklist_output = add_new_tasklist(tasks, "", **task_lists)
pprint(new_tasklist_output)
