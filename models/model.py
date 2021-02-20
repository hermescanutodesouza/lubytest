from app import db
from .basemodel import BaseModel

parent_child = db.Table('parent_child',
                        db.Column('parent_id', db.Integer, db.ForeignKey('parent.id')),
                        db.Column('child_id', db.Integer, db.ForeignKey('child.id'))
                        )


class Parent(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(150), nullable=False)
    createdAt = db.Column('CreatedAt', db.DateTime, server_default=db.func.now())
    updatedAt = db.Column('UpdatedAt', db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    child = db.relationship("Child",
                            secondary=parent_child,
                            backref=db.backref("child"),
                            lazy='dynamic',
                            passive_deletes=True)


class Child(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(150), nullable=False)
    createdAt = db.Column('CreatedAt', db.DateTime, server_default=db.func.now())
    updatedAt = db.Column('UpdatedAt', db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    parent = db.relationship("Parent", secondary=parent_child,
                             backref=db.backref("parent"),
                             lazy='dynamic',
                             cascade="all,delete",
                             passive_deletes=True)