file_open = open("Questions", 'r')
question_file = file_open.readline()

questions = []

for line in file_open:
    question = line.strip("\n").split(",")
    questions.append(question)

file_open.close()
