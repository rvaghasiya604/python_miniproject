#1
from connect import myconnect
from PermanentEmployee import Per_Emp
from validation import validations

class Employee:
      
      _empname=""
      _emptype=""
      _empemail=""
      _empsalary=""

      def __init__(self):
            self._empname = input("Enter name : ")
            self._empemail=input("Enter email : ")
            objvalidation = validations()
            while(not objvalidation.validateeml(self._empemail)):
                  self._empemail=input("Re-enter email : ")

            self._empmob=input("Enter mobile no : ")
            objvalidation = validations()
            while(not objvalidation.validatemob(self._empmob)):
                  self._empmob=input("Re-enter mobile no : ")


            self._emptype = input("Enter type : ")
            self._empexp = int(input("Enter experience : "))
            self._empsalary = self.getsalary()
            
      def getsalary(self):
            if self._emptype=="P" or self._emptype=="p":
                  Opemp = Per_Emp()
                  return Opemp.calculatesalary(self._empexp)
            else:
                  print("Invalid Employee...  Please enter only 'p' or 'P'")
                  
      #3
      @staticmethod
      def addnote(): 
            note = input("Enter a note : ")
            f = open("note.txt","a+")
            print("Note added...")
            f.write(note)
            f.close

print("1. Add Emp")
print("2. Display Emp")
print("3. Add Notes")
choice = int(input("Enter your Choice : "))
if choice == 1:
      c = Employee()
      obj = myconnect()
      obj.savetodb(c._empname,c._empemail,c._empmob,c._emptype,c._empexp,c._empsalary)
elif choice == 2:
      obj = myconnect()
      obj.display()
elif choice == 3:
      Employee.addnote()
else:
      print("invalid choice...")
      
