import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Post",
                     "http://www,youtube.com/watch?v=-9ceBgWV8io")
print(avatar.storyline)
print(avatar.trailer_youtube_url)
print(media.Movie.VALID_RATINGS)
print('-'*20)
print(media.Movie.__doc__)
print(media.Movie.__name__)    # output the class name
print(media.Movie.__module__)   #output the module name


movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)


