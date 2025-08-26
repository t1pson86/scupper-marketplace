from sqlalchemy import text
from enum import Enum
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class CategoryEnum(str, Enum):
    ELECTRONICS = "electronics"
    CLOTHES = "clothes"
    CLOTHING = "clothing"
    FOOD = "food"
    OTHER = "other"


class AdvertisementsModel(Base):
    __tablename__ = "advertisements"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    uniq_id: Mapped[str] = mapped_column(nullable=False, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    category: Mapped[CategoryEnum] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    creator_id: Mapped[int] = mapped_column(nullable=False)