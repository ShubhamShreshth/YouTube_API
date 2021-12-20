from django.shortcuts import render

# Create your views here.
import requests
import json


# USING API STARTS HERE
# HERE I HAVE USED API RESULT LIMIT OF 100 ONLY (maxResults=100)


class YTData:
    def __init__(self, api_key, query):  # taking arguments for API key and query that is to be searched
        self.api_key = api_key
        self.query = query
        self.next_page_token = None  # token for next page as YouTube API key only provides maximum 0f 50 data in single page and provide key for next page for further data
        self.data = dict()  # dictionary for storing relevent fields from API key (here video title, description, publishtime, image url, channel is extracted)
        self.data['Video List'] = []
        self.count = 1

    # creating function for page 1 to get the required fields
    def get_channel_stats_page1(self):
        # using URL to get data from API
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={self.query}&maxResults=100&type=video&eventType=completed&order=date&key={self.api_key}'
        # getting data in json form and converting it into string for extraction of relevent fields
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            self.next_page_token = data["nextPageToken"]
            # getting max number of data given in that page
            n = data['pageInfo']['resultsPerPage']
            # looping through each data for fields
            for i in range(n):
                video_title = data['items'][i]['snippet']['title']
                descrip = data['items'][i]['snippet']['description']
                publishTime = data['items'][i]['snippet']['publishedAt']
                image = data['items'][i]['snippet']['thumbnails']['high']['url']
                channel = data['items'][i]['snippet']['channelTitle']
                # storing data into dictionary
                self.data['Video List'].append(
                    {"index": self.count, "title": video_title, "description": descrip, "publishtime": publishTime,
                     "image": image, "channel":channel})
                self.count += 1

        except:
            data = None

    # function for other pages other than first page to get required fields
    def get_channel_stats_pagen(self):
        # using URL to get data from API and applying token received from previous page
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&pageToken={self.next_page_token}&maxResults=100&q={self.query}&type=video&eventType=completed&order=date&key={self.api_key}'
        # getting data in json form and converting it into string for extraction of relevent fields
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            self.next_page_token = data["nextPageToken"]
            # getting max number of data given in that page
            n = data['pageInfo']['resultsPerPage']
            # looping through each data for fields
            for i in range(n):
                video_title = data['items'][i]['snippet']['title']
                descrip = data['items'][i]['snippet']['description']
                publishTime = data['items'][i]['snippet']['publishedAt']
                image = data['items'][i]['snippet']['thumbnails']['high']['url']
                channel = data['items'][i]['snippet']['channelTitle']
                # storing data into dictionary
                self.data['Video List'].append(
                    {"index": self.count, "title": video_title, "description": descrip, "publishtime": publishTime,
                     "image": image, "channel":channel})
                self.count += 1

        except:
            data = None

    # returning dictionary that has relevent fields for displaying
    def return_data(self):
        return self.data


# function for calling class YTdata which will call API to get data
def display_string(request):
    # List of API keys that can be used
    API_Key = ["AIzaSyB9QNacHSAQ4deQp4RjVf3gXZOKXtMCwJk", "AIzaSyDK-WNR6d2LayUqiemCKOcMYPlDV6jvTh0",
               "AIzaSyCmLgeX3GtUgfn7ZjkkWHfOWCMb1MkDEpU", "AIzaSyAip91VlvxNxaw7Fd1mF1s0lUtegg5WtPU",
               "AIzaSyDAYksLzTBkPf9TQC6th2c9iBSXZ6-Dl8I", "AIzaSyDa1vWMOyRYGq4Qv4Lg_AelhTAiHw4E7OQ"]
    # specific query (here used is "Football")
    query = "Football"
    # Code to check whether a key is exhausted or not
    for i in range(len(API_Key)):
        if i == len(API_Key):
            # checking and printing in console if all API keys are used
            print("All API Keys are Exhausted!\nTry Again Tomorrow!")
            break
        # checking if API key is giving data or not
        # if API key is not giving data then it will give a error message if we try to call the API
        # if API key is working then it will give the relevent data
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&maxResults=100&type=video&eventType=completed&order=date&key={API_Key[i]}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        # checking if API key is giving error or data
        if "error" in data:
            pass
        else:
            # printing in console the number of API key that is being used or are used previous to this
            print("API Key", i + 1, "is used!")
            current_api = API_Key[i]
    # Calling class for API Data
    yt = YTData(current_api, query)
    yt.get_channel_stats_page1()
    yt.get_channel_stats_pagen()
    # Getting data here in form of dictionary
    dictionary_data = yt.return_data()
    dictionary_data = dictionary_data['Video List']
    # passing data to HTML file for displaying in web page
    context = {'data': dictionary_data}
    return render(request, 'yt/home.html', context)
