
class Movie:
    def __init__(self, title, hero, heroin):
        self.title=title
        self.hero=hero
        self.heroin=heroin
    def info(self):
        print('Movie name :', self.title)
        print('Movie hero :', self.hero)
        print('Movie heroin:', self.heroin)
list_of_movies = []
while True:
    title = input('Enter movie name:')
    hero = input('Enter hero name')
    heroin = input('Enetr heroin name')
    m = Movie(title,hero,heroin)
    list_of_movies.append(m)
    print("Movie added to the list successfully")
    option = input("Do you want to add one more movie details [yes|No]")
    if option.lower() == 'no':
        break

    print ("All movies information")
    print ('#' * 40)
    for movie in list_of_movies:
        movie.info()
        print()

        

















