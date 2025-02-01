import pyttsx3
import random
import time
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#lets make intro side where user keeps the max limit
def main():
    speak("Welcome to number guessing game.")
    time.sleep(1)
    speak ("please enter max limit")
    limit = int(input("enter max limit: "))
    speak(f"okay.I entered that the highest limit is  {limit}")

    speak(f"I'm thinking of a number between 1 and {limit}. can you guess it?")
    
    #generating a random number between 1 and 100
    secret_number = random.randrange(1,limit)
    
    attemts = 0
    while True:
        guess = int(input("Enter the number that you are guessing  "))
        attemts += 1
        if guess < secret_number:
            print("Analyzing...")
            time.sleep(2)
            speak("its Too low! Try again")
        elif guess > secret_number:
            print("Analyzing...")
            time.sleep(2)
            speak("Too high!, try again")
        else:
            print("Analyzing...")
            time.sleep(2)
            speak(f"Congratulations! you guessed the number {secret_number} in {attemts} attempts")
            break
    try:
        speak("do you wanted to play again, type yes or no")
        ask = input()
        if ask == 'yes':
            main()
        
        elif ask == 'no':
            speak("Thankyou for trying the number guessing game")
            sys.exit()
        else:
            speak("since you didn't enter valid thing, i am closing the game")
            
    except Exception as e:
        print(e)
        pass 
if __name__ == "__main__":
    speak(audio="Hello Boss!")
    main()