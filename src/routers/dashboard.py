
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter

router = APIRouter()

@router.get('/dashboard')
def dashboard():
    return HTMLResponse(open('static/dashboard.html', 'r', encoding='utf-8').read())

