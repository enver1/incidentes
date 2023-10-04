from app.infraestructure.outputadapter.Environment import get_environment_variables
from typing import Iterator
from sqlalchemy.orm import  Session
from fastapi_utils.session import FastAPISessionMaker


# Runtime Environment Configuration
env = get_environment_variables()
# Generate Database URL
DATABASE_URL = f"{env.DATABASE_DIALECT}://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}"

def get_db_connection() -> Iterator[Session]:
    """ FastAPI dependency that provides a sqlalchemy session """
    yield from _get_fastapi_sessionmaker().get_db()

@lru_cache()
def _get_fastapi_sessionmaker() -> FastAPISessionMaker:
    """ This function could be replaced with a global variable if preferred """
    database_uri = DATABASE_URL
    return FastAPISessionMaker(database_uri)