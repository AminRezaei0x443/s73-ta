from app.core.network import Network
from .models import JoinRequest, LeaveRequest
from fastapi.routing import APIRouter

router = APIRouter()
network = Network()


@router.post("/network/join")
async def join(req: JoinRequest):
    c = req.capacity
    _id = network.add_node(c)
    return {
        "id": _id
    }


@router.post("/network/leave")
async def leave(req: LeaveRequest):
    return {
        "ok": network.remove_node(req.id)
    }


@router.get("/network/state")
async def state(format: str = "json"):
    return network.topology(format=format)


@router.get("/")
async def root():
    return {"message": "Welcome To P2P Network"}
