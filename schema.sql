-- Schema for netflix movie data
PRAGMA foreign_keys=off;

CREATE TABLE IF NOT EXISTS tv_types(
	id integer PRIMARY KEY,
	type_name varchar(255),
	duration_measure varchar(255)
);

CREATE TABLE IF NOT EXISTS countries(
	id integer PRIMARY KEY,
	country_name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS ratings(
	rating_code varchar(255) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS directors(
	id integer PRIMARY KEY,
	name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS actors(
	id integer PRIMARY KEY,
	name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS genres(
	id integer PRIMARY KEY,
	genre_name varchar(255) NOT NULL
);

GO

CREATE TABLE IF NOT EXISTS tv_shows(
	show_id varchar(255) PRIMARY KEY,
	type integer,
	title varchar(255) NOT NULL,
	director integer,
	country integer,
	date_added date,
	release_year integer,
	rating varchar(255),
	duration varchar(255),
	description varchar(4096),

	FOREIGN KEY (type)
		REFERENCES tv_types(id),
	FOREIGN KEY (director)
		REFERENCES directors(id),
	FOREIGN KEY (country)
		REFERENCES countries(id),
	FOREIGN KEY (rating)
		REFERENCES ratings(rating_code)
);

GO

CREATE TABLE IF NOT EXISTS tv_show_actors(
	tv_show varchar(255),
	actor integer,

	PRIMARY KEY (tv_show, actor),

	FOREIGN KEY (tv_show)
		REFERENCES tv_shows(id),
	FOREIGN KEY (actor)
		REFERENCES actors(id)
);

CREATE TABLE IF NOT EXISTS tv_show_genres(
	tv_show varchar(255),
	genre integer,

	PRIMARY KEY (tv_show, genre),

	FOREIGN KEY (tv_show)
		REFERENCES tv_shows(id),
	FOREIGN KEY (genre)
		REFERENCES genres(id)
);

