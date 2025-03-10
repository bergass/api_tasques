from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate


import sqlite3

def get_tasks():
    # Connexió a la base de dades
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Consulta per obtenir totes les tasques
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    # Tancar la connexió
    conn.close()

    return tasks



def create_task(task_name, task_description):
    # Connexió a la base de dades
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Inserir la tasca a la taula de tasques
    cursor.execute("INSERT INTO tasks (name, description) VALUES (?, ?)", (task_name, task_description))

    # Guardar els canvis
    conn.commit()

    # Tancar la connexió
    conn.close()



def update_tasks(db: Session, task_id: int, task_update: TaskUpdate):
    """
    Input:
        db: database session
    Output:
        Updated some task fields
    """
    # TODO: El vostre codi va aqui
    pass


def delete_tasks(db: Session, task_id: int):
    """
    Input:
        db: database session
    Output:
        Return delete task
    """
    # TODO: El vostre codi va aqui
    pass
