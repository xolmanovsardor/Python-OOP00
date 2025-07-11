class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def show_summary(self):
        print(f"{self.title} — {self.genre} janridagi film. Reyting: {self.rating}/10.")

# Test
m = Movie("Inception", "fantastika", 148, 8.8)
m.show_summary()
