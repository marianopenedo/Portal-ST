from fastapi import Response, status
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter

from repositories.users import UserRepository
from schemas.login import Login
from security.security import create_access_token, verify_password

router = APIRouter()
user_repository = UserRepository()

@router.get('/login')
def get_login_page():
    return HTMLResponse(open('static/login.html', 'r', encoding='utf-8').read())

@router.post('/logout')
def logout(response: Response):
    response.delete_cookie(
        key="access_token",
        path="/"
    )
    return {"message": "Logout Realizado"}

@router.post('/login')
def login_post(response: Response, user_info: Login):
    
    user = user_repository.get_by_login(user_info.user)

    if not user:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    if not verify_password(user_info.pwd, user.password):
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    token = create_access_token({
        "sub": user.login,
        "user_id": user.id,
        "user_type": user.user_type
    })

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax"
    )

    return {"message": "Login realizado com sucesso"}