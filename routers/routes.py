from .models import JoinRequest, LeaveRequest
from fastapi.routing import APIRouter

router = APIRouter()

@router.post("/network/join")
async def join(req: JoinRequest):
    return req

    
@router.post("/network/leave")
async def leave(req: LeaveRequest):
    return req

    
@router.get("/network/state")
async def root():
    return "Topology of Network"


@router.get("/")
async def root():
    return {"message": "Welcome To P2P Network"}