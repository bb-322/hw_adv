import sqlite3
from dateutil.parser import parse
from datetime import datetime, date

class User:
    def __init__(self, name:str, surname:str, lastname:str, birthday_str:str, email:str):
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self.birthday = parse(birthday_str).date()
        self.birthday_iso = self.birthday.isoformat()
        self.email = email
    
    def get_full_name(self):
        return f'{self.surname} {self.name} {self.lastname}'
    
    def get_short_name(self):
        return f'{self.surname} {self.name[:1]}. {self.lastname[:1]}.'
    
    def get_age(self):
        today = date.today()
        age = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
        return age
    
    def __str__(self):
        return f'{self.get_full_name()} {self.birthday_iso}'

conn = sqlite3.connect("users.sqlite3")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

users = []

def create_table():
    query = '''
        CREATE TABLE IF NOT EXISTS Users (
        name VARCHAR(255),
        surname VARCHAR(255),
        last_name VARCHAR(255),
        birthday DATETIME,
        email VARCHAR(255)
        );
        '''
    cursor.execute(query)
    conn.commit()

create_table()

def add_hooman_to_db(name:str, surname:str, lastname:str, birthday_str:str, email:str):   
    birthday = parse(birthday_str).date()
    birthday_formatted = birthday.isoformat()
    
    query = f'''
        INSERT INTO Users (name, surname, last_name, birthday, email) VALUES(?,?,?,?,?)
        '''
    cursor.execute(query, (name, surname, lastname, birthday_formatted, email))
    conn.commit()
    users.append(User(name, surname, lastname, birthday_str, email))



def find_by_name(name:str):
    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        if row["name"] == name:
            result.append(User(
                row["name"],
                row["surname"],
                row["last_name"],
                row["birthday"],
                row["email"]
            ))
    return result

def find_by_surname(surname:str):
    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        if row["surname"] == surname:
            result.append(User(
                row["name"],
                row["surname"],
                row["last_name"],
                row["birthday"],
                row["email"]
            ))
    return result

def find_by_email(email:str):
    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        if row["email"] == email:
            result.append(User(
                row["name"],
                row["surname"],
                row["last_name"],
                row["birthday"],
                row["email"]
            ))
    return result

add_hooman_to_db('test_subject', 'test_subject', 'test_subject', '12-12-1221', 'emal')

print(find_by_name('test_subject')[0])
print(find_by_surname('test_subject')[0])
print(find_by_email('emal')[0])