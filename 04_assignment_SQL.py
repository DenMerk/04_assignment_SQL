import sqlalchemy

db = 'postgresql://denmerk:1234@localhost:5432/assignment_db_third'


def db_connect(database):
    engine = sqlalchemy.create_engine(database)
    connection = engine.connect()
    return connection


def released_albums():
    first_task = db_connect(db).execute("""SELECT album_name, year_of_issue FROM album
                 WHERE year_of_issue = '2018-01-01';
    """).fetchall()
    print(f"These albums are released in 2018: {first_task[0][0]}")


def longest_song():
    second_task = db_connect(db).execute("""SELECT track_name, duration FROM track
    WHERE duration = (
        SELECT MAX (duration)
        FROM track
    );
    """).fetchall()
    print(f"The longest song name is '{second_task[0][0]}', its duration is {second_task[0][1]} min")


def long_tracks():
    track_names = []
    third_task = db_connect(db).execute("""SELECT track_name FROM track
    WHERE duration >= 3.5;
    """).fetchall()
    for track in third_task:
        track_names.append(track[0])
    print(f"These tracks are longer than 3.5 minutes: {track_names}")


def collection_released():
    collection_names = []
    fourth_task = db_connect(db).execute("""SELECT collection_name FROM collection
    WHERE year_of_issue BETWEEN '2018-01-01' AND '2020-01-01';
    """).fetchall()
    for collection in fourth_task:
        collection_names.append(collection[0])
    print(f"These collections are released between 2018 and 2020: {collection_names}")


def one_word_names():
    names = []
    fifth_task = db_connect(db).execute("""SELECT nickname FROM artist
    WHERE nickname NOT LIKE '%% %%';
    """).fetchall()
    for name in fifth_task:
        names.append(name[0])
    print(f"These artists names contain only one word: {names}")


def my_word_tracks():
    track_names_with_my = []
    sixth_task = db_connect(db).execute("""SELECT track_name FROM track
    WHERE track_name iLIKE '%%мой%%';
    """).fetchall()
    for track_my in sixth_task:
        track_names_with_my.append(track_my[0])
    print(f"These track names contain a word 'мой': {track_names_with_my}")


if __name__ == '__main__':
    released_albums()
    longest_song()
    long_tracks()
    collection_released()
    one_word_names()
    my_word_tracks()

