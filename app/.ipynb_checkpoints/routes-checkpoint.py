from fastapi import APIRouter, Query
from app.model_loader import load_model
from app.database import load_database
from app.comparator import get_top_matches 

router = APIRouter()

model = load_model()
db = load_database()

@router.get("/compare")
def compare_query(q: str = Query(..., description="Search for symptoms or medicine")):
    matches = get_top_matches(model, db, q)

    return matches

@router.get("/product/{product_name}")
def get_product(product_name: str):
    product_name = product_name.replace("_", " ")
    row = db[db["name"].str.lower() == product_name.lower()]
    if row.empty:
        return {"error": "Product not found"}
    
    product = row.iloc[0]
    return {
        "name": product["name"],
        "composition": product["composition"],
        "uses": product["uses"],
        "side_effects": product["side_effects"],
        "image_url": product["image_url"]
    }
