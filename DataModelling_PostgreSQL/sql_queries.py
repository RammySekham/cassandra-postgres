# DROP TABLES

songplay_table_drop = "DROP table songplays"
user_table_drop = "DROP table users"
song_table_drop = "DROP table songs"
artist_table_drop = "DROP table artists"
time_table_drop = "DROP table time"

# CREATE TABLES

songplay_table_create = (""" Create table songplays(
                                    songplay_id serial PRIMARY KEY, 
                                    start_time TIMESTAMP, 
                                    user_id int, 
                                    level text, 
                                    song_id varchar,
                                    artist_id varchar,
                                    session_id int, 
                                    location text, 
                                    user_agent text)
                        """)

user_table_create = (""" Create table users(
                                 user_id int PRIMARY KEY, 
                                 first_name text, 
                                 last_name text, 
                                 gender text, 
                                 level text)
                    """)

song_table_create = (""" Create table songs(
                                song_id varchar PRIMARY KEY, 
                                title text, 
                                artist_id varchar, 
                                year int, 
                                duration float(8))
                    """)

artist_table_create = (""" Create table artists(
                                  artist_id varchar PRIMARY KEY, 
                                  name text, 
                                  location text, 
                                  latitude float(8), 
                                  longitude float(8))
                      """)

time_table_create = (""" Create table time(
                                start_time TIMESTAMP NOT NULL, 
                                hour int, 
                                day int, 
                                week int, 
                                month int, 
                                year int, 
                                weekday int)
                     """)

# INSERT RECORDS

songplay_table_insert = (""" Insert into songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
""" + "Values ( %s, %s, %s, %s, %s, %s, %s, %s)")

user_table_insert =(""" Insert into users(user_id, first_name, last_name, gender, level)
                           Values ( %s, %s, %s, %s, %s)  
                           ON CONFLICT(user_id)
                           DO 
                            UPDATE SET first_name = EXCLUDED.first_name,
                            last_name = EXCLUDED.last_name,
                            gender = EXCLUDED.gender,
                            level = EXCLUDED.level
                          
                    """)

song_table_insert = ("""Insert into songs(song_id, title, artist_id, year, duration)
""" + "Values ( %s, %s, %s, %s, %s)")

artist_table_insert = ("""Insert into artists(artist_id, name, location, latitude, longitude)
                          Values ( %s, %s, %s, %s, %s)  
                          ON CONFLICT(artist_id)
                          DO 
                            UPDATE SET name = EXCLUDED.name,
                            location = EXCLUDED.location,
                            latitude = EXCLUDED.latitude,
                            longitude = EXCLUDED.longitude
                          
                       """)


time_table_insert = ("""Insert into time(start_time, hour, day, week, month, year, weekday)
""" + "Values ( %s, %s, %s, %s, %s, %s, %s)")

# FIND SONGS

song_select = (""" Select song_id, artists.artist_id from artists 
                   Join songs On 
                   songs.artist_id = artists.artist_id 
                   where title = %s and name = %s and duration = %s ;
               """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]