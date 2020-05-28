import requests

outfile = open("covid_data.txt", "w")

def getCovidData():
    url = "https://covid-193.p.rapidapi.com/history"

    year = "2020"
    global month
    global day
    month = 3
    day = 21
    new_cases = []
    total_cases = []
    new_deaths = []
    total_deaths = []

    while month != 5 or day != 25:
        d = ""
        if day < 10:
            d = "0" + str(day)
        else:
            d = str(day)
        date = year + "-" + "0" + str(month) + "-" + d

        querystring = {"day": date, "country": "usa"}

        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "b0ca58cb10msh4cb9eb7e8f6f27ap1efd3bjsn108a4f7b1c63"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        d = response.json()
        print(d)
        data = []
        if d['response']:
            data = d['response'][len(d['response'])-1]

            cases = data['cases']
            cases_new = cases['new']
            cases_new = ''.join(cases_new.split('+', 1))
            new_cases.append(int(cases_new))
            total_cases.append(int(cases['total']))

            deaths = data['deaths']
            deaths_new = deaths['new']
            deaths_new = ''.join(deaths_new.split('+', 1))
            new_deaths.append(int(deaths_new))
            total_deaths.append(deaths['total'])

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

    # print(date)
    # print("New Deaths: ", end="")
    # print(new_deaths)
    # print("Total Deaths: ", end="")
    # print(total_deaths)
    # print("Total Cases: ", end="")
    # print(total_cases)
    # print("New Cases: ", end="")
    # print(new_cases)

    # print("New Deaths: ", end="", file=outfile)
    for i in new_deaths:
        print(str(i), end=", ", file=outfile)
    print("\n", file=outfile)
    for i in total_deaths:
        print(str(i), end=", ", file=outfile)
    print("\n", file=outfile)
    for i in new_cases:
        print(str(i), end=", ", file=outfile)
    print("\n", file=outfile)
    for i in total_cases:
        print(str(i), end=", ", file=outfile)


getCovidData()

outfile.close()
