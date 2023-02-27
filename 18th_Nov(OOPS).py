class Stud :
    pass

rushi = Stud ()
print(type(rushi))
print(rushi)
print(id(Stud))


class Student :
    pass

s1 = Student ()
s1.name = 'Shreya'
s1.roll = 23
s1.subject = 'History'

print('\n'f"Student name is {s1.name} and her roll number is {s1.roll} with subject {s1.subject}")

s2 = Student ()
s2.name = 'Rushi'
s2.roll = 98
s2.subject = 'computer'

print('\n'f"Student name is {s2.name} his roll number is {s2.roll} with subject of {s2.subject}")

s3 = Student ()
s3.name = 'Timmi'
s3.roll = 99
s3.subject = 'IT'

print('\n'f"Student name is {s3.name} his roll number is {s3.roll} with subject of {s3.subject}"'\n\n')
