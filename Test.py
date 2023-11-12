from discord_webhook import DiscordWebhook, DiscordEmbed
import time
import os
import sys

print("""
      
    Discord Chatteer  
      
    [1] - Chat with Sal
    [2] - Exit


    """)

X = int(input("Choose: "))

Z = "Chat"
Z1 = Z.center(250)
open("Logs.txt", "w")

P = False

def check_P():

    if X == 1:
        os.system("cls")
        P = True
        print("Loading...")
        for i in range(10, 110, 10):
            time.sleep(1)
            print(i, "%")
    elif X == 2:
        os.system("cls")
        print("Exiting....")
        time.sleep(2)
        sys.exit()

name = input("\nYour name: ")

print(f"Welcome {name}!")
time.sleep(3)
os.system("cls")

print("""
          
        [1] - Send Message
        [2] - Send Embed
        [3] - Send image
          
        Notice: You can use the number 5 to go back and the number 0 to exit.
          
        """)
def normal_message():
    while True:
        Y = input("You: ")
        if Y == "1":
            print("Going back....")
        elif Y == "0":
            print("Exiting....")
            time.sleep(3)
            sys.exit()
    
        elif Y != "1":

            X = input("Your message: ")
        
            try:
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1172913800006094888/2wYTsKqbvPfiDE4mCIxous-hDZcJzYKhr6JMIitQuPWvZZSpkYN7jufZpiUlu9eN6jKN", content = X)
                webhook.execute()
            except SystemError:
                print("Nuh uh")

            with open("Logs.txt", "a") as file:
                file.write(X)
                file.close()
    

def choice():

    Y = input("You: ")

    if Y == 1:

        normal_message()
    
    elif Y == 2:

        embed_message()

choice()

