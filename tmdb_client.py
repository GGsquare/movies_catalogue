from flask import Flask
import requests
import tmdb_client

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZDJjN2EyMWY4OWQzMTU2MTJiOTE3ZWZlNTFjYmJlMSIsInN1YiI6IjYyNjJmMWM1MmZkZWM2MDA2ODhhYTQzYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TngAcVhN5uxheWv9SrEyAmAJ9K7gMiFGwQxe6NOe978"

app = Flask(__name__)

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")

def get_movies(how_many, list_type='popular'):
    movie_types=['popular', 'top_rated', 'upcoming']
    if not list_type in movie_types:
        list_type='popular'
    data = get_movies_list(list_type)
    return data["results"][:how_many]

"""@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}"""
