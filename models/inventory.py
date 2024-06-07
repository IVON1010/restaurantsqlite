from db import conn, cursor

class Inventory:
    TABLE_NAME = "inventory"

    def __init__(self, customer_id, total):
        self.id = None
        self.customer_id = customer_id
        self.total = total
        self.Created_at = None

    def __repr__(self) -> str:
        return f"<Order {self.id}, {self.customer_id}, {self.total}>"

    def save(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (customer_id, total)
        VALUES (?, ?)
        """

        cursor.execute(sql, (self.customer_id, self.total))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def row_to_instance(cls, row):
        if row == None:
            return None

        inventory = cls(row[1], [2])
        inventory.id = row[0]
        inventory.Created_at = row[3]

        return inventory

    @classmethod
    def create_table(cls):
        sql = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT NOT NULL,
            total INTEGER
            Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        cursor.execute(sql)
        conn.commit()
        print("order table created")

    @classmethod
    def drop_table(self):
        cursor.execute("DROP TABLE IF EXISTS menus")
        conn.commit()
        

Inventory.create_table()
#Order.drop_table()