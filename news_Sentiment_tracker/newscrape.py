import requests

response = requests.get("https://gnews.io/api/v3/search?q=covid19&max=100&token=api-key")

data = response.json()

# for dict in data:
#    print(dict, end=": ")
#    print(data[dict])

articles = data['articles']
titles = []
for element in articles:
    titles.append(element['title'])

print(titles)
url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

score = 0.0
counter = 0
for element in titles:
    counter += 1
    querystring = {"text": element}

    headers = {
        'x-rapidapi-host': "twinword-sentiment-analysis.p.rapidapi.com",
        'x-rapidapi-key': "api-key"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    score += data['score']

score /= counter

if score >= .05:
    print("Average score is positive: ", score)
elif score <= .05:
    print("Average score is negative: ", score)
else:
    print("Average score is neutral: ", score)
