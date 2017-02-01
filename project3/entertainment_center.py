# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4",
                        "1995")

avatar = media.Movie("Avatar",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io",
                     "2009")
gone_with_the_wind = media.Movie("Gone with the Wind",
                     "http://a1.att.hudong.com/02/59/01300000167882121489590059133.jpg",
                     "https://www.youtube.com/watch?v=8mM8iNarcRc",
                     "1939")

movies = [toy_story, avatar, gone_with_the_wind]
fresh_tomatoes.open_movies_page(movies)
