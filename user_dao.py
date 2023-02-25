from sqlalchemy import MetaData, Table, Column, BigInteger, String, select

from authentication_exception import AuthenticationException
from user import User

metadata_obj = MetaData()

user = Table(
    "user",
    metadata_obj,
    Column("id", BigInteger, primary_key=True),
    Column("username", String(50), nullable=False),
    Column("password", String(50), nullable=False)
)


def find(conn, username):
    stmt = select(user.c.username, user.c.password).\
        select_from(user).\
        where(user.c.username == username)

    result = conn.execute(stmt)

    if result.rowcount == 0:
        raise AuthenticationException(f"Invalid username/password for username={username}")

    r = result.fetchone()
    return User(username, r.password)
