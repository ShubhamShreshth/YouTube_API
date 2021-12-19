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

# Functionality Covered -
```buildoutcfg
- Server call the YouTube API continuously in background with some interval (here - 20)
- Fetch the latest videos for a predefined search query (here - "Football")
- Stores the data of videosin a database with proper indexes (here - Index starts with 1)
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- It should be scalable and optimised.
- Added support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
```

# Key Files Used - 
```buildoutvfg
mysite/yt/views.py
mysite/yt/templates/yt/home.html
```

# Instructions to start django server on localhost - 
1- Create virtualenv: 
```buildoutcfg
cd src
virtualenv venv
```
2- Install required packages
```buildoutcfg
pip install -r requirements.txt
```
3- Makemigrations, migrate
```buildoutcfg
python manage.py makemigrations
python manage.py migrate
```
4- Createsuperuser
```
python manage.py createsuperuser
```
5- Runserver
```buildoutcfg
python manage.py runserver
```

# APIs
```buildoutcfg
https://www.googleapis.com/youtube/v3/search?part=snippet&q=football&maxResults=1&type=video&eventType=completed&order=date&key=AIzaSyB9QNacHSAQ4deQp4RjVf3gXZOKXtMCwJk
```
NOTE - Here in above API maxResults is set is to 1
### The API is query capable and paginated.
### GET Request will return data in following json with datetime order:
 ```buildoutcfg
{
    "kind": "youtube#searchListResponse",
    "etag": "P21syQ_ArG6t4T5qx-9l9b7TJwg",
    "nextPageToken": "CAEQAA",
    "regionCode": "US",
    "pageInfo": {
        "totalResults": 1000000,
        "resultsPerPage": 1
    },
    "items": [
        {
            "kind": "youtube#searchResult",
            "etag": "23Tx-VWvzQg8CZRevFv50ADMcCc",
            "id": {
                "kind": "youtube#video",
                "videoId": "ZJFSmxfjfIw"
            },
            "snippet": {
                "publishedAt": "2021-12-19T16:05:51Z",
                "channelId": "UC7AiAq4zB5ylQy23gg3H8hA",
                "title": "Wolves vs Chelsea LIVE WATCHALONG",
                "description": "Support the stream: https://streamlabs.com/younestalksfootball ➢ My Second Channel: ...",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/ZJFSmxfjfIw/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/ZJFSmxfjfIw/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/ZJFSmxfjfIw/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "Younes Talks Football",
                "liveBroadcastContent": "none",
                "publishTime": "2021-12-19T16:05:51Z"
            }
        }
    ]
}
```
