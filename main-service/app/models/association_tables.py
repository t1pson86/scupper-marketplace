from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from database import Base


class CartsAdvertisementsModel(Base):
    __tablename__ = 'carts_advertisements'

    cart_id: Mapped[int] = mapped_column(ForeignKey('carts.id'), primary_key=True, nullable=False)
    advertisement_id: Mapped[int] = mapped_column(ForeignKey('advertisements.id'), primary_key=True, nullable=False)
    added_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    cart: Mapped["CartsModel"] = relationship(back_populates="carts_advertisements")
    advertisement: Mapped["AdvertisementsModel"] = relationship(back_populates="carts_advertisements")