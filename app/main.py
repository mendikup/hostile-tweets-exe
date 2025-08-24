import uvicorn
from fastapi import FastAPI
from app.manager import Manager
from app.helpers import convert_bson_types




app = FastAPI()
manager = Manager()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/analysis_information")
def analysis_information():
    results =convert_bson_types(manager.run())
    return results


if __name__=="__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)