from anime_list import AnimeList

def getUserMood():
    yourMood = 'dark'
    # yourMood = input('Input your mood (excite, dark, suy): ')
    return yourMood

if __name__ == '__main__':
    print('This is a automating decision-making project')
    print('---------------------------------------------------------')

    # declare data
    animeList = AnimeList()
    animeList.getApiData()

    # check
    animeList.printList()

    # # get user mood
    # userMood = getUserMood()

    # # get random anime
    # randomAnime = animeList.getRandomAnime()
    # while (userMood != randomAnime.getMood()):
    #     randomAnime = animeList.getRandomAnime()

    # randomAnime.printInfo()