# Type of Variable
'''
1. Instance Variable
2. Class Variable / Static Variable
'''

# Instance Variable
'''
Instance variables are the variables whose separate copy is created in every object.
Instance variables are defined and initialized using a constructor with self parameter.
'''
class Mobile:
    def init (self):
        self.model = 'RealMe X'     # <--- this is instance variable
    def show_model(self):
        print(self.model)
        
realme = Mobile()

# Accessing Instance Variable
'''
1. With Instance Method
    1.1] To access instance variable, we need instance methods with self as first parameter then
    1.2] We can access instance variable using self.variable_name
'''