import datetime,os

status=True

# title/printout
title="\t\tVaccination Report"

while(status):
   
   # date and time
   current_date=datetime.date.today()
   current_time=datetime.datetime.now().strftime("%H:%M:%S")
   
   # printout
   dash="-------------------------------------------------------------"
   
   # file opening
   file=open(f"{current_date}.txt","a")
   
   # printing out the title only once in the file
   if not os.path.exists(f"{current_date}.txt"):
      file.write(title)

   # printing out the dashes/sepration
   file.write(dash)

   # date and time
   file.write(f"Date : {current_date}")
   file.write(f"Time : {current_time}\n")

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

   # printing out the patient info
   file.write(info)
   
   # for more patients
   more=input("Do you want to add another patient? [y/n] : ").casefold()
   
   if more=="y" or more=="yes":
      status=True
   else:
      status=False