import html  

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
# extracting questions and answers
question = trivia["question"]
answer01 = html.unescape(trivia["incorrect_answers"][0])
answer02 = html.unescape(trivia["incorrect_answers"][1])
answer03 = html.unescape(trivia["incorrect_answers"][2])
correctanswer = html.unescape(trivia["correct_answer"])

# prints question and answers
print(question + '\nA.'+answer01+ ' \nB' +answer02+ '\nC.' +answer03+' \nD.' +correctanswer)

# asking user for input
user_input = input('Please select one of the answers')

# checking user input
if user_input.upper() == "D":
    print("That is correct!")
else:
    print("That is incorrect!")
