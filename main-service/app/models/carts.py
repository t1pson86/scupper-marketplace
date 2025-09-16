from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database import Base

class CartsModel(Base):
    __tablename__ = "carts" 

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)

    carts_advertisements: Mapped["CartsAdvertisementsModel"] = relationship(
        "CartsAdvertisementsModel",
        back_populates="cart",
        cascade="all, delete-orphan"
    )

    