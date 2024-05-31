class EExam:
    
    
    def __init__(self):
        self.questions = []
        self.question={}
        self.finalQuestions = []
        self.score = 0
        pass
    
    def readQuestion(self):
        
        file = open("question.txt", "r")
        self.questions = file.readlines()
        #print(self.questions)
        for i in self.questions:
            questionpart = i.split()
            for j in questionpart:
                ques ={
                    "question":questionpart[0],
                    "option1":questionpart[1],
                    "option2":questionpart[2],
                    "option3":questionpart[3],
                    "option4":questionpart[4],
                    "answer":questionpart[5]
                }
            self.finalQuestions.append(ques)
           
    def startExam(self):
        self.readQuestion()
        
        for i in self.finalQuestions:
            print(i["question"])
            print(i["option1"])
            print(i["option2"])
            print(i["option3"])
            print(i["option4"])
            answer = int(input("Enter the answer: "))
            if answer == i["answer"]:
                print("Correct")
                self.score += 1
            
                
        
        self.showResult()
        
    
    def showResult(self):
        print("Your score is: ", self.score)
        



eexam = EExam()
eexam.startExam()
#eexam.readQuestion()
        
    