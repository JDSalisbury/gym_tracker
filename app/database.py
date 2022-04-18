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


MACHINE_DB = {
    'collection': machine_collection,
    'helper': machine_helper
}

WORKOUT_DB = {
    'collection': workout_collection,
    'helper': workout_helper
}


async def db_add(collection_info: dict, item_data: dict) -> dict:
    collection_item = await collection_info['collection'].insert_one(item_data)
    new_collection_item = await collection_info['collection'].find_one({"_id": collection_item.inserted_id})
    return collection_info['helper'](new_collection_item)
