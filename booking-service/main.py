from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

INVENTORY_SERVICE_URL = "http://inventory-service:80/movies"


# this communicates with ./inventory-service/test_main.py
@app.post("/book/")
async def book_tickets(movie_id: int, quantity: int):
    response = requests.put(f"{INVENTORY_SERVICE_URL}/{movie_id}/book", params={"tickets": quantity})
    if response.status_code == 200:
        return {"message": "Tickets successfully booked", "movie": response.json()}
    elif response.status_code == 400:
        raise HTTPException(status_code=400, detail=response.json())
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail=response.json())
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/")
def root():
    return {"message": "Yo"}
