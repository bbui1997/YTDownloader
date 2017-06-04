# ytDownload

## Prerequisites

1. Clone the repository
2. Keep the ytDownload.exe file in the same directory as ffmpeg.exe, ffplay.exe, ffprobe.exe, and youtube-dl.exe

## Usage

1. Run ytDownload.exe
2. It will ask whether you want to download the full video, otherwise it will download mp3s.
3. It will prompt you for two inputs your YouTube Search Queries (separated by returns). To stop entering queries and begin downloading, enter "start download" or ".".
4. The script parses the search page based on your query for the amount of links you requested. It parses the first link based on the query you input.
5. After parsing the YouTube links, the script runs each link to youtube-dl
6. youtube-dl downloads the mp4 of the YouTube video and converts it using ffmpeg.
7. After the script has finished running, the mp3s will be located in the downloaded_music directory and will be titled as the YouTube video title. If you decided to download mp4s, the mp4s will be located in the downloaded_videos directory.

## About

This project is Python script that converts the first link of a YouTube search query to either an mp3 or mp4. 

You can also input the actual YouTube link to convert (generally, querying the YouTube link of a public video on the search bar will return that video as the first result).

It uses BeautifulSoup4 to parse the HTML and find the YouTube link.

It uses youtube-dl to convert the YouTube link to the highest quality possible. youtube-dl can be found here: https://github.com/rg3/youtube-dl

I plan to add a GUI to this project in the future, rather than a command prompt-like interface.

![Example Runthrough](https://github.com/bbui1997/YTDownloader/blob/master/runthrough.png?raw=true)
