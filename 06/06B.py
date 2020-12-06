questions_acc = 0
answered_questions = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z'}

def do_check():
    global answered_questions, questions_acc
    print("answered_questions: " + str(answered_questions))
    questions_acc += len(answered_questions)
    answered_questions = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z'}


for line in open('input.txt', 'r').readlines():
    if len(line) == 1:
        do_check()
    else:
        line = line.rsplit()[0]
        for q in answered_questions.copy():
            if q not in line.rsplit()[0]:
                answered_questions.remove(q)
do_check()

print("Answered questions: " + str(questions_acc))
