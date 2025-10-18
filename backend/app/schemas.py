from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    status: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    budget: Optional[float]
    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    project_id: int
    title: str
    description: Optional[str] = None
    estimate_days: Optional[int] = 1

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    assignee_id: Optional[int]
    status: Optional[str]
    class Config:
        orm_mode = True

class AIRequest(BaseModel):
    project_id: int
    task_title: str
    task_description: str

class AIRecommendation(BaseModel):
    recommended_assignee: Optional[str]
    risk_score: float
    estimated_days: int
