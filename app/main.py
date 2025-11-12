from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

BOOKS = [
    {"name": "Clean Code", "rating": 8, "author": "Robert C. Martin"},
    {"name": "Design Patterns", "rating": 7, "author": "Erich Gamma et al."},
    {"name": "The Pragmatic Programmer", "rating": 9, "author": "Andrew Hunt"},
    {"name": "Continuous Delivery", "rating": 10, "author": "Jez Humble"},
    {"name": "Accelerate", "rating": 8, "author": "Nicole Forsgren"},
]


@app.get("/")
async def root():
    return RedirectResponse(url="/books")


@app.get("/books", response_class=HTMLResponse)
async def get_books(request: Request):
    return templates.TemplateResponse(
        "books.html", {"request": request, "books": BOOKS}
    )
