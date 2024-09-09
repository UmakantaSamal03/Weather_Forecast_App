from tkinter import *
import tkinter as tk

import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import pytz
from PIL import Image, ImageTk


def TK():
    return tk.Tk()


root = TK()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)


def getWeather():
    city = textfield.get()
    if not city:
        return  # Do nothing if the city is empty

    geolocator = Nominatim(user_agent="geoapiExercises")
    obj = TimezoneFinder()

    location = None  # Initialize location to ensure it's defined

    try:
        location = geolocator.geocode(city, timeout=10)
        if location is None:
            timezone.config(text="Location not found")
            long_lat.config(text="")
            clock.config(text="")
            return

        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        timezone.config(text=result)
        long_lat.config(text=f"{round(location.latitude, 1)}°N, {round(location.longitude, 1)}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)

        # Replace YOUR_API_KEY with your actual OpenWeatherMap API key
        api_key = "YOUR_API_KEY"  # Use a valid API key
        api = f"https://api.openweathermap.org/data/2.5/onecall?lat={location.latitude}&lon={location.longitude}&units=metric&exclude=hourly&appid={api_key}"
        response = requests.get(api)

        # Check if response status is OK
        if response.status_code == 200:
            json_data = response.json()

            # Extracting weather data
            temp = json_data['current']['temp']
            humidity = json_data['current']['humidity']
            pressure = json_data['current']['pressure']
            wind = json_data['current']['wind_speed']
            description = json_data['current']['weather'][0]['description']

            # Update labels with weather data
            t.config(text=f"{temp} °C")
            h.config(text=f"{humidity} %")
            p.config(text=f"{pressure} hPa")
            w.config(text=f"{wind} m/s")
            d.config(text=description)

            # First cell
            firstdayimage = json_data['daily'][0]['weather'][0]['icon']
            img = (Image.open(f"icon/{firstdayimage}@2x.png"))
            resized_image = img.resize((50, 50))
            photo1 = ImageTk.PhotoImage(resized_image)
            firstimage.config(image=photo1)
            firstimage.image = photo1

            tempday1 = json_data['daily'][0]['temp']['day']
            tempnight1 = json_data['daily'][0]['temp']['night']
            day1temp.config(text=f"Day: {tempday1}°C\nNight: {tempnight1}°C")

            # Second cell
            seconddayimage = json_data['daily'][1]['weather'][0]['icon']
            img = (Image.open(f"icon/{seconddayimage}@2x.png"))
            resized_image = img.resize((50, 50))
            photo2 = ImageTk.PhotoImage(resized_image)
            secondimage.config(image=photo2)
            secondimage.image = photo2

            tempday2 = json_data['daily'][1]['temp']['day']
            tempnight2 = json_data['daily'][1]['temp']['night']
            day2temp.config(text=f"Day: {tempday2}°C\nNight: {tempnight2}°C")

            # Third cell
            thirddayimage = json_data['daily'][2]['weather'][0]['icon']
            img = (Image.open(f"icon/{thirddayimage}@2x.png"))
            resized_image = img.resize((50, 50))
            photo3 = ImageTk.PhotoImage(resized_image)
            thirdimage.config(image=photo3)
            thirdimage.image = photo3

            tempday3 = json_data['daily'][2]['temp']['day']
            tempnight3 = json_data['daily'][2]['temp']['night']
            day3temp.config(text=f"Day: {tempday3}°C\nNight: {tempnight3}°C")

            # Fourth cell
            fourthdayimage = json_data['daily'][3]['weather'][0]['icon']
            img = (Image.open(f"icon/{fourthdayimage}@2x.png"))
            resized_image = img.resize((50, 50))
            photo4 = ImageTk.PhotoImage(resized_image)
            fourthimage.config(image=photo4)
            fourthimage.image = photo4

            tempday4 = json_data['daily'][3]['temp']['day']
            tempnight4 = json_data['daily'][3]['temp']['night']
            day4temp.config(text=f"Day: {tempday4}°C\nNight: {tempnight4}°C")

            # Fifth cell
            fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
            img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
            resized_image = img.resize((50, 50))
            photo5 = ImageTk.PhotoImage(resized_image)
            fifthimage.config(image=photo5)
            fifthimage.image = photo5

            tempday5 = json_data['daily'][4]['temp']['day']
            tempnight5 = json_data['daily'][4]['temp']['night']
            day5temp.config(text=f"Day: {tempday5}°C\nNight: {tempnight5}°C")

            # Sixth cell
            sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
            img = (Image.open(f"icon/{sixthdayimage}@2x.png"))
            resized_image = img.resize((50, 50))
            photo6 = ImageTk.PhotoImage(resized_image)
            sixthimage.config(image=photo6)
            sixthimage.image = photo6

            tempday6 = json_data['daily'][5]['temp']['day']
            tempnight6 = json_data['daily'][5]['temp']['night']
            day6temp.config(text=f"Day: {tempday6}°C\nNight: {tempnight6}°C")

            # Seventh cell
            seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
            img = (Image.open(f"icon/{seventhdayimage}@2x.png"))
            resized_image = img.resize((50, 50))
            photo7 = ImageTk.PhotoImage(resized_image)
            seventhimage.config(image=photo7)
            seventhimage.image = photo7

            tempday7 = json_data['daily'][6]['temp']['day']
            tempnight7 = json_data['daily'][6]['temp']['night']
            day7temp.config(text=f"Day: {tempday7}°C\nNight: {tempnight7}°C")

            # Days of the week
            first = datetime.now()
            day1.config(text=first.strftime("%A"))

            second = first + timedelta(days=1)
            day2.config(text=second.strftime("%A"))

            third = first + timedelta(days=2)
            day3.config(text=third.strftime("%A"))

            fourth = first + timedelta(days=3)
            day4.config(text=fourth.strftime("%A"))

            fifth = first + timedelta(days=4)
            day5.config(text=fifth.strftime("%A"))

            sixth = first + timedelta(days=5)
            day6.config(text=sixth.strftime("%A"))

            seventh = first + timedelta(days=6)
            day7.config(text=seventh.strftime("%A"))

        else:
            # Handle error
            print(f"Error: Non-successful status code {response.status_code}")
            timezone.config(text="Error fetching data")
            long_lat.config(text="")
            clock.config(text="")
            t.config(text="N/A")
            h.config(text="N/A")
            p.config(text="N/A")
            w.config(text="N/A")
            d.config(text="N/A")

    except Exception as e:
        print(f"Error: {e}")
        timezone.config(text="Error fetching data")
        long_lat.config(text="")
        clock.config(text="")
        t.config(text="N/A")
        h.config(text="N/A")
        p.config(text="N/A")
        w.config(text="N/A")
        d.config(text="N/A")


# Icon
image_icon = PhotoImage(file=r"D:\Python Project\Images\logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file=r"D:\Python Project\Images\Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

# Labels
label1 = Label(root, text="Temperature", font=('Helvetica', 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=('Helvetica', 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=('Helvetica', 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed", font=('Helvetica', 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=('Helvetica', 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

t = Label(root, font=("arial", 11), fg="white", bg="#203243")
t.place(x=150, y=120)

h = Label(root, font=("arial", 11), fg="white", bg="#203243")
h.place(x=150, y=140)

p = Label(root, font=("arial", 11), fg="white", bg="#203243")
p.place(x=150, y=160)

w = Label(root, font=("arial", 11), fg="white", bg="#203243")
w.place(x=150, y=180)

d = Label(root, font=("arial", 11), fg="white", bg="#203243")
d.place(x=150, y=200)

# Search Box
Search_image = PhotoImage(file=r"D:\Python Project\Images\Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file=r"D:\Python Project\Images\Layer 7.png")
myimage_icon = Button(image=weat_image, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=620, y=125)

textfield = tk.Entry(root, justify='center', width=17, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

# Bottom box
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# Timezone and Clock
timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

clock = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
clock.place(x=700, y=90)

# First cell
firstframe = Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=35, y=315)

day1 = Label(firstframe, font=("Helvetica", 20), fg="#fff", bg="#282829")
day1.place(x=100, y=5)

firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=1, y=15)

day1temp = Label(firstframe, font=("Helvetica", 15), fg="#fff", bg="#282829")
day1temp.place(x=100, y=50)

# Second cell
secondframe = Frame(root, width=70, height=115, bg="#282829")
secondframe.place(x=305, y=325)

day2 = Label(secondframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day2.place(x=10, y=5)

secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=7, y=20)

day2temp = Label(secondframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day2temp.place(x=10, y=50)

# Third cell
thirdframe = Frame(root, width=70, height=115, bg="#282829")
thirdframe.place(x=405, y=325)

day3 = Label(thirdframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day3.place(x=10, y=5)

thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=7, y=20)

day3temp = Label(thirdframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day3temp.place(x=10, y=50)

# Fourth cell
fourthframe = Frame(root, width=70, height=115, bg="#282829")
fourthframe.place(x=505, y=325)

day4 = Label(fourthframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day4.place(x=10, y=5)

fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=7, y=20)

day4temp = Label(fourthframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day4temp.place(x=10, y=50)

# Fifth cell
fifthframe = Frame(root, width=70, height=115, bg="#282829")
fifthframe.place(x=605, y=325)

day5 = Label(fifthframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day5.place(x=10, y=5)

fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=7, y=20)

day5temp = Label(fifthframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day5temp.place(x=10, y=50)

# Sixth cell
sixthframe = Frame(root, width=70, height=115, bg="#282829")
sixthframe.place(x=705, y=325)

day6 = Label(sixthframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day6.place(x=10, y=5)

sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=7, y=20)

day6temp = Label(sixthframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day6temp.place(x=10, y=50)

# Seventh cell
seventhframe = Frame(root, width=70, height=115, bg="#282829")
seventhframe.place(x=805, y=325)

day7 = Label(seventhframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day7.place(x=10, y=5)

seventhimage = Label(seventhframe, bg="#282829")
seventhimage.place(x=7, y=20)

day7temp = Label(seventhframe, font=("Helvetica", 10), fg="#fff", bg="#282829")
day7temp.place(x=10, y=50)

root.mainloop()




