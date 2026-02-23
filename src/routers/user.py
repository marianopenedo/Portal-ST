
from fastapi import APIRouter, Depends, status
from fastapi.responses import HTMLResponse

from permissions import CheckInternalUser
from repositories.users import UserRepository
from schemas.user_info import UserSchema
from security.security import hash_password

router = APIRouter()
user_repository = UserRepository()

@router.get('/users',
        dependencies=[Depends(CheckInternalUser())]
)
def user_page():
    return HTMLResponse(open('static/users.html', 'r', encoding='utf-8').read())

@router.get('/list-users',
        dependencies=[Depends(CheckInternalUser())]
)
def list_user():
    return user_repository.catch_all_users()

@router.get('/user-register',
        dependencies=[Depends(CheckInternalUser())]
)
def user_register():
    return HTMLResponse(open('static/user_register.html', 'r', encoding='utf-8').read())

@router.post('/create-user',
          dependencies=[Depends(CheckInternalUser())],
          status_code=status.HTTP_201_CREATED
)
def create_user(user_info: UserSchema):
    user_info.password = hash_password(user_info.password)
    return user_repository.create_new_user(user_info)

@router.put('/update-user/{id}',
        dependencies=[Depends(CheckInternalUser())]
)
def update_user(id: int, user_info: UserSchema):
    return user_repository.update_user(id, user_info)

@router.delete('/delete-user/{id}',
        dependencies=[Depends(CheckInternalUser())]
)
def delete_user(id: int):
    return user_repository.delete_user(id)
