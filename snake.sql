create table Snakes (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(50),
	owner_id INT,
	species_id INT,
	gender VARCHAR(50),
	color VARCHAR(50)
);
insert into Snakes (id, name, owner_id, species_id, gender, color) values (1, 'Annotée', 2, 2, 'Female', 'Turquoise');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (2, 'Lorène', 1, 1, 'Male', 'Green');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (3, 'Alizée', 8, 1, 'Female', 'Blue');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (4, 'Océane', 7, 1, 'Male', 'Khaki');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (5, 'Almérinda', 4, 4, 'Male', 'Yellow');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (6, 'Athéna', 3, 5, 'Female', 'Violet');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (7, 'Bénédicte', 8, 2, 'Male', 'Mauv');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (8, 'Solène', 2, 3, 'Male', 'Yellow');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (9, 'Aí', 6, 4, 'Female', 'Goldenrod');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (10, 'Andréa', 9, 5, 'Male', 'Turquoise');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (11, 'Noémie', 6, 2, 'Male', 'Crimson');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (12, 'Gwenaëlle', 4, 1, 'Male', 'Puce');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (13, 'Océane', 9, 5, 'Male', 'Turquoise');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (14, 'Bérengère', 5, 2, 'Female', 'Turquoise');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (15, 'Lyséa', 7, 2, 'Male', 'Fuscia');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (16, 'Méghane', 1, 2, 'Male', 'Crimson');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (17, 'Léonore', 5, 1, 'Female', 'Yellow');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (18, 'Anaël', 6, 5, 'Female', 'Puce');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (19, 'Nélie', 7, 1, 'Female', 'Pink');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (20, 'Béatrice', 9, 1, 'Female', 'Green');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (21, 'Gösta', 5, 2, 'Female', 'Mauv');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (22, 'Clélia', 5, 3, 'Male', 'Purple');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (23, 'Méng', 2, 5, 'Female', 'Khaki');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (24, 'Angélique', 2, 1, 'Female', 'Mauv');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (25, 'Aimée', 10, 2, 'Female', 'Pink');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (26, 'Marie-françoise', 2, 1, 'Female', 'Green');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (27, 'Tán', 4, 2, 'Female', 'Teal');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (28, 'Andréanne', 5, 4, 'Female', 'Green');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (29, 'Stéphanie', 8, 5, 'Female', 'Purple');
insert into Snakes (id, name, owner_id, species_id, gender, color) values (30, 'Liè', 7, 1, 'Female', 'Maroon');

DROP TABLE IF EXISTS Snakes;
