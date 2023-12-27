import datetime,os

status=True

# printouts
title="Vaccination Report".center(50)
dash="-------------------------------------------------------------"
print(title)

while(status):
   
   # date and time
   current_date=datetime.date.today()
   current_time=datetime.datetime.now().strftime("%H:%M:%S")
   
   print(dash)
   # patient info
   name=input("Enter Name : ")
   age=input("Entere Age : ")
   contact=input("Enter Contact no : ")
   vaccine_name=input("Enter Vaccine name : ")
   vaccine_dose=input("Enter Vaccine dose : ")

   # patient info printout
   info=f"""\nName : {name}
Age : {age}
Contact no : {contact}
Vaccine Name : {vaccine_name}
Vaccine Dose : {vaccine_dose}\n"""
   
   # opening the file
   file=open(f"{current_date}.txt","a")
   file_read=open(f"{current_date}.txt","r")
   
   # printing out the title only once
   if len(file_read.readlines())==0:
      file.write(title+"\n")

   # printing out the patient info with date and time
   file.write(f"{dash}\nDate : {current_date}\nTime : {current_time}\n{info}")
   
   # for more patients
   more=input("\nDo you want to add another patient? [y/n] : ").casefold()
   
   if more=="y" or more=="yes":
      status=True
   else:
      # closing the file
      file.close()
      status=False