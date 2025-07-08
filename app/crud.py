from sqlalchemy.orm import Session
from app import models


def create_user(db: Session, name: str, email: str, password_hash: str):
    user = models.User(name=name, email=email, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def delete_user(db: Session, user_id: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

def create_leadership_assessment(db: Session, user_id: str, skill_name: str, self_rating: int):
    assessment = models.LeadershipAssessment(user_id=user_id, skill_name=skill_name, self_rating=self_rating)
    db.add(assessment)
    db.commit()
    db.refresh(assessment)
    return assessment

def delete_leadership_assessment(db: Session, assessment_id: str):
    assessment = db.query(models.LeadershipAssessment).filter(models.LeadershipAssessment.id == assessment_id).first()
    if assessment:
        db.delete(assessment)
        db.commit()
    return assessment

def get_all_development_plans(db: Session, user_id: str):
    return db.query(models.DevelopmentPlan).filter(models.DevelopmentPlan.user_id == user_id).all()

def delete_development_plan(db: Session, plan_id: str):
    plan = db.query(models.DevelopmentPlan).filter(models.DevelopmentPlan.id == plan_id).first()
    if plan:
        db.delete(plan)
        db.commit()
    return plan

def create_coaching_module(db: Session, title: str, topic: str, content: dict, format: str, difficulty: str, estimated_time: int):
    module = models.CoachingModule(
        title=title, topic=topic, content=content, format=format, difficulty=difficulty, estimated_time=estimated_time
    )
    db.add(module)
    db.commit()
    db.refresh(module)
    return module

def delete_coaching_module(db: Session, module_id: str):
    module = db.query(models.CoachingModule).filter(models.CoachingModule.id == module_id).first()
    if module:
        db.delete(module)
        db.commit()
    return module

def update_user_module_progress(db: Session, progress_id: str, status: str):
    progress = db.query(models.UserModuleProgress).filter(models.UserModuleProgress.id == progress_id).first()
    if progress:
        progress.status = status
        db.commit()
        db.refresh(progress)
    return progress

def delete_user_module_progress(db: Session, progress_id: str):
    progress = db.query(models.UserModuleProgress).filter(models.UserModuleProgress.id == progress_id).first()
    if progress:
        db.delete(progress)
        db.commit()
    return progress