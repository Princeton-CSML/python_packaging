from walrus.movies import best_movie


def test_bestmovie1():
    assert best_movie('1972')=='The Godfather'
