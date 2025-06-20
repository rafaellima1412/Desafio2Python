from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

todo_router = APIRouter()
todo_list = []
templates = Jinja2Templates(directory="templates/")

