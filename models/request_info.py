from sqlalchemy import Column, Integer, String, DateTime

from service.database import Base


class RequestInfo(Base):
    __tablename__ = 'request_info'

    id = Column(Integer, primary_key=True)
    request_dt = Column(DateTime, nullable=False)
    user_agent = Column(String, nullable=False)
