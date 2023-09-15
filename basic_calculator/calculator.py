class Calculator:
    def __init__(self):
       self.actions =  ['add','sub', 'div','mul']
    
    def _input(num1, num2, action):
        actions = str(Calculator().actions)
        if action in actions:
            if action == "add":
                ans = num1+num2
                return ans
            if action == "mul":
                ans = num1*num2
                return ans
            if action == "div":
                ans = num1/num2
                return ans
            if action == "sub":
                ans = num1 - num2
                return ans
          