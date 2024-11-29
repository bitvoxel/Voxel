from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/healthcheck/")
def healthcheck():
    return 'Health - OK'

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.4", port=30000)