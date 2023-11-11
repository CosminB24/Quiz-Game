#Mincate - quiz game
import pandas as pd
import random

df = pd.read_csv("questions.csv")
random_line = df.sample()
used_questions = set() #facem o lista in care sa tinem cont de intrebarile puse deja
#selected_columns = ['Intrebari', 'A', 'B', 'C', 'D']
#for column in selected_columns:
    #print((f"{random_line[column].values[0]}"))
#exit()

score = 0 #aceasta variabila este un counter pentru scor
print("Bine ai venit la testul meu de cultură generală! Vom trece prin diferite întrebări și îți vom testa cunosțințele.\n"
      "Să trecem la treabă!")
name = input("Pentru început, te rog să îți introduci numele:\n").capitalize() #.capitalize() capitalize the first letter of your word
while True:
    if name == "":
        print("Trebuie să introduci un nume!")
        name = input()
    else:
        break

#variabila name este pentru setarea numelui de catre jucator
print("Spor la joc, " + str(name) + "!")

#selected_columns = ['Intrebari', 'A', 'B', 'C', 'D']
#for x in selected_columns:
    #print((f"{df.sample()[x].values[0]}"))
for x in range(1,8):
    while True:
        while random_line.index[0] in used_questions:
            random_line = df.sample()

        used_questions.add(random_line.index[0])
        selected_columns = ['Intrebari', 'A', 'B', 'C', 'D']
        for x in selected_columns:
            print(f"{random_line[x].values[0]}")
        correct = random_line['Raspuns corect'].values[0]
        answer = input().upper()
        while True:
            if answer == "A" or answer == "B" or answer == "C" or answer == "D":
                break
            else:
                print("Trebuie să alegi una dintre variantele disponibile.")
                answer = input().upper()

        if answer != correct:
            print(f"Răspunsul tău este greșit. Cel corect era {correct}.")
        else:
            print("Corect! Ai câștigat un punct.")
            score += 1

        print(score)
        break
percent_score = (score/7) * 100
exit(f"Jocul s-a încheiat! Ai obținut {score} puncte ({int(percent_score)}%).")