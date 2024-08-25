import os
import random
from anime import Anime
from anime_api_client import AnimeApiClient

class AnimeList:
    def __init__(self, size = 0, animeList = []):
        self.animeList = animeList
        self.size = size

    def __str__(self):
        return f'AnimeList: {self.animeList} {self.size}'

    def printList(self):
        for i in self.animeList:
            print(i.details())

    def getRandomAnime(self):
        randomIndex = random.randint(0, self.size - 1)
        choice = self.animeList[randomIndex]
        return choice
    
    def getApiData(self, url = None):
        # # load data from api
        source = AnimeApiClient(url) # api-default: https://api.jikan.moe/v4
        apiDataList = source.getTopAnimeFromJikan()

        for i in apiDataList:
            tmp = Anime().jikanFilter(i)
            self.animeList.append(tmp)
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