happylist=[]
sadlist=[]

x=0
print("Δώστε 5 ευγενικές προτάσεις. Για να σταματήσετε, γράψε ΣΤΟΠ:  ")
while x!=1:
    phr=input()
    if phr=="ΣΤΟΠ":
        break
    else:
        happylist.append(phr)

print("Τώρα δώστε 5 άσχημες προτάσεις. Για να σταματήσετε, γράψε ΣΤΟΠ:  ")
x=0
while x!=1:
    phr=input()
    if phr=="ΣΤΟΠ":
        break
    else:
        sadlist.append(phr)


print("Δοκίμαστε να πείτε κάτι στον υπολογιστή και δείτε \nεάν θα αναγνωρίσει ένα κομπλιμέντο; Για να σταματήσετε γράψε ΣΤΟΠ")
phrase = input()
while phrase!="ΣΤΟΠ":
    flag1=0
    for index in happylist:
        if happylist.count(phrase)==1:
            flag1=1
    if flag1==1:
        print(" :) Ευχαριστώ!")
    flag2=0
    for index in sadlist:
       if sadlist.count(phrase)==1:
           flag2=1
    if flag2==1:
        print(":(")

    if flag1==flag2==0:
        flag3=0
        typos = input("Δεν γνωρίζω αυτή την πρόταση, γράψε μου αν είναι ΚΑΛΗ ή ΚΑΚΗ: ")
        while flag3==0:
            if typos== "ΚΑΛΗ":
                happylist.append(phrase)
                print(":)")
                print("Δώσε μια άλλη πρόταση: ")
                flag3=1
            elif typos== "ΚΑΚΗ":
                sadlist.append(phrase)
                print(":(")
                print("Δώστε μια άλλη πρόταση: ")
                flag3=1
            else:
                print("Γράψτε 'ΚΑΛΗ' αν η πρόταση ήταν ευγενική, αλλιώς γράψτε 'ΚΑΚΗ'")
                typos=input()

    phrase = input()
