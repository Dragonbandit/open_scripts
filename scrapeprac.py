from tkinter import *
from bs4 import BeautifulSoup
import requests

#scrape
url = input("enter url ")
r = requests.get(url)
result = (r.text)
doc = BeautifulSoup(result, "html.parser")

tag_1 = doc.title
ticket = tag_1.string
#print(doc.prettify())
#print(tag)
tag_2 = doc.###add tag
hostserial = tag_2.string

tag_3 = doc.###add tag
location = tag_3.string

tag_4 = doc.###add tag
asset = tag_4.string

tag_5 = doc.###add tag
console = tag_5.string

tag_6 = doc.###add tag
power = tag_6.string

tag_7 = doc.###add tag
overview = tag_7.string


#gui
master = Tk()
master.geometry('400x350')
Label(master, text=f'Ticket: {ticket}').grid(row=0)
Label(master, text=f'Host Serial: {hostserial}').grid(row=1)
Label(master, text=f'Location: {location}').grid(row=2)
Label(master, text=f'Asset ID: {asset}').grid(row=3)
Label(master, text=f'Console: {console}').grid(row=4)
Label(master, text=f'Power: {power}').grid(row=5)
Label(master, text=f'Overview: {overview}').grid(row=6)

#e1 = Entry(master)
#e2 = Entry(master)
#e3 = Entry(master)
#e4 = Entry(master)
#e5 = Entry(master)
#e6 = Entry(master)

#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)
#e3.grid(row=2, column=1)
#e4.grid(row=3, column=1)
#e5.grid(row=4, column=1)
#e6.grid(row=5, column=1)

mainloop()
