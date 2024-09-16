import os

from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

from models import DiaryEntry, DiaryEntryCreate

MONGODB_CONNECTION_STRING = os.environ["MONGODB_CONNECTION_STRING"]

db_client = AsyncIOMotorClient(MONGODB_CONNECTION_STRING, uuidRepresentation="standard")
db = db_client.diary_db
entries = db.entries

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/entries", response_model=DiaryEntry)
async def create_entry(entry: DiaryEntryCreate):
    new_entry = DiaryEntry(mood=entry.mood, note=entry.note, date=entry.date)
    await entries.insert_one(new_entry.model_dump(by_alias=True))
    return new_entry


@app.get("/entries", response_model=list[Optional[DiaryEntry]])
async def get_entries(id: Optional[int] = None, date: Optional[datetime] = None):
    filter = {}
    if id:
        filter["_id"] = id
    if date:
        filter["date"] = date
    return await entries.find(filter).to_list(length=None)


@app.delete("/entries/{id}")
async def remove_entry(id: int):
    result = await entries.delete_one(id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"Entry with id: {id} not found.")
    return {"message": f"Entry with id: {id} deleted succesfully."}
