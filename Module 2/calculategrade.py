import pdb

def get_scores(category, total_scores):
    score = 0
    i = 1
    while i <= total_scores:
        message = "Please enter %s %s score: " % (category, i)
        score += int(raw_input(message))
        i += 1
    
    pdb.set_trace()
    return score / total_scores # Show this ERROR

def main():
    homework_weight = .40
    lab_weight = .40
    quiz_weight = .20

    pdb.set_trace()
    homework = get_scores('Homework', 4)
    lab = get_scores('Lab', 4)
    quiz = get_scores('Quiz', 3)
    final_score = ((homework * homework_weight) + (lab * lab_weight) + 
                    (quiz * quiz_weight)) 
    print final_score

main()
