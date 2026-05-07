from faimport pytest
from httpx import AsyncClient
from src.main import app

@pytest.mark.asyncio
async def test_get_existed_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        user_data = {"name": "Test User", "email": "test@example.com"}
        create_response = await client.post("/users", json=user_data)
        user_id = create_response.json()["id"]
        
        response = await client.get(f"/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["name"] == "Test User"

@pytest.mark.asyncio
async def test_get_user_not_found():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/users/99999")
        assert response.status_code == 404

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        user_data = {"name": "New User", "email": "new@example.com"}
        response = await client.post("/users", json=user_data)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "New User"
        assert data["email"] == "new@example.com"

@pytest.mark.asyncio
async def test_update_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        user_data = {"name": "Old Name", "email": "old@example.com"}
        create_response = await client.post("/users", json=user_data)
        user_id = create_response.json()["id"]
        
        update_data = {"name": "Updated Name"}
        response = await client.put(f"/users/{user_id}", json=update_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Updated Name"

@pytest.mark.asyncio
async def test_delete_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        user_data = {"name": "To Delete", "email": "delete@example.com"}
        create_response = await client.post("/users", json=user_data)
        user_id = create_response.json()["id"]
        
        response = await client.delete(f"/users/{user_id}")
        assert response.status_code == 204
        
        get_response = await client.get(f"/users/{user_id}")
        assert get_response.status_code == 404