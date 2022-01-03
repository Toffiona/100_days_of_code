################VERSION 1#################
# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain

# question_bank = []

# for question in question_data:
#     question_text = question["text"]
#     correct_answer = question["answer"]
#     new_question = Question(question_text, correct_answer)
#     question_bank.append(new_question)


# quiz = QuizBrain(question_bank)
# while quiz.still_have_question():
#     quiz.next_question()



#########VERSION 2 WITH new_data obtained from TRIVIA database##############
from question_model import Question
from new_data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    correct_answer = question["correct_answer"]
    new_question = Question(question_text, correct_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_have_question():
    quiz.next_question()






