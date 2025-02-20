CREATE TABLE author (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        );
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE type (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        );
CREATE TABLE cantica (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
        );
CREATE TABLE divine_comedy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cantica_id INTEGER,
            canto INTEGER,
            start_verse INTEGER,
            end_verse INTEGER,
            text TEXT,
            author_id INTEGER,
            type_id INTEGER,
            UNIQUE(cantica_id, canto, start_verse, end_verse, author_id, type_id) 
        );
CREATE TABLE verse_mappings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cantica_id INTEGER,
            canto INTEGER,
            start_verse INTEGER,
            end_verse INTEGER,
            cumulative_indices TEXT,
            UNIQUE(cantica_id, canto, start_verse, end_verse)
        );
