#import module
import sys
import random
import time
import os
import winsound
from tkinter import *
from tkinter import ttk
	
#progressbar


from console_progressbar import ProgressBar

pb = ProgressBar(total=100,prefix='Loading', suffix='Sabar... ', decimals=3, length=50, fill='#', zfill='-')
pb.print_progress_bar(2)
time.sleep(1)
pb.print_progress_bar(25)
time.sleep(1)
pb.print_progress_bar(50)
time.sleep(2)
pb.print_progress_bar(95)
time.sleep(3)
pb.print_progress_bar(100)

#ascii banner art

from pyfiglet import Figlet
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('BlackArch'))
custom_fig2 = Figlet(font='mini')
print(custom_fig2.renderText("                  Created by Doni"))

#random

# ans = True
# question = ("arisyamimunisa")
# while ans:
# 	question = input("input password: ")

# 	answer = random.randint(1,2)


# 	if question == "arisyamimunisa":
# 		break
        
# 	elif answer == 1:
# 		print ("salah password gblk")
        

        
# 	elif answer == 2:
# 		print ("salah password bangsat")

# TKINTER

window = Tk()

U = StringVar()
P = StringVar()

def login():
    if U.get() == 'putra' and P.get() == 'arisyamimunisa':
        print ("logged in successfully")
        window.quit()
        window.destroy()
    elif U.get() == 'kejol' and P.get() == 'arisyamimunisa':
        print ("logged in successfully")
        window.quit()
        window.destroy()   
    else:
        print('salah password')

ttk.Label(window, text="username : " ).grid(row= 0, column= 0, padx= 10, pady= 10)
ttk.Label(window, text = "password: " ).grid(row= 1, column= 0, padx= 10, pady= 10)
ttk.Entry(window, textvariable=U ).grid(row= 0, column= 1, padx= 10, pady= 10)
ttk.Entry(window, textvariable=P, show="*").grid(row= 1, column= 1, padx= 10, pady= 10)
ttk.Button(window, text="Login", command=login).grid(row= 2, column= 1, padx= 10, pady= 10)

window.mainloop()




# simple aritmatics

# a =  int (input("input number a: "))
# b =  int (input("input number b: "))

# print ("hasil a kali b =", a *b)

# @name   : Doni - Email BlackArch


# if elif

print (100*"=")
print ("enter name")

name = input ("Nama: ")

if name == "doni":
    print ((name + " ganteng " ) * 100)
else:
    print ((name + " goblok ") * 100 )

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak(name + "Hello Goblok tai anjing ")

age = int(input("Umur: "))

days = age * 365
minutes = age * 525948
seconds = age * 31556926
print(name, "telah hidup selama", days,"hari", minutes, "menit, dan", seconds, "detik!    \nWOW Semoga Anda Cepet MATI!!! ")

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak(name + " i hope you dead as soon as possible")

#for looping

number = int (input("Choose Your Lucky Number (1-10): "))
data = [(name + " nikah sama marissa, SELAMAT!"), (name + " besok mati, SELAMAT!"), (name + " nge gay sama ferry, MANTAP!"),(name + " di coliin MARISSA, SELAMAT!"), (name + " di sepongin via, SELAMAT!"), (name + " ngentot sama kambing, MANTAP!"), (name+ " kontolnya kecil, SELAMAT!"), (name + " kontolnya gede, SELAMAT!"), (name + " kontolnya pecah, SELAMAT!"), (name + " bijinya pecah, SELAMAT!")]

for i in range (1,11):
    print (i)

    if i is number:
        print ("Number Found!" ,i)
        if i == 1:
            print (data[0])
        if i == 2:
            print(data[1])
        if i == 3:
            print(data[2])
        if i == 4:
            print(data[3])
        if i == 5:
            print(data[4])
        if i == 6:
            print(data[5])
        if i == 7:
            print(data[6])
        if i == 8:
            print(data[7])
        if i == 9:
            print(data[8])
        if i == 10:
            print(data[9])
        break

else:
    print ("number not found!")


nama = (name)

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak(nama + " mampos lo")



#windsound

from PIL import Image 

fr = 3000   #frequency

d = 500    #duration
na = input ("lanjut? (yes/no): ")
nama = (name)
if na == "yes":
        winsound.Beep(fr,d)
        if nama == "putra":
           speak = wincl.Dispatch("SAPI.SpVoice")
           speak.Speak(name + " duar memek ") 
           try:
               im = Image.open(r"E:\blacktool\p61424.jpg")  
               im.show() 
           except:
               print("Image not found!")
          
        if nama == "kevin":
           speak = wincl.Dispatch("SAPI.SpVoice")
           speak.Speak(name + " duar memek ") 
           try:
                im = Image.open(r"E:\blacktool\k61423.jpg")  
                im.show()    
           except:
                print("image not found") 
        
        if nama == "doni":
           speak = wincl.Dispatch("SAPI.SpVoice")
           speak.Speak(name + " ganteng ") 
           try:
                im = Image.open(r"E:\blacktool\d61422.jpg")  
                im.show()
           except:
                print("Image not found") 
    
        print ("--lol-- ") 
        shutdown = input("wanna shut down your computer?(yes/no): ")
        if shutdown == "yes":
              
 	          os.system("shutdown /s /t 1")
    
        else:
         print("bye noob") 
         speak = wincl.Dispatch("SAPI.SpVoice")
         speak.Speak(name + " GOODBYE NOOB")  
        sys.exit()

    

if na == "no":
     shutdown = input("wanna shut down your computer?(yes/no): ")
     if shutdown == "yes":
         
 	    os.system("shutdown /s /t 1")
    
else:
 print("bye noob")
sys.exit()
