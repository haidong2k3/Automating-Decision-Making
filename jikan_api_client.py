import requests
import json

class JikanApiClient:
    def __init__(self, url = 'https://api.jikan.moe', version = '/v4'):
        self.base_url = f'{url}{version}'
    
    def __str__(self):
        return f'AnimeApiClient: {self.base_url}'

    def getTopAnime(self, page = 1, limit = 25):
        endpoint = f"{self.base_url}/top/anime"
        params = {'page': page, 'limit': limit}
        response = requests.get(endpoint, params)

        # store requested data (response_dict) to file
        response_dict = response.json()
        with open('api_data/jikan_top_anime.json', 'w') as file:
            json.dump(response_dict, file, indent = 4)

        # store anime list to file
        top_anime_list = response_dict["data"]
        with open('api_data/top_anime_list.json', 'w') as file:
            json.dump(top_anime_list, file, indent = 4)

        return top_anime_list