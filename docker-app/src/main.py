from fastapi import FastAPI, status
from database import *
from model import Logs_API
from ai_request import make_ai_call

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}

@app.post("/logs", status_code=status.HTTP_201_CREATED)
async def post_log(log: str) :

    db = SessionLocal()

    prompt = "Fais un mini rapport en une seule phrase du log que tu reçois." \
    "Voici le log : " + log

    ia_response = make_ai_call(prompt=prompt)    

    try :
        log = Logs_API(description=log, ia_response=ia_response)
        db.add(log)
        db.commit()
    except :
        db.rollback()
        raise
    finally :
        db.close()

    return "Log created."