import pymysql
#
# Function to create a connection to mysql database
def create_connection():
    return pymysql.connect(
        # host='host.docker.internal',
        # host='172.17.0.2',
        # host='mysqldb',
        host='localhost',
        user='root',
        password='root',
        charset='utf8',
        db='userinfo'
    )

# function to create a table to store names if it doesn't exist
def create_table(connection):
    cursor = connection.cursor()
    create_query = """
        CREATE TABLE IF NOT EXISTS names (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        )
    """
    cursor.execute(create_query)
    connection.commit()
    cursor.close()

# function to insert a name into the database
def insert_name(connection, name):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO names (name) VALUES (%s)", (name,)
    )
    connection.commit()
    cursor.close()

# function to fetch all names from the database
def fetch_all_names(connection):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT name FROM names"
    )
    names = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return names

# main function
def main():
    connection = create_connection()
    create_table(connection)

    while True:
        print("1. Add name")
        print("2. Show name")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            insert_name(connection, name)
        elif choice == "2":
            names = fetch_all_names(connection)
            if names:
                print("Names in database: ")
                for name in names:
                    print(name)
            else:
                print("No names found in database")
        elif choice == "3":
            print("GoodBye!!")
            break
        else:
            print("Invalid choice")

    connection.close()

if __name__ == "__main__":
    main()

# Database connection parameters
# host = "localhost"
# user = "root"
# password = "root"
# database = "userinfo"
#
# connection = None  # Initialize the connection variable
#
#
# try:
#     # Connect to the database
#     connection = pymysql.connect(host=host, user=user, password=password, database=database)
#     print("Connected to the database!")
#
#     # Create a cursor object
#     cursor = connection.cursor()
#
#     # CREATE: Insert a record into a table
#     create_query = "INSERT INTO userinfo (column1, column2) VALUES (%s, %s)"
#     cursor.execute(create_query, ('value1', 'value2'))
#     connection.commit()  # Commit the transaction
#     print("Record inserted successfully!")
#
#     # READ: Fetch records from the table
#     read_query = "SELECT * FROM your_table"
#     cursor.execute(read_query)
#     rows = cursor.fetchall()
#     print("Records retrieved:")
#     for row in rows:
#         print(row)
#
#     # UPDATE: Update a record in the table
#     update_query = "UPDATE your_table SET column2 = %s WHERE column1 = %s"
#     cursor.execute(update_query, ('new_value2', 'value1'))
#     connection.commit()  # Commit the transaction
#     print("Record updated successfully!")
#
#     # DELETE: Delete a record from the table
#     delete_query = "DELETE FROM your_table WHERE column1 = %s"
#     cursor.execute(delete_query, ('value1',))
#     connection.commit()  # Commit the transaction
#     print("Record deleted successfully!")
#
# except pymysql.MySQLError as e:
#     print(f"An error occurred: {e}")
#
# finally:
#     # Ensure the connection is closed
#     if connection:
#         connection.close()
#         print("Connection closed.")