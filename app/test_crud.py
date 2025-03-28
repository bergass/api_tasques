import sqlite3
import pytest
from crud import get_tasks, create_task, update_task, delete_task

@pytest.fixture
def setup_db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    """)
    
    cursor.execute("INSERT INTO tasks (name, description) VALUES ('Tasca 1', 'Descripció 1')")
    cursor.execute("INSERT INTO tasks (name, description) VALUES ('Tasca 2', 'Descripció 2')")
    conn.commit()

    yield conn
    
    conn.close()

def test_get_tasks(setup_db):
    conn = setup_db
    tasks = get_tasks(conn)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    expected_tasks = cursor.fetchall()
    
    assert tasks == expected_tasks

def test_create_task(setup_db):
    conn = setup_db
    create_task("Nova Tasca", "Nova Descripció", conn)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE name='Nova Tasca'")
    task = cursor.fetchone()
    
    assert task is not None
    assert task[1] == "Nova Tasca"
    assert task[2] == "Nova Descripció"

def test_update_task(setup_db):
    conn = setup_db
    update_task(1, "Tasca Actualitzada", "Descripció Actualitzada", conn)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=1")
    task = cursor.fetchone()
    
    assert task is not None
    assert task[1] == "Tasca Actualitzada"
    assert task[2] == "Descripció Actualitzada"

def test_delete_task(setup_db):
    conn = setup_db
    delete_task(1, conn)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=1")
    task = cursor.fetchone()
    
    assert task is None