import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository


album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("David", "Bowie")
artist_repository.save(artist_1)

album_1 = Album("Hunky Dory", "Rock", artist_1)
album_repository.save(album_1)

artists = artist_repository.select_all()

albums = album_repository.select_all()


artist = artist_repository.select(artist_1.id)
album = album_repository.select(album_1.id)
pdb.set_trace()

# album_repository.delete_all()
# artist_repository.delete_all()

# albums = album_repository.select_all()





# albums = album_repository.select_all()
# artists = artist_repository.select_all()









