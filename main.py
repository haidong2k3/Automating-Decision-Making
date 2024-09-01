from anime_list import AnimeList
from jikan_api_client import JikanApiClient

# def getUserMood():
#     yourMood = 'dark'
#     # yourMood = input('Input your mood (excite, dark, suy): ')
#     return yourMood

if __name__ == '__main__':
    print('This is a automating decision-making project')
    print('---------------------------------------------------------')

    # create api client
    source = JikanApiClient()

    # get data
    anime_list = AnimeList()
    anime_list.getTopAnimeFromApi(source)

    # check
    anime_list.printList()

    # # get user mood
    # userMood = getUserMood()

    # # get random anime
    # randomAnime = animeList.getRandomAnime()
    # while (userMood != randomAnime.getMood()):
    #     randomAnime = animeList.getRandomAnime()

    # randomAnime.printInfo()