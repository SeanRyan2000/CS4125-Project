import model.Movie.Movie as Movie

class NewReleaseMovie(Movie.Movie):

    def __init__(self, title, length, tickets):
        super().__init__(title, length, tickets)
        self.type = "new"

    def getMovieType(self):
        return self.type

    def __call__(self):
        return self
