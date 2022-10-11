import re
import os
import sys
import requests
import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import logging

load_dotenv(find_dotenv())


CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
CACHE = ".cache"
SCOPE = "playlist-modify-private"

# logger = logging.getLogger('examples.create_playlist')
# logging.basicConfig(level='DEBUG')


def validate(date_text):
    """Validate dates"""
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


# def get_args(album_date):
#     """Get needed arguments for creating playlist on Spotify"""
#     parser = argparse.ArgumentParser(description="Creates a playlist for user")
#     parser.add_argument("-p", "--playlist", required=True,
#                         help=f"Hot 100 songs of {album_date}")
#     parser.add_argument("-d", "--description", required=False, default="",
#                         help="Best songs at this date")
#     return parser.parse_args()


def main():

    # Checking for arguments and validation of them
    if len(sys.argv) != 2:
        os.system("clear") # "cls" for Windows
        print("date in format of YYYY-MM-DD\n\nRun program like this: python3 main.py date")
    travel_to_date = sys.argv[1]
    validate(travel_to_date)
    os.system("clear")

    # Best 100 songs
    print("Program for Time Travelling in Music\n\n")
    URL = f"https://www.billboard.com/charts/hot-100/{travel_to_date}/"

    response = requests.get(URL)
    billboard_hot_100 = response.content
    soup = BeautifulSoup(billboard_hot_100, "html.parser")

    # Spotipy
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=SCOPE,
            redirect_uri=REDIRECT_URI,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            show_dialog=True,
            cache_path=CACHE
        )
    )



    # songs_with_trim = [song.getText() for song in soup.find_all(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]
    # # songs = [re.sub(r"\s", "", str(song)) for song in songs_with_trim]
    # songs = [str(song).strip() for song in songs_with_trim]
    # artist_with_trim = [artist.getText() for artist in soup.find_all(name="span", class_="ic-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")]
    # # artists = [re.sub(r"\s", "", str(artist)) for artist in artist_with_trim]
    # artists = [str(artist).strip()) for artist in artist_with_trim]
    # print(songs)
    # print(artists)

    # Creating list with song + it's artist
    web_content = soup.find_all("div", class_="o-chart-results-list-row-container")
    song_list = []
    artist_list = []
    for track in web_content:
        song_list.append(track.find("h3").text.strip())
        artist_list.append(track.find("h3").find_next("span").text.strip())

    song_artist_list = dict(zip(artist_list, song_list))

    # Current user
    user_id = sp.current_user()["id"]

    # Creating playlist and collecting song uris
    spotify_song_uris = []

    for key, value in song_artist_list.items():
        spotify_result = sp.search(q=f"artist:{key} track:{value} year:{travel_to_date[:4]}", type="track")
        try:
            song_uri = spotify_result['tracks']['items'][0]['uri']
            spotify_song_uris.append(song_uri)
        except IndexError:
            print(f"{value} doesn't exist in Spotify. Skipped.")

    print(len(spotify_song_uris))

    my_playlist = sp.user_playlist_create(
                                      user=f"{user_id}",
                                      name=f"{travel_to_date[:4]} Billboard Top Tracks",
                                      public=False,
                                      description="Top Tracks from back in the days"
                                      )
    

    # Adding songs to playlist
    # playlist_id = sp.user_playlists(user=user_id)["items"][0]["id"]
    # playlist_id = sp.user_playlists(user=user_id)["items"][0]
    # print(playlist_id)

    # sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=spotify_song_uris)


if __name__ == "__main__":
    main()
