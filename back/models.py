from sqlalchemy import Column, Integer, String
from sqlalchemy.types import PickleType
from database import Base

class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    title = Column(String)
    comments = Column(PickleType, default=[])
#    comment = Column(MutableList.as_mutable(PickleType), default=[])
