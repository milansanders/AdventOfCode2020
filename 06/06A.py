questions_acc = 0
answered_questions = set()

def do_check():
    global answered_questions, questions_acc
    questions_acc += len(answered_questions)
    answered_questions = set()


for line in open('input.txt', 'r').readlines():
    if len(line) == 1:
        do_check()
    else:
        for q in line.rsplit()[0]:
            answered_questions.add(q)
do_check()

print("Answered questions: " + str(questions_acc))
