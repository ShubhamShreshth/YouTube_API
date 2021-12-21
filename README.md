# YouTube_API
This Project is developed in Django Python.

# Project Goal - 
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# What this Project basically does is - 
```buildoutvfg
1. Uses YouTube API to fetch list of videos of certain search keyword
2. Stores it in dictionary
3. Displays that dictionary in web page in paginated response
```

# Result - 
After running this django project in your local system the final paginated response will look like this - 

![alt text](https://github.com/ShubhamShreshth/YouTube_API/blob/master/final.png?raw=true)

# Functionality Covered -
```buildoutcfg
- Server call the YouTube API continuously in background with some interval (here - 20 seconds)
- Fetch the latest videos for a predefined search query (here - "Football")
- Stores the data of videosin a database with proper indexes (here - Index starts with 1)
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- Scalable and optimised.
- Added support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
```

# Key Files Used - 
```buildoutvfg
mysite/yt/views.py
mysite/yt/templates/yt/home.html
```
- "views.py" contains the code for the API usage and data extraction.
- "home.html" contains the code for the UI of the web page in which the final paginated response from API will be displayed.

# Instructions to start Django Server on Localhost - 

1. Download ZIP file of this repo and extract it in local system.
2. Open the extracted file in Pyhton IDE.
3. Then in your terminal direct to the folder which has this project.
4. Then type the below commands in your terminal for the web server to start.
```buildoutcfg
cd mysite
python manage.py runserver
```
5. Do this in your terminal to run the program in your web browser.
6. You will get a link of your web page open that link to see the final paginated response.

# API -
```buildoutcfg
https://www.googleapis.com/youtube/v3/search?part=snippet&q=football&maxResults=1&type=video&eventType=completed&order=date&key=AIzaSyB9QNacHSAQ4deQp4RjVf3gXZOKXtMCwJk
```
### NOTE - Here in above API maxResults is set is to 1
## API keys used in this project -
```buildoutcfg
AIzaSyB9QNacHSAQ4deQp4RjVf3gXZOKXtMCwJk
AIzaSyDK-WNR6d2LayUqiemCKOcMYPlDV6jvTh0
AIzaSyCmLgeX3GtUgfn7ZjkkWHfOWCMb1MkDEpU
AIzaSyAip91VlvxNxaw7Fd1mF1s0lUtegg5WtPU
AIzaSyDAYksLzTBkPf9TQC6th2c9iBSXZ6-Dl8I
AIzaSyDa1vWMOyRYGq4Qv4Lg_AelhTAiHw4E7OQ
```
### - To test the API key use above URL and change the key value to any of the above mentioned keys.
### - GET Request will return data in following json with datetime order:
 ```buildoutcfg
{
  "kind": "youtube#searchListResponse",
  "etag": "0aOb7M7XGxvgrX6-CuTADDkWwbM",
  "nextPageToken": "CAEQAA",
  "regionCode": "IN",
  "pageInfo": {
    "totalResults": 1000000,
    "resultsPerPage": 1
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "uOoyNl-TKZ8B11Zzcz8LdUAe_Sk",
      "id": {
        "kind": "youtube#video",
        "videoId": "GBcQ2MySPsE"
      },
      "snippet": {
        "publishedAt": "2021-12-20T17:06:56Z",
        "channelId": "UCkyRPvjEgrtUgnaVMyYr_hQ",
        "title": "Good Morning Football LIVE HD 12/20/2021 | GMFB -Breaking News - Predict - analysis NFL Season 2021",
        "description": "Good Morning Football LIVE HD 12/20/2021 | GMFB -Breaking News - Predict - analysis NFL Season 2021.",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/GBcQ2MySPsE/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/GBcQ2MySPsE/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/GBcQ2MySPsE/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "BeerusS TV",
        "liveBroadcastContent": "none",
        "publishTime": "2021-12-20T17:06:56Z"
      }
    }
  ]
}
```
