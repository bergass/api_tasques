from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate
import sqlite3 # Importamos la libreria sqlite3


def get_tasks(db: Session):
    """
    Input:
        db: database session
    Output:
        List all tasks
    """
    # TODO: El vostre codi va aqui
    pass


def create_tasks(db: Session, task: TaskCreate):
    """
    Input:
        db: database session
    Output:
        Return the new task
    """
    # TODO: El vostre codi va aqui
    pass


def update_task(task_id, new_name, new_description):
    # Nos conectamos a la base de datos
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor() # Creamos un cursor, para poder ejecutar ordenes

    # Actualizamos la nueva taera con un nuevo nombre, descripcion e id
    cursor.execute("UPDATE tasks SET name = ?, description = ? WHERE id = ?", (new_name, new_description, task_id))

    # Nuestro querido commit (Actualizamos)
    conn.commit()

    # Cerramos conexion 
    conn.close()


def delete_task(task_id):
    # Nos volvemos a conectar a la base de datos
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor() # Creamos un cursor para poder ejecutar comandos

    # Eliminamos la tarea que tenga el ID que hemos decidido
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    # Guardamos los cambios
    conn.commit()

    # Nos vamos
    conn.close()
