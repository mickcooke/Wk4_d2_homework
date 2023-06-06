import unittest
from models.artist import Artist
class TestArtist(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("David", "Bowie")
    
    def test_artist_has_first_name(self):
        self.assertEqual("David", self.artist.first_name)
    
    def test_artist_has_second_name(self):
        self.assertEqual("Bowie", self.artist.last_name)
