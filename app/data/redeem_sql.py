import sqlite3
from datetime import datetime, date

try:
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    # Dropping the 'voucher_model' table if it exists
    cursor.execute('''DROP TABLE IF EXISTS redeem_model''')

    # Creating a table named 'voucher_model'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS redeem_model (
            id INTEGER PRIMARY KEY,
            created_date DATE,
            voucher_code TEXT,
            user_id TEXT,
            transaction_id TEXT,
            staff_id TEXT,
            products_redeemed TEXT,
            amount REAL,
            discount REAL,
            net_amount REAL
        )
    ''')
    
    # Inserting sample redemption data with amount, discount, and net_amount
    redemption_data = [
        # Redemption 1
        (date(2023, 10, 30), 'V0001', 'user_1', 'transaction_1', 'staff_1', 'product_b', 10, 10.0, 140.0),
    
        # Redemption 2
        (date(2023, 11, 30), 'V0002', 'user_2', 'transaction_2', 'staff_2', 'product_b, product_c', 10, 5.0, 75.0),
    
        # Redemption 3
        (date(2024, 11, 15), 'V0003', 'user_3', 'transaction_3', 'staff_3', 'product_c, product_d', 5, 20.0, 180.0),
    ]
    
    cursor.executemany('''
        INSERT INTO redeem_model (created_date, voucher_code, user_id, transaction_id, staff_id, products_redeemed, amount, discount, net_amount)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', redemption_data)
    
    # Committing the changes
    conn.commit()
    print("Sample redemption data with amount, discount, and net_amount inserted successfully.")

    print("Sample vouchers inserted successfully.")

except Exception as e:
    print(e)

finally:
    # Closing the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
