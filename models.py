from pydantic import BaseModel, Field
from functools import cache
import settings
import requests

# "API": "AdoptAPet",
# "Description": "Resource to help get pets adopted",
# "Auth": "apiKey",
# "HTTPS": true,
# "Cors": "yes",
# "Link": "https://www.adoptapet.com/public/apis/pet_list.html",
# "Category": "Animals"

class Item(BaseModel):
    api: str = Field(alias="API")
    description: str = Field(alias="Description")
    auth: str = Field(alias="Auth")
    https: bool = Field(alias="HTTPS")
    cors: str = Field(alias="Cors")
    link: str = Field(alias="Link")
    category: str = Field(alias="Category")

    @classmethod
    @cache
    def get_data(cls):
        return sorted([cls(**x) for x in requests.get(settings.DATA_ENDPOINT).json()['entries'] if x['HTTPS'] is True], key=lambda x: x.api)
