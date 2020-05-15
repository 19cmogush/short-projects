import requests

url = "https://numbersapi.p.rapidapi.com/6/21/date"

querystring = {"fragment":"true","json":"true"}

headers = {
    'x-rapidapi-host': "numbersapi.p.rapidapi.com",
    'x-rapidapi-key': "b0ca58cb10msh4cb9eb7e8f6f27ap1efd3bjsn108a4f7b1c63"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)