class Artist:
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        if self.birth_year >= 0 and self.death_year >= 0:
            print(f"Artist: {self.name} ({self.birth_year} to {self.death_year})")
        elif self.birth_year >= 0 and self.death_year < 0:
            print(f"Artist: {self.name} ({self.birth_year} to present)")
        else:
            print(f"Artist: {self.name} (unknown)")


class Artwork:
    def __init__(self, title="unknown", year_created=-1, artist=None):
        if artist is None:
            artist = Artist()  # Default to an unknown artist if not provided
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        self.artist.print_info()  # Call the print_info of the artist
        print(f"Title: {self.title}, {self.year_created}")


if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    # Create an artist object with the input
    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    # Create an artwork object with the input and the artist object
    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    # Print the artwork info
    new_artwork.print_info()
