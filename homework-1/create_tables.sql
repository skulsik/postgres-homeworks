-- SQL-команды для создания таблиц
CREATE DATABASE north;
CREATE TABLE employees_data
(
    employee_id serial PRIMARY KEY,
	first_name varchar(15) NOT NULL,
	last_name varchar(15) NOT NULL,
    title varchar(100) NOT NULL,
	birth_date date,
	notes text
);
CREATE TABLE customers_data
(
    customer_id varchar(5) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(50) NOT NULL
);
CREATE TABLE orders_data
(
	order_id serial PRIMARY KEY,
    customer_id varchar(5) REFERENCES customers_data(customer_id) NOT NULL,
	employee_id int NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(30)
);