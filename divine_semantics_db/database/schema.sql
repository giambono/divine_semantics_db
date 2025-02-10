-- Drop existing tables if they exist
DROP TABLE IF EXISTS divine_comedy;
DROP TABLE IF EXISTS type;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS cantica;

-- Table for the three canticas
CREATE TABLE cantica (
                         id INT AUTO_INCREMENT PRIMARY KEY,
                         name VARCHAR(20) UNIQUE NOT NULL
);

-- Insert predefined values
INSERT INTO cantica (name) VALUES ('Inferno'), ('Purgatorio'), ('Paradiso');

-- Table for authors
CREATE TABLE author (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255) UNIQUE NOT NULL
);

-- Table for types (TEXT, commentary, outline)
CREATE TABLE type (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      name VARCHAR(50) UNIQUE NOT NULL
);

-- Insert predefined values
INSERT INTO type (name) VALUES ('TEXT'), ('commentary'), ('outline');

CREATE TABLE weighted_embeddings (
                                     cantica_id INT,
                                     canto INT,
                                     start_verse INT,
                                     end_verse INT,
                                     type_id INT,
                                     model_name VARCHAR(50), -- Name of the embedding model
                                     weight_set_name VARCHAR(50), -- Name of the weight set
                                     weighted_embedding JSON, -- Store embeddings as JSON
                                     PRIMARY KEY (cantica_id, canto, start_verse, end_verse, model_name, weight_set_name)
);

-- Main table linking everything
CREATE TABLE divine_comedy (
                               id INT AUTO_INCREMENT PRIMARY KEY,
                               cantica_id INT NOT NULL,
                               canto INT NOT NULL CHECK (canto BETWEEN 1 AND 34),
                               start_verse INT NOT NULL,
                               end_verse INT NOT NULL,
                               text TEXT NOT NULL,
                               author_id INT NOT NULL,
                               type_id INT NOT NULL,
                               UNIQUE (cantica_id, canto, start_verse, end_verse, author_id, type_id),
                               FOREIGN KEY (cantica_id) REFERENCES cantica(id) ON DELETE CASCADE,
                               FOREIGN KEY (author_id) REFERENCES author(id) ON DELETE CASCADE,
                               FOREIGN KEY (type_id) REFERENCES type(id) ON DELETE CASCADE
);
