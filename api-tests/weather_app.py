# Application - build my GUI

from tkinter import *
import requests

class Application(Frame):
    # class attributes
    WIDTH = 1000
    HEIGHT = 700
    # constructor
    def __init__(self, window):
        super().__init__(window)
        self.config(background="#ffcc00")
        self.grid()

        # GUI components

        self.label1 = Label(window, text="Type a city in the box below to see the weather there", height=2, width=50)
        self.label1.grid(row=0, column=0, rowspan=1, columnspan=1)

        self.txtBox = Text(window, bg="#7F7F7F", height=1, width=50)
        self.txtBox.config(state="normal")
        self.txtBox.grid(sticky='N', row=1, column=0)

    def getTxt(self):
        return self.txtBox


def search(app):
    city = app.getTxt().get(0.0, END)
    app.getTxt().delete(0.0, END)
    # print(city)
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=fc0ac9e5c5427635f55eaae1e37eadc1")
    # print(response.status_code)

    if response.status_code != 404:
        data = response.json()
        results = ""
        name = data['name']
        results += name + " weather:\n"

        # get description
        if 'weather' in data:
            weather = data['weather']
            id = weather[0]
            description = id['description']
            results += "Description: " + description + "\n"

        # get temperature in Milwaukee
        if 'main' in data:
            temps = data['main']
            mketmp = int((temps['temp'] - 273.15) * float(9 / 5) + 32)
            results += "Temperature: " + str(mketmp) + "ºF\n"

        # get rain volume in last hour
        if 'rain' in data:
            rain = data['rain']
            volume = rain['1h']
            results += "Rain in the last hour: " + str(volume) + "mm\n"

        # get wind speed
        if 'wind' in data:
            wind = data['wind']
            speed = wind['speed']
            results += "Wind: " + str(speed) + "mph\n"

        labela = Label(text=results, height=10, width=50)
        labela.grid(row=3, column=0, rowspan=1)
        # print(results)


def main():
    root = Tk()
    root.title("Weather App")
    root.geometry("500x500")
    app = Application(root)
    button = Button(root, text="Search", activebackground="#0000FF", command=lambda: search(app))
    button.grid(sticky='N', row=2, column=0)
    root.mainloop()

# call main
main()
