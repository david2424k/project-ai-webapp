from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    role = Column(String)
    hashed_password = Column(String)

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    status = Column(String, default='new')
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    budget = Column(Integer, nullable=True)
    tasks = relationship('Task', backref='project')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    title = Column(String)
    description = Column(Text)
    assignee_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    status = Column(String, default='todo')
    estimate_days = Column(Integer, default=1)
