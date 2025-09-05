from pydantic import BaseModel

from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class PaginatedResponse(BaseModel, Generic[T]):
    total_count: int
    total_pages: int
    current_page: int
    items_per_page: int
    items: List[T]

    class Config:
        from_attributes = True