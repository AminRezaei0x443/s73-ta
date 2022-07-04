from pydantic import BaseModel

class JoinRequest(BaseModel):
    capacity: int

class LeaveRequest(BaseModel):
    id: int
