from fastapi import FastAPI

app = FastAPI()


@app.get("/center")
async def root():
    return {"message": "Hello World"}