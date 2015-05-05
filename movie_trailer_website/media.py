# import modules

import webbrowser

# Movie class representing a movie with its attributes title, storyline,
# url to the poster image and url to the youtube trailer.


class Movie():
    'Movie class representing a movie with its essential attributes'

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        'constructor of Movie class'
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        'Opens a webbrowser page with the movies youtube webtraler'
        webbrowser.open(self.trailer_youtube_url)
