from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QButtonGroup, QRadioButton, QGroupBox
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    

app = QApplication([])
main_win = QWidget()
question = QLabel('как правельно смеяться????')
chtoo = QPushButton('ответить')

RadioGroupBox = QGroupBox('варианты ответов')
rbtn_1 = QRadioButton('мухахаха')
rbtn_2 = QRadioButton('хихихи')
rbtn_3 = QRadioButton('хехехе')
rbtn_4 = QRadioButton('хахаха')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

linia = QVBoxLayout()
shtuka1 = QHBoxLayout()
shtuka2 = QHBoxLayout()
shtuka3 = QHBoxLayout()

shtuka1.addWidget(question)
shtuka2.addWidget(RadioGroupBox)
shtuka3.addWidget(chtoo)

RadioGroupBox2 = QGroupBox('ответить')
linia2 = QVBoxLayout()

ruchka = QLabel('ответ:')
ruchka2 = QLabel('НА САМОМ ДЕЛЕ СМЕЯТСЯ НУЖНО В ГС')
linia2.addWidget(ruchka)
linia2.addWidget(ruchka2)

RadioGroupBox2.setLayout(linia2)
shtuka2.addWidget(RadioGroupBox2)

RadioGroupBox2.hide()

linia.addLayout(shtuka1)
linia.addLayout(shtuka2)
linia.addLayout(shtuka3)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

ansvers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:Question):
    shuffle(ansvers)
    question.setText(q.question)
    ansvers[0].setText(q.right_answer)
    ansvers[1].setText(q.wrong1)
    ansvers[2].setText(q.wrong2)
    ansvers[3].setText(q.wrong3)
    ruchka2.setText(q.right_answer)
    show_question()

def show_correct(res):
    ruchka.setText(res)
    show_result()

def check_answer():
    if ansvers[0].isChecked():
        show_correct('правильно')
        main_win.schot += 1
    elif ansvers[1].isChecked() or ansvers[2].isChecked() or ansvers[3].isChecked():
        show_correct('не правильно')
    print('статиситеп')
    print('-всего вопросов:', main_win.total) 
    print('-првельных ответов:', main_win.schot)
    print('-рейтинг:', main_win.schot/main_win.total*100)


def show_result():
    RadioGroupBox.hide()
    RadioGroupBox2.show()
    chtoo.setText('следующий вопрос')

def show_question():
    RadioGroupBox2.hide()
    RadioGroupBox.show()
    chtoo.setText('ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def next_question():
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
    main_win.total += 1 

def click_ok():
    if chtoo.text() == "ответить":
        check_answer()
    else:
        next_question()

main_win.schot = 0
main_win.total = 0

question_list = []
question_list.append(Question('как правельно смеяться????', 'мухахаха', 'хихихи', 'хахаха', 'хехехе'))

question_list.append(Question('пипипяуу', 'ААААААА', 'нет.', 'хахах', 'чё'))

question_list.append(Question('самый крутой чел во вселенной?', 'дори', 'доричка', 'доря', 'дорик'))

question_list.append(Question('самый крутой клан во вселенной?', 'пкф', 'хранители кристального леса', 'pcf', 'наш'))

question_list.append(Question('привяучикиряу', '', '', '', ''))

#если ответить == chtoo.text():
chtoo.clicked.connect(click_ok)
next_question()
main_win.setLayout(linia)
main_win.show()
app.exec_()