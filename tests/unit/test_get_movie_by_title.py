# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_get_movie_by_title():
    test_movie = get_movie_repository()
    test_movie.create_movie("Star Wars Episode 3", "George Lucas", 5)
    get_title = test_movie.get_movie_by_title("Star Wars Episode 3")
    
    assert get_title.title == "Star Wars Episode 3"
    assert get_title.director == "George Lucas"
    assert get_title.rating == 5
    

