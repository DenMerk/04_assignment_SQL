create table if not exists artist (
	id serial primary key,
	nickname varchar(100)
);

alter table artist 
	add constraint artist_name_unique unique(nickname);

create table if not exists genre (
	id serial primary key,
	genre_name varchar(50) unique not null
);

create table if not exists GenreArtist (
	genre_id integer references genre(id),
	artist_id integer references artist(id),
	constraint artist_pk primary key (genre_id, artist_id)
);

create table if not exists album (
	id serial primary key,
	album_name varchar(120) not null,
	year_of_issue date
);

create table if not exists album_artist (
	id_album integer references album(id),
	id_artist integer references artist(id),
	constraint album_pk primary key (id_album, id_artist)
);

create table if not exists track (
	id serial primary key,
	track_name varchar(150) not null,
	duration numeric(3, 2) not null,
	id_album integer references album(id)
);

create table if not exists collection (
	id serial primary key,
	collection_name varchar(150) not null,
	year_of_issue date not null
);

create table if not exists track_collection (
	id_track integer references track(id),
	id_collection integer references collection(id),
	constraint track_pk primary key (id_track, id_collection)
);



