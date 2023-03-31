import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

from sqlmodel import create_engine, Session
import models
from config import database_url

engine = create_engine(database_url, echo=False)
models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
