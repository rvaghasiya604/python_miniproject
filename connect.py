import sqlite3
class myconnect:
      
      def __init__(self):
            #4
            self.conn=sqlite3.connect("emp.db")
            
            #5
            try:
                  self.conn.execute('''create table if not exists emp (name text,email text,emp_type char,mobile text,experience integer,salary integer)''')
            except:
                  pass
      
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6
            
            self.conn.execute("insert into emp values (?,?,?,?,?,?)",(ename,eemail,etype,emob,eexp,esalary))
            self.conn.commit()
            print("Record Added Successfully")
             
      def display(self):
            #7
            email=input("enter the email : ")
            data=self.conn.execute("select * from emp where email=:eml",{"eml":email})
            for row in data:
                  print("Name:",row[0])
                  print("Email:",row[1])
                  print("Emp_Type:",row[2])
                  print("Mobile no:",row[3])
                  print("Experience:",row[4])
                  print("Salary:",row[5])
