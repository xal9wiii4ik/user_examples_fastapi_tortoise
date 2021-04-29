from apps.social_account.models import SocialAccount
from apps.social_account.schemas import SocialAccountCreate

from apps.user.services import get_user_from_email, user_create
from apps.user.schemas import UserCreate


async def update_social_account(request_dict: dict, pk: int, item_dict: dict) -> bool or dict:
    """ Getting social account using email """

    user = await get_user_from_email(email=item_dict.get('email'))
    is_new_user = False
    if user is None:
        is_new_user = True
        account = await SocialAccount.get(pk=pk)
        password = f'{account.account_id}_{account.provider}/{account.pk}'
        new_dict = UserCreate(
            password=password,
            repeat_password=password,
            email=item_dict['email'],
            username=account.username
        )
        user = await user_create(
            request_dict=request_dict,
            item=new_dict,
            additional_text=f'Your password is: {password}. '
                            f'That is if you want to login with password (username: {account.username})'
        )
    item_dict.update({'user_id': user.pk})
    await SocialAccount.filter(pk=pk).update(**item_dict)
    if not is_new_user:
        return {'user_id': user.pk}
    return False


async def create_social_auth_account(item: SocialAccountCreate) -> dict:
    """ Creating social auth account with out relation with user"""

    item_dict = item.dict()
    account = await SocialAccount.create(**item_dict)
    item_dict.update({'id': account.pk})
    return item_dict


async def check_exist_social_auth_account(username: str, account_id: int) -> dict or bool:
    """ Check if social auth account exist in db"""

    account = await SocialAccount.filter(username=username, account_id=account_id)
    if account:
        return account
    return False
