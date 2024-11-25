# __AI-Driven Insights Generator__

This project is an AI-powered application for generating insights from stories. Using NLP models, it summarizes input text, analyzes sentiment, and identifies key insights dynamically. The application is built with FastAPI for serving the API and a simple frontend for user interaction.

## __Technologies__

FastAPI: Backend framework for building RESTful APIs.
Transformers: NLP models (Hugging Face) for text summarization.
NLTK: Natural language processing for text tokenization and stopword removal.
TextBlob: Sentiment analysis.
HTML, JavaScript, jQuery: Frontend for user interaction.

## __The Requirements.txt__

file specifies the Python libraries project needs. Based on the dependencies would look like this:

## Dependencies
- fastapi
- uvicorn
- transformers
- nltk
- textblob


Generate requirements.txt 

pip freeze > requirements.txt

This command creates a requirements.txt file with all installed libraries and their versions.



# Insights App

A FastAPI-based application for summarizing text and generating dynamic insights.

## Features
- Summarizes stories using Hugging Face models.
- Extracts keywords and performs sentiment analysis.
- Provides an interactive web interface.

## Install them using:

pip install -r requirements.txt

## Running the Application
Clone the repository:

git clone https://github.com/your-username/insights-app.git

cd insights-app

## Install the dependencies:

pip install -r requirements.txt

## Run the application:

python -m uvicorn insights_app:app --reload

Open 
http://127.0.0.1:8000 in your browser.

#Notes:
Ensure you have Python 3.8 or higher installed.
NLTK data (e.g., stopwords) will be downloaded automatically during the first run.

## Working Mode:
Access the Frontend
Navigate to http://127.0.0.1:8000
to use the form for submitting stories and generating insights.

Use API for Automation You can interact with the API using curl or tools like Postman.

Example using Curl:


curl --location 'http://127.0.0.1:8000/generate_insights/' \
--header 'Content-Type: application/json' \
--data '{
  {
  "text": "Rocky Balboa, a small-time boxer living in Philadelphia, is struggling to make a name for himself. Known as the 'Italian Stallion,' he works as a debt collector and fights in small-time matches to get by. One day, Rocky is unexpectedly chosen by the world heavyweight champion, Apollo Creed, as his next opponent for a publicity stunt. Although Rocky is seen as an underdog with no chance of winning, he decides to take the fight seriously. With the help of his trainer Mickey and the emotional support of his girlfriend Adrian, Rocky begins an intense training regimen. On the night of the fight, Rocky shocks everyone by holding his own against Apollo, going the full 15 rounds in a grueling match. Though he loses by split decision, Rocky earns respect and proves his determination, showing that perseverance and belief in oneself can lead to personal triumph."
}

}'

### Response Example:


{
  "summary": " Rocky Balboa...",
  "insights": [
  
    "The story highlights perseverance and patience leading to eventual success."
  ]
}

Features:

### Frontend:

A user-friendly form for submitting stories.
Real-time response display for insights.

### Backend:

Summarization: Uses Hugging Face's DistilBart model for text summarization.
Sentiment Analysis: Analyzes text polarity and subjectivity.
Keyword Extraction: Identifies important keywords and themes from the text.
Dynamic Insights: Provides insights based on text analysis.

#### Future Plans:
Authentication/Authorization: Add user-specific access controls.
Docker Image:  To Create a containerized version for deployment.

#### Contribution:
Feel free to contribute by opening issues or pull requests.
