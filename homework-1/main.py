from utils import DB_Operations


# Запрос на создание таблицы employees_data
sql_employees_data = """CREATE TABLE IF NOT EXISTS employees_data(
                                            employee_id serial PRIMARY KEY,
                                            first_name varchar(15) NOT NULL,
                                            last_name varchar(15) NOT NULL,
                                            title varchar(100) NOT NULL,
                                            birth_date date, notes text
                                            );"""

# Запрос на создание таблицы customers_data
sql_customers_data = """CREATE TABLE IF NOT EXISTS customers_data(
                                            customer_id varchar(5) PRIMARY KEY,
                                            company_name varchar(100) NOT NULL,
                                            contact_name varchar(50) NOT NULL
                                            );"""

# Запрос на создание таблицы orders_data
sql_orders_data = """CREATE TABLE IF NOT EXISTS orders_data(
                                            order_id serial PRIMARY KEY,
                                            customer_id varchar(5) REFERENCES customers_data(customer_id) NOT NULL,
                                            employee_id int NOT NULL,
                                            order_date date NOT NULL,
                                            ship_city varchar(30)
                                            );"""

# Экземпляр класса операции БД
db = DB_Operations(db_name='north', user='postgres', password='12345', host='localhost', port='5432')

# Если БД не существует, создает ее
db.creating_db()

# Если таблица employees_data не существует, создает ее
db.SQL_request(sql_request=sql_employees_data)

# Если таблица customers_data не существует, создает ее
db.SQL_request(sql_request=sql_customers_data)

# Если таблица orders_data не существует, создает ее
db.SQL_request(sql_request=sql_orders_data)


"""---------------------- Запись из файлов в таблицы БД ----------------------"""
# Путь к фаилу
path_to_customers_data = "north_data/customers_data.csv"
# Запись файла в БД (таблица customers_data)
db.csv_to_db(path=path_to_customers_data, table_name='customers_data')

# Путь к фаилу
path_to_employees_data = "north_data/employees_data.csv"
# Запись файла в БД (таблица employees_data)
db.csv_to_db(path=path_to_employees_data, table_name='employees_data')

# Путь к фаилу
path_to_orders_data = "north_data/orders_data.csv"
# Запись файла в БД (таблица orders_data)
db.csv_to_db(path=path_to_orders_data, table_name='orders_data')
