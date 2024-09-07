from anime_list import AnimeList
from jikan_api_client import JikanApiClient
import json

def getGenreListFromUser(valid_genre_list):
    genre_list = []
    stop_keyword = "."

    while True:
        genre = input(f"Input a genre ('{stop_keyword}' to stop): ")

        while ((genre not in valid_genre_list) and (genre != stop_keyword)):
            genre = input(f"Invalid genre, please type again ('{stop_keyword}' to stop): ")

        if (genre == stop_keyword):
            break

        genre_list.append(genre)

    return genre_list

def main():
    print('This is a automating decision-making project')
    print('---------------------------------------------------------')

    # create api client
    source = JikanApiClient()

    # get data
    anime_list = AnimeList()
    anime_list.getTopAnimeFromApi(source)
    anime_list.printList()

    # get all valid genre list
    all_genres = anime_list.getAllGenres()
    anime_list.storeGenreList()

    # get anime genres from user 
    input_genre_list = getGenreListFromUser(all_genres)
    print(input_genre_list)

    # get random anime
    print("Getting a random anime: ")
    randomAnime = anime_list.getRandomAnime()
    print(randomAnime.details())

    # get random anime matching all genre list
    print("Getting a random anime matching all genres in list: ")
    randomAnime = anime_list.getAnimeMatchingAllGenres(input_genre_list)
    print(randomAnime.details())

if __name__ == '__main__':
    main()