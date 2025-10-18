from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import SessionLocal, engine, Base
from . import models, schemas, crud, ai_module

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Project Company AI")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/health')
def health():
    return {"status": "ok"}

@app.post('/projects', response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate):
    db = SessionLocal()
    p = crud.create_project(db, project)
    db.close()
    return p

@app.get('/projects')
def list_projects():
    db = SessionLocal()
    items = crud.get_projects(db)
    db.close()
    return items

@app.post('/tasks', response_model=schemas.Task)
def create_task(task: schemas.TaskCreate):
    db = SessionLocal()
    t = crud.create_task(db, task)
    db.close()
    return t

@app.post('/ai/recommend', response_model=schemas.AIRecommendation)
def ai_recommend(payload: schemas.AIRequest):
    rec = ai_module.recommend(payload.dict())
    return rec
