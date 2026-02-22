import json
import os

from typing import Optional
from fastapi import Body, FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from schemas.company import CompanySchema
from schemas.user_info import UserInfo
from database.session import db
from repositories.users import UserRepository
from repositories.company import CompanyRepository

user_repository = UserRepository()
company_repository = CompanyRepository()

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

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    print(request.url.path)
    if not request.cookies and request.url.path != '/login':
        return HTMLResponse(open('static/login.html', 'r', encoding='utf-8').read(), status_code=401)
    
    return await call_next(request)

@app.get('/list-company')
def index():
    return company_repository.all_company()

@app.get('/list-database')
def index():
    return user_repository.catch_all_users()

@app.get('/index')
def index():
    return HTMLResponse(open('static/index.html', 'r', encoding='utf-8').read())

@app.get('/pending')
def pending_company():
    return HTMLResponse(open('static/list.html', 'r', encoding='utf-8').read())

@app.get('/pending-company')
def pending_company():
    return company_repository.pending_company()

@app.patch('/decision')
def pending_company(company_id: int = Body(), decision: str = Body(), reason: Optional[str] = Body(default="")):
    return company_repository.decision(company_id, decision, reason)
    
@app.post('/save-company-info')
def save_on_database(file: UploadFile, company_info: str = Body()) -> CompanySchema:
    company_info: CompanySchema = CompanySchema(**json.loads(company_info))
    company_info.path_file = f'temp_files/{file.filename}'
    open(company_info.path_file, 'wb').write(file.file.read())
    
    return company_repository.insert_company(company_info)

@app.post('/login')
def login(response: Response, user_info: UserInfo):
    if user_info.user == 'admin' and user_info.pwd == 'admin':
        response.set_cookie('EMPRESA_MASTER', 'true')
        response.status_code = 200
        return response

    response.set_cookie('EMPRESA_CADASTRO', 'true')
    response.status_code = 200
    return response
