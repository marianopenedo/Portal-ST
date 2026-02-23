
import json
import os
from typing import Optional

from fastapi import Body, Depends, HTTPException, Request, UploadFile, status
from fastapi.routing import APIRouter
from fastapi.responses import FileResponse, HTMLResponse

from permissions import CheckInternalUser
from repositories.company import CompanyRepository
from schemas.company import CompanySchema
from utils import check_admin_permission

company_repository = CompanyRepository()

router = APIRouter()

@router.get('/all-company',
         dependencies=[Depends(CheckInternalUser())])
def all_company():
    return HTMLResponse(open('static/all_company.html', 'r', encoding='utf-8').read())

@router.get('/list-company',
        dependencies=[Depends(CheckInternalUser())]
    )
def list_company():
    return company_repository.all_company()

@router.get('/pending',
    dependencies=[Depends(CheckInternalUser())]
)
def pending():
    return HTMLResponse(open('static/list.html', 'r', encoding='utf-8').read())

@router.get('/pending-company',
         dependencies=[Depends(CheckInternalUser())]
)
def pending_company():
    return company_repository.pending_company()

@router.patch('/decision')
def decision(company_id: int = Body(), decision: str = Body(), reason: Optional[str] = Body(default="")):
    return company_repository.decision(company_id, decision, reason)

@router.get('/download-file/{company_id}')
def download_file(company_id: int):
    file_path = company_repository.catch_file_path(company_id)
    if os.path.exists(file_path):
        filename = file_path.rsplit('/')[-1]
    return FileResponse(path=file_path, filename=filename)

@router.post('/save-company-info',
        status_code=status.HTTP_201_CREATED
)
def save_on_database(request: Request, file: UploadFile, user_type: str = Body(), company_info: str = Body()):# -> CompanySchema:
    if file.filename.rsplit('.')[-1].lower() not in ['png', 'pdf', 'jpg', 'jpeg']:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="This file is not supported.")
    
    company_info: CompanySchema = CompanySchema(**json.loads(company_info))
    company_info.path_file = f'temp_files/{file.filename}'

    if user_type == "internal":
        check_admin_permission(request)
        company_info.status = 'ACCEPTED'

    open(company_info.path_file, 'wb').write(file.file.read())
    
    return company_repository.insert_company(company_info)

@router.get('/index')
def index():
    return HTMLResponse(open('static/index.html', 'r', encoding='utf-8').read())
