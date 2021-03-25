import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get('SPOTIFY_ID'),
                                               client_secret=os.environ.get('SPOTIFY_KEY'),
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path='token.txt'
                                               )
                     )

user_id = sp.current_user()['id']

travel = input('Which year do you want to travel to? Enter date in YYYY-MM-DD format: ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{travel}')
response.raise_for_status()
billboard = response.text



chart = BeautifulSoup(billboard, 'html.parser')

songs = chart.find_all(name='span', class_='chart-element__information__song')

list_of_songs = []

for song in songs:
    list_of_songs.append(song.getText())

song_uris = []
year = travel.split('-')[0]

print(year)

for song in list_of_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f'{travel} Billboard 100', public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)