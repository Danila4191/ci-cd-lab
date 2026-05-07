from fastapi import APIRouter, HTTPException

router = APIRouter()

users_db = {}
counter = 1

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@router.post("/users")
async def create_user(user: dict):
    global counter
    user["id"] = counter
    users_db[counter] = user
    counter += 1
    return user

@router.put("/users/{user_id}")
async def update_user(user_id: int, user_data: dict):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id].update(user_data)
    return users_db[user_id]

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted"}