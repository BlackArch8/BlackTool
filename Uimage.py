import winsound
import sys
import os
from PIL import Image 

fr = 3000   #frequency

d = 5000    #duration
na = input ("lanjut?(yes/no): ")
nama = (name)
if na == "yes":
        winsound.Beep(fr,d)
        if nama == "putra":
           im = Image.open(r"E:kali undercover.png")  
           im.show() 
          
        if nama == "kevin":
           im = Image.open(r"E:Screenshot_2019-12-28_16-51-27.png")  
           im.show()     
        
        if nama == "doni":
           im = Image.open(r"E:kali undercover.png")  
           im.show() 
    
        print (("lol ") * 10)
        shutdown = input("wanna shut down your computer?(yes/no): ")
        if shutdown == "yes":
              
 	          os.system("shutdown /s /t 1")
    
        else:
         print("bye noob")   
        sys.exit()

    

if na == "no":
     shutdown = input("wanna shut down your computer?(yes/no): ")
     if shutdown == "yes":
         
 	    os.system("shutdown /s /t 1")
    
else:
 print("bye noob")
sys.exit()

