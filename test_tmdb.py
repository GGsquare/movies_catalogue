from unittest.mock import Mock
import pytest
from . import tmdb_client 


def test_get_poster_url_users_default_size():
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url

def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None

def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("movies_project.test_tmdb.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2

"""def test_get_popular_movies(monkeypatch):
    #lista zwracana przez przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']
    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    responce = requests_mock.return_value
    #przysłaniamy wynik wywołania metody .json()
    responce.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_popular_movies(list_type='popular')
    assert movies_list == mock_movies_list"""

def test_get_single_movie(monkeypatch):
    #lista zwracana przez przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1']
    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    responce = requests_mock.return_value
    #przysłaniamy wynik wywołania metody .json()
    responce.json.return_value = mock_movies_list
    monkeypatch.setattr("movies_project.tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_single_movie(movie_id=1)
    assert movies_list == mock_movies_list

def test_get_movie_images(monkeypatch):
    mock_movies_list = ['Movie 1', 'Movie 2']
    requests_mock = Mock()
    responce = requests_mock.return_value
    responce.json.return_value = mock_movies_list
    monkeypatch.setattr("movies_project.tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_movie_images(movie_id=1)
    assert movies_list == mock_movies_list

def test_get_single_movie_cast(monkeypatch):
    mock_movies_list = [{'adult': False, 'gender': 0, 'id': 1426170, 'known_for_department': 'Acting', 'name': 'Johnny Sachon', 'original_name': 'Johnny Sachon', 'popularity': 0.612, 'profile_path': None, 'cast_id': 4, 'character': 'Issac', 'credit_id': '5f4c7f0a223a8b0038af579a', 'order': 1}]
    requests_mock = Mock()
    responce = requests_mock.return_value
    responce.json.return_value = mock_movies_list
    monkeypatch.setattr("movies_project.tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_single_movie_cast(movie_id=725273, how_many=1)
    assert movies_list == mock_movies_list
