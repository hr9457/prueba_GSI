from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

# declarative base class
class Base(DeclarativeBase):
    pass


class Kanba(Base):

    __tablename__ = "kanban"

    id: Mapped[int] = mapped_column(primary_key=True)
    name_kanban: Mapped[str] = mapped_column(String(100))