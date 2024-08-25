import requests
import os

class AnimeApiClient:
    def __init__(self, url = None):
        if (url is None):
            self.url = 'https://api.jikan.moe/v4'
    
    def __str__(self):
        return f'AnimeApiClient: {self.url}'

    def getTopAnimeFromJikan(self, page = 1, limit = 3, filename = 'animes.json'):
        endpoint = f"{self.url}/top/anime"
        params = {'page': page, 'limit': limit}

        response = requests.get(endpoint, params)
        response_dict = response.json()

        # luu response_dict ra file 
        # TODO
        file = open(filename, 'w')
        file.write(str(response_dict))
        file.close()

        top_anime = response_dict["data"] # list

        return top_anime