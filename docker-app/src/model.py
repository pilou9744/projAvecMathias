from sqlalchemy import Column, Integer, String
from database import Base


class Logs_API(Base):
    __tablename__ = "logs_api"

    id_log = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)

    def __init__(self, description: str):
        self.description = description
