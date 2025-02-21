import requests 
from bs4 import BeautifulSoup
import base64
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def spotify_music(nome_musica):
    client_id = '60f7b9e5a2a04a9e81ca9277adc41a52'
    client_secret = 'd09a0c470e8e4480883412403de47550'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Realizar a busca
    resultados = sp.search(q=nome_musica, type='track', limit=1)
    
    
    for track in resultados['tracks']['items']:
        musica = {
            'Música': track['name'],
            'Artista': track['artists'][0]['name'],
            'Álbum': track['album']['name'],
            #'preview_url': track['preview_url'],
            'Link do Spotify': track['external_urls']['spotify']
        }
        
    
    return musica

def get_music(date_str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    # Missing closing parenthesis here:
    page = requests.get(f'https://www.billboard.com/charts/hot-100/{date_str}/', headers=headers)
    print(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = []
    for e in soup.find_all(attrs={'class':'o-chart-results-list-row'}):
        #pede pro chatGPT achar o link da musica a partir do title e author
        if e.li.find_next('span').get_text(strip=True) == '11':
            break; 
        data.append({
            'title':e.h3.get_text(strip=True),
            'author':e.h3.find_next('span').get_text(strip=True)
        
        })
    return data