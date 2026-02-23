from fastapi import Request, HTTPException, status
from fastapi.responses import RedirectResponse
from security.security import decode_token

class RedirectToDashboard(Exception):
    pass

class CheckInternalUser:

    def __call__(self, request: Request):
        token = request.cookies.get("access_token")
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required."
            )

        payload = decode_token(token)

        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token."
            )

        user_type = payload.get("user_type")

        if user_type != "internal":
            raise RedirectToDashboard()

        return payload