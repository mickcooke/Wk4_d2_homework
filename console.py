import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository
artist_repository.delete_all()
album_repository.delete_all()




artist_1 = Artist("David", "Bowie")
artist_repository.save(artist_1)
artist = artist_repository.select_all()



album_1 = Album("Hunky Dory", "Rock", artist_1)
album_repository.save(album_1)
album = album_repository.select_all()






