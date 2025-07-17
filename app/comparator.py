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



#OR

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# def filter_top_matches(query, df, top_k=5):
#     vectorizer = TfidfVectorizer()
#     uses = df['uses'].fillna("").tolist()
#     tfidf_matrix = vectorizer.fit_transform(uses + [query])
#     similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]
#     top_indices = similarities.argsort()[::-1][:top_k]
#     return df.iloc[top_indices]
