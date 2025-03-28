import sqlite3

def get_tasks(conn=None):
    should_close = False
    if conn is None:
        conn = sqlite3.connect('tasks.db')
        should_close = True
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    if should_close:
        conn.close()
    return tasks

def create_task(task_name, task_description, conn=None):
    should_close = False
    if conn is None:
        conn = sqlite3.connect('tasks.db')
        should_close = True
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (name, description) VALUES (?, ?)", 
                  (task_name, task_description))
    conn.commit()
    if should_close:
        conn.close()

def update_task(task_id, new_name, new_description, conn=None):
    should_close = False
    if conn is None:
        conn = sqlite3.connect('tasks.db')
        should_close = True
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET name = ?, description = ? WHERE id = ?", 
                  (new_name, new_description, task_id))
    conn.commit()
    if should_close:
        conn.close()

def delete_task(task_id, conn=None):
    should_close = False
    if conn is None:
        conn = sqlite3.connect('tasks.db')
        should_close = True
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    if should_close:
        conn.close()