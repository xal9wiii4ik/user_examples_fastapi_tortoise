# user_examples_fastapi_tortoise

# manipulations with user/authentication/permissions 
# using tortoise orm
CRUD user
1) custom jwt authentication
2) verification user using smtp
3) terminal commands
4) Git authorization

## for create superuser:
python scripts/createsuperuser

## for create SECRET_KEY:
''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))

# main libraries:
1) fastapi
2) alembic
3) smtplib
4) bcrypt
5) databases
6) psycopg2
7) uvicorn
8) tortoise
9) asyncpg

# Database PostgreSQL
date the code was written: 30.04.2021
