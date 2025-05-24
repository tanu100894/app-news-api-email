import requests

url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-04-24&sortBy=publishedAt&"
       "apiKey=b6b943e5e3424027b0ace04bfec08639")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
