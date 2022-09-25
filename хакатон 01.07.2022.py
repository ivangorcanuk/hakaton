# Написать систему для обучения.
# Есть студенты и преподаватели.
# Преподаватели могут добавлять задания.
# Студенты могут получать задания, и отправлять решения
# Преподаватели могут проверять решенные студентами задания и выставлять отметки.
# Студенты могут узнавать свои (и только свои) отметки за конкретное задание, а так же свой средний балл.
# Задания и оценки студентов за задания должны быть сохранены в файлы/базу данных.

# Выход из программы.
# Преподавателей и студентов добавить в файл, а так же можно регистрировать новых.
# Если не найден преподаватель, выводить, что его нет.
# Сделать менюшку приветствия, а так же красиво оформить все командные строки.
# Очистить консоль, чтобы каждая новая строка была единственной.
# Вводить отдельно фамилию и пароль.
# Оставить больше комментариев.
# Добавить функции, на считывание с файла и запись, должно получится около 6 функций.

# Сократить функции, чтобы в if повторялось минимальное кол-во строк.
# Добавит словарь, где фамилия - ключ, пароль - значение. Чтобы словарь выводился из функции в четком виде.
# Среднее арифметическое высчитывать отдельно у студентов.
# Задания должны быть для конкретных учеников.

def registration(name,password,isTeacher):
    fileName = 'prepodHackathon.txt'
    if not isTeacher:
        fileName = 'studentHackathon.txt'

    with open(fileName, 'a', encoding="utf-8") as file:  # записываем нового преподавателя и его пароль
            file.write(name + '\n')
            file.write(password + '\n')
            file.close()

def surnameUser(isTeacher):
    fileName = 'prepodHackathon.txt'
    if not isTeacher:
        fileName = 'studentHackathon.txt'

    with open(fileName, 'r', encoding="utf-8") as file: #считываем содержимое файла в список
        spis = file.readlines()
        file.close()
    d = listVdict(spisok=spis) #перезаписываем список в словарь
    return d

def readOrAddSolutions(isReading, slovar=None):
    if isReading:
        with open("domachkaHackathon.txt", "r", encoding="utf-8") as domachka:  #считываем содержимое файла с решенными заданиями от студентов в список
            spis = domachka.readlines()
            domachka.close()
        d = listVdict(spisok=spis) #перезаписываем список в словарь
        return d
    else:
        with open("domachkaHackathon.txt", "w", encoding="utf-8") as domachka:  #дозаписываем решенные задания от студентов в файл
            for keys in slovar.keys():
                domachka.write(keys + '\n')
                for values in slovar[keys]:
                    domachka.write(values + '\n')
            domachka.close()

def readOrAddGrades(isWriting, slovar=None):
    if isWriting:
        with open('gradeHackathon.txt', 'w', encoding="utf-8") as grade1:  #открываем файл для дозаписи оценок
            for keys in slovar.keys():
                grade1.write(keys + '\n')
                for values in slovar[keys]:
                    grade1.write(values + ' ')
                grade1.write('\n')
            grade1.close()
    else:
        with open('gradeHackathon.txt', 'r', encoding='utf-8') as grade:  #считываем результаты в список
            spisokGrade = grade.readlines()
            grade.close()
            d = listVdict(spisok=spisokGrade) #переписываем список в словарь
            return d

def readOrAddTask(isReading, slovar=None):
    if isReading:
        with open("tasksHackathon.txt", "w", encoding="utf-8") as task:  #открываем файл для дозаписи нового задания для студентов
            for keys in slovar.keys():
                task.write(keys + '\n')
                for values in slovar[keys]:
                    task.write(values + ' = \n')
            task.close()
    else:
        with open("tasksHackathon.txt", "r", encoding="utf-8") as task: #считываем содержимое файла с заданиями от преподавателей
            spisok = task.readlines()
            task.close()
            d = listVdict(spisok=spisok) #переписываем список в словарь
            return d

def printStudentNames(slovar):
    print('Список студентов выполнивших домашнее задание: ')
    i = 0  # переменная счетчик
    spisok = []  # список фамилий студентов, чтобы потом их проще было найти
    for key in slovar.keys():
        i += 1
        spisok.append(key)
        print(str(i) + ')', key.strip())
    return spisok

def listVdict(spisok):
    slovar = {}
    for i in range(len(spisok)):  # переписываем список в словарь
        f = []
        if spisok[i].strip().isalpha():
            for j in range(i + 1, len(spisok)):
                if spisok[j].strip().isalpha():
                    break
                f.append(spisok[j].strip())
            slovar[spisok[i].strip()] = f
    return slovar


mainMenu = input('Добро пожаловать в систему обучения!')

while True:
    menu = input('Выберете тип: 1) преподаватель\n '
                 '             2) студент\n'
                 '              3) выйти\n'
                 '')

    if menu == '1':
        userPrepod = input('Желаете: 1) зарегестрироваться\n'
                  '         2) войти\n'
                  '')

        if userPrepod == '1':
            newNamePrepod = input('Введите вашу фамилия: ')
            newPasswordPrepod = input('Придумайте пароль: ')
            registration(name=newNamePrepod, password=newPasswordPrepod, isTeacher=True) #вызываем функцию для записи нового пользователя

        elif userPrepod == '2':
            surnamePrepod = input('Введите вашу фамилию: ')
            dictPrepod = surnameUser(isTeacher=True) #вызываем функцию для считывания фамилий и паролей в виде словаря

            if surnamePrepod in dictPrepod.keys(): #проверяем есть ли фамилия преподавателя среди ключей словаря
                passwordPrepod = input('Введите пароль: ')

                if passwordPrepod in dictPrepod[surnamePrepod]: #проверяем совпадает ли пароль со значением ключа(фамилии)
                    while True:
                        action = input('Ваши действия: 1) проверить\n'
                                       '               2) добавить задачу\n'
                                       '               3) выйти\n'
                                       '')

                        if action == '1':
                            dictDomachka = readOrAddSolutions(isReading=True)  #вызываем функцию для считывания решений студентов

                            if len(dictDomachka) >= 1:
                                printStudentNames(slovar=dictDomachka)  #вызываем функцию для просмотра фамилий стунтов
                                student = int(input('Выберите студента: '))

                                if student <= len(dictDomachka) and student >= 1:  # условие, чтобы преподаватель попал в диапозон студентов
                                    nameStudent = list(dictDomachka.keys())[student - 1]  #фамилия выбранного студента
                                    listGrade = []  # список в который будут записываться оценки

                                    dictGrade = readOrAddGrades(isWriting=False)  #считываем с файла выставленные оценки в виде словаря

                                    for values in dictDomachka[nameStudent]:  #перебираем решения студентов
                                        print(values)
                                        grade = input('Поставьте оценку: ')
                                        listGrade.append(grade)

                                    del dictDomachka[nameStudent] #удаляем из словаря проверенного студента
                                    readOrAddSolutions(isReading=False, slovar=dictDomachka) #перезаписываем наш файл со студентами и их решениями

                                    dictGrade[nameStudent] = listGrade
                                    readOrAddGrades(slovar=dictGrade,isWriting=True)  #вызываем функцию для дозаписи оценок в файл

                                else:
                                    print('Данного студента не существует!')

                            else:
                                print('Домашних заданий нет.')

                        elif action == '2':
                            dictStudent = surnameUser(isTeacher=False)  #вызываем функцию для считывания студентов в виде словаря
                            print('Список студентов: ')
                            printStudentNames(slovar=dictStudent) #вызываем функцию для итерации фамилий

                            studentNum = int(input('Выберите студента для которого вы напишите задание: '))

                            if studentNum >= 1 and studentNum <= len(dictStudent):  #попал ли преподаватель в диапозон студентов
                                studentName = list(dictStudent.keys())[studentNum - 1]  #фамилия выбранного студента
                                dictTaskStudent = readOrAddTask(isReading=False)  #вызываем функцию для считывания студентов с их заданиями

                                listTasks = [] #список куда будем записывать задания

                                while True:
                                    task = input('Придумайте условие задания:\n'
                                                 '')
                                    listTasks.append(task)
                                    print('Ваше задание успешно добавлено.')
                                    h = input('1) Добавить ещё\n'
                                              '2) Назад\n'
                                              '')
                                    if h == '2':

                                        if studentName in dictTaskStudent.keys(): #если есть студент в словаре
                                            dictTaskStudent[studentName] += listTasks #добавляем новые задания к старым
                                        else:
                                            dictTaskStudent[studentName] = listTasks #иначе просто добавляем новые задания

                                        readOrAddTask(slovar=dictTaskStudent,isReading=True)  # вызываем функцию для дозаписи списка в файл новых заданий
                                        break

                            else:
                                print('Данного студента не существует!')

                        elif action == '3':
                            break

                else:
                    print('Неверный пароль!')

            else:
                print('Данной фамилии не существет!')

        else:
            print('Неверный ввод!')

    elif menu == '2':
        userStudent = input('Желаете: 1) зарегестрироваться\n'
                           '         2) войти\n'
                           '')
        if userStudent == '1':
            newNameStudent = input('Введите вашу фамилию: ')
            newPasswordStudent = input('Введите пароль: ')
            registration(name=newNameStudent, password=newPasswordStudent, isTeacher=False)  # вызываем функцию для записи нового пользователя

        elif userStudent == '2':
            surnameStudent = input('Введите вашу фамилию: ')
            dictStudent = surnameUser(isTeacher=False) #вызываем функцию для считывания содержимого в виде словаря

            if surnameStudent in dictStudent.keys():  #проверяем есть ли фамилия студента среди ключей словаря
                passwordStudent = input('Введите пароль: ')

                if passwordStudent in dictStudent[surnameStudent]:  #проверяем совпадает ли пароль со значением ключа(фамилии)
                    while True:
                        c = input('Ваши действия: 1) решать\n'
                                  '               2) посмотреть результаты\n'
                                  '               3) выйти\n'
                                  '')

                        if c == '1':
                            dictTask = readOrAddTask(isReading=False)  #вызываем функцию для считывания заданий в словарь

                            if surnameStudent in dictTask.keys():
                                listSolutions = []  #список с именем студента и в будущем его решениями

                                for i in dictTask[surnameStudent]:
                                    solutions = input(i.strip() + ' ')  #ответ, который вводит пользователь
                                    listSolutions.append(i.strip() + ' ' + solutions)  #записываем решение в список

                                del dictTask[surnameStudent] #удаляем задания, которые студент уже решил
                                readOrAddTask(slovar=dictTask, isReading=True) #перезаписываем наш файл

                                dictDomachka = readOrAddSolutions(isReading=True) #считываем содержимое файла с решенными заданиями от студентов в словарь

                                if surnameStudent in dictDomachka:  # если фамилии студента есть в словаре
                                    dictDomachka[surnameStudent] += listSolutions  #если да, мы добавляем решение  старому

                                else:
                                    dictDomachka[surnameStudent] = listSolutions #если нет, мы просто добавляем решение

                                readOrAddSolutions(isReading=False,slovar=dictDomachka)  #вызываем функцию для дозаписи решения студента в файл

                            else:
                                print('Для вас нет заданий.')

                        elif c == '2':
                            dictGrade = readOrAddGrades(isWriting=False) #вызываем функцию для считывания оценок в список

                            if surnameStudent in dictGrade.keys(): #проверяем есть ли фамилия студента в списке с оценками
                                s = ' '.join(dictGrade[surnameStudent]) #преобразовываем список в строковый тип данных
                                t = s.split() #разделяем между собой все элементы и преобразовываем в список
                                result = list(map(int, t)) #все элемены списка преобразовываем в числоваой тип данных
                                average = sum(result) / len(result) #находим среднее арифметическое
                                print(surnameStudent + '\n',s + ':', average)

                            else:
                                print('Ваших результатов нет.')

                        elif c == '3':
                            break

                        else:
                            print('Неверный ввод!')

                else:
                    print('Неверный пароль!')

            else:
                print('Данной фамилии не существет!')

        else:
            print('Неверный ввод!')

    elif menu == '3':
        print('Спасибо, что воспользовались моей системой обучения!')
        break

    else:
        print('Указанного типа:', menu,'- не существует.')