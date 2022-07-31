This project is an IP Adress based weather report Application. To run it, simply double click the weather_gui.exe or run the weather_gui.py file.
The tkinter GUI is generated from a JSON file that is created by a GO language scrubber that first scrubs an IP website to get your location, then scrubs a Weather CODE lookup website to find your
weather code, so that it can go to that specific location's 14 day weather report via URL without having to use an API. The go scraper then scrapes the webpage for Date, Weather, HI/LOW temperature, 
percipitation % and wind speed for each of the 14 days.   

To get the IP functionality, a VPN was used to simulate different IP addresses.