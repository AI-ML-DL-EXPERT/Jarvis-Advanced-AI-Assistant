# Library Dependencies

# Speech Input and Speech Output Libraries
import speech_recognition as sr
import pyttsx3

# Basic Libraries
import time
import datetime
import requests
import random
import os

# Web browser Libraries
import webbrowser
import logging
import wikipedia

# YouTube Data API Dependencies
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Email Library Dependencies
from simplegmail import Gmail

# Google Tasks API Dependencies
from PracticeCodes import tasks_api_functions

"""
Functionalities in my AI:

Must Have Features:
1. Friendly conversation.
2. Manage apps or websites automatically, like managing instagram, GitHub, Various other accounts.
3. Search Online and answer you real time.
4. Open any app in the PC and perform specific actions in it.
5. Manage your social media accounts, and much more.
6. Customizable notifications and alerts for important events.
7. Able to make changes in apps using my voice commands.
8. Automated documentation generation for projects.
9. Real-time weather and traffic updates.
10. Personalized assistance and recommendations.
11. Search online and answer you real time.
12. Tell you jokes.
13. Use Word API for better search results, like asking same questions with different words like synonyms.
14. 

Future Features:
1. Able to modify itself, and upgrade itself.
2. Code Analysis and Optimization suggestions.
3. Real time Screen Monitoring.
4. Personal finance management and budgeting assistance.
5. Information retrieval and analysis  
6. Strategic decision-making support
7.

"""


class AiAssistant:
    """
    Class for the AI Assistant.
    """

    # Constructor method of AiAssistant class
    def __init__(self):
        """
            Constructor for the AI Assistant.
        """
        # Initializing the speech recognition Recognizer and the Microphone
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Loading the.env file where the api file is stored (Use your own API key)
        load_dotenv("YOUTUBE_DATA_API_KEY.env")

        # Getting the api key from the environment variable
        self.API_KEY = os.getenv("YOUTUBE_DATA_API_KEY")

        # Setting an instance variable for Gmail class
        self.gmail = Gmail()

        # Setting the Instance of the build class of a googleapiclient library
        self.youtube = build("youtube", "v3", developerKey=self.API_KEY)

        pass

    # Takes Input from the User and returns the output in a string
    def TakeCommand(self):
        """
            Listens for user input and returns the recognized text as a string.
            Handles potential errors and prompts the user to speak again if necessary.
        """

        with self.microphone as source:
            print("Listening...")

            # Adjusts the energy threshold dynamically using audio from the source to account for Ambient Noise.
            self.recognizer.adjust_for_ambient_noise(source)

            # If the user takes a pause of 1 Second, then it will stop listening.
            self.recognizer.pause_threshold = 1

            # Audio variable stores the input said by the user, as an AudioData object.
            audio = self.recognizer.listen(source)

            try:
                print("Recognizing...")
                # Here instead of using recognize_google, we can also use google.recognize_legacy
                # function as internally recognizer.recognize_google uses google.recognize_legacy
                # function.
                # Recognize_google converts the input audio data into a string format in Indian English format.
                user_text_input = self.recognizer.recognize_google(audio, language="en-in")
                print("User said: ", user_text_input)
                return user_text_input

            except Exception as e:
                # If some error occurs during hearing the Command, then this block of code will run so, that the program
                # won't get terminated
                print("Say that again Please")
                return "None"

    # Using pyttsx3 to convert my text to audio
    def Speak(self, audio):
        """
        Speak function converts the text to audio.
        parameter:
            audio: The text you want to speak
        return:
            None
        """
        # Initializing the engine
        engine = pyttsx3.init("sapi5")

        # Getting the list of available voices
        voices = engine.getProperty("voices")
        # print(voices[1].id)

        # Setting the Voice from the list of available voices
        engine.setProperty("voice", voices[1].id)

        engine.say(audio)
        engine.runAndWait()

    # Wish Message whenever you run the code
    def WishMessage(self):
        """
        WishMessage function returns the wish message.
        :return:
        str: A greeting based on the current time of day
        """
        currentTimeNow = datetime.datetime.now().hour

        if currentTimeNow < 12:
            return "Good Morning Boss"

        elif currentTimeNow < 15:
            return "Good Afternoon Boss"

        elif currentTimeNow < 19:
            return "Good Evening Boss"

        else:
            return "Good Night Boss"

    # Tells you a random Joke
    def RandomJoke(self):
        # Random Jokes
        randomJokeURL = "https://icanhazdadjoke.com/"
        randomJokeHeaders = {"Accept": "application/json"}
        randomJokeResponse = requests.get(randomJokeURL, headers=randomJokeHeaders)

        return randomJokeResponse.json()["joke"]

    # Searching On Google
    def search_on_google(self, query):
        """
            Opens Google search results for the provided query in the default browser.
            Logs an informative message if the operation is successful or encounters an error.
        """

        searchURL = f"https://www.google.com/search?q={query}"  # Construct search URL
        try:
            webbrowser.open(searchURL)
            logging.info(f"Opened Google search for: {query}")
        except webbrowser.Error as e:
            logging.error(f"Failed to open Google search: {e}")

    # Searching On YouTube
    def open_youtube(self):
        """Opens YouTube search results for the provided query in the default browser.
        Logs an informative message if the operation is successful or encounters an error.
        """
        searchURL = f"https://www.youtube.com"  # Construct search URL
        try:
            webbrowser.open(searchURL)
            logging.info(f"Opened YouTube")
        except webbrowser.Error as e:
            logging.error(f"Failed to Open YouTube: {e}")

    # Calling the request to search for a particular topic
    def search_youtube(self, search_query):
        yt_request = self.youtube.search().list(
            q=search_query,
            maxResults=3,
            part="snippet",
            type="video"
        )

        search_response = yt_request.execute()

        return search_response

    # Fetching every video from the list of videos
    def fetching_video_details(self, lst_of_video_ids):
        vid_request = self.youtube.videos().list(
            part="contentDetails, statistics, snippet",
            id=",".join(lst_of_video_ids)
        )

        vid_response = vid_request.execute()

        return vid_response

    # Open Instagram in the default browser
    def open_instagram(self):
        """Opens Instagram in the default browser.
        Logs an informative message if the operation is successful or encounters an error.
        """
        instagramURL = "https://www.instagram.com/"
        try:
            webbrowser.open(instagramURL)
            logging.info(f"Opened Instagram")
        except webbrowser.Error as e:
            logging.error(f"Failed to open Instagram: {e}")

    # Open Twitter
    def open_twitter(self):
        """Opens Twitter in the default browser.
        Logs an informative message if the operation is successful or encounters an error.
        """
        twitterURL = "https://twitter.com/home"
        try:
            webbrowser.open(twitterURL)
            logging.info(f"Opened Twitter")
        except webbrowser.Error as e:
            logging.error(f"Failed to open Twitter: {e}")

    # Search wikipedia and get a short summary of the topic
    def get_wikipedia_introduction(self, search_term, sentences=2):
        """Retrieves a brief introduction of the provided search term from Wikipedia.

      Handles potential errors like disambiguation or page not found, logging informative messages.

      Args:
          search_term (str): The topic to search for on Wikipedia.
          Sentences(int, optional): The number of sentences for the summary.
          Default to 2.

      Returns:
          str: The retrieved summary of the search term or an informative error message.
      """
        logging.basicConfig(level=logging.INFO)  # Set logging level

        try:
            summary = wikipedia.summary(search_term, sentences=sentences)
            logging.info(f"Successfully retrieved summary for: {search_term}")
            return summary
        except wikipedia.DisambiguationError as e:
            logging.warning(f"Disambiguation required: {e}")
            return f"Disambiguation required for '{search_term}': {e}"
        except wikipedia.PageError as e:
            logging.warning(f"Page not found: {e}")
            return f"Wikipedia page not found for '{search_term}'"
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return f"An error occurred while retrieving information for '{search_term}'"

    # Open GitHub in the default browser
    def open_github(self):
        """Opens GitHub in the default browser.
        Logs an informative message if the operation is successful or encounters an error.
        """
        githubURL = "https://github.com/AI-ML-DL-EXPERT"
        try:
            webbrowser.open(githubURL)
            logging.info(f"Opened GitHub")
        except webbrowser.Error as e:
            logging.error(f"Failed to open GitHub: {e}")

    # Send an Email
    def send_mail(self, to, subject, message):
        """
        Send an email using Gmail.
        :param to: The email address to send
        :param subject: Subject of the email
        :param message: Message for the email
        :return: Param (Dictionary of parameters to send to the instance of gmail class)
        """

        # Sending an email
        params = {
            "to": to,
            "sender": "noname7231236@gmail.com",
            "subject": subject,
            "msg_html": f"<p>{message}</p>",
            "msg_plain": message,
            "signature": True  # use my account signature
        }

        return params

    def add_a_task(self, tasks_api_instance, tasklist_title="Jarvis AI Assistant Tasks"):
        # Calling the function to add a task
        task_lists_dict = tasks_api_functions.get_task_lists(tasks_api_instance)
        print("What do you want to add: ")
        self.Speak("What do you want to add")
        # Taking the input from user
        task_title = self.TakeCommand()
        tasks_api_functions.add_new_task(tasks, task_lists_dict[tasklist_title], task_title)
        self.Speak("Task Added Successfully")


if __name__ == '__main__':

    assistant = AiAssistant()
    assistant.Speak(assistant.WishMessage())
    assistant.Speak("How can I help you")

    while True:
        user_input = assistant.TakeCommand().lower()

        try:
            # Tell you the current Time
            if "time" in user_input:
                currentTime = datetime.datetime.now().time().strftime("%I:%M %p")
                print(f"\nBoss the time is: {currentTime}")
                assistant.Speak(f"Boss the time is: {currentTime}")

            # Tell you the Current Date
            elif "date" in user_input:
                date = datetime.datetime.now().date().strftime("%A, %d %B %Y")
                print(f"\nBoss the date is: {date}")
                assistant.Speak(f"Boss the date is: {date}")

            # Who Made this AI
            elif "who made you" in user_input or "who is your boss" in user_input or "who developed you" in user_input:
                print("I was developed by Boss Diwakar.")
                assistant.Speak("I was developed by Boss Diwakar.")
                continue

            # Functionalities it can perform
            elif "what can you do" in user_input or "what actions can you perform" in user_input:
                functionalities = ("\nI am an Advanced Helpful Assistant and I can perform actions like: \n"
                                   "1. Perform Human Like Friendly Conversation. \n"
                                   "2. Tell you a random Jokes.\n"
                                   "3. Set Reminders, Alarms, Events and much more.\n"
                                   "4. Search Online and answer you real time.\n"
                                   "5. Open any app in the PC and perform specific actions in it.\n"
                                   "6. Manage your social media accounts, and much more.\n")

                print(functionalities)
                assistant.Speak(functionalities)

            # Name of the Assistant
            elif "your name" in user_input:
                print("I am Jarvis an Advanced Helpful Assistant.")
                assistant.Speak("I am Jarvis an Advanced Helpful Assistant.")

            # Exit the Assistant
            elif "exit" in user_input:
                print("\nExiting...")
                assistant.Speak("Exiting Assistant Boss!")
                exit(0)

            # Tell you the Joke on any topic you want to hear the joke
            elif "joke" in user_input and "topic" in user_input:
                # Taking input from the user, asking him on which topic, he wants to hear the joke
                assistant.Speak("On which topic you want to hear the joke about")
                jokeTopic = assistant.TakeCommand().lower()
                print(f"Joke Topic: {jokeTopic}")

                # Hitting the url and fetching the joke from the API server
                url = f"https://icanhazdadjoke.com/search?term={jokeTopic}"
                headers = {"Accept": "application/json"}  # Specify JSON format for response
                response = requests.get(url, headers=headers)
                response = response.json()

                # Checking if the joke is there about a certain topic is there or not, if not, then try another topic
                if len(response["results"]) == 0:
                    print("No Jokes found for this topic, please search for another topic")
                    assistant.Speak("No Jokes found for this topic, please search for another topic")
                else:
                    randomList = random.choice(response["results"])
                    print(f"Joke: {randomList["joke"]}")
                    time.sleep(1)
                    assistant.Speak(randomList["joke"])

            # Tell you a random Joke
            elif "joke" in user_input:
                # Fetches a random Joke
                joke = assistant.RandomJoke()
                print(f"Joke: {joke}")
                time.sleep(1)
                assistant.Speak(joke)

            # Open Google and search for a query
            elif "open google" in user_input:
                # Set logging level for informative messages
                logging.basicConfig(level=logging.INFO)
                print("What do you want to search:- ")
                assistant.Speak("What do you want to search")
                user_input = assistant.TakeCommand().lower()
                assistant.search_on_google(user_input)

            # Open YouTube and search for a query
            elif "open youtube" in user_input:
                # Set logging level for informative messages
                logging.basicConfig(level=logging.INFO)
                assistant.Speak("Opening YouTube")
                assistant.open_youtube()

            # Searching for a particular video on YouTube
            elif "search" in user_input and "youtube" in user_input:
                try:
                    # Search for a specific video
                    assistant.Speak("What do you want to search")
                    query = assistant.TakeCommand().lower()

                    # Contains the list of top 3 suggested videos from YouTube for the particular search query
                    yt_response = assistant.search_youtube(query)["items"]

                    # This stores the list of all the videos
                    video_ids = []

                    # print(video_ids)

                    # Iterating through the every video in the list and extracting their video_ids
                    for item in yt_response:
                        video_ids.append(item["id"]["videoId"])

                    # Hitting the request to fetch the details of every video present in the playlist.
                    vid_response = assistant.fetching_video_details(video_ids)

                    # Storing the list of all the video details
                    lst_of_vid_details = vid_response["items"]

                    # List to store Number of likes on each video
                    vid_likes = []

                    # Iterating through the every video in the list and extracting their number of likes
                    for video in lst_of_vid_details:
                        vid_likes.append(int(video["statistics"]["likeCount"]))

                    # print(vid_likes)

                    # Setting the index of the highest number of likes on the video to 0
                    idx_with_highest_likes = 0

                    # Iterating through every value of the vid_likes list to get the index of the video with the highest
                    # number of likes
                    for i in range(len(lst_of_vid_details)):
                        if vid_likes[i] > vid_likes[idx_with_highest_likes]:
                            idx_with_highest_likes = i

                    # Fetching the details of the video who has the highest number of likes.
                    video_title = lst_of_vid_details[idx_with_highest_likes]["snippet"]["title"]
                    channel_title = lst_of_vid_details[idx_with_highest_likes]["snippet"]["channelTitle"]
                    video_description = lst_of_vid_details[idx_with_highest_likes]["snippet"]["description"]
                    number_likes = lst_of_vid_details[idx_with_highest_likes]["statistics"]["likeCount"]
                    number_views = lst_of_vid_details[idx_with_highest_likes]["statistics"]["viewCount"]
                    video_id = lst_of_vid_details[idx_with_highest_likes]["id"]

                    # pprint(lst_of_vid_details[idx_with_highest_likes])

                    # Printing the details of the videos
                    print("Video Title: ", video_title)
                    print("Channel Name: ", channel_title)
                    print("Number of Likes: ", number_likes)
                    print("Number of Views: ", number_views)
                    # print("Video Description: ", video_description)

                    # Opening the search result page on YouTube
                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

                    # Playing the video
                    print("\nPlaying the video")
                    assistant.Speak("Playing the video")
                    webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")

                    logging.info(f"Opening YouTube and Playing the video: {query}")

                except webbrowser.Error as e:
                    logging.error(f"Failed to Open YouTube: {e}")

            # Open Instagram
            elif "open instagram" in user_input:
                # Set logging level for informative messages
                logging.basicConfig(level=logging.INFO)
                assistant.open_instagram()

            # Open Twitter
            elif "open twitter" in user_input:
                # Set logging level for informative messages
                logging.basicConfig(level=logging.INFO)
                assistant.open_twitter()

            # Open GitHub
            elif "open github" in user_input:
                # Set logging level for informative messages
                logging.basicConfig(level=logging.INFO)
                assistant.open_github()

            # Search on Wikipedia on a specific topic
            elif "search wikipedia" in user_input:
                print("What do you want to search:- ")
                assistant.Speak("What do you want to search")
                user_input = assistant.TakeCommand().lower()
                print("Output:- ", assistant.get_wikipedia_introduction(user_input, sentences=2))
                assistant.Speak(assistant.get_wikipedia_introduction(user_input, sentences=2))

            # Sending a Gmail
            elif "send mail" in user_input or "send gmail" in user_input or "send email" in user_input:
                assistant.Speak("Enter the Email Address to whom you want to send the Email")
                to = input("To: ")

                assistant.Speak("What is the Subject of the Email")
                subject = assistant.TakeCommand().lower()
                print("Subject of the Email: ", subject)

                assistant.Speak("What is the Message of the Email")
                message = assistant.TakeCommand().lower()
                print("Subject of the Email: ", message)

                # Calling send_mail function to get the Parameters of the Email
                params = assistant.send_mail(to=to, subject=subject, message=message)

                # Sending the message
                # equivalent to send_message(to="you@youremail.com", sender=...)
                email = assistant.gmail.send_message(**params)

                assistant.Speak("Message Sent")

            # Adding a task
            elif "add a task" in user_input or "add task" in user_input:
                print("Do you want to add the task in default tasklist or Create a new tasklist? \n"
                      "Yes or No?")

                assistant.Speak("Do you want to add the task in default tasklist or create a new tasklist? Yes or No?")
                user_input = assistant.TakeCommand().lower()

                # Initializing the Google Tasks API
                credentials = tasks_api_functions.get_credentials()
                tasks = tasks_api_functions.get_service(credentials)

                # If the User Says Yes or Default, then add the task in the default tasklist
                if "yes" in user_input or "default" in user_input:
                    # Adding the task in the default tasklist
                    assistant.add_a_task(tasks)

                else:
                    # If the User Says No, then create a new tasklist
                    print("What do you want to name the tasklist: ")
                    assistant.Speak("What do you want to name the tasklist")
                    task_list_title = assistant.TakeCommand().lower()

                    # Calling the function to create a new tasklist
                    task_lists = tasks_api_functions.get_task_lists(tasks)
                    new_tasklist_output = tasks_api_functions.add_new_tasklist(tasks, task_list_title, **task_lists)

                    # Updating the tasklist
                    task_lists = tasks_api_functions.get_task_lists(tasks)

                    if new_tasklist_output is None:
                        print("Tasklist Already Exists")
                        assistant.Speak("Tasklist Already Exists")

                    elif task_list_title is None:
                        print("Nothing to add")
                        assistant.Speak("Nothing to add")

                    else:
                        print("Tasklist Created Successfully")
                        assistant.Speak("Tasklist Created Successfully")

                        # Adding the Task
                        assistant.add_a_task(tasks, task_list_title)

            # Mark a task as done
            elif ("mark" in user_input and "task" in user_input) or "mark task as done" in user_input:
                # Initializing the Google Tasks API
                credentials = tasks_api_functions.get_credentials()
                tasks = tasks_api_functions.get_service(credentials)

                # List of Task lists
                tasklists = tasks_api_functions.get_task_lists(tasks)

                print("Task list Title: ")
                assistant.Speak("What is the Name of the tasklist")

                # Checking from which Task lists user wants to update the tasks
                task_lists_title = assistant.TakeCommand().lower()

                # Checking if the Tasklist exists in the TaskLists
                if task_lists_title in tasklists.keys():

                    # List of tasks in a TaskList
                    tasks_list = tasks_api_functions.get_tasks(tasks, tasklists[task_lists_title])

                    # Which task you want to update
                    print("Which task do you want to update?")
                    assistant.Speak("Which task do you want to update?")
                    task_title = assistant.TakeCommand().lower()

                    # Checking if the Task exists in the TaskList
                    for task in tasks_list:
                        if task_title == task["title"]:
                            # Updating the Task
                            tasks_api_functions.task_mark_as_done(tasks, task_id=task["id"],
                                                                  tasklist_id=tasklists[task_lists_title])
                            assistant.Speak("Task Updated Successfully")

                else:
                    print("Task does not exist")
                    assistant.Speak("Task does not exist")

            # Reminders Functionalities
            elif "reminders" in user_input:
                pass

            # Exiting the program
            elif "exit" in user_input or "quit" in user_input:
                print("Exiting the Assistant Boss")
                assistant.Speak("Exiting the Assistant Boss")
                exit(0)

            # If any other command is entered, then print this message, and say the command again.
            else:
                print("Say it again please!")
                continue

        # If any error occurred, then print this error message, and say the command again.
        except Exception as e:
            print("Say it again please! An Error has occurred")
