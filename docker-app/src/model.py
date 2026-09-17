from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Logs_API(Base):
    __tablename__ = "logs_api"

    id_log = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    analysis = Column(String, index=True)
    amogus = Column(Boolean, index=True)

    def __init__(self, description: str, analysis: str, amogus: bool):
        self.description = description
        self.analysis = analysis
        self.amogus = amogus