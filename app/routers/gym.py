import datetime
from starlette.requests import Request
from fastapi import APIRouter, Query, Body
from app import database
from app.models import routine
from app.models.routine import Machine, Workout
r = APIRouter()


@r.get("/gym/{user_id}")
async def gym_stats(user_id: int):

    return {"message": f"gym info for user: {user_id}"}


@r.post('/add_workout')
async def add_workout(request: Request, workout: Workout = Body(...)):

    workout.date = datetime.datetime.now()
    workout.sub = request.session['user']['sub']

    new_workout = await database.db_add(database.WORKOUT_DB, workout.dict())

    return routine.ResponseModel(new_workout, "Workout added Correctly")


@r.post('/reg_machine')
async def reg_machine(request: Request, mech: Machine = Body(...)):

    mech.set_date = datetime.datetime.now()
    mech.last_used = datetime.datetime.now()
    mech.sub = request.session['user']['sub']

    new_mech = await database.db_add(database.MACHINE_DB, mech.dict())

    return routine.ResponseModel(new_mech, "Machine registerd Correctly")
