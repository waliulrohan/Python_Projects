import random
import time
'''
0 for rock
1 for paper
2 for scissors
'''
my_list = ['rock' , 'paper' , 'scissors']

while True:
    print(' \n 0 for rock, 1 for paper, 2 for scissors')
    user_input = input("\n \n Choose (or type 'exit' to stop) :")

    if user_input == "exit":
      print("Thanks for playing.Goodbye.")
      break

    if user_input in ["1" ,"2","0"]:
        user = int(user_input)
        print(f"you choose: {my_list[user]}")
        comp = random.choice([0 ,1 ,2])
        print(f'Computer choose: {my_list[comp]}')

        
        if user == comp:
            print("It's a DRAW")
        elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
            print("YOU WON")
        else:
            print("YOU LOST")
        time.sleep(2)    
    else:
        print("Invalid input. Please enter 0 for rock, 1 for paper, or 2 for scissors.")