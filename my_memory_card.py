# библиотеки
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

class CLASS():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([])
main_win = QWidget()

list1 = []
list1.append(CLASS('Сколько золотых мячей получил Месси?','6','2','4','7'))
list1.append(CLASS('Самое маленькое государство','Ватикан','Сан-Марино','Монако','Науру'))
list1.append(CLASS('Что является национальным животным Шотландии?','единорог','корова','страус','волк'))
list1.append(CLASS('Какая страна производит больше всего кофе в мире?','Бразилия','США','Узбекистан','Россия'))
list1.append(CLASS('За какую страну играл Дэвид Бекхэм?','Ангия','Испания','Италия','Франция'))
list1.append(CLASS('Как назывался батончик “Сникерс” до его смены названия в 1990 году?','Marathon','Race','Smile','Sprint'))

# виджеты
main_win.setWindowTitle('Memory Card')
text = QLabel('Сколько золотых мячей получил Месси?')
button = QPushButton('Ответить')

# группа варианты ответов
RadioGroupBox = QGroupBox('Варианты ответов')

c_1 = QRadioButton('6')
c_2 = QRadioButton('2')
c_3 = QRadioButton('0')
c_4 = QRadioButton('15')

layout_quest1 = QVBoxLayout()
layout_quest2 = QHBoxLayout()
layout_quest3 = QHBoxLayout()

layout_quest2.addWidget(c_1)
layout_quest2.addWidget(c_2)
layout_quest3.addWidget(c_3)
layout_quest3.addWidget(c_4)

layout_quest1.addLayout(layout_quest2)
layout_quest1.addLayout(layout_quest3)

RadioGroupBox.setLayout(layout_quest1)

# группа результаты теста
RadioGroupBox2 = QGroupBox('Результат теста')
t_text1 = QLabel('прав ты или нет?')
t_text2 = QLabel('ответ будет тут!')

l_Line1 = QVBoxLayout()

l_Line1.addWidget(t_text1, alignment=(Qt.AlignLeft | Qt.AlignTop))
l_Line1.addWidget(t_text2, alignment=Qt.AlignCenter)

RadioGroupBox2.setLayout(l_Line1)

# специальная группа
RadioGroup = QButtonGroup()
RadioGroup.addButton(c_1)
RadioGroup.addButton(c_2)
RadioGroup.addButton(c_3)
RadioGroup.addButton(c_4)

# прикрепляем виджеты к линиям
Line_1 = QHBoxLayout()
Line_2 = QHBoxLayout()
Line_3 = QHBoxLayout()
Line_4 = QVBoxLayout()

Line_1.addWidget(text, alignment=Qt.AlignCenter)

Line_2.addWidget(RadioGroupBox)
Line_2.addWidget(RadioGroupBox2)
RadioGroupBox2.hide()

Line_3.addWidget(button)

Line_4.addLayout(Line_1)
Line_4.addLayout(Line_2)
Line_4.addLayout(Line_3)

main_win.setLayout(Line_4)

# функцию show_result()
def show_result():
    RadioGroupBox2.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)    
    c_1.setChecked(False)
    c_2.setChecked(False)
    c_3.setChecked(False)
    c_4.setChecked(False)
    RadioGroup.setExclusive(True)

# функция show_question()
def show_question():
    RadioGroupBox.hide()
    RadioGroupBox2.show()
    button.setText('Следующий вопрос')

# функция ask()
ask1 = [c_1, c_2, c_3, c_4]
def ask(q: CLASS):
    shuffle(ask1)
    text.setText(q.question)
    ask1[0].setText(q.right)
    ask1[1].setText(q.wrong1)
    ask1[2].setText(q.wrong2)
    ask1[3].setText(q.wrong3)
    t_text2.setText(q.right)
    show_result()
def check_answer():
    if ask1[0].isChecked():
        show_correct('Правильно!!!')
        main_win.aaa += 1
    else:
        if ask1[1].isChecked() or ask1[2].isChecked() or ask1[3].isChecked():
            show_correct('Неверно')
    print('Всего вопросов',main_win.bbb)
    print('Всего правильных вопросов',main_win.aaa)
    print('Рейтинг',int((main_win.aaa/main_win.bbb)*100))
def next_question():
    main_win.bbb += 1
    main_win.ii += 1
    if main_win.ii == len(list1) - 1:
        main_win.ii = -1
    q = list1[main_win.ii]
    ask(q)
def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
def show_correct(fff):
    t_text1.setText(fff)
    show_question()
button.clicked.connect(click_ok)
main_win.ii = -1
main_win.aaa = 0
main_win.bbb = 0
next_question()
main_win.resize(300,200)
main_win.show()
app.exec_()