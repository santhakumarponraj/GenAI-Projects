import mysql.connector
from ollama import chat


# -------------------------
# Database connection
# -------------------------

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="YOUR_PASSWORD",
    database="hr_database"
)

cursor = connection.cursor()


# -------------------------
# Database schema
# -------------------------

schema = """
Database: hr_database

Table: employees

Columns:
- employee_id
- employee_name
- department
- designation
- joining_date
- salary
- leave_balance

Table: leave_records

Columns:
- leave_id
- employee_id
- leave_type
- start_date
- end_date
- status
"""


# -------------------------
# Question
# -------------------------

question = input("Ask your HR question: ")


# -------------------------
# Generate SQL
# -------------------------

sql_prompt = f"""
You are an SQL assistant.

Convert the user's question into a MySQL SELECT query.

Database schema:

{schema}

Rules:
- Generate ONLY SELECT queries.
- Do not generate INSERT, UPDATE, DELETE, DROP, ALTER or TRUNCATE.
- Use only tables and columns from the schema.
- Do not invent columns.
- Return only SQL.

Question:
{question}
"""

response = chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": sql_prompt
        }
    ]
)

sql = response["message"]["content"].strip()

sql = sql.replace("```sql", "")
sql = sql.replace("```", "")
sql = sql.strip()

print("\nGenerated SQL:")
print(sql)


# -------------------------
# Safety check
# -------------------------

if not sql.lower().startswith("select"):
    raise ValueError("Only SELECT queries are allowed.")


# -------------------------
# Execute SQL
# -------------------------

cursor.execute(sql)

result = cursor.fetchall()

print("\nDatabase Result:")
print(result)


# -------------------------
# Generate final answer
# -------------------------

answer_prompt = f"""
You are an HR assistant.

Answer the user's question using ONLY the database result.

Question:
{question}

Database result:
{result}

Give a concise and accurate answer.
Do not invent information.
"""

response = chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": answer_prompt
        }
    ]
)

print("\nAnswer:")
print(response["message"]["content"])


cursor.close()
connection.close()