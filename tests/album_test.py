import unittest
from models.album import Album
from models.artist import Artist
class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("David", "Bowie")
        self.album = Album("Hunky Dory", "Rock", self.artist)

    def test_has_title(self):
        self.assertEqual("Hunky Dory", self.album.title)
    
    def test_has_genre(self):
        self.assertEqual("Rock", self.album.genre)
    
    def test_has_artist(self):
        self.assertEqual("David", self.album.artist.first_name)