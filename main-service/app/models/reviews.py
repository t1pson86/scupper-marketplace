from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class ReviewsModel(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    stars: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True, default=None)

    advertisement_id: Mapped[int] = mapped_column(
        ForeignKey("advertisements.id", ondelete="CASCADE"), 
        nullable=False
    )

    advertisement: Mapped["AdvertisementsModel"] = relationship(
        "AdvertisementsModel", 
        back_populates="reviews"
    )
    