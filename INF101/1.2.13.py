print("Donner trois entiers :\n")

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

# a,b,c = input("Entrer a,b,c".split(","))

question1_reponse = input("Jeu du \"Vrai ou Faux ?\" (répondez en tapant V ou F)\nQuestion1: %s < %s < %s ? "%(a, b, c))

question1_correct = a < b < c

if question1_reponse == "V":
    if question1_correct == True:
        print("Question1 Correst!")
    else:
        print("Question1 False")
elif question1_reponse == "F":
    if  question1_correct == False:
        print("Question1 Correst!")
    else:
        print("Question1 False")
else:
    print("Saissez V ou F SVP")

question2_reponse = input("\nY a-t-il un seul nombre impair parmi %s , %s , %s ?\nVotre reponse: " % (a, b, c))

if question2_reponse == "V" or question2_reponse == "F":
    if a%2 == 0 and b%2 == 0 and c%2 == 0:
        if question2_reponse == "V":
            print("Question2 Correct")
        else:
            print("Question2 False")
    else:
        if question2_reponse == "F":
            print("Question2 Correct")
        else:
            print("Question2 False")
else:
    print("Saissez V ou F SVP")

question3_reponse = input("\n%s %s %s distincts deux à deux ?\nVotre reponse: "%(a, b, c))

if question3_reponse == "V" or question3_reponse == "F":
    if a==b or a == c or b == c:
        if question3_reponse == "V":
            print("Question3 Correct")
        else:
            print("Quesstion3 False")
    else:
        if question3_reponse == "F":
            print("Question3 Correct")
        else:
            print("Quesstion3 False")
else:
    print("Saissez V ou F SVP")