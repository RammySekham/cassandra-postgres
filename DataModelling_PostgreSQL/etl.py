import os
import glob
import psycopg2
import pandas as pd
import settings
from sql_queries import *


def process_song_file(cur, filepath):
    """
    process the json song file to insert song record into SQL table
    """
    
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df.loc[0, ['artist_id', 'artist_name', 'artist_location', 'artist_latitude','artist_longitude']].values.tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    process the json log file to dump data into SQL table
    """
    
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df.loc[:, 'page']=="NextSong"] 

    # convert timestamp column to datetime
    t = pd.to_datetime((df.ts)/1000)
    
    # insert time data records
    time_data = {'t':t, 'hour':t.dt.hour, 'day':t.dt.day, 'week':t.dt.isocalendar().week, 'month':t.dt.month, 'year':t.dt.year, 'weekday':t.dt.weekday}
    column_labels = ['t', 'hour', 'day', 'week', 'month', 'year', 'weekday'] 
    time_df = pd.DataFrame(data=time_data, columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = (df.loc[:, ['userId', 'firstName', 'lastName', 'gender', 'level']])

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (pd.Timestamp(row.ts/1000, unit='s'), row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    process the file based on given func 
    """
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Calling process_data function to process the raw files to insert data into SQL tables
    """
    
    conn = psycopg2.connect(host=settings.host, dbname=settings.new_db, user=settings.user, password=settings.password, port=settings.port)
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()