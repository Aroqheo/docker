from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Moist 守护者已激活", "code": 200}
