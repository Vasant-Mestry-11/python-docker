import pymysql
# Function to create a connection to mysql database
def create_connection():
    return pymysql.connect(
        # host='host.docker.internal',
        # host='172.17.0.2',
        host='mysqldb',
        # host='localhost',
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