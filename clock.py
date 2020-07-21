#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter.ttk import *
from time import strftime
from psutil import sensors_battery


# In[36]:


root= Tk()
root.title('Clock_Battery')

def time():
    power= sensors_battery()
    Battery_percent =("Battery=",power.percent,"percentage")
    if power.power_plugged==True:
        Charging =("Charger Connected")
    else:
        Charging=("Charger Disconnected")
    string1=(strftime("%H:%M:%S %p"),Battery_percent,Charging)
    lbl.config(text= string1) 
    lbl.after(1000,time)
lbl= Label(root,font=("Arial Bold",35 ),background='black',foreground='white')
lbl.pack(anchor='center')
time()
mainloop()


# In[ ]:





# In[ ]:




