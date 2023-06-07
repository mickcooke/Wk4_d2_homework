import pdb
from db.run_sql import run_sql
from models.artist import Artist

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    #process list of dictionary of users 

    for row in results:
        artist = Artist(
            row['first_name'], 
            row['last_name'], 
            row['id'])
        
        artists.append(artist)
    return artists


def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = Artist(
            result["first_name"],
            result["last_name"],
            result["id"])
        
    return artist

def save(artist):
    sql = "INSERT INTO artists (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values =[artist.first_name, artist.last_name]
    result = run_sql(sql, values)
    id = result [0]["id"]
    artist.id = id 
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql) 

def delete(id):
    sql ="DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(artist):
    sql ="UPDATE artists SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [artist.first_name, artist.last_name, artist.id]
    run_sql(sql, values)

