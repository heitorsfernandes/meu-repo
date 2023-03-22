alunos_reprovados = []
file = open("alunos.txt", mode="r")
for line in file:
    if int(line.split()[1]) < 6:
        alunos_reprovados.append(line.split()[0] + '\n')
reprovados = open("reprovados.txt", mode='w')
reprovados.writelines(alunos_reprovados)


recuStudents = []
with open("file.txt") as gradesFile:
    for line in gradesFile:
        student_grade = line
        student_grade = student_grade.split(" ")
        if int(student_grade[1]) < 6:
            recuStudents.append(student_grade[0] + "\n")


with open("recuStudents.txt", mode="w") as recuStudentsFile:
    print(recuStudents)
    recuStudentsFile.writelines(recuStudents)
