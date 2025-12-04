class Song:
       # class attributes (shared by all song objects)
    count = 0                   # total number of songs created
    genres = []                 # list of unique genres
    artists = []                # list of unique artists
    genre_count = {}            # counts of songs per genre, e.g. {"Rap": 5}
    artists_count = {}          # counts of songs per artist, e.g. {"Beyonce": 17}
    artist_count = {}           # alias so tests that use 'artist_count' still work

    def __init__(self, name, artist, genre):
        # instance attributes (specific to each song)
        self.name = name
        self.artist = artist
        self.genre = genre

        # when a new song is created, update the class-level information
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        #increments the total song count
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        #adds the genre to the genres list
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        #adds the artist to the artists list
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        #updates the genre_count dictionary
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
      
        # update artists_count
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1

        # keep artist_count in sync (so Song.artist_count["Jay Z"] works)
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1