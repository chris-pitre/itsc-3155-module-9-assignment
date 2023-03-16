# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import _movie_repo

def test_search_movies_page(test_app: FlaskClient):

    _movie_repo.create_movie("Star Wars Episode Three", "George Lucas", 5)

    response = test_app.get("/movies/search?title=Star+Wars+Episode+3")

    
    assert response.status_code == 200
    assert _movie_repo.get_movie_by_title('Star Wars Episode Three') !=  None

