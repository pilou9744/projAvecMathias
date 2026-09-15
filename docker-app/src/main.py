from fastapi import FastAPI, status
from database import *
from model import Logs_API

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}

@app.post("/logs", status_code=status.HTTP_201_CREATED)
async def post_log(log: str) :

    db = SessionLocal()

    try :
        log = Logs_API(description=log)
        print("YO LES GARS")
        db.add(log)
        db.commit()
        # db.refresh()
    except :
        db.rollback()
        raise
    finally :
        db.close()

    return "Log created."