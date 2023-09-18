from Database.MySQL_Connection import connect_to_database


def remove_user():
    pass


def print_all_users():
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT username FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    for user in result:
        print(user[0])


functions = {
     0: "exit",
     1: print_all_users,
     2: remove_user
 }


def print_functions():
    print("0: exit")
    print("1: Print all users")
    print("2: Remove user")


choice = 400
while (choice != 0):
    print_functions()
    choice = int(input("Choose action\n"))
    functions[choice]()

