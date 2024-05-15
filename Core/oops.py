# OOPS in Python 
'''
class   - class keyword is used to create a class
object  - object represents the base class name from where all classes in Python are derived. This class is also derived from object class. This is optional.
init()  - This method is used to initialize the variables. This is a special method. We do not call this method explicitly.
self    - self is a variable which refers to current class instance/object.
'''

class Student(object):
    def __int__(self) -> None:
        self.name = "Rupesh"
        self.email = "rupesh@gmail.com"
        self.uid = 11201
        self.phone = 9848167864
    
    def get_student(self):
        std = {
            'name' : self.name,
            'email' : self.email,
            'uid' : self.uid,
            'phone' : self.phone
        }
        return std
    
stdobj = Student()
print("the result of get_student() func of Student Class is : ", stdobj.get_student())