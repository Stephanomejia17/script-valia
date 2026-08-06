import pandas as pd
import pyodbc

from database import get_connection

print(pyodbc.drivers())

conn = get_connection()

print("Conexión exitosa")

# query = """
# SELECT
#     name AS DatabaseName
# FROM sys.databases
# ORDER BY name;
# """

# query = """
# SELECT
#     TABLE_SCHEMA,
#     TABLE_NAME
# FROM INFORMATION_SCHEMA.TABLES
# WHERE TABLE_TYPE = 'BASE TABLE'
# ORDER BY TABLE_SCHEMA, TABLE_NAME;
# """

# query = """
# SELECT
#     TABLE_SCHEMA,
#     TABLE_NAME,
#     COLUMN_NAME,
#     DATA_TYPE
# FROM INFORMATION_SCHEMA.COLUMNS
# ORDER BY
#     TABLE_SCHEMA,
#     TABLE_NAME,
#     ORDINAL_POSITION;
# """

# query = """
# SELECT COUNT(*) AS Total
# FROM usuarios_permisos_web;
# """

query = """
SELECT *
FROM usuarios_permisos_web;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()