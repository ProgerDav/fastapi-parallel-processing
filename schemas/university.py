from typing import Optional
from pydantic import BaseModel


class University(BaseModel):
    country: Optional[str] = None
    name: Optional[str] = None
    alpha_two_code: Optional[str] = None
    web_pages: list[str] = []
    domains: list[str] = []
