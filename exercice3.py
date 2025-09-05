phrase=input("entrer une phase svp:")
print(phrase)
print("le nombres de caractere de cette phrase est:",len(phrase))
print("la phrase en majuscule est:",phrase.upper())
List_mot=phrase.split()
print("le nombre de mots est:",len(List_mot))
print( "la liste des mots est:",List_mot)
dernier_mot=phrase.split()[-1]
print("le dernier mot est:",dernier_mot)
