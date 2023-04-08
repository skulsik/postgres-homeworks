import psycopg2


class HeaderOperation:
    """ Преобразует в пригодную sql строку"""
    def __init__(self, header: str = ''):
        self.header_new = header.replace('"', '')

    def __str__(self):
        return self.header_new


class DB_Operations:
    def __init__(self, db_name: str = '', user: str = '', password: str = '', host: str = '', port: str = '') -> None:
        self.db_name: str = db_name
        self.user: str = user
        self.password: str = password
        self.host: str = host
        self.port: str = port

    def SQL_request(self, sql_request: str = '') -> object:
        """ Выполняет SQL запрос """
        # Соединение с БД
        with psycopg2.connect(dbname=self.db_name, user=self.user, password=self.password, host=self.host, port=self.port) as connection:
            # Создание курсора
            with connection.cursor() as cursor:
                # Получение списка всех баз данных
                sql_request_result = cursor.execute(sql_request)
        connection.close()
        return sql_request_result

    def creating_db(self) -> None:
        """ Создает БД, если бд с таким именем не существует"""
        connection = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port)
        connection.autocommit = True
        cursor = connection.cursor()
        # Проверка, существует ли уже база данных
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{self.db_name}'")
        exists = cursor.fetchone()

        # Если база данных не существует, то создаем её
        if not exists:
            cursor.execute(f"CREATE DATABASE {self.db_name}")
            print(f"DB {self.db_name} создана!")
        connection.commit()
        cursor.close()
        connection.close()

    def csv_to_db(self, path: str = '', table_name: str = '') -> None:
        """ Заполняет таблицу в бд из фаила"""
        # Соединение с БД
        connection = psycopg2.connect(dbname=self.db_name, user=self.user, password=self.password, host=self.host, port=self.port)
        # Открытие курсора для выполнения запросов
        cursor = connection.cursor()
        # Чтение файла CSV и создание DataFrame из данных
        with open(path, 'r') as f:
            # Читает заголовок
            header: str = next(f)
            # Передает заголовок, получает кусок sql кода
            sql_str = HeaderOperation(header)

            # Использование copy_expert для вставки данных из файла CSV в таблицу PostgreSQL
            cursor.copy_expert(f"COPY {table_name}({sql_str}) FROM STDIN WITH CSV DELIMITER ','", f)
        connection.commit()
        cursor.close()
        connection.close()
