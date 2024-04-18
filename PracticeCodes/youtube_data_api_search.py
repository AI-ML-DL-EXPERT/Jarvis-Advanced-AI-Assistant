from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
from pprint import pprint
import webbrowser

# Loading the.env file where the api file is stored ( Use your own API key )
load_dotenv("YOUTUBE_DATA_API_KEY.env")

# Getting the api key from the environment variable
API_KEY = os.getenv("YOUTUBE_DATA_API_KEY")

# Setting the Instance of the build class of googleapiclient library
youtube = build("youtube", "v3", developerKey=API_KEY)


# Calling the request to search for a particular topic
def search_youtube(search_query):
    yt_request = youtube.search().list(
        q=search_query,
        maxResults=3,
        part="snippet",
        type="video"
    )

    response = yt_request.execute()

    return response


# Fetching every video from the list of videos
def fetching_video_details(lst_of_video_ids):
    vid_request = youtube.videos().list(
        part="contentDetails, statistics, snippet",
        id=",".join(lst_of_video_ids)
    )

    response = vid_request.execute()

    return response


# Search for a specific video
query = input("Search for video:- ")

# Contains the list of top 3 suggested videos from YouTube for the particular search query
yt_response = search_youtube(query)["items"]

# This stores the list of all the videos
video_ids = []

# print(video_ids)

# Iterating through the every video in the list and extracting their video_ids
for item in yt_response:
    video_ids.append(item["id"]["videoId"])

# Hitting the request to fetch the details of every video present in the playlist.
vid_response = fetching_video_details(video_ids)

# Storing the list of all the videos details
lst_of_vid_details = vid_response["items"]

# List to store Number of likes on each video
vid_likes = []

# Iterating through the every video in the list and extracting their number of likes
for video in lst_of_vid_details:
    vid_likes.append(int(video["statistics"]["likeCount"]))

# print(vid_likes)

# Setting the index of the highest number of like on the video to 0
idx_with_highest_likes = 0

# Iterating through every value of the vid_likes list to get the index of the video with the highest number of likes
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

# Playing the video
print("Playing the video")
webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")
