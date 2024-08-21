# a dictionary that store questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the kay value pair 
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1":{
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2":{
        "question": "What is the capital of Germany?",
        "answer": "Berlin"

    },
    "question3":{
        "question": "What is the capital of India?",
        "answer": "New Delhi"

    },
    "question4":{
        "question": "What is the capital of Italy?",

        "answer": "Rome"

    },
    "question5":{
        "question": "What is the capital of Spain?",
        "answer": "Madrid"

    },
    "question6":{
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"

    },
    "question7":{
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"

    },
}

score = 0

for kay, value in quiz.items():
    print(value['question'])
    answer = input("Answer?")

    if answer.lower() == value['answer'].lower():
        print("correct")
        score = score + 1
        print("your score is: " + str(score))
        print("")
        print("")

    else:
        print("Wrong!")
        print("The answer is :" + value['answer'])
        print("your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(score/7 * 100) + "%" ) 
