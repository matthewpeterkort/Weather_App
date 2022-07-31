import json
import os
from tkinter import *
from PIL import ImageTk, Image
import time
#OS commands that clean up json files in directory and run the go backend then search for the only json remaining
# to use for showing the weather report

for f in os.listdir("C:/Users/matth/Desktop/weather_app/"):
    if not f.endswith(".json"):
        continue
    os.remove(os.path.join("C:/Users/matth/Desktop/weather_app/", f))
 
os.system('cd C:/Users/matth/Desktop/weather_app/')
os.system('go run weather.go')
OEFILE=" "
time.sleep(1.5) 
for root, dirs, files in os.walk("C:/Users/matth/Desktop/weather_app/"):
    for file in files:
        if file.endswith('.json'):
            OEFILE=file


with open (OEFILE) as f:
	data = json.load(f)

win = Tk()
#Changing the decapitalized Country letter back to capital
index=OEFILE.find(',')
nen_letter= OEFILE[index+1].upper()
OEFILE= OEFILE[:index+1]+ nen_letter + OEFILE[index+2:]

#chopping off the file extension 
win.title("14 Day Weather Report For: " + OEFILE[0:-5])

#loading all of the images needed to do create the weather report GUI
win.configure(bg='white')
rain=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/rain.png")
partly_cloudy=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/partly_cloudy.png")
percip=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/percip.png")
rain_light=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/rain_light.png")
rain_s_cloudy=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/rain_s_cloudy.png")
Scattered_Thunderstorms=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/Scattered_Thunderstorms.png")
Sunny=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/Sunny.png")
Sunny_s_rain=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/sunny_s_rain.png")
Thunderstorms=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/thunderstorms.png")
wind=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/wind.png")
mostly_sunny=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/mostly_sunny.png")
Sunny_Wind=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/Sunny_Wind.png")
Isolated_Thunderstorms=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/Isolated_Thunderstorms.png")
Mostly_Cloudy=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/mostly_cloudy.png")
Clear=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/Clear.PNG")
Place_Holder=Image.open("C:/Users/matth/Desktop/weather_app/Weather_Assets/placeholder.PNG")
idx=0
myimg=" "
#for each day, check weather the weather keyword and match it with its picture
for i in range(14):
	#print(data[i]['Weather'])
	if   "Thunderstorms" in data[i]['Weather']:
		myimg = ImageTk.PhotoImage(Thunderstorms)
	if "Clear" in data[i]['Weather']:
		myimg = ImageTk.PhotoImage(Clear)
	if(data[i]['Weather']) == "Mostly Clear":
		myimg = ImageTk.PhotoImage(Clear)
	if(data[i]['Weather']) == "AM Thunderstorms":
		myimg = ImageTk.PhotoImage(Thunderstorms)
	if(data[i]['Weather']) == "Thunderstorms Late":
		myimg = ImageTk.PhotoImage(Thunderstorms)
		data[i]['Weather']="Thunderstorms \n Late"
	if(data[i]['Weather']) == "Thunderstorms":
		myimg = ImageTk.PhotoImage(Thunderstorms)
	if( "Mostly Cloudy" in data[i]['Weather']):
		myimg = ImageTk.PhotoImage(Mostly_Cloudy)
	if( "Showers" in data[i]['Weather']):
		myimg = ImageTk.PhotoImage(rain)

	if( "Partly Cloudy" in data[i]['Weather']):
		myimg = ImageTk.PhotoImage(partly_cloudy)
	if(data[i]['Weather']) == "Partly Cloudy":
		myimg = ImageTk.PhotoImage(partly_cloudy)
	if(data[i]['Weather']) == "Showers":
		myimg = ImageTk.PhotoImage(rain)
	if(data[i]['Weather']) == "Light Rain":
		myimg = ImageTk.PhotoImage(rain)
	if(data[i]['Weather']) == "Scattered Thunderstorms":
		myimg = ImageTk.PhotoImage(Scattered_Thunderstorms)
		data[i]['Weather']="Scattered \n Thunderstorms"
	if(data[i]['Weather']) == "Sunny":
		myimg = ImageTk.PhotoImage(Sunny)
	if(data[i]['Weather']) == "Mostly Sunny":
		myimg = ImageTk.PhotoImage(mostly_sunny)
	if(data[i]['Weather']) == "AM Light Rain":
		myimg = ImageTk.PhotoImage(rain)
	if(data[i]['Weather']) == "PM Light Rain":
		myimg = ImageTk.PhotoImage(rain)
	if(data[i]['Weather']) == "AM Showers":
		myimg = ImageTk.PhotoImage(rain)
	if(data[i]['Weather']) == "PM Showers":
		myimg = ImageTk.PhotoImage(rain)
	if(data[i]['Weather']) == "Sunny/Wind":
		myimg = ImageTk.PhotoImage(Sunny_Wind)
	if(data[i]['Weather']) == "Isolated Thunderstorms":
		myimg = ImageTk.PhotoImage(Isolated_Thunderstorms)
		data[i]['Weather']="Isolated \n Thunderstorms"
	if(data[i]['Weather']) == "Mostly Cloudy":
		myimg = ImageTk.PhotoImage(Mostly_Cloudy)
	if( "Sunny" in data[i]['Weather']):
		myimg = ImageTk.PhotoImage(Sunny)
	if( "Clouds" in data[i]['Weather']):
		myimg = ImageTk.PhotoImage(partly_cloudy)
	if(myimg == " "):
		myimg = ImageTk.PhotoImage(Place_Holder)

	
	#chopping erronous character that was created when scraping weather.com so that the degree character can be shown properly
	j= data[i]['High']
	j=j[0:len(j)-2]+ j[len(j)-1]

	k=data[i]['Low']
	k=k[0:len(k)-2] + k[len(k)-1]
	
	#formatting the GUI to show all of the info in a centered neat, line.
	new_img= ImageTk.PhotoImage(percip)
	newest_img=ImageTk.PhotoImage(wind)

	img = Label(win, image=myimg, text= data[i]['Day'] +'  \n \n \n \n \n \n \n' + data[i]['Weather']+ '\n'  +j +
	' / '+k, compound='center')

	img_two=Label(win,image=new_img,text=data[i]['Percip'] ,compound='left')

	img_three=Label(win,image=newest_img,text=data[i]['Wind'],compound='bottom')

	img.config(bg="white")
	img_two.config(bg="white")
	img_three.config(bg="white")

	img.grid(row=0,column=i,padx=0,sticky="W")
	img_two.grid(row=1,column=i,sticky="W")
	img_three.grid(row=2,column=i)

	idx=idx+1

	img.image=myimg
	img_two.image=new_img
	img_three.image=newest_img

win.mainloop()
