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
        for i in self.anime_list:
            print(i.details())

    def getRandomAnime(self):
        random_index = random.randint(0, self.size - 1)
        random_anime = self.anime_list[random_index]
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