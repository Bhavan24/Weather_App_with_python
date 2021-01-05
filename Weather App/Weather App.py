import tkinter as tk
import tkinter.font as tkFont
from bs4 import BeautifulSoup
import requests


root = tk.Tk()
root.title("Weather App")
root.geometry("376x300")
root.resizable(width=False, height=False)

def weather(city):
    city = city+" weather"
    city = city.replace(" ","+")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')   
    location = soup.select('#wob_loc')[0].getText().strip()  
    time = soup.select('#wob_dts')[0].getText().strip()       
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
    weatherC = weather+"°C"
    displayText.delete(1.0, tk.END) 
    displayText.insert('end',f'{location}\n{time}\n{info}\n{weatherC}')

def btn_command():
    weather(cityName.get())

btn = tk.Button(root)
btn["bg"] = "#5aff13"
ft = tkFont.Font(family='Times',size=18)
btn["font"] = ft
btn["fg"] = "#000000"
btn["justify"] = "center"
btn["text"] = "Get Weather"
btn["relief"] = "groove"
btn.place(x=40,y=60,width=301,height=38)
btn["command"] = btn_command

lbl1 = tk.Label(root)
ft = tkFont.Font(family='Times',size=18)
lbl1["font"] = ft
lbl1["fg"] = "#333333"
lbl1["justify"] = "center"
lbl1["text"] = "City Name: "
lbl1.place(x=20,y=10,width=113,height=38)

cityName = tk.Entry(root)
cityName["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=23)
cityName["font"] = ft
cityName["fg"] = "#333333"
cityName["justify"] = "center"
cityName["text"] = ""
cityName.place(x=140,y=10,width=214,height=37)

displayText = tk.Text(root)
displayText["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
displayText["font"] = ft
displayText["fg"] = "#333333"
displayText.place(x=20,y=110,width=335,height=170) 

root.mainloop()