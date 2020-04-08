# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt
from myflaskapp.database import Column, Model, SurrogatePK, db


class Config(SurrogatePK, Model):
    """A user of the app."""
    __tablename__ = 'config'
    id = Column(db.Integer, primary_key=True)

    USL = Column(db.String(), unique=False, nullable=True)
    UCL = Column(db.String(), unique=False, nullable=True)
    T = Column(db.String(), unique=False, nullable=True)
    LCL = Column(db.String(), unique=False, nullable=True)
    LSL = Column(db.String(), unique=False, nullable=True)
    IP_address = Column(db.String(), unique=False, nullable=True)
    IP_port = Column(db.String(), unique=False, nullable=True)
    CSV_data = Column(db.String(), unique=False, nullable=True)
    Room = Column(db.String(), unique=False, nullable=True)
    Furnace = Column(db.String(), unique=False, nullable=True)
    Pieces = Column(db.String(), unique=False, nullable=True)
    MIN = Column(db.String(), unique=False, nullable=True)
    MAX = Column(db.String(), unique=False, nullable=True)
    Set = Column(db.String(), unique=False, nullable=True)
    Platform = Column(db.String(), unique=False, nullable=True)
    Pipe = Column(db.String(), unique=False, nullable=True)
    Version = Column(db.String(), unique=False, nullable=True)
    TestPoint = Column(db.String(), unique=False, nullable=True)
    CSV_file = Column(db.String(), unique=False, nullable=True)
    Excel_output = Column(db.String(), unique=False, nullable=True)
    Break_points = Column(db.String(), unique=False, nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    only_pipe = Column(db.Integer(), default=0)
    is_use = Column(db.Integer(), default=0)
