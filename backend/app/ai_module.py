# demo AI module — rule-based + toy ML
from typing import Dict
from .db import SessionLocal
from .models import User, Task

def recommend(payload: Dict):
    db = SessionLocal()
    users = db.query(User).filter(User.role == 'employee').all()
    if not users:
        return {"recommended_assignee": None, "risk_score": 0.5, "estimated_days": 3}
    load = []
    for u in users:
        cnt = db.query(Task).filter(Task.assignee_id == u.id).count()
        load.append((u, cnt))
    load.sort(key=lambda x: x[1])
    chosen = load[0][0]
    risk = min(0.9, 0.1 + 0.1 * load[0][1])
    estimate = max(1, int(3 + (len(payload.get('task_description','')) // 200)))
    db.close()
    return {
        "recommended_assignee": chosen.name,
        "risk_score": round(risk, 2),
        "estimated_days": estimate
    }
