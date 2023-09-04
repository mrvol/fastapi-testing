from fastapi import FastAPI
from models import Item

app = FastAPI()


@app.get(
    "/categories",
    summary="Receiving a list of unique categories",
    description="Receiving a list of unique categories from https://api.publicapis.org/entries",
)
def get_categories():
    return sorted({it.category for it in Item.get_data()})


@app.get(
    "/data/{category}",
    summary="Receiving a list of APIs filtered by category",
    description="Receiving a list of APIs filtered by category and optional param `search` what is searching in `api`/`description` fields in the taken list from [https://api.publicapis.org/entries](https://api.publicapis.org/entries)",
)
def get_by_category(category: str, search: str | None = None):
    data = [{
        'api': it.api,
        'desctription': it.description,
        'link': it.link}
        for it in Item.get_data() if it.category == category and ((search in it.api or search in it.description) if search else True)]
    return data