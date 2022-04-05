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

    new_workout = await database.add_workout(workout.dict())

    return routine.ResponseModel(new_workout, "Workout added Correctly")


@r.post('/reg_machine')
async def reg_machine(request: Request, mech: Machine = Body(...)):

    today = datetime.datetime.now()
    mech2 = {
        'sub': request.session['user']['sub'],
        'name': mech.name,
        'target_day': mech.target_day,
        'set_date': today,
        'last_used': today
    }

    new_mech = await database.add_machine(mech2)

    return routine.ResponseModel(new_mech, "Machine registerd Correctly")
