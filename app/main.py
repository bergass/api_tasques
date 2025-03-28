from fastapi import FastAPI, HTTPException
from crud import get_tasks, create_task, update_task, delete_task
import logging

app = FastAPI()

# Configurar el logger
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@app.get("/tasks")
def read_tasks():
    try:
        return get_tasks()
    except Exception as e:
        logger.error(f"Error reading tasks: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/tasks")
def add_task(name: str, description: str):
    try:
        create_task(name, description)
        return {"message": "Task created successfully"}
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.put("/tasks/{task_id}")
def modify_task(task_id: int, name: str, description: str):
    try:
        update_task(task_id, name, description)
        return {"message": "Task updated successfully"}
    except Exception as e:
        logger.error(f"Error updating task: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    try:
        delete_task(task_id)
        return {"message": "Task deleted successfully"}
    except Exception as e:
        logger.error(f"Error deleting task: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")