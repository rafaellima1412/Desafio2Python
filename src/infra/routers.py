from fastapi import APIRouter, Path, HTTPException, status, Request, Depends, Form
from starlette.responses import HTMLResponse

from src.application.todo import templates
from src.domain.todo import Todo, TodoItem

router = APIRouter()

todo_list = []


# @router.get("/todo")
# async def retrieve_todos() -> dict:
#     return {"todos": todo_list}
#
# @router.get("/todo/{todo_id}")
# async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
#         for todo in todo_list:
#             if todo.id == todo_id:
#                 return {
#                 "todo": todo
#                 }
#         # return {
#         # "message": "Todo with supplied ID doesn't exist."
#         # }
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Todo with supplied ID doesn't exist",
#         )
# @router.post("/todo", status_code=201)
# async def add_todo(todo: Todo) -> dict:
#     todo_list.append(todo)
#     return {"message": "Todo added successfully"}

# @router.put("/todo/{todo_id}")
# async def update_todo(todo_data: TodoItem, todo_id: int =Path(..., title="The ID of the todo to be updated")) -> dict:
#     for todo in todo_list:
#         if todo.id == todo_id:
#             todo.item = todo_data.item
#             return {
#             "message": "Todo updated successfully."
#             }
#     # return {
#     # "message": "Todo with supplied ID doesn't exist."
#     #  }
#
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Todo with supplied ID doesn't exist",
#     )

# @router.delete("/todo/{todo_id}")
# async def delete_single_todo(todo_id: int) -> dict:
#     for index in range(len(todo_list)):
#         todo = todo_list[index]
#         if todo.id == todo_id:
#             todo_list.pop(index)
#             return {
#             "message": "Todo deleted successfully."
#             }
#     # return {
#     # "message": "Todo with supplied ID doesn't exist."
#     # }
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail = "Todo with supplied ID doesn't exist",
#     )


# @router.post("/todo")
# async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
#     todo.id = len(todo_list) + 1
#     todo_list.append(todo)
#     return templates.TemplateResponse("todo.html",
#     {
#     "request": request,
#     "todos": todo_list
#     })

@router.get("/todo", response_model=TodoItem)
async def retrieve_todo(request: Request):
    return templates.TemplateResponse("todo.html", {
    "request": request,
    "todos": todo_list
    })

@router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int= Path(..., title="The ID of the todo to retrieve.")):

    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
            "todo.html", {
            "request": request,
            "todo": todo
            })
    return templates.TemplateResponse("error.html", {
        "request": request,
        "detail": "Todo com ID fornecido não existe."
    }, status_code=404)

    # raise HTTPException(
    # status_code=status.HTTP_404_NOT_FOUND,
    # detail="Todo with supplied ID doesn't exist",
    # )

@router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html",
                                      {
                                          "request": request,
                                          "todos": todo_list
                                      })

@router.post("/todo/{todo_id}/edit", response_class=HTMLResponse)
async def update_todo(request: Request, todo_id: int, item: str = Form(...)):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = item
            return templates.TemplateResponse("todo.html", {
                "request": request,
                "todos": todo_list
            })
    return templates.TemplateResponse("error.html", {
        "request": request,
        "detail": "Todo com ID fornecido não existe."
    }, status_code=404)

    # raise HTTPException(
    #     status_code=status.HTTP_404_NOT_FOUND,
    #     detail="Todo with supplied ID doesn't exist",
    # )


@router.post("/todo/{todo_id}/delete", response_class=HTMLResponse)
async def delete_single_todo(request: Request, todo_id: int):
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return templates.TemplateResponse("todo.html", {
                "request": request,
                "todos": todo_list
            })
    return templates.TemplateResponse("error.html", {
        "request": request,
        "detail": "Todo com ID fornecido não existe."
    }, status_code=404)

    # raise HTTPException(
    #     status_code=status.HTTP_404_NOT_FOUND,
    #     detail="Todo with supplied ID doesn't exist",
    # )

@router.post("/todo/delete_all")
async def delete_all_todo(request: Request):
    todo_list.clear()
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })
