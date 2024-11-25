from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from fastapi.responses import HTMLResponse
from textblob import TextBlob

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Initialize the Hugging Face summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Initialize the FastAPI app
app = FastAPI()

class Story(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def get_index():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Generate Insights</title>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #response { margin-top: 20px; padding: 10px; border: 1px solid #ccc; }
            textarea { width: 100%; height: 150px; }
            button { padding: 10px 20px; font-size: 16px; }
        </style>
    </head>
    <body>
        <h1>Generate Insights</h1>
        <form id="storyForm">
            <label for="storyInput">Enter your story:</label>
            <textarea id="storyInput" name="story"></textarea>
            <br>
            <button type="button" id="submitButton">Submit</button>
        </form>
        <div id="response">
            <h3>Insights:</h3>
            <p id="output"></p>
        </div>

        <script>
            $(document).ready(function() {
                $('#submitButton').click(function() {
                    const storyText = $('#storyInput').val();
                    if (!storyText.trim()) {
                        alert("Please enter a story.");
                        return;
                    }

                    // Make an API call
                    $.ajax({
                        url: "/generate_insights",
                        type: "POST",
                        contentType: "application/json",
                        data: JSON.stringify({ text: storyText }),
                        success: function(response) {
                            $('#output').text(response.insights);
                        },
                        error: function(error) {
                            $('#output').text("Error generating insights: " + error.responseText);
                        }
                    });
                });
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
@app.post("/generate_insights/")
async def generate_insights(story: Story):
    # Summarize the text using the Hugging Face summarization model
    summary = summarizer(story.text, max_length=200, min_length=50, do_sample=False)
    summary_text = summary[0]['summary_text']
    
    # Generate insights dynamically from the summarized story
    insights = generate_dynamic_insights(summary_text)
    
    return {"summary": summary_text, "insights": insights}

def generate_dynamic_insights(summary_text):
    # Tokenizing the text and removing stop words to extract important keywords
    words = word_tokenize(summary_text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words and word.isalnum()]
    
    # Count frequency of words to get the most frequent keywords
    word_counts = Counter(filtered_words)
    most_common_words = word_counts.most_common(5)  # Get top 5 most common words
    
    # Analyze the sentiment of the summary using TextBlob
    sentiment = TextBlob(summary_text).sentiment
    
    # Generate insights based on the keywords and sentiment analysis
    insights = []
    if 'effort' in [word[0].lower() for word in most_common_words]:
        insights.append("Consistent effort, even when results aren't visible, is key to long-term success.")
    if 'growth' in [word[0].lower() for word in most_common_words]:
        insights.append("Growth often requires patience and a strong foundation before visible results appear.")
    if sentiment.polarity > 0.1:
        insights.append("The positive sentiment indicates an encouraging outcome from persistence and belief.")
    elif sentiment.polarity < -0.1:
        insights.append("The story suggests overcoming challenges and setbacks is part of the journey.")
    
    if not insights:
        insights.append("The story highlights perseverance and patience leading to eventual success.")
    
    return insights

# To run the app, use this command:
# uvicorn insights_app:app --reload
