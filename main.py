from fastapi import FastAPI

app = FastAPI()

# root
@app.get("/")
async def root():
    return {"message": "Hello Khan"}

# path parameter
@app.get("/items/{id}")
async def getItem(id):
    return {"message": f"This is item with ID: {id}"}

# Query paramters + path parameters
@app.get("/paths/{id}/dummy")
async def getPaths(id, skip: int = 0, limit: int = 10):
    return {"path paramter": f"path Parameter is {id}", "query parameter": f"query paramters are {skip} and {limit}"}