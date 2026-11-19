from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from utils.db import Base

class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default="pending")
    # created_at = Column(DateTime, nullable=False)
    # updated_at = Column(DateTime, nullable=False)
    # user_id = Column(Integer, ForeignKey("users.id"), nullable=False)