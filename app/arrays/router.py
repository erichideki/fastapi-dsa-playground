from fastapi import APIRouter
from pydantic import BaseModel

from .problems import two_sum

router = APIRouter(prefix="/arrays", tags=["Arrays"])


class TwoSumRequest(BaseModel):
    nums: list[int]
    target: int


@router.post("/two-sum")
def solve_two_sum(data: TwoSumRequest):
    result = two_sum(data.nums, data.target)

    return {
        "problem": "Two Sum",
        "input": data,
        "result": result
    }