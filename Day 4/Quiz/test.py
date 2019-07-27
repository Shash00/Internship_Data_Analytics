from quiz import Quiz

class Question:
    questions = []

    @classmethod
    def load_questions(cls):
        with open("qus.txt") as f:
            data = f.readlines()
            for i in data:
                lines = i.split(',')
                cls.questions.append(Question(*lines))

    @classmethod
    def beginTest(cls):
        num_correct = 0
        num_wrong = 0
        cls.load_questions()
        print(f"Total questions:{len(cls.questions)}")

        for i,question in enumerate(cls.questions):
            print(f"{i+1}, {question}")
            ans = input('Enter your choice:')
            if ans == question.cans.strip():
                num_correct += 1
            else:
                num_wrong += 1

        cls.show_result(num_correct,num_wrong)

    @classmethod
    def show_result(cls, num_correct, num_wrong):

        total_q = len(cls.questions)
        print(f"Total correct ans:{num_correct}")
        print(f"Total wrong ans:{num_wrong}")
        print(f"Total questions:{total_q}")
        percentage = (num_correct/total_q)*100
        print(f"Percentage:{percentage}")
        if percentage >= 60:
            print('Congratulations')
        else:
            print('Better luck next time')

    

