from transformers import pipeline

def load_model():
    return pipeline("text2text-generation", model="Mayank-22/Mayank-AI")
