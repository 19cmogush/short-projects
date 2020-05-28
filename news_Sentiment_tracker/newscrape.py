import requests


doc = open("sentiment.csv", "w")


year = "2020"
month = 3
day = 21

while month != 5 or day != 25:
    d = ""
    if day < 10:
        d = "0" + str(day)
    else:
        d = str(day)
    date = year + "-" + "0" + str(month) + "-" + d

    response = requests.get("https://gnews.io/api/v3/search?q=covid19&maxdate=" + date + "&token=dc54b534c13117f14bb9ad291ac81e62")

    news_data = response.json()

    # for dict in data:
    #    print(dict, end=": ")
    #    print(data[dict])

    headers = {
        'x-rapidapi-host': "twinword-sentiment-analysis.p.rapidapi.com",
        'x-rapidapi-key': "api-key"
        }

    articles = news_data['articles']
    titles = []
    for element in articles:
        titles.append(element['title'])

    # print(titles)
    url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

    score = 0.0
    counter = 0
    for element in titles:
        counter += 1
        querystring = {"text": element}

        headers = {
            'x-rapidapi-host': "twinword-sentiment-analysis.p.rapidapi.com",
            'x-rapidapi-key': "b0ca58cb10msh4cb9eb7e8f6f27ap1efd3bjsn108a4f7b1c63"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        sentiment = response.json()
        # print(sentiment)
        # print(sentiment['score'])
        s = sentiment.get('score')
        if s:
            score += s

    score /= counter
    print(score, end=", ", file=doc)

    if month == 2 and day == 29:
        month = 3
        day = 0
    elif month == 3 and day == 31:
        month = 4
        day = 0
    elif month == 4 and day == 30:
        month = 5
        day = 0

    day += 1
    print("done")


# if score >= .05:
    # print("Average score is positive: ", score)
# elif score <= -.05:
    # print("Average score is negative: ", score)
# else:
    # print("Average score is neutral: ", score)
