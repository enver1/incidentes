from infrastructure.outputadapter.Environment import get_environment_variables
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Runtime Environment Configuration
env = get_environment_variables()
DATABASE_URL = f"{env.DATABASE_DIALECT}://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}"
engine = create_engine(DATABASE_URL)
localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()