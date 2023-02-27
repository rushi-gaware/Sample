class Student :
     def __init__ (self,rno,nm,cont):
          self.roll = rno
          self.name = nm
          self.contact = cont

s1 = Student (1,"Rushi",8657730558)
s2 = Student (2,"Shreya",8017993204)
s3 = Student (3,"Mimi",8888888888)
s4 = Student (4,"Akshya",9503908206)


dic = {s1.roll : s1,
       s2.roll : s2,
       s3.roll : s3,
       s4.roll : s4}
       