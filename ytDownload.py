import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import os

def main():
  print("Created by Brandon Bui\n")
  filetype = getFileType()
  print()

  list = get_download_list(filetype) # get list
  print() # blank line

  # Use youtube-dl to get mp3 files
  # 1) Get mp4 file
  # 2) Convert it to mp3, necessary

  if(filetype == "mp4"):
    convert_mp4(list)
  else:
    convert_mp3(list)

  input("\nDownload complete!")


# for each link in list, print out on command for youtube-dl to convert to mp4 with the best possible resolution and audio quality
def convert_mp4(list):
  for link in list:
    os.system("youtube-dl -o \"downloaded_videos/%(title)s.%(ext)s\" -f 22 --audio-quality 0 " + link)


# for each link in list, print out on command for youtube-dl to convert to mp3 audio quality
def convert_mp3(list):
  for link in list:
    os.system("youtube-dl -o \"downloaded_music/%(title)s.%(ext)s\" --extract-audio --audio-format mp3 --audio-quality 0 " + link)


# get first user input: choose whether we want to download only the mp3 or the whole video
def getFileType():
  print("ytDownload has an option to download either audio files or video files")
  print("By default, it will only install the mp3 file, but if you want to download video, enter \"mp4\"")
  return input("Please choose your filetype: ")


# get the list of links after finding desired file type
def get_download_list(filetype):
  # Declarations
  searchList = get_inputs(filetype)
  toDownload = []

  # get YouTube link from each desired query
  for search in searchList:
    print("\nSearching for: %s" % (search) )

    # parse the html of the query you made from user inputs
    query = urllib.parse.quote_plus(search)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    # add all youtube links to a list, prepare for downloading process
    foundLink = False

    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
      # it is possible for the parser to return a YouTube channel or playlist. Although youtube-dl can handle playlists
      # with a different command, the users would most likely prefer single YouTube videos
      if(vid['href'].startswith("/watch")):
        foundLink = True
        toDownload.append("https://www.youtube.com" + vid['href'])
        print("https://www.youtube.com" + vid['href']) # print out the link in case the user wants to see it
        break # get out of the loop after finding the first valid link

    if(not foundLink):
      print("No results for: {}".format(search))

  # return the download list
  return toDownload


# get search queries
def get_inputs(filetype):
  # by default, we will be converting it to mp3, but there is an option to convert it to mp4
  type = "mp3"
  if(filetype == "mp4"):
    type = filetype

  search_queries = []
  print("Press ctrl+c to quit without downloading anything")
  print("Enter a list of searches that you want to download and convert to %s" % (filetype) )
  print("Type and enter \"start download\" or \".\" to stop inputing searches and begin downloading your list of songs\n")

  # prompts input until user enters anything
  search_query = input("Enter your search query: ")

  # infinite loop, ends when user enters "start download" or "."
  # adds each input to a list
  while True:
    if(search_query == "start download" or search_query == "."):
      return search_queries
    search_queries.append(search_query)
    search_query = input("Enter your next search query: ")

if __name__ == "__main__":
    main()
