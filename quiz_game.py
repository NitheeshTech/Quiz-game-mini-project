print('Welcome to Learn with Quiz Game!')

player = input('Do you want to play? ')

if player.lower() != "yes":
    quit()

print('Okay, let\'s play!')
score = 0

question = input("1. How many days do we have in a week? ")
if question.lower() == "seven":
    print('Correct ✅')
    score += 1
else:
    print('Incorrect ❌')

question = input("2. A doctor gives you 3 pills and tells you to take one every 30 minutes. How long will it take to finish them all? ")
if question.lower() == "one":
    print('Correct ✅')
    score += 1
else:
    print('Incorrect ❌')

question = input("3. What is always in front of you but can’t be seen? ")
if question.lower() == "future":
    print('Correct ✅')
    score += 1
else:
    print('Incorrect ❌')

question = input("4. Which company developed ChatGPT? ")
if question.lower() == "openai":
    print('Correct ✅')
    score += 1
else:
    print('Incorrect ❌')

question = input("5. Which algorithm is used in Google Search ranking? ")
if question.lower() == "pagerank":
    print('Correct ✅')
    score += 1
else:
    print('Incorrect ❌')

question = input("6. What is the important thing to succeed in life? ")
if question.lower() == "discipline":
    print('Correct ✅')
    score += 1
else:
    print('Incorrect ❌')

question = input("7. Which AI concept mimics the way the human brain works? ")
if question.lower() == "neural network":
    print('Correct ✅')
    score += 1
else:
    print('Incorrect ❌')

question = input("8. What does NLP stand for in AI? ")
if question.lower() == "natural language processing":
    print('Correct ✅')
    score += 1
else:
    print('Incorrect ❌')

print("Your final score is: " + str(score) + " out of 8")
