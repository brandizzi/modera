from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from entity import User
from modera.util import get_hashed_password
from modera.db import create_session


def authenticate(username, password):
    """
    Tries to authenticate a user with a username and a password. Returns the
    authenticated user if authentication succeeds; return None otherwise.
    """
    session = create_session()
    password = get_hashed_password(password)
    try:
        user = session.query(User).filter_by(
                username=username, password=password).one()
    except (MultipleResultsFound, NoResultFound) as e:
        user = None
    return user
