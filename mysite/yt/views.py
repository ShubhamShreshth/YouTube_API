from django.shortcuts import render

# Create your views here.
import requests
import json


# USING API STARTS HERE
# HERE I HAVE USED API RESULT LIMIT OF 100 ONLY (maxResults=100)


class YTData:
    def __init__(self, api_key, query):
        self.api_key = api_key
        self.query = query
        self.next_page_token = None
        self.data = dict()
        self.data['Video List'] = []
        self.count = 1

    def get_channel_stats_page1(self):
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={self.query}&maxResults=100&type=video&eventType=completed&order=date&key={self.api_key}'

        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            self.next_page_token = data["nextPageToken"]
            n = data['pageInfo']['resultsPerPage']
            for i in range(n):
                video_title = data['items'][i]['snippet']['title']
                descrip = data['items'][i]['snippet']['description']
                publishTime = data['items'][i]['snippet']['publishedAt']
                image = data['items'][i]['snippet']['thumbnails']['high']['url']
                self.data['Video List'].append(
                    {"index": self.count, "title": video_title, "description": descrip, "publishtime": publishTime,
                     "image": image})
                self.count += 1

        except:
            data = None

    def get_channel_stats_pagen(self):
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&pageToken={self.next_page_token}&maxResults=100&q={self.query}&type=video&eventType=completed&order=date&key={self.api_key}'

        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            self.next_page_token = data["nextPageToken"]
            n = data['pageInfo']['resultsPerPage']
            for i in range(n):
                video_title = data['items'][i]['snippet']['title']
                descrip = data['items'][i]['snippet']['description']
                publishTime = data['items'][i]['snippet']['publishedAt']
                image = data['items'][i]['snippet']['thumbnails']['high']['url']
                self.data['Video List'].append(
                    {"index": self.count, "title": video_title, "description": descrip, "publishtime": publishTime,
                     "image": image})
                self.count += 1

        except:
            data = None

    def return_data(self):
        return self.data


def display_string(request):
    # List of API keys that can be used
    API_Key = ["AIzaSyB9QNacHSAQ4deQp4RjVf3gXZOKXtMCwJk", "AIzaSyDK-WNR6d2LayUqiemCKOcMYPlDV6jvTh0",
               "AIzaSyCmLgeX3GtUgfn7ZjkkWHfOWCMb1MkDEpU", "AIzaSyAip91VlvxNxaw7Fd1mF1s0lUtegg5WtPU",
               "AIzaSyDAYksLzTBkPf9TQC6th2c9iBSXZ6-Dl8I", "AIzaSyDa1vWMOyRYGq4Qv4Lg_AelhTAiHw4E7OQ"]
    query = "football"
    # Code to check whether a key is exhausted or not
    for i in range(len(API_Key)):
        if i == len(API_Key):
            print("All API Keys are Exhausted!\nTry Again Tomorrow!")
            break
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&maxResults=100&type=video&eventType=completed&order=date&key={API_Key[i]}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        if "error" in data:
            pass
        else:
            print("API Key", i + 1, "is used!")
            current_api = API_Key[i]
    # Calling class for API Data
    yt = YTData(current_api, query)
    yt.get_channel_stats_page1()
    yt.get_channel_stats_pagen()
    # Getting data here in form of dictionary
    dictionary_data = yt.return_data()
    dictionary_data = dictionary_data['Video List']
    context = {'data': dictionary_data}
    return render(request, 'yt/home.html', context)
