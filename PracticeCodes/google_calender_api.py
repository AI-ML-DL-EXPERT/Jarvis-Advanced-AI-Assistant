from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import datetime
import os
from pprint import pprint

"""
1. Set Reminders
2. Set Events
3. Search for Holidays
"""

CLIENT_SECRET_FILE = "calender_client_secret.json"

scopes = ["https://www.googleapis.com/auth/calendar"]

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, scopes=scopes)

try:
    with open("calender_token.pickle", "rb") as token:
        credentials = pickle.load(token)
    credentials.refresh(Request())  # Refresh token if it exists
except Exception as e:
    credentials = flow.run_local_server(port=0)
    with open("calender_token.pickle", "wb") as token:
        pickle.dump(credentials, token)

service = build("calendar", "v3", credentials=credentials)

now = datetime.datetime.now(datetime.UTC).isoformat()
print(now)

service_events = service.events().list(
    calendarId="primary",
    timeMin=now,
    maxResults=1000,
    singleEvents=True,
    orderBy="startTime"
).execute()

events = service_events.get("items", [])
pprint(events)
