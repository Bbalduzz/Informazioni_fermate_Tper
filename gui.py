from tkinter import *
import json
from urllib.request import urlopen

window = Tk()
window.option_add('*Font', '16')
window.configure(background='#0D1B2A')
window.title("Trova il nome della fermata")
window.geometry('400x110')

nu_fermata = Label(window, text="Numero fermata: ")
nu_fermata.grid(column=0, row=0, sticky=W)
nu_fermata.configure(background='#0D1B2A', foreground='#E0E1DD')

codice_fermata = Entry(window,width=10)
codice_fermata.grid(column=1, row=0, sticky=W)

no_fermata = Label(window, text="Nome fermata: ")
no_fermata.grid(column=0, row=1)
no_fermata.configure(background='#0D1B2A', foreground='#E0E1DD')
no_fermata_value = Label(window, text="")
no_fermata_value.grid(column=1, row=1)
no_fermata_value.configure(background='#0D1B2A', foreground='#E0E1DD')

co_fermata = Label(window, text="Comune fermata: ")
co_fermata.grid(column=0, row=2)
co_fermata.configure(background='#0D1B2A', foreground='#E0E1DD')
co_fermata_value = Label(window, text="")
co_fermata_value.grid(column=1, row=2)
co_fermata_value.configure(background='#0D1B2A', foreground='#E0E1DD')

po_fermata = Label(window, text="Nome fermata: ")
po_fermata.grid(column=0, row=3)
po_fermata.configure(background='#0D1B2A', foreground='#E0E1DD')
po_fermata_value = Label(window, text="")
po_fermata_value.grid(column=1, row=3)
po_fermata_value.configure(background='#0D1B2A', foreground='#E0E1DD')

url = "https://raw.githubusercontent.com/Bbalduzz/Tper-jsondataset/main/tper-fermate-autobus.json"
# store the response of URL
response = urlopen(url)
data = json.loads(response.read())
def clicked():
    for d in data:
        cod_int_fermata = d["fields"]["codice"]
        cod_fermata = str(cod_int_fermata) #codice fermata
        fermata = d["fields"]["denominazione"] #nome fermata
        # via = d["fields"]["ubicazione"] #via della fermata #--> rompe turro per qualche motivo (?)
        coords= d["fields"]["geopoint"] #coordinate della fermata
        comune = d["fields"]["comune"] #comune della fermata
        fod = d["fields"]["quartiere"] #quatiere, fuori o dentro bologna?

        if codice_fermata.get() == cod_fermata:
            no_fermata_value.configure(text=fermata),
            co_fermata_value.configure(text=comune+", "+fod)
            po_fermata_value.configure(text=coords)
            break

btn = Button(window, text="Controlla", background='#778DA9', command=clicked)
btn.grid(column=2, row=0, padx=10, sticky=N+S+E+W)

window.mainloop()