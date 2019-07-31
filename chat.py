import paho.mqtt.client as mqtt
import time
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as scrolltxt



root = tk.Tk()
root.title("PyChat")
root.geometry("500x540")
root.resizable(0, 0)

#score = Label(height=2, width=10, text="Recieved")
#score.pack(side="top")
frame = tk.Frame(
    master = root,
    bg = 'gray'
)

frame.pack(fill='both', expand='yes')


recievelab = Label(master=frame, text="RECIEVED",fg ='white',bg='gray',bd='0')
recievelab.pack(side="top")

recieve = scrolltxt.ScrolledText(
    master=frame,
    wrap = tk.WORD,
    width = 20,
    height = 25,
    bg = 'black',
    fg ='white'
)

recieve.pack(padx=10,pady=10,fill=tk.BOTH, expand=True)

#score = Label(height=2, width=10, text="Recieved")
#score.pack(side="top")

send = Entry(master=frame,width=50,bg = 'black',fg ='white')
sendlab = Label(master=frame, text="SEND",fg ='white',bg='gray',bd='0')
butt=Button(master=frame,text='SEND',height=0)

sendlab.pack(side="top")
butt.pack(side=RIGHT)
send.pack(padx=10,pady=10,side=LEFT)


#root.update()

#-------------------adding the broker------------------------------------ 
"""def on_connect(client, userdata, flags, rc):
    if rc == 0:
        send.insert(tk.END,"Connected to broker")
        #print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        send.insert(tk.END,"Connection failed")
        #print("Connection failed")


Connected = False  # global variable for the state of the connection

client = mqtt.Client()
client.on_connect = on_connect
client.connect("104.248.163.70", 1883, 60)
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)


try:
    topic = input("Enter chatroom : ")
    while True:
        message = input('Your message: ')
        if message == "#quit":
            topic = input("Enter a new chatroom: ")
        else:
            client.publish("glblcd/sam" , "Ralph(KTU):" + message)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()


 #----------------------END OF SEND-------------------------------   

"""





root.mainloop()