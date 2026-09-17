from fastapi import FastAPI, status
from database import *
from model import Logs_API
from ai_request import make_ai_call
from sqlalchemy import func
import json

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

@app.get("/health")
async def get_health():
    db = SessionLocal()

    response = "DB active : " + str(db.is_active)

    return response

@app.get("/logs")
async def get_logs(max_count: int):
    db = SessionLocal()

    last_id = db.query(func.max(Logs_API.id_log)).scalar()

    response = [] 

    id = 0  

    while(last_id > 0 and id != max_count) :
        log = db.get(Logs_API, last_id)
        response.append(log)
        last_id-=1
        id+=1

    return response


@app.post("/logs", status_code=status.HTTP_201_CREATED)
async def post_log(log: str) :

    db = SessionLocal()

    # prompt = "Fais un mini rapport en une seule phrase du log que tu reçois." \
    # "Voici le log : " + log

    prompt = "Réponds en format JSON strictement avec la syntaxe suivante :" \
    "{" \
    "\"analysis\" : \"Ton analyse\"," \
    "\"amogus\": \"false ou true\"" \
    "}" \
    "Le champ 'analysis' contient une analyse en une seule phrase du log que tu reçois," \
    "et le 'amogus' est egal à 'True' si le log est suspect, et 'False' sinon." \
    "Voici le log à analyser : " + log

    ai_response = make_ai_call(prompt=prompt)

    jsonParsing = ""
    amogus = False

    try :
        jsonParsing = json.loads(ai_response)
        analysis = jsonParsing["analysis"]
        amogus = jsonParsing["amogus"] == 'True'
    except :    
        analysis = "Une erreur s'est produite : l'IA n'a pas pu analyser ce log."

    try :
        log = Logs_API(description=log, analysis=analysis, amogus=amogus)
        db.add(log)
        db.commit()
    except :
        db.rollback()
        raise
    finally :
        db.close()

    return "Log created."