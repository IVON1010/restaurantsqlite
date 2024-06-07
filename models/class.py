# ORM
"""
->class can be referenced to a whole db table
-> attributes are columns
-> a class instance can be associated with a table row
"""

import sqlite3

# create a connection to the db
conn = sqlite3.connect("restaurant.sqlite")

# in order to execute sql queries, we need a cursor
cursor = conn.cursor()

create_menus_table_sql = """
    CREATE TABLE IF NOT EXISTS menus (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description VARCHAR NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        preparation_time TEXT NOT NULL
    );
"""

#cursor.execute(create_menus_table_sql)

#cursor.execute("DROP TABLE menus")

class Menu:
    TABLE_NAME = "menus"

    def __init__(self, name, description, price, quantity, preparation_time):
        self.id = None
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.preparation_time = preparation_time

    # return a printable representation of the object
    def __repr__(self) -> str:
        return f"<Menu {self.id}: {self.name}, {self.description}, {self.price}, {self.quantity}, {self.preparation_time}>"

    def save(self):
        """
        the qn marks are known as parameter binding which handles
        sql injections attacks
        """
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name, description, price, quantity, preparation_time)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.description, self.price, self.quantity, self.preparation_time))

        conn.commit()
        self.id = cursor.lastrowid
        print(f"{self.name} created successfully")

    def update(self):
        sql = f"""
        UPDATE {self.TABLE_NAME}
        SET name = ?, description = ?, price = ?, quantity = ?, preparation_time = ?
        WHERE id = ?
        """

        cursor.execute(sql, (self.name, self.description, self.price, self.quantity,
        self.preparation_time, self.id))
        conn.commit()

    def delete(self):
        sql = f"""
        DELETE FROM {self.TABLE_NAME}
        WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()
        # reset id to None
        self.id = None
        print(f"{self.name} with id{self.id} deleted successfully")

    @classmethod
    def find_one(cls, id):
        sql = f"""
        SELECT * FROM {cls.TABLE_NAME}
        WHERE id = ?
        """

        row = cursor.execute(sql, (id,)).fetchone()

        #menu = cls(row[1], row[2], row[3], row[4], row[5])
        #menu.id = row[0]

        if row == None:
            return None

        #return menu
        #return row

        return cls.row_to_instance(row)

    @classmethod
    def row_to_instance(cls, row):
        menu = cls(row[1], row[2], row[3], row[4], row[5])
        menu.id = row[0]

        return menu

    @classmethod
    def find_all(cls):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
        """

        rows = cursor.execute(sql).fetchall()
        
        return rows


    @classmethod
    def create_table(cls):
        cursor.execute(create_menus_table_sql)
        print("Menus table created")
        #commit transaction
        conn.commit()

    @classmethod
    def drop_table(self):
        cursor.execute("DROP TABLE IF EXISTS menus")
        conn.commit()
    
    @classmethod
    def alter_table(cls, type, column_name, data_type = None):
        sql = f" ALTER TABLE {cls.TABLE_NAME} DROP COLUMN {column_name}" if type == "drop" else f"ALTER TABLE {cls.TABLE_NAME} ADD COLUMN {column_name}"

        print(sql)

        cursor.execute(sql)
        conn.commit()

#Menu.alter_table("", "preparation_time")
#Menu.drop_table()
Menu.create_table()

#rnb = Menu("Rice n Beans", "With Avocado", 120, 2, "40 mins")
#rnb.create_table()
#rnb.save()

#rice_n_stew = Menu("Rice n Stew", "With Avocado", 200, 3, "1 hour")
#print(rice_n_stew)

#rice_n_stew.save()

#print(rice_n_stew)

#rice_n_stew.name = "ugali beef"
#rice_n_stew.price = 250
#rice_n_stew.update()

#print(rice_n_stew)


menu_1 = Menu.find_one(2)

print(menu_1)

menus = Menu.find_all()

print(menus)

#menu_1.name = "burger"

#menu_1.update()

#print(menu_1)

#menu_2 = Menu.find_one(1)

#menu_1.name = "Fries"

#menu_1.update()

#print(menu_1)




