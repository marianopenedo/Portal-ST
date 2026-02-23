

from fastapi import HTTPException, Request, status

from security.security import decode_token


def check_admin_permission(request: Request):
    token = request.cookies.get('access_token')
    payload = decode_token(token)
    if payload['user_type'] == "external":
        raise HTTPException(detail="You don't have permission to complete this request.", status_code=status.HTTP_401_UNAUTHORIZED)