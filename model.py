from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Unmanaged(Base):
    __tablename__ = "unmanaged"

    key = mapped_column(String(64), primary_key=True)
    value = mapped_column(String(1024), nullable=False)


class User(Base):
    __tablename__ = "app_user"

    username = mapped_column(String(32), primary_key=True)
    password = mapped_column(String(512), nullable=False)

