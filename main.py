import requests, os
from dotenv import load_dotenv
from send_email import send_email

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("api_key")

topic = "tesla"

url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       f"sortBy=publishedAt&"
       f"language=en&"
       f"apiKey={api_key}")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the titles and description
body = "Subject: Today's news \n\n"
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = (body + article["title"]
                + "\n" + article["description"]
                + "\n" + article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(message=body)


