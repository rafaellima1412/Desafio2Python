from fastapi import APIRouter, Path, HTTPException, status
from src.domain.packbook import Todo, TodoItem

router = APIRouter()

todo_list = []


@router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}

@router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
        for todo in todo_list:
            if todo.id == todo_id:
                return {
                "todo": todo
                }
        # return {
        # "message": "Todo with supplied ID doesn't exist."
        # }
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
        )
@router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

@router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int =Path(..., title="The ID of the todo to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
            "message": "Todo updated successfully."
            }
    # return {
    # "message": "Todo with supplied ID doesn't exist."
    #  }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

@router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
            "message": "Todo deleted successfully."
            }
    # return {
    # "message": "Todo with supplied ID doesn't exist."
    # }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = "Todo with supplied ID doesn't exist",
    )