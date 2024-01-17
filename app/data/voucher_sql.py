import sqlite3
from datetime import date

try:
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    # Dropping the 'voucher_model' table if it exists
    cursor.execute('''DROP TABLE IF EXISTS voucher_model''')

    # Creating a table named 'voucher_model'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS voucher_model (
            id INTEGER PRIMARY KEY,
            code TEXT,
            type TEXT,
            value REAL,
            discount REAL,
            expiration_date DATE,
            redemption_limit INTEGER,
            user_restrictions TEXT,
            products TEXT
        )
    ''')

    # Committing the changes
    conn.commit()
    print("Table 'voucher_model' created successfully.")

    # Inserting 20 sample vouchers into the table
    sample_vouchers = [
        # gift/meal/travel voucher for product_b
        ('V0001', 'gift voucher', 100.0, 0, date(2024, 10, 30), 50, 'user_1,user_2', 'product_b'),
        
        # discount voucher for any product
        ('V0002', 'discount voucher', 0, 10, date(2024, 10, 30), 50, 'user_1,user_2', ''),
        
        # cash voucher
        ('V0003', 'cash voucher', 40, 0, date(2024, 10, 30), 1, 'user_1,user_2', ''),
    ]

    cursor.executemany('''
        INSERT INTO voucher_model (code, type, value, discount, expiration_date, redemption_limit, user_restrictions, products)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', sample_vouchers)

    # Committing the changes
    conn.commit()
    print("Sample vouchers inserted successfully.")

except Exception as e:
    print(e)

finally:
    # Closing the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
