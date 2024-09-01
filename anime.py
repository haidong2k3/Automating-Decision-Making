class Anime:
    def __init__(self, title = '', genres = [], season_year = '', anime_type = ''):
        self.title = title
        self.genres = genres
        self.season_year = season_year
        self.anime_type = anime_type
    
    def __str__(self):
        return f'Anime: {self.title} {self.genres} {self.season_year} {self.anime_type}'
    
    def details(self):
        return f'{self.title} - {self.season_year} - {self.anime_type} - {self.genres}'
    
    # ref 'jikan_api_structure.json' for jikan api top anime
    def jikanFilter(self, anime_info):
        self.title = anime_info['title']
        self.anime_type = anime_info['type']
        self.season_year = f'{anime_info['season']}_{anime_info['year']}'

        genres = []
        genres = anime_info['genres']
        for i in genres:
            self.genres.append(i['name'])
        
        return self