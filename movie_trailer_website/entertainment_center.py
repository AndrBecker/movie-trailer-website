# This python script creates the media.Movie objects describing
# the favourite movies and calls fresh_tomatoes open_movies_page
# with the list of the movie objects (which generates the
# fresh_tomatoes.html file and opens it in a webbrowser).

# Import modules

import media
import fresh_tomatoes


# Create media.Movies-objects

avatar = media.Movie(
 "Avatar",
 "A marine on an alien planet",
 "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
 "https://www.youtube.com/watch?v=Ckke5wA0ncM")

onceupon = media.Movie(
 "Once Upon a Time in the West",
 "Harmonica playing gunslinger taking revenge for the death of this brother",
 """https://upload.wikimedia.org/wikipedia/en/a/a2/
Once_upon_a_Time_in_the_West.jpg""",
 "https://www.youtube.com/watch?v=aO_uW_VDsO8")

fitzcarraldo = media.Movie(
 "Fitzcarraldo",
 """Opera-crazed eccentric struggling to build an opera
 in the Amazonian jungle""",
 "https://upload.wikimedia.org/wikipedia/en/a/ae/Fitzcarraldo.jpg",
 "https://www.youtube.com/watch?v=H_OgtTZMSXI")

eraserhead = media.Movie(
 "Eraserhead",
 "Surrealistic horror movie",
 "https://upload.wikimedia.org/wikipedia/commons/1/18/Eraserhead.jpg",
 "https://www.youtube.com/watch?v=J0Eq5GtCYdA")

discreetcharm = media.Movie(
 "The Discreet Charm of the Bourgeoisie",
 """Surrealistic classic about a group of people repeatedly
 trying in vain to dine together""",
 "https://upload.wikimedia.org/wikipedia/en/d/d3/Discreet-charm-poster.jpg",
 "https://www.youtube.com/watch?v=QZfCoTvbXXc")

apocalypsenow = media.Movie(
 "Apocalypse Now",
 """US special agent sent on mission to Vietnam to kill renegade and
 presumed insane US colonel""",
 "https://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",
 "https://www.youtube.com/watch?v=IkrhkUeDCdQ")


# Insert media.Movies-objects in movies list

movies = [avatar, fitzcarraldo, eraserhead, onceupon,
          discreetcharm, apocalypsenow]


# Generate the html-file and open it in a webbrowser

fresh_tomatoes.open_movies_page(movies)
