import tkinter as tk
from retry_requests import retry
import requests_cache
import openmeteo_requests
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


## THIS TOOK ME 4.414 HOURS FOR SOME REASON

# Dont spam the button, because geopy is rate limited


class WeatherGUI():
    def __init__(self,tkinter_object : tk):
        self.canvas = tkinter_object
        self.canvas.geometry("600x500")
        self.canvas.title("Weather App")
        self.canvas.attributes(topmost = "True")
        
        self.gui_font = ("poppins",20, "bold")



        self.user_input = ""
        self.textfield = tk.Entry(self.canvas,font = self.gui_font)
        self.textfield.pack(pady=20,)

        self.inputbutton = tk.Button(self.canvas,width=10,height=1, text = "Enter")
        self.inputbutton.pack()


        self.frame = tk.Frame(self.canvas, )
        self.frame.pack()

        self.label1 = tk.Label(self.frame,font = self.gui_font)
        self.label2 = tk.Label(self.frame,font = self.gui_font)
        self.label3 = tk.Label(self.frame,font = self.gui_font)
        self.label4 = tk.Label(self.frame,font = self.gui_font)
        self.label5 = tk.Label(self.frame,font = self.gui_font)

        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()
        
       

    def get_input(self):
        self.input =self.textfield.get().strip()
        return self.input

    
        


    def show(self):
        self.canvas.mainloop()




class WeatherAPI():
    def __init__(self):
        # Like a python session object, sessions allows the the persistance of specific parameters, cookies, and auth credentials across multiple HTTP requests to the same host
        # normal requests forget everything after one request, a session object acts like an active web browser tab that remebers the current state
        # Caching - the process of storing copies of frequently accessed data
        # When requesting data, if it is already stored in a cache, it is loaded immediately,
        # Cache miss, if the data isnt in a cache, the system goes to the primary source, the stores a copy in the cache

        self.cache_session = requests_cache.CachedSession(".cache",expire_after=120)
        self.retry_session = retry(self.cache_session,retries=  3, backoff_factor= 0.2)
        self.openmeteo = openmeteo_requests.Client(session = self.retry_session)
        self.url = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self,latitude = 0, longitude = 0):
        self.params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m", "relative_humidity_2m", "precipitation", "surface_pressure","wind_speed_10m"],
            "timezone": "auto",
            "wind_speed_unit": "mph",
            "temperature_unit": "fahrenheit",
            "precipitation_unit": "inch",
        }
        self.responses = self.openmeteo.weather_api(self.url, params = self.params)
        self.response = self.responses[0]

        self.current = self.response.Current()
        self.current_data = {"current_temperature_2m" : self.current.Variables(0).Value(),"current_relative_humidity_2m" : 
                        self.current.Variables(1).Value(),"current_precipitation" : self.current.Variables(2).Value(),"current_surface_pressure" : self.current.Variables(3).Value(),"wind_speed_10m":self.current.Variables(4).Value()}

        return self.current_data
        
class WeatherApp():
    def __init__(self):
        self.tk_object = tk.Tk()
        self.gui = WeatherGUI(self.tk_object)
        self.api = WeatherAPI()
        self.loc = Nominatim(user_agent='Geopy Library', timeout = 10)
        self.geocoder = RateLimiter(self.loc.geocode, min_delay_seconds=1)
        self.gui.inputbutton.config(command = self.city_to_weather)


    def city_to_weather(self):
        self.text = self.gui.get_input()
        self.getLoc = self.loc.geocode(self.text)
    
        try:
            if self.getLoc:
                self.coords = {
                    "latitude": self.getLoc.latitude,
                    "longitude": self.getLoc.longitude
                }
    
                self.data = self.api.get_weather(self.coords["latitude"],self.coords["longitude"])
                print(self.data)
            else:
                print('City Not Found')

        except Exception as e:
            print(f"An error occurred: {e}")
   
        self.gui.label1.config(text=f"Temperature: {self.data["current_temperature_2m"]:.2f}")
        self.gui.label2.config(text=f"Relative Humidity: {self.data["current_relative_humidity_2m"]}")
        self.gui.label3.config(text=f"Precipitation: {self.data["current_precipitation"]}")
        self.gui.label4.config(text=f"Surface Pressure: {self.data["current_surface_pressure"]:.2f}")
        self.gui.label5.config(text=f"Wind Speed: {self.data["wind_speed_10m"]:.2f}")
       
    
    def show_gui(self):
        self.gui.show()
  
        
weather_app = WeatherApp()
weather_app.show_gui()