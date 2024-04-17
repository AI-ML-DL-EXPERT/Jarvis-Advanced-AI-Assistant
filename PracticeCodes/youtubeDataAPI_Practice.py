# Libraries Used
from googleapiclient.discovery import build
from pprint import pprint
import re
from datetime import timedelta
import os
from dotenv import load_dotenv

# Loading the .env file where the api file is stored
load_dotenv("YOUTUBE_DATA_API_KEY.env")

# Setting the API key
api_key = os.getenv('YOUTUBE_DATA_API_KEY')

# Setting the Playlist ID, (This particular playlist ID is of CampusX DataScience Playlist)
playlistID = "PLKnIA16_RmvbAlyx4_rdtR66B7EHX5k3z"

# Setting the Regular Expressions for the string preprocessing to extract the hours, minutes and seconds.
hours_pattern = re.compile(r"(\d+)H")
minutes_pattern = re.compile(r"(\d+)M")
seconds_pattern = re.compile(r"(\d+)S")

# Initially Setting total seconds value to 0
total_seconds = 0

# Creating an instance of Build class to access the API
youtube = build("youtube", "v3", developerKey=api_key)

# Setting next page token to none, this will help to load all the pages of the playlist.
nextPageToken = None

# Running while look until the last page of the playlist.
while True:

    # Fetching a Dictionary of the items of the playlist
    pl_request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=playlistID,
        maxResults=50,
        pageToken=nextPageToken
    )

    # Respecting the output from the API
    pl_response = pl_request.execute()
    # pprint(pl_request)

    # Empty list to store the id's of the videos
    vid_ids = []

    # Running a for loop for every items of the playlist to fetch it's videoID
    for item in pl_response["items"]:
        vid_ids.append(item["contentDetails"]["videoId"])

    # Hitting a request to fetch the details of every video present in the playlist.
    vid_request = youtube.videos().list(
        part="contentDetails",
        id=",".join(vid_ids)
    )

    # Respecting the output from the API
    vid_response = vid_request.execute()
    # pprint(vid_response)

    # Fetching the Duration of every video and storing it into variables.
    for item in vid_response["items"]:
        # Total Duration of the video
        duration = item["contentDetails"]["duration"]

        # Applying regular expressions to extract the duration of each video
        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        # Checking if value is present or not, if not replace it by 0
        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        # Converting the hours, minutes and seconds into datetime total_seconds
        video_seconds = timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds
        ).total_seconds()

        # Adding total_seconds of every video to get the total seconds of the whole playlist
        total_seconds += int(video_seconds)

    # Setting the next page token to the next page token of the playlist
    nextPageToken = pl_response.get("nextPageToken")

    # print(nextPageToken)
    # print()

    # If the next page token is none then break the loop
    if not nextPageToken:
        break

# Total seconds of the playlist
print("Total Seconds: ", total_seconds)

# Converting the total seconds to Hours, minutes and seconds
minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)

# Printing the total Duration of the playlist
print(f"{hours}:{minutes}:{seconds}")
