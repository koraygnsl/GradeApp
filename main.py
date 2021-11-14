def grade_calculation(line):

    line = line[:-1]
    list = line.split(':')

    studentName = list[0]
    grades = list[1].split(',')

    midterm = int(grades[0])
    final = int(grades[1])

    average = ((midterm*0.4)+(final*0.6))

    if average>=90 and average<=100:
        letter = "AA"
    elif average>=85 and average<=89:
        letter = "BA"
    elif average>=80 and average<=84:
        letter = "BB"
    elif average>=75 and average<=79:
        letter = "CB"
    elif average>=70 and average<=74:
        letter = "CC"
    elif average>=65 and average<=69:
        letter = "DC"
    elif average>=60 and average<=64:
        letter = "DD"
    elif average>=50 and average<=59:
        letter = "FD"
    else:
        letter = "FF"

    return studentName + ": " + letter + "\n"


def read_grade():
    with open("exam_notes.txt","r",encoding="utf-8") as file:
        for line in file:
            print(grade_calculation(line))

def enter_grade():
    fName = input('First Name : ')
    sName = input('Last Name : ')
    midterm = input('Midterm : ')
    final = input('Final : ')

    with open("exam_notes.txt","a", encoding="utf-8") as file:
        file.write(fName+' '+ sName+ ':'+midterm+','+final+'\n')        

def save_average():
    with open('exam_notes.txt',"r",encoding="utf-8") as file:
        list = []

        for i in file:
            list.append(grade_calculation(i))

        with open("averages.txt","w",encoding="utf-8") as file2:
            for i in list:
                file2.write(i)

choice = 1
while choice != 4:
	print('\n*******WELCOME TO GRADE SYSTEM*******')
	print('****************************************')
	print('1. ENTER GRADE')
	print('2. READ AVERAGE')
	print('3. SAVE GRADE')
	print('4. EXIT')
	choice = int(input('ENTER YOUR CHOICE: '))
	if choice == 1:
		enter_grade()
	elif choice == 2:
		read_grade()
	elif choice == 3:
		save_average()
	elif choice == 4:
		break
	else:
		print('WRONG INPUT. ENTER THE CHOICE AGAIN')
