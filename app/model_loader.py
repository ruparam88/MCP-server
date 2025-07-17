from transformers import pipeline

def load_model():
    return pipeline("text-generation", model="Mayank-22/Mayank-AI")
