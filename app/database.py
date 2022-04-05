import motor.motor_asyncio
from starlette.config import Config
config = Config(".env")
MONGO_DETAILS = config.get("MONGO")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)


db = client.workout

machine_collection = db.get_collection('machines')

workout_collection = db.get_collection('workout')


def machine_helper(machine) -> dict:
    return {
        "id": str(machine["_id"]),
        "sub": machine["sub"],
        "name": machine["name"],
        "target_day": machine["target_day"],
        "set_date": machine["set_date"],
        "last_used": machine["last_used"],
    }


def workout_helper(workout) -> dict:
    return {
        "id": str(workout["_id"]),
        "sub": workout["sub"],
        "machine_id": workout["machine_id"],
        "last_weight": workout["last_weight"],
        "reps": workout["reps"],
        "time": workout["time"],
        "date": workout["date"],
    }


async def add_machine(machine_data: dict) -> dict:
    machine = await machine_collection.insert_one(machine_data)
    new_machine = await machine_collection.find_one({"_id": machine.inserted_id})
    return machine_helper(new_machine)


async def add_workout(workout_data: dict) -> dict:
    workout = await workout_collection.insert_one(workout_data)
    new_workout = await workout_collection.find_one({"_id": workout.inserted_id})
    return workout_helper(new_workout)
