import sqlite3

connection = sqlite3.connect("names.sqlite")

# Bootstrap Version 0
version_table_name = "DB_VERSION"
version_table_column = "version"
version_table = connection.execute(
    f"SELECT name FROM sqlite_master WHERE type='table' AND name='{version_table_name}';"
).fetchone()
VERSION = 0
if version_table is None:
    connection.execute(f"DROP TABLE IF EXISTS {version_table_name};")
    connection.execute(
        f"CREATE TABLE {version_table_name} ({version_table_column} INT);"
    )
    connection.execute(
        f"INSERT INTO {version_table_name} ({version_table_column}) VALUES ({VERSION})"
    )
    connection.commit()
else:
    VERSION = connection.execute(
        f"SELECT {version_table_column} FROM {version_table_name}"
    ).fetchone()[0]


def set_db_version(new_version):
    """Set migration version of database."""
    global VERSION
    connection.execute(
        f"UPDATE {version_table_name} SET {version_table_column} = {new_version}"
    )
    connection.commit()
    VERSION = new_version


# Contacts table
if VERSION < 1:
    CONTACTS_TABLE = "CONTACTS"
    connection.execute(f"DROP TABLE IF EXISTS {CONTACTS_TABLE};")
    connection.execute(
        f"""CREATE TABLE {CONTACTS_TABLE} (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       first TEXT,
                       last TEXT,
                       phone TEXT,
                       email TEXT
        );"""
    )
    set_db_version(1)
