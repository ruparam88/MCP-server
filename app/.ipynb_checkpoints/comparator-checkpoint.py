from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_top_matches(model, df, query, top_k=5):
    results = []

    for _, row in df.iterrows():
        prompt = (
            f"Query: {query}\n"
            f"Medicine Name: {row['name']}\n"
            f"Composition: {row['composition']}\n"
            f"Uses: {row['uses']}"
        )

        description = model(prompt, max_length=80, truncation=True)[0]['generated_text']

        results.append({
            "name": row["name"],
            "description": description,
            "image_url": row["image_url"],
            "url": f"http://127.0.0.1:8000/product/{row['name'].replace(' ', '_')}"
        })

    return results[:top_k]