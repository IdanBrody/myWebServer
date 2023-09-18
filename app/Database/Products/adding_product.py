from Database.MySQL_Connection import connect_to_database


def add_product():
    product_name = input("Enter product name\n")
    product_link = input("Enter product image link\n")
    vendor = input("Enter Vendor name\n")
    category = input("Enter Category\n")
    price = int(input("Enter price\n"))
    gender = input("Enter gender: Male/Female/Unisex\n")

    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO products (product_name, product_link, vendor, category, price, gender) VALUES (%s, %s, %s, " \
            "%s, %s, %s)"
    values = (product_name, product_link, vendor, category, price, gender)


    try:
        cursor.execute(query, values)
        connection.commit()
        print("Product added successfully")
    except Exception as ex:
        connection.rollback()
        print("An Error occured while adding the product to the database", str(ex))
    finally:
        cursor.close()
        connection.close()
    pass
add_product()