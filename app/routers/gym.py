from fastapi import APIRouter, Query
r = APIRouter()


@r.get("/gym/{user_id}")
async def gym_stats(user_id: int):

    return {"message": f"gym info for user: {user_id}"}


@r.get('/test')
async def test_endpoint():
    return {'tets': 'True'}
