import sqlite3
import pandas as pd

# connect to the DB
conn = sqlite3.connect('data.sqlite')

# One to many reltionships

##Sales Rep Employees
q = """
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
;
"""
df = pd.read_sql(q, conn)

print("number of results:", len(df))
print("number of results:", df.head()) #displays  only 5 


##Cities for Sales Re Employees

q = """
SELECT firstName, lastName, email,
city
FROM employees
JOIN offices
    USING(officeCode)
WHERE jobTitle = 'Sales Rep'
;
"""
df = pd.read_sql(q, conn)
print("number of results:", len(df))
print("number of results:", df.head()) #displays  only 5 

#More One to Many Relationships
## Product Lines
q ="""
SELECT productLine, textDescription
FROM productlines
;
"""
df =pd.read_sql(q, conn)
print("number of results:", len(df))
print("number of results:", df)

#Joining with Products

q = """
SELECT  productLine, textDescription, productVendor, productDescription
FROM productlines
JOIN products
    USING(productLine)
;
"""
df = pd.read_sql(q, conn)
print("number of results:", len(df))
print("number of results:", df.head()) #displays  only 5 

#Many to Many Relationships
## Just Offices
q = """
SELECT *
FROM offices

;
"""
df = pd.read_sql(q, conn)
print("Number of results", len(df))
print("Number of results", df)

## Just Customers
q = """
SELECT *
FROM customers

;
"""
df = pd.read_sql(q, conn)
print("Number of results", len(df))
print("Number of results", df)

## Joined Offices and Customers
q = """
SELECT *
FROM offices
JOIN customers
    USING(state)

;
"""
df = pd.read_sql(q, conn)
print("Number of results", len(df))
print("Number of results", df)

conn.close()



