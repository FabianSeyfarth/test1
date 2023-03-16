for _ in range(3):
    Passwort = "Katze2"
    PasswortEingabe = input("Passwort eingeben: ")
    if Passwort == PasswortEingabe:
        print("Passwort korrekt!")
        break
    else:
        print("Passwort falsch bitte erneut eingeben!: ")
else:
    print("Passwort zu oft falsch ihr System wird gesperrt!")