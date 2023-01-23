import sqlite3
import json
from models import Owner, Snake, Species


def all(resource):
    # Open a connection to the database
    with sqlite3.connect("./snake.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        if resource == 'species':
            db_cursor.execute("""
            SELECT
                s.id,
                s.name
            FROM Species s
            """)

            # Initialize an empty list to hold all animal representations
            species = []

            # Convert rows of data into a Python list
            dataset = db_cursor.fetchall()

            # Iterate list of data returned from database
            for row in dataset:

                # Create an animal instance from the current row.
                # Note that the database fields are specified in
                # exact order of the parameters defined in the
                # Animal class above.
                single_species = Species(row['id'], row['name'])

                # Add the dictionary representation of the animal to the list
                species.append(single_species.__dict__)

            return species

        if resource == 'snakes':
            db_cursor.execute("""
            SELECT
                s.id,
                s.name,
                s.owner_id,
                s.species_id,
                s.gender,
                s.color
            FROM Snakes s
            """)

            # Initialize an empty list to hold all animal representations
            snakes = []

            # Convert rows of data into a Python list
            dataset = db_cursor.fetchall()

            # Iterate list of data returned from database
            for row in dataset:

                # Create an animal instance from the current row.
                # Note that the database fields are specified in
                # exact order of the parameters defined in the
                # Animal class above.
                snake = Snake(row['id'], row['name'], row['owner_id'],
                              row['species_id'], row['gender'], row['color'])

                # Add the dictionary representation of the animal to the list
                snakes.append(snake.__dict__)

            return snakes

        if resource == 'owners':
            db_cursor.execute("""
            SELECT
                o.id,
                o.first_name,
                o.last_name,
                o.email
            FROM Owners o
            """)

            # Initialize an empty list to hold all animal representations
            owners = []

            # Convert rows of data into a Python list
            dataset = db_cursor.fetchall()

            # Iterate list of data returned from database
            for row in dataset:

                # Create an animal instance from the current row.
                # Note that the database fields are specified in
                # exact order of the parameters defined in the
                # Animal class above.
                owner = Owner(row['id'], row['first_name'],
                              row['last_name'], row['email'])

                # Add the dictionary representation of the animal to the list
                owners.append(owner.__dict__)

            return owners


def retrieve(resource, id):
    with sqlite3.connect("./snake.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        if resource == 'species':
            db_cursor.execute("""
            SELECT
                s.id,
                s.name
            FROM Species s
            WHERE s.id = ?
            """, (id, ))

            # Load the single result into memory
            data = db_cursor.fetchone()

            # Create an animal instance from the current row
            single_species = Species(data['id'], data['name'])

            return single_species.__dict__

        if resource == 'snakes':

            db_cursor.execute("""
            SELECT
                s.id,
                s.name,
                s.owner_id,
                s.species_id,
                s.gender,
                s.color
            FROM Snakes s
            WHERE s.id = ?
            """, (id, ))

            # Load the single result into memory
            data = db_cursor.fetchone()

            # Create an animal instance from the current row
            snake = Snake(data['id'], data['name'], data['owner_id'],
                          data['species_id'], data['gender'], data['color'])

            if snake.species_id == 2:
                return []
            elif snake is not None:
                return snake.__dict__
            

        if resource == 'owners':
            db_cursor.execute("""
            SELECT
                o.id,
                o.first_name,
                o.last_name,
                o.email
            FROM Owners o
            WHERE o.id = ?
            """, (id, ))

            # Load the single result into memory
            data = db_cursor.fetchone()

            # Create an animal instance from the current row
            owner = Owner(data['id'], data['first_name'],
                          data['last_name'], data['email'])

            return owner.__dict__


def get_snakes_by_species(species):
    with sqlite3.connect("./snake.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            s.id,
            s.name,
            s.owner_id,
            s.species_id,
            s.gender,
            s.color
        from Snakes s
        WHERE s.species_id = ?
        """, (species, ))

        snakes = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            snake = Snake(
                row['id'], row['name'], row['owner_id'], row['species_id'], row['gender'], row['color'])
            snakes.append(snake.__dict__)

    return snakes


def update(id, new_snake):
    with sqlite3.connect("./snake.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Snakes
            SET
                name = ?,
                owner_id = ?,
                species_id = ?,
                gender = ?,
                color = ?
        WHERE id = ?
        """, (new_snake['name'], new_snake['owner_id'], new_snake['species_id'], new_snake['gender'], new_snake['color'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


def create(resource, new_snake):
    with sqlite3.connect("./snake.sqlite3") as conn:
        db_cursor = conn.cursor()
        if resource == 'snakes':
            db_cursor.execute("""
            INSERT INTO Snakes
                ( name, owner_id, species_id, gender, color )
            VALUES
                ( ?, ?, ?, ?, ?);
            """, (new_snake['name'], new_snake['owner_id'],
                  new_snake['species_id'], new_snake['gender'],
                  new_snake['color'], ))

            id = db_cursor.lastrowid

            new_snake['id'] = id

            return new_snake
