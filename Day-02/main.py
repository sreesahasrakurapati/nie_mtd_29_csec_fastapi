from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def home():
    return {"messege" : "Enterprise IT Desk"}
db ={
    1 : {"id": 1,"Title":"Computer is not ON",
         "description":"power button is not working",
         "category":"Hardware",
         "status":"NEW"},
    2 : {"id": 2,"Title":"Internet is not working.",
         "description":"WIFI Problem",
         "category":"Hardware",
         "status":"NEW"}
}

class TicketCreate(BaseModel):
    title: str
    description: str
    category: str
    status: str

class TicketResponse(TicketCreate):
    id: int

@app.get("/tickets")
def ticket_read_all():
    return list(db.values())

@app.get("/tickets/{id}")
def ticket_read_all(id : int):
    if id not in db:
        raise HTTPException(detail = "Ticket Not Found",status_code=404)
    return db[id]

@app.post("/tickets",status_code=201,response_model=TicketResponse)
def ticket_create(ticket_payload : TicketCreate):
    new_id= max(db.keys(), default = 0) + 1
    db[new_id]= {"id" : new_id, **ticket_payload.model_dump()}
    return db[new_id]



