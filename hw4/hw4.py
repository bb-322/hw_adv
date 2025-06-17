import sqlite3
import requests
import json

conn = sqlite3.connect("db.sqlite3")

cursor = conn.cursor()

response = requests.get('https://api.monobank.ua/bank/currency')
curr_info = response.json()

def create_table():
    query = '''
        CREATE TABLE IF NOT EXISTS Payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purpose VARCHAR(255),
        money VARCHAR(255) NOT NULL,
        currency VARCHAR(3) DEFAULT "UAH",
        time DATETIME
        );
        '''
    cursor.execute(query)

create_table()

def outlay():
    summ = ('-') + str(int(input('cost: ')))
    purpose = input('payment purpose: ')
    query = "INSERT INTO Payments (purpose, money, time) VALUES(?,?,datetime('now'))"
    cursor.execute(query, (purpose, summ))
    conn.commit()

def income():
    summ = ('+') + str(int(input('income: ')))
    purpose = input('payment purpose: ')
    query = "INSERT INTO Payments (purpose, money, time) VALUES(?,?,datetime('now'))"
    cursor.execute(query, (purpose, summ))
    conn.commit()

def get_avg_rate():
    for item in curr_info:
        if item['currencyCodeA'] == 840 and item['currencyCodeB'] == 980:
            rate_buy = item['rateBuy']
            rate_sell = item['rateSell']
            return (rate_buy + rate_sell) / 2

def uah_to_usd(sum_uah:float|int):
    for item in curr_info:
        if item['currencyCodeA'] == 840 and item['currencyCodeB'] == 980:
            rate = get_avg_rate()
            sum_usd = sum_uah / rate
            return round(sum_usd, 2)

def usd_to_uah(sum_usd:float|int):
    for item in curr_info:
        if item['currencyCodeA'] == 840 and item['currencyCodeB'] == 980:
            rate = get_avg_rate()
            sum_uah = sum_usd * rate
            return round(sum_uah, 2)

def all_to_usd():
    query = '''UPDATE Payments SET currency = "USD" WHERE currency = "UAH"'''
    cursor.execute(query)
    query = '''SELECT id, money FROM Payments'''
    payments_data = cursor.execute(query).fetchall()
    for row in payments_data:
        payment_id = row[0]
        payment = row[1]
        
        sign = payment[0]
        amount = float(payment[1:])
        
        usd_amount = uah_to_usd(amount)
        new_money = sign + str(round(usd_amount, 2))
        
        query_update = "UPDATE Payments SET money = ? WHERE id = ?"
        cursor.execute(query_update, (new_money, payment_id))
    conn.commit()

def all_to_uah():
    query = '''UPDATE Payments SET currency = "UAH" WHERE currency = "USD"'''
    cursor.execute(query)
    query = '''SELECT id, money FROM Payments'''
    payments_data = cursor.execute(query).fetchall()
    for row in payments_data:
        payment_id = row[0]
        payment = row[1]
        
        sign = payment[0]
        amount = float(payment[1:])
        
        uah_amount = usd_to_uah(amount)
        new_money = sign + str(round(uah_amount, 2))
        
        query_update = "UPDATE Payments SET money = ? WHERE id = ?"
        cursor.execute(query_update, (new_money, payment_id))
    conn.commit()

while True:
    print('1 - outlay\n2 - income\n3 - convert everything to USD\n4 - convert everything to UAH\n0 - break')
    operation = int(input())
    match operation:
        case 1:
            outlay()
        
        case 2:
            income()
        
        case 3:
            all_to_usd()
        
        case 4:
            all_to_uah()
        
        case 0:
            break
        
        case _:
            print('no such operation')
            continue