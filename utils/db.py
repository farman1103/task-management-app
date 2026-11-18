from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from utils.settings import settings

# Create the SQLAlchemy engine using the database connection string from settings
engine = create_engine(settings.DB_CONNECTION)

# Create a session factory
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for declarative models
Base = declarative_base()

def get_db():
    """
    Dependency function to get a database session.
    This function can be used in FastAPI routes to provide a database session.
    """
    dbsession = LocalSession()
    try:
        yield dbsession
    finally:
        dbsession.close()