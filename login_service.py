from werkzeug.security import check_password_hash

import user_dao
from authentication_exception import AuthenticationException
from database import engine


def authenticate(user):
    with engine.begin() as conn:
        db_user = user_dao.find(conn, user.username)
        if not check_password_hash(db_user.password, user.password):
            raise AuthenticationException(f"Invalid username/password for username={user.username}")
