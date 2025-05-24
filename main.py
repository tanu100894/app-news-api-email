import requests, os
from dotenv import load_dotenv
from send_email import send_email

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("API_KEY")

url = (f"https://newsapi.org/v2/everything?q=tesla&from=2025-04-24&sortBy=publishedAt&"
       f"apiKey={api_key}")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)


