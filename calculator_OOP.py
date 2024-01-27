class Calculator:
    def __init__(self):
        while True:
            self.user_input = input().lower().strip()
            self.calculation()
    
    
    def calculation(self):
        if self.user_input.isalpha():
            self.command()
        else:
            self.result = eval(self.user_input)
            print(self.result)
            
        
    def command(self):
        if self.user_input == "ac":
            self.result = 0
            print(self.result)
        elif self.user_input == "exit":
            exit()
        else:
            print("This is calculator.😊")
            
Calculator()