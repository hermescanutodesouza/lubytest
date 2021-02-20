from flask_sqlalchemy import SQLAlchemy
from .basemodel import BaseModel
from .model import Parent,Child

db = SQLAlchemy()

__all__ = ['BaseModel', 'Parent', 'Child']
