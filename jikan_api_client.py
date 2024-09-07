import requests
import json

class JikanApiClient:
    def __init__(self, url = 'https://api.jikan.moe', version = '/v4'):
        self.base_url = f'{url}{version}'
    
    def __str__(self):
        return f'AnimeApiClient: base_url = {self.base_url}'

    def getTopAnime(self, count):
        endpoint = f"{self.base_url}/top/anime"

        PER_PAGE = 25
        page = 1
        limit = count
        top_anime_list = []

        while (limit >= PER_PAGE):
                params = {'page': page, 'limit': PER_PAGE}
                response_page = requests.get(endpoint, params).json()
                page_data = response_page.get("data", [])
                top_anime_list.extend(page_data)
                limit -= PER_PAGE
                page += 1

        if (limit > 0):
            params = {'page': page, 'limit': limit}
            response_page = requests.get(endpoint, params).json()
            page_data = response_page.get(response_page["data"])
            top_anime_list.extend(page_data)

        # store anime list to file
        with open('api_data/top_anime_list.json', 'w') as file:
            json.dump(top_anime_list, file, indent = 4)

        return top_anime_list