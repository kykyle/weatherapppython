from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

#url
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

api_key = '06d813f45eacda00565ce7c6d7331777'

def weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        # turn result into json
        json = result.json()
        #extracts infor based on the json formatter
        city=json['name']
        country = json['sys']['country']
        tempkelvin = json['main']['temp']
        tempcelsius = tempkelvin-273.15
        weather = json['weather'][0]['main']
        icons = json['weather'][0]['icon']

        final = [city, country, tempcelsius, weather]
        return final
    else:
        return None


#define search
def search():
    global img;
    city = city_usertext.get()
    weathercheck = weather(city)
    if weathercheck:
        location_label['text']='{}'.format(weathercheck[0])
        temp_label['text'] = '{:.3f}°'.format(weathercheck[2])
        weather_label['text'] = weathercheck[3]
       # image['file'] = 'icons2/{}.jpg'.format(weather[4])
    else:
        messagebox.showerror('error', 'cannot find city {}'.format(city))

app = Tk()
app.geometry('300x400')

Headings = Label(app, text = "Enter City :", font=("Tacoma", 20))
Headings.pack()


#user input
city_usertext = StringVar()
city_entry= Entry(app, textvariable=city_usertext)
city_entry.pack()

#button
search_city = Button(app, text ="Search", command = search)
search_city.pack()

#getinformation



location_label = Label(app, text= "", font=("Tacoma", 15))
location_label.pack()


temp_label = Label(app, text= "")
temp_label.pack()

weather_label= Label(app, text="")
weather_label.pack()

#img = PhotoImage(file="")
#image = Label(app, image = img)
#image.pack();

app.mainloop()

