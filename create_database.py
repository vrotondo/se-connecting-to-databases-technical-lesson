import sqlite3

# Create and connect to the database
conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

# Create the offices table
cur.execute('''
CREATE TABLE IF NOT EXISTS offices (
    officeCode TEXT PRIMARY KEY,
    city TEXT,
    phone TEXT,
    addressLine1 TEXT,
    addressLine2 TEXT,
    state TEXT,
    country TEXT,
    postalCode TEXT,
    territory TEXT
)
''')

# Sample data for offices table
offices_data = [
    ('1', 'San Francisco', '+1 650 219 4782', '100 Market Street', 'Suite 300', 'CA', 'USA', '94080', 'NA'),
    ('2', 'Boston', '+1 215 837 0825', '1550 Court Place', 'Suite 102', 'MA', 'USA', '02107', 'NA'),
    ('3', 'NYC', '+1 212 555 3000', '523 East 53rd Street', 'apt. 5A', 'NY', 'USA', '10022', 'NA'),
    ('4', 'Paris', '+33 14 723 4404', "43 Rue Jouffroy D'abbans", '', '', 'France', '75017', 'EMEA'),
    ('5', 'Tokyo', '+81 33 224 5000', '4-1 Kioicho', '', 'Chiyoda-Ku', 'Japan', '102-8578', 'Japan'),
    ('6', 'Sydney', '+61 2 9264 2451', '5-11 Wentworth Avenue', 'Floor #2', '', 'Australia', 'NSW 2010', 'APAC'),
    ('7', 'London', '+44 20 7877 2041', '25 Old Broad Street', 'Level 7', '', 'UK', 'EC2N 1HN', 'EMEA')
]

# Insert data into the offices table
cur.executemany('INSERT OR REPLACE INTO offices VALUES (?,?,?,?,?,?,?,?,?)', offices_data)

# Create some additional tables mentioned in the lesson
cur.execute('''CREATE TABLE IF NOT EXISTS orderdetails (orderNumber INTEGER, productCode TEXT, quantityOrdered INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS payments (customerNumber INTEGER, paymentDate TEXT, amount REAL)''')
cur.execute('''CREATE TABLE IF NOT EXISTS customers (customerNumber INTEGER, customerName TEXT, contactLastName TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS orders (orderNumber INTEGER, orderDate TEXT, status TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS productlines (productLine TEXT, textDescription TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS products (productCode TEXT, productName TEXT, productLine TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS employees (employeeNumber INTEGER, lastName TEXT, firstName TEXT)''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created successfully with sample data!")