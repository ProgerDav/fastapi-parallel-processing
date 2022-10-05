from pydantic import BaseModel


class Country(BaseModel):
    countries: list[str]

    class Config:
        schema_extra = {
            "example": {
                "countries": ["armenia", "india", "iran"],
            }
        }
