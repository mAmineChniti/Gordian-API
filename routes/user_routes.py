from fastapi import HTTPException, APIRouter, status
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from models.user_model import User
from config.database import users_collection
from bcrypt import hashpw, gensalt, checkpw
from uuid import uuid4

UsersRouter = APIRouter()

# Redirection to documentation page
@UsersRouter.get("/", include_in_schema=False, status_code=308)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')

# API Status check
@UsersRouter.get("/status", include_in_schema=False, status_code=200)
async def status():
    try:
        return {"status": "ok"}
    except Exception as e:
        # Handle the exception properly and return an error response
        raise HTTPException(status_code=500, detail=str(e))

@UsersRouter.post("/register", status_code=201)
async def register(user: User):
    try:
        # Check if the username already exists
        if await users_collection.find_one({"username": user.username}):
            raise HTTPException(status_code=400, detail="Username already exists")

        # Hash the password with a stronger encoding
        hashed_password = hashpw(user.password.encode("utf-8"), gensalt(rounds=12, prefix=b"2b"))

        # Generate UUID for the user
        user_id = str(uuid4())

        # Save the user in the database
        user_data = {
            "_id": user_id,
            "username": user.username,
            "password": hashed_password.decode("utf-8")
        }
        await users_collection.insert_one(user_data)

        return {"message": "User registered successfully"}
    except Exception as e:
        # Handle the exception properly and return an error response
        raise HTTPException(status_code=500, detail=str(e))

@UsersRouter.post("/login", status_code=200)
async def login(user: User):
    try:
        # Retrieve the user from the database
        stored_user = await users_collection.find_one({"username": user.username})

        # Check if the user exists and the password matches
        if not stored_user or not checkpw(user.password.encode("utf-8"), stored_user["password"].encode("utf-8")):
            raise HTTPException(status_code=401, detail="Invalid username or password")
        stored_user.pop("password")
        json_user = jsonable_encoder(stored_user)
        return JSONResponse(content=json_user)

    except Exception as e:
        # Handle the exception properly and return an error response
        raise HTTPException(status_code=500, detail=str(e))
