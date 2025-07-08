from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, Text, JSON, UUID
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.sql import func
import uuid
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(100))
    industry = Column(String(100))
    experience_level = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class LeadershipAssessment(Base):
    __tablename__ = 'leadership_assessments'
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(PGUUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    skill_name = Column(String(100), nullable=False)
    self_rating = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DevelopmentPlan(Base):
    __tablename__ = 'development_plans'
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(PGUUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    goal_title = Column(String(255), nullable=False)
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String(50), default='in progress')
    priority = Column(String(20))

class CoachingModule(Base):
    __tablename__ = 'coaching_modules'
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    topic = Column(String(100))
    content = Column(JSON, nullable=False)
    format = Column(String(50))
    difficulty = Column(String(50))
    estimated_time = Column(Integer)

class UserModuleProgress(Base):
    __tablename__ = 'user_module_progress'
    id = Column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(PGUUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    module_id = Column(PGUUID(as_uuid=True), ForeignKey('coaching_modules.id', ondelete='CASCADE'))
    status = Column(String(50), default='not started')
    completed_at = Column(DateTime(timezone=True))
