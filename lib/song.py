class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class tracking
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls):
        if cls.genres is None:
            cls.genres = []
        if cls._instance_genre() not in cls.genres:
            cls.genres.append(cls._instance_genre())
    
    @classmethod
    def add_to_artists(cls):
        if cls.artists is None:
            cls.artists = []
        if cls._instance_artist() not in cls.artists:
            cls.artists.append(cls._instance_artist())
    
    @classmethod
    def add_to_genre_count(cls):
        if cls.genre_count is None:
            cls.genre_count = {}
        genre = cls._instance_genre()
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
    
    @classmethod
    def add_to_artist_count(cls):
        if cls.artist_count is None:
            cls.artist_count = {}
        artist = cls._instance_artist()
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
    
    # Helper methods to get current instance's genre and artist
    @classmethod
    def _instance_genre(cls):
        # Get the genre of the current instance
        # This assumes the method is called from within __init__
        return cls._current_instance.genre
    
    @classmethod
    def _instance_artist(cls):
        # Get the artist of the current instance
        return cls._current_instance.artist
    
    # Store the current instance for helper methods
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls._current_instance = instance
        return instance