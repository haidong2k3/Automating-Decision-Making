import os
import random
from anime import Anime

class AnimeList:
    def __init__(self):
        self.anime_list = []
        self.size = 0

    def __str__(self):
        return f'AnimeList: {self.anime_list} {self.size}'

    def printList(self):
        print("This is a anime list: ")
        for i in self.anime_list:
            print(i.details())
    
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
        random_anime = self.getRandomAnime()
        random_anime_genres = random_anime.getGenres()

        required_genre_list_sz = len(required_genre_list)
        i = 0
        
        while (i < required_genre_list_sz):
            if (required_genre_list[i] not in random_anime_genres):
                random_anime = self.getRandomAnime()
                random_anime_genres = random_anime.getGenres()
                i = 0
            else:
                i += 1

        return random_anime
    
    def getTopAnimeFromApi(self, source):
        api_anime_list = source.getTopAnime()

        for i in api_anime_list:
            tmp = Anime().filter(source, i)
            self.anime_list.append(tmp)
            self.size += 1
    
    '''
    def readFile(self, fileName):
        # check file existance
        if not os.path.exists(fileName):
            print("Can't find file. Pls check again.")
            return
    
        # Open file - read file
        file = open(fileName, 'r')

        ##Handling data - append to 2d_list
        line = file.readline()
        while line: # line != ''
            arguments = line.strip().split(', ')
            self.listOfAnime.append(Anime(*arguments))
            self.size += 1
            line = file.readline()

        # Close file
        file.close()
    '''