from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_healthcheck():
    return {"status": "Green"}
