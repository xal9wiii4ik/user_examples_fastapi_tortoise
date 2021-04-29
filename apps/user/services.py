from fastapi import HTTPException

from typing import Optional

from apps.auth.models import Uid
from apps.user.models import User
from core.security import get_hashed_password

from apps.auth.services import get_web_url, create_uuid, send_email
from apps.user.schemas import UserCreate, UserInDb


async def get_user_from_email(email: str) -> dict or None:
    """ Getting user using email """

    user = await User.get_or_none(email=email)
    if user is not None:
        return user
    else:
        return None


async def create_super_user(item: dict):
    """ Check if user already exist and creating superuser """

    item = await _validate_password(item=item)
    user = await User.get_or_none(email=item.get('email'))
    if user is None:
        user = await User.get_or_none(username=item.get('username'))
        if user is None:
            item['is_active'], item['is_superuser'] = True, True
            await User.create(**item)


async def user_create(request_dict: dict, item: UserCreate, additional_text: Optional[str] = '') -> dict:
    """ Creating user """

    url = await get_web_url(request_dict=request_dict)
    item_dict = await _validate_password(item=item.dict())
    item_dict.update({'is_active': False, 'is_superuser': False})
    try:
        user = await User.create(**item_dict)
        item_dict.update({'id': user.pk})
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
    uid_items = await create_uuid(user_id=user.pk)
    await send_email(
        title='This is your verification link:',
        link=f'{url}/auth/verification/{uid_items["uid"]}/{uid_items["pk"]}',
        email=item_dict.get('email'),
        additional_text=additional_text
    )
    return item_dict


async def user_verification(u: str, pk: int) -> None:
    """ Set is_active to true """

    true_uuid = await Uid.get_or_none(pk=pk)
    if true_uuid is not None and true_uuid.uid == u:
        # if true_uuid['uid'] == u:
        await User.filter(pk=true_uuid.pk).update(**{'is_active': True})
        await Uid.filter(pk=pk).delete()


async def user_update(pk: int, item: UserInDb) -> dict:
    """ Update user profile"""

    item_dict = item.dict()
    item_dict['id'] = pk
    if item_dict['password'] is not None:
        item_dict.update({'hashed_password': get_hashed_password(password=item_dict['password'])})
    item_dict.pop('password')
    if item_dict['email'] is None:
        item_dict.pop('email')
    await User.filter(pk=pk).update(**item_dict)
    return item_dict


async def user_delete(pk: int) -> None:
    """ Delete user profile"""

    await User.filter(pk=pk).delete()


async def get_user(pk: int) -> dict or None:
    """ Getting user """

    user = await User.get(pk=pk)
    if user is not None:
        return user
    else:
        return None


async def _validate_password(item: dict) -> dict:
    """ Validate password and return dict with hashed password """

    password = item.pop('password')
    repeat_password = item.pop('repeat_password')
    if password == repeat_password:
        item.update({'hashed_password': get_hashed_password(password=password)})
        return item
    raise HTTPException(status_code=404, detail='The password and the repeat password didnt match')
