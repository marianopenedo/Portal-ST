from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi import status

from permissions import RedirectToDashboard
from security.security import decode_token
from database.session import db
from routers.company import router as company_router
from routers.dashboard import router as dashboard_router
from routers.login import router as login_router
from routers.user import router as user_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    db.create_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(company_router, tags=["Company"])
app.include_router(dashboard_router, tags=["Dashboard"])
app.include_router(login_router, tags=["Login"])
app.include_router(user_router, tags=["Users"])

@app.exception_handler(RedirectToDashboard)
async def redirect_dashboard_handler(request: Request, exc: RedirectToDashboard):
    return RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    public_routes = ["/login"]

    if request.url.path in public_routes:
        return await call_next(request)

    token = request.cookies.get("access_token")

    if not token:
        return HTMLResponse(
            open('static/login.html', 'r', encoding='utf-8').read(),
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    payload = decode_token(token)

    if not payload:
        return HTMLResponse(
            open('static/login.html', 'r', encoding='utf-8').read(),
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    return await call_next(request)

