# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays 
(
songplay_id SERIAL PRIMARY KEY,
start_time timestamp NOT NULL REFERENCES time(start_time), 
user_id int NOT NULL REFERENCES users(user_id), 
level text, 
song_id text REFERENCES songs(song_id), 
artist_id text REFERENCES artists(artist_id), 
session_id int, 
location text, 
user_agent text)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users 
(user_id int PRIMARY KEY, 
first_name text, 
last_name text, 
gender text NOT NULL, 
level text NOT NULL, 
last_start_time timestamp NOT NULL)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs 
(song_id text PRIMARY KEY, 
title text NOT NULL, 
artist_id text NOT NULL, 
year int NOT NULL, 
duration numeric)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists 
(artist_id text PRIMARY KEY, 
name text NOT NULL, 
location text, 
lattitude float8, 
longitude float8)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time 
(start_time timestamp PRIMARY KEY, 
hour int NOT NULL, 
day int NOT NULL, 
week int NOT NULL, 
month int NOT NULL, 
year int NOT NULL, 
weekday int NOT NULL)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT (songplay_id) 
DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level, last_start_time) 
VALUES (%s, %s, %s, %s, %s, %s) 
ON CONFLICT (user_id) 
DO UPDATE SET level = 
    (CASE WHEN EXCLUDED.last_start_time > users.last_start_time 
    THEN EXCLUDED.level ELSE users.level END)
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) 
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (song_id) 
DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, lattitude, longitude) 
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (artist_id) 
DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT (start_time) 
DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id 
FROM songs s 
LEFT JOIN artists a 
    ON s.artist_id = a.artist_id 
WHERE s.title = %s 
    AND a.name = %s 
    AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [time_table_create, user_table_create, song_table_create, artist_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]