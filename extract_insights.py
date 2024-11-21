from transformers import pipeline
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize

# New story
story = """
Santiago was just a shepherd boy with a recurring dream of treasure. He left his comfort behind, journeying through deserts and dangers, only to discover the greatest treasure lay within himself. His story reminds us to follow our hearts, for they know the way.
"""

sentences = sent_tokenize(story)

# Initialize  pipeline
summarizer = pipeline("summarization")

#relevant keywords for filtering 
keywords = ["dream", "treasure", "journey", "self-discovery", "heart", "growth"]


filtered_sentences = [s for s in sentences if any(k in s.lower() for k in keywords)]

# Summarize  filtered sentences
if filtered_sentences:
    summary = summarizer(" ".join(filtered_sentences), max_length=50, min_length=10, do_sample=False)
    print("Key Insights:", summary[0]["summary_text"])
else:
    # If no filtered sentences match, summarize the entire text
    summary = summarizer(story, max_length=50, min_length=10, do_sample=False)
    print("Summary:", summary[0]["summary_text"])
