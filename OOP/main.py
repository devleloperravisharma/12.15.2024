import pgzrun

WIDTH = 1000
HEIGHT = 1000
TITLE = "ask about OOP"
file = "oop.txt"

#boxes
what1 = Rect(0, 0, 450, 150)
what2 = Rect(0, 0, 450, 150)
what3 = Rect(0, 0, 450, 150)
what4 = Rect(0, 0, 450, 150)
answer_box = Rect(0, 0, 950, 100)

#lists n numbers
whats = [what1, what2, what3, what4]
question_answers = []
answer_count = 0
answer_index = 0
answers = []
questions = []
answer = ""
#positions
what1.move_ip(20, 270)
what2.move_ip(530, 270)
what3.move_ip(20, 450)
what4.move_ip(530, 450)
answer_box.move_ip(20,20)


def draw():
    screen.clear()
    screen.fill("pink")
    screen.draw.filled_rect(answer_box, "white")
    for what in whats:
        screen.draw.filled_rect(what, "white")
    #screen.draw.textbox(answer[1].strip(), answer_box, color = "pink")

    index_number = 0
    for what in whats:
        screen.draw.textbox(question_answers[index_number].split(",")[0].strip(), what, color = "pink")
        index_number += 1
    screen.draw.textbox(answer, answer_box, color = "pink")

    
def update():
    pass

def read():
    global answer_count, question_answers
    oop_file = open(file, "r")
    for row in oop_file:
        question_answers.append(row)
        answer_count += 1
    oop_file.close()
read()
print(question_answers)

'''def next_answer():
    global answer_index
    answer_index += 1
    return answers.pop(0).split(",")'''

def on_mouse_down(pos):
    global answer
    if whats[0].collidepoint(pos):
        answer = question_answers[0].split(",")[1].strip()

pgzrun.go()