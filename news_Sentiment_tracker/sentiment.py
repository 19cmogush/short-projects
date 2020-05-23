import requests

url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

querystring = {"text":"great value in its price range!"}

headers = {
    'x-rapidapi-host': "twinword-sentiment-analysis.p.rapidapi.com",
    'x-rapidapi-key': "b0ca58cb10msh4cb9eb7e8f6f27ap1efd3bjsn108a4f7b1c63"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()
print(data)