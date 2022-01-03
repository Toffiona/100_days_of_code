class QuizBrain:
    def __init__(self, q_list):        
    #initialise attribute 'question_number' to be 0 
    #and initiallise attribute 'q_list to an input of question list
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def still_have_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"You have competed the quiz. \nYour total score is {self.score}/{self.question_number}")
            return False
            
    
    def check_answer(self, user_answer, correct_answer):
        # give user feed back
        if user_answer.lower() == correct_answer.lower():
            print("It is correct")
            self.score += 1
        else:
            print("It is incorrect")

        print(f"Your current score is {self.score}/{self.question_number}")
        print(f"The correct answer is {correct_answer}")
        print("\n")
    
          

    def next_question(self):
        #access each question object in the question list above
        #allow user to answer the question and check is answer is correct
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q{self.question_number}: {current_question.text}: ").lower()
        self.check_answer(user_answer, current_question.answer)
    
    
            












# class QuizBrain:
#     def __init__(self, question_list):
#         self.question_number = 0
#         self.question_list = question_list
#         self.score = 0
#         self.total_question_passed = 0

#     def still_have_question(self):
#         if self.question_number < len(self.question_list):
#             return True
#         else:
#             return False


#     def next_question(self, question_list):
#         current_question = question_list[self.question_number]
#         self.question_number += 1
#         user_answer = input(f"Q{self.question_number}: {current_question.text}. (True/False?: )").lower()
#         self.check_answer(user_answer, current_question.answer)

#     def check_answer(self, user_answer, correct_answer):
#         if user_answer.lower() == correct_answer.lower():
#             print("It is correct")
#             self.score +=1
            
#         else:
#             print("It is incorrect")
#         print(f"The correct answer is: {correct_answer}")
#         self.total_question_passed +=1
#         print(f"Your current score is {self.score}/{self.total_question_passed}")
#         print("\n")