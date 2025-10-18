from . import models, schemas

def create_project(db, project: schemas.ProjectCreate):
    p = models.Project(name=project.name, description=project.description)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

def get_projects(db):
    return db.query(models.Project).all()

def create_task(db, task: schemas.TaskCreate):
    t = models.Task(**task.dict())
    db.add(t)
    db.commit()
    db.refresh(t)
    return t
