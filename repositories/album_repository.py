import pdb
from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository 

def select_all():  
    # pdb.set_trace()
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)


    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(
                row['title'], 
                row['genre'],
                artist,
                row['id'])
        
        albums.append(album)
    return albums

def select(id):
    task = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result["artist_id"])
        album = Album(
                result['title'], 
                result['genre'],
                artist,
                result['id'])

        
        return album

def save(album):
    # sql statement like INSERT INTO
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values =[album.title, album.genre, album.artist.id] 
    # pass it into run_sql()
    # pdb.set_trace()
    result = run_sql(sql, values)
    id = result [0]["id"] 
    album.id = id
    return album  

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql) 

def delete(id):
    sql ="DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# def update(task):
#     sql ="UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [task.description, task.user.id, task.duration, task.completed, task.id]
#     run_sql(sql, values)

# def tasks_for_user(user):
#     tasks =[]

#     sql = "SELECT * FROM tasks WHERE user_id =%s"
#     values = [user.id]
#     results = run_sql(sql, values)

#     for row in results:
#         task = Task(row["description"], user, row["duration"], row["completed"], row["id"])
#         tasks.append(task)
#     return tasks 