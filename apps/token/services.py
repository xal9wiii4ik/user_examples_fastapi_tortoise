import jwt
import logging

from fastapi import Request, HTTPException

from datetime import timedelta, datetime

from apps.user.models import User
from core.config import (
    SECRET_KEY,
    TOKEN_TYPE,
    ALGORITHM,
    ACCESS_TOKEN_JWT_SUBJECT,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from core.security import verify_password


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


async def authenticate_user(password: str, username: str = None, email: str = None) -> dict or None:
    """ Authenticate user """

    user = await _get_user(username=username, email=email)
    if user is None:
        raise HTTPException(status_code=404, detail='User does not exist')
    else:
        if verify_password(plain_password=password, hashed_password=user.hashed_password):
            return user
        else:
            raise HTTPException(status_code=400, detail='invalid password')


async def authenticate(request: Request) -> dict or None:
    """ Authenticate user """

    authorization_header = request.headers.get("Authorization")
    if authorization_header is not None:
        token = authorization_header.split(' ')
        if (token[0] != '') and (token is not None) and (token[0] == TOKEN_TYPE):
            try:
                payload = jwt.decode(token[1], SECRET_KEY, algorithms=[ALGORITHM])
                user_id: int = payload.get('user_id')
                user = await User.get_or_none(pk=user_id)
                if user is not None:
                    return user
            except Exception as e:
                logging.info(e)
    raise HTTPException(status_code=401, detail='Given credentials are not provide')


def create_access_token(data: dict):
    """ Create access token """

    to_encode = data.copy()
    if ACCESS_TOKEN_EXPIRE_MINUTES is not None:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire, 'sub': ACCESS_TOKEN_JWT_SUBJECT})
    encoded_jwt = jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    data.update({'access_token': encoded_jwt, 'token_type': TOKEN_TYPE})
    return data


async def _get_user(username: str = None, email: str = None) -> dict or None:
    """ Get user from db """

    if username is None:
        user = await User.get(email=email)
    else:
        user = await User.get(username=username)
    if user is None:
        return None
    else:
        return user
