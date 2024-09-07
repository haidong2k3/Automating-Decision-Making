import os
import random
from anime import Anime

class AnimeList:
    def __init__(self):
        self.anime_list = []
        self.size = 0

    def __str__(self):
        return f'AnimeList: anime_list = {self.anime_list}, size = {self.size}'

    def printList(self):
        print(f"This is an anime list ({self.size}): ")
        for i in range(0, self.size):
            print(f"{i}: {self.anime_list[i].details()}")

    def getAllGenres(self):
        all_genres = []
        for anime in self.anime_list:
            for genre in anime.getGenres():
                if genre not in all_genres:
                    all_genres.append(genre)

        return all_genres
    
    def storeGenreList(self, file_name = "api_data/genre_list.txt"):
        all_genres = self.getAllGenres()

        with open(file_name, "w") as file:
            file.write('\n'.join(map(str, all_genres)))
    
    def getRandomAnime(self):
        random_index = random.randint(0, self.size - 1)
        random_anime = self.anime_list[random_index]
        return random_anime
    
    def getAnimeMatchingAllGenres(self, required_genre_list):

        random_count = 1
        MAX_RANDOM_COUNT = 500

        random_anime = self.getRandomAnime()
        random_anime_genres = random_anime.getGenres()

        required_genre_list_sz = len(required_genre_list)

        if (required_genre_list_sz == 0):
            while (len(random_anime_genres) > 0):
                if (random_count == MAX_RANDOM_COUNT):
                    random_count = 0
                    break
                random_anime = self.getRandomAnime()
                random_anime_genres = random_anime.getGenres()
                random_count += 1
        else: 
            require_genre = 0
            while (require_genre < required_genre_list_sz):
                if (required_genre_list[require_genre] not in random_anime_genres):
                    if (random_count == MAX_RANDOM_COUNT):
                        random_count = 0
                        break
                    random_anime = self.getRandomAnime()
                    random_anime_genres = random_anime.getGenres()
                    random_count += 1
                    require_genre = 0
                else:
                    require_genre += 1

        if (random_count == 0):
            print("No Anime Satisfied Genres List. Return any anime: ")

        return random_anime
    
    def getTopAnimeFromApi(self, source, count = 50):
        api_anime_list = source.getTopAnime(count)

        for i in api_anime_list:
            self.anime_list.append(Anime().filter(api_source= source, anime_info= i))
            self.size += 1
    