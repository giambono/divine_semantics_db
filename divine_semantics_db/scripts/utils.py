

def get_or_create_id_sqlite(cursor, table, column, value):
    """
    Retrieves the ID of a record if it exists; otherwise, inserts a new record and returns its ID.

    :param cursor: SQLite cursor object
    :param table: Name of the table (e.g., 'author', 'type')
    :param column: Name of the column to check (e.g., 'name')
    :param value: The value to check for or insert
    :return: ID of the existing or newly inserted record
    """
    query = f"SELECT id FROM {table} WHERE {column} = ?"
    cursor.execute(query, (value,))
    result = cursor.fetchone()

    if result:
        return result[0]  # Return existing ID
    else:
        insert_query = f"INSERT INTO {table} ({column}) VALUES (?)"
        cursor.execute(insert_query, (value,))
        return cursor.lastrowid  # Return new ID