from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})


@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}

@app.post("/logs")
async def post_log(log: str) :
    return "Ton log '" + log + "' a bien été post"