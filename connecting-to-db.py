import sqlite3
import pandas as pd

# Section 1: Connecting to the Database using sqlite3
print("\n--- SECTION 1: CONNECTING TO DATABASE ---\n")

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

# Section 2: Viewing the List of Tables
print("\n--- SECTION 2: VIEWING TABLE NAMES ---\n")

# Execute the query to get table names
cur.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""")
# Fetch the result and store it in table_names
table_names = cur.fetchall()
print("Table names in the database:")
print(table_names)

# Section 3: Selecting All Data from the offices Table
print("\n--- SECTION 3: SELECTING ALL DATA FROM OFFICES TABLE ---\n")

cur.execute("""SELECT * FROM offices;""")
office_data = cur.fetchall()
print("All office data:")
print(office_data)

# Alternative approach combining execute and fetchall
print("\n--- ALTERNATIVE APPROACH ---\n")

office_data = cur.execute("""SELECT * FROM offices;""").fetchall()
print("All office data (alternative approach):")
print(office_data)

# Section 4: Viewing the Column Names from the offices Table
print("\n--- SECTION 4: VIEWING COLUMN NAMES ---\n")

cur.execute("""SELECT * FROM offices;""").fetchall()
print("Column descriptions:")
print(cur.description)

# Section 5: Combining steps to create a pandas DataFrame
print("\n--- SECTION 5: CREATING PANDAS DATAFRAME ---\n")

df = pd.DataFrame(
    data=cur.execute("""SELECT * FROM offices;""").fetchall(),
    columns=[x[0] for x in cur.description]
)
print("DataFrame from offices table:")
print(df)

# Section 6: Using pandas with sqlite3
print("\n--- SECTION 6: USING PANDAS WITH SQLITE3 ---\n")

# Close the previous connection
conn.close()

# Create a new connection for pandas
conn = sqlite3.connect("data.sqlite")

# Get table names using pandas
print("Table names using pandas:")
df_tables = pd.read_sql("""SELECT name FROM sqlite_master WHERE type = 'table';""", conn)
print(df_tables)
print(f"Type of result: {type(df_tables)}")

# Get offices data using pandas
print("\nOffices data using pandas:")
office_data_pd = pd.read_sql("SELECT * FROM offices;", conn)
print(office_data_pd)

# Close the connection
conn.close()
print("\nConnection closed.")