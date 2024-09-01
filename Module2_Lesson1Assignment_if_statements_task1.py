#Task 1: Code Correction Below is a piece of Python code with incorrect indentation. Your task is to correct it.

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")


#Task 2: Your Mood Today Ask the user how they feel today. If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!". Ensure your if statement is properly indented. HINT: Use the input() function to ask the user how they feel! If you need a refresher, check this out here: https://www.w3schools.com/python/python_user_input.asp


input_mood = input("How are you doing today?")

if input_mood == "Happy":
    print("That's great to hear!")
elif input_mood == "Sad":
    print("I hope your day gets better!")
else:
    print("I hear you. I hope you have a great day either way!")