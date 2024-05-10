# SATTOROV SHUHRAT N42

import psycopg2


# 1-masala
# db = psycopg2.connect(dbname='project',
#                       user='postgres',
#                       host='localhost',
#                       password='1',
#                       port=5432)
#
# cur = db.cursor()
#
#
# create_table = """CREATE TABLE IF NOT EXISTS product (
#                     id SERIAL PRIMARY KEY,
#                     name VARCHAR(255) NOT NULL,
#                     price NUMERIC(10,2) NOT NULL,
#                     color VARCHAR(255) NOT NULL,
#                     image VARCHAR(255));  """
#
# cur.execute(create_table)
# db.commit()
#
#
# # 2-masala
#
# insert_product = """INSERT INTO product (name, price, color, image) VALUES ('Iphone', 1200, 'titanium');"""
# cur.execute(insert_product)
# db.commit()
#
# select_all_product = """SELECT * FROM product WHERE id = '%s' """
# cur.execute(select_all_product)
#
# update_product = """UPDATE product SET name = '%s', name = '%s', price = '%s', color = '%s', image = '%s' WHERE id = '%s'"""
# cur.execute(update_product)
# db.commit()
#
# delete_product = """DELETE FROM product WHERE id = '%s' """
# cur.execute(delete_product)
# db.commit()


# 3-masala

# alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# class Alphabet:
#     def __init__(self):
#         self.alf = alf
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.alf):
#             x = self.alf[self.index]
#             self.index += 1
#             return x
#         else:
#             raise StopIteration
#
# alphabet = Alphabet()
#
# for x in alphabet:
#     print(x)


# 4-masala

# import threading
# import time
#
# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         time.sleep(1)
#
#
# def print_leters():
#     for i in 'ABCDE':
#         print(i)
#         time.sleep(1)
#
# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_leters)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()



# 5,6 -masala

db_params = {
    'host': 'localhost',
    'database': 'project',
    'user': 'postgres',
    'password': '1',
    'port': 5432
}


class DbConnect:
    def __init__(self, db_params):
        self.db_params = db_params
        self.conn = psycopg2.connect(**self.db_params)

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()



class Product:
    def __init__(self,
                 id: int | None = None,
                 name: str | None = None,
                 price: int | None = None,
                 color: str | None = None,
                 image: str | None = None):
        self.id = id
        self.name = name
        self.price = price
        self.color = color
        self.image = image


    def save(self):
        with DbConnect(db_params) as cur:
            insert_query = 'insert into product (name, price, color, image) values (%s, %s, %s, %s);'
            insert_params = (self.name, self.price, self.color, self.image)
            cur.execute(insert_query, insert_params)
            print('INSERT 0 1')

    def __repr__(self):
        return f'Product({self.id} => {self.name} => {self.price}, {self.color}, {self.image})'

product = Product(name='Iphone', price=1200, color='titanium', image='images/person.jpg')
product.save()
print(Product())
