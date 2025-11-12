class Movie:
    def __init__(self, title, director, rental_price):
        self.title = title
        self.director = director
        self.rental_price = rental_price
        self.is_rented = False

    def __str__(self):
        status = "Rented" if self.is_rented else "Available"
        return f'"{self.title}" by {self.director} - ${self.rental_price:.2f} ({status})'


class Rental:
    def __init__(self):
        self.movies = []
        self.total_income = 0.0

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f'Added movie: {movie.title}')

    def rent_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                if not movie.is_rented:
                    movie.is_rented = True
                    self.total_income += movie.rental_price
                    print(f'You rented "{movie.title}" for ${movie.rental_price:.2f}')
                    return
                else:
                    print(f'Sorry, "{movie.title}" is already rented.')
                    return
        print(f'Movie "{title}" not found.')

    def return_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                if movie.is_rented:
                    movie.is_rented = False
                    print(f'You returned "{movie.title}". Thank you!')
                    return
                else:
                    print(f'"{movie.title}" was not rented.')
                    return
        print(f'Movie "{title}" not found.')

    def get_rented_movies(self):
        return [m for m in self.movies if m.is_rented]

    def get_total_income(self):
        return self.total_income

    @property
    def list_all_movies(self):
        print("\nMovie List:")
        for movie in self.movies:
            print(movie)


m1 = Movie("Inception", "Christopher Nolan", 4.99)
m2 = Movie("Interstellar", "Christopher Nolan", 5.99)
m3 = Movie("The Matrix", "Lana Wachowski", 3.99)

rental = Rental()

rental.add_movie(m1)
rental.add_movie(m2)
rental.add_movie(m3)

rental.rent_movie("Inception")
rental.rent_movie("The Matrix")
rental.rent_movie("Inception")
rental.return_movie("The Matrix")
rental.list_all_movies

print(f"\nTotal income: ${rental.get_total_income():.2f}")
