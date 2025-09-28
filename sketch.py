# from play_board import board

# def __main__():
#     pass


# def start():
#     b = board()
#     print(b)

# #start()

# user_input = input()

# def uinput(user_input, ):
#     while user_input is True:
#         i =0
#         update_b=[]
#         b = start(b)
#         past_turns = []
#         for r in b:
#             if isinstance(r,list):
#                 print(r)
#                 for f in r:
#                     if user_input == 'd':
#                         i+=1
#                         print(i)
                        
#                         update_b = [element for i, element in enumerate(b)]
#                         update_b("_"[i])
#                         print(update_b)
class Colors:
    
    def __init__(self):

#Regular colors:
        self.red = '\033[91m'
        self.green = '\033[92m'
        self.blue = '\033[94m'
        self.yellow = '\033[93m'
        self.magenta = '\033[95m'
        self.cyan = '\033[96m'
        self.white = '\033[97m'
        self.reset = '\033[0m'

#Add color to text, auto reset
    def colorize(self, text, color):
        color_code = getattr(self, color.lower(), '')
        return f"{color_code}{text}{self.reset}"


#create an instance:
colors = Colors()

# Usage examples:
print(colors.colorize("Warning: Low disk space" , "cyan"))
print(colors.colorize("Error: Connection failed", "yellow"))
print(colors.colorize("Success: Test passed", "magenta"))
