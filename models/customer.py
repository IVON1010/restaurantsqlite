from db import conn, cursor

class Customer:
    TABLE_NAME = "customers"

    def __init__(self, name, phone):
        self.id = None
        self.name = name
        self.phone = phone
        self.created_at = None
        #self.updated_at = None(keeps track of )


    def __repr__(self) -> str:
        return f"<Customer {self.id}, {self.name}, {self.phone}>"


    def save(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (name, phone)
        VALUES (?, ?)
        """

        cursor.execute(sql, (self.name, self.phone))
        conn.commit()

        self.id = cursor.lastrowid

    def inventory(self):
        sql = f"""
        SELECT * FROM inventory
        WHERE id = ?
        """

    @classmethod
    def find_one(cls, id):
        sql = f"""
        SELECT * FROM {cls.TABLE_NAME}
        WHERE id =?
        """

        row = cursor.execute(sql, (id,)).fetchone()
        conn.commit()

        return cls.row_to_instance(row)

    @classmethod
    def row_to_instance(cls, row):
        if row == None:
            return None

        customer = cls(row[1], row[2])
        customer.id = row[0]
        customer.created_at = row[3]
        
        return customer

    @classmethod    
    def create_table(cls):
        sql = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        cursor.execute(sql)
        conn.commit()
        print("created successfully")

    #@classmethod
    # def make_phone_unique(cls):
       # cursor.execute("CREATE UNIQUE INDEX unique_customers_phone ON customers (phone)")
        #conn.commit()



Customer.create_table()
#Customer.make_phone_unique()