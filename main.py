import sqlite3

conn = sqlite3.connect('FairShare.db')
cur = conn.cursor()


def create_groups_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY,
                    owner_id INTEGER,
                    group_name TEXT UNIQUE,
                    description TEXT,
                    category TEXT,
                    currency VARCHAR
                    )""")
    conn.commit()

def create_expense_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY,
                        group_id INTEGER,
                        expense_name TEXT,
                        amount FLOAT,
                        category TEXT,
                        date TEXT,
                        paid_by VARCHAR,
                        paid_for VARCHAR
                        )""")

def create_memberships_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS memberships (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        group_id INTEGER
                        )""")

def create_users_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email VARCHAR(255) UNIQUE NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        CONSTRAINT email_format CHECK (email LIKE '%_@__%.__%')
                    )""")

def create_invitations_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS invitations (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        friend_id INTEGER,
                        group_id INTEGER
                        )""")

def create_profiles_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS profiles (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        first_name TEXT,
                        last_name TEXT,
                        username VARCHAR
                        )""")


def insert_user(email, password):
    try:
        cur.execute("""INSERT INTO users (email, password)
                        VALUES (?, ?)""", (email, password))
        conn.commit()
        print("User added successfully!")
    except sqlite3.IntegrityError:
        print("User with the provided email already exists.")


def delete_all_user():
    cur.execute("DELETE FROM users")
    conn.commit()

def insert_group(id, owner_id, group_name, description, category, currency):
    try:
        cur.execute("""INSERT INTO groups (id, owner_id, group_name, description, category, currency)
                        VALUES (?, ?, ?, ?, ?, ?)""", (id, owner_id, group_name, description, category, currency))
        conn.commit()
        print("Group added successfully!")
    except sqlite3.IntegrityError:
        print("Group with the provided name already exists.")

def insert_expense(group_id, expense_name, amount, category, date, paid_by, paid_for):
    cur.execute("""INSERT INTO expenses (group_id, expense_name, amount, category, date, paid_by, paid_for)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""", (group_id, expense_name, amount, category, date, paid_by, paid_for))
    conn.commit()

def delete_group(group_id):
    cur.execute("""DELETE FROM groups WHERE id = ?""", (group_id,))
    conn.commit()

def get_expense_by_name(expense_name):
    cur.execute("SELECT * FROM expenses WHERE expense_name = ?", (expense_name,))
    return cur.fetchall()

# You can add more functions here for interacting with the database
create_groups_table()



# Remember to close the connection when done
conn.close()
