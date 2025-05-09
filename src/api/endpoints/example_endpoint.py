from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ExampleModel(BaseModel):
    id: int
    name: str
    description: str

example_data = []

@router.post("/examples/", response_model=ExampleModel)
async def create_example(example: ExampleModel):
    example_data.append(example)
    return example

@router.get("/examples/", response_model=List[ExampleModel])
async def get_examples():
    return example_data

@router.get("/examples/{example_id}", response_model=ExampleModel)
async def get_example(example_id: int):
    for example in example_data:
        if example.id == example_id:
            return example
    raise HTTPException(status_code=404, detail="Example not found")

@router.put("/examples/{example_id}", response_model=ExampleModel)
async def update_example(example_id: int, example: ExampleModel):
    for index, existing_example in enumerate(example_data):
        if existing_example.id == example_id:
            example_data[index] = example
            return example
    raise HTTPException(status_code=404, detail="Example not found")

@router.delete("/examples/{example_id}")
async def delete_example(example_id: int):
    for index, existing_example in enumerate(example_data):
        if existing_example.id == example_id:
            del example_data[index]
            return {"detail": "Example deleted"}
    raise HTTPException(status_code=404, detail="Example not found")