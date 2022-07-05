from app.core.network import Network
from .models import JoinRequest, LeaveRequest
from fastapi.routing import APIRouter

router = APIRouter()
network = Network()


@router.post("/network/join")
async def join(req: JoinRequest):
    """
    Request for joining the network, node announces a capacity and get assigned an id
    """
    c = req.capacity
    _id = network.add_node(c)
    return {
        "id": _id
    }


@router.post("/network/leave")
async def leave(req: LeaveRequest):
    """
    Request for leaving the network, node announces departure, network restructures to maintain min height
    """
    return {
        "ok": network.remove_node(req.id)
    }


@router.get("/network/state")
async def state(format: str = "json"):
    """
    Request for querying network state - topology, you can either request json format or text format
    """
    return network.topology(format=format)


@router.get("/")
async def root():
    return {"message": "Welcome To P2P Network"}
