from fastapi import FastAPI, HTTPException
from django.http import JsonResponse
from pydantic import BaseModel
from typing import Dict
from starlette import status
import uvicorn
app = FastAPI()


@app.get("/hello")
async def get_hello():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def get_hello_name(name: str):
    return {"message": "Hello {}".format(name)}


# Define a Pydantic model for the character
class Personnage(BaseModel):
    nom: str
    age: int


# Create a dictionary to store characters
characters_db = dict()
characters_db[1] = Personnage(nom="Anne", age=33)
characters_db[2] = Personnage(nom="Michel", age=20)
character_id = 3  # Initial character ID

print(list(characters_db.values()))

# Add a character
@app.post("/character/")
def create_character(character: Personnage):
    global character_id
    characters_db[character_id] = character
    character_id += 1
    return character

# Get characters
@app.get("/character")
async def get_character():
    return list(characters_db.values())

#Modify character
@app.put("/character/{id}")
async def modify_character(id, new_name):
    if id not in characters_db.keys():
        return JsonResponse(status_code=status.HTTP_404_NOT_FOUND)
    else:
        characters_db[id].name = new_name




# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9876)
