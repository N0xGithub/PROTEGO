import random  
import string

print(""" 
                                                                                                
                                ########  ########   #######  ######## ########  ######    #######  
                                ##     ## ##     ## ##     ##    ##    ##       ##    ##  ##     ## 
                                ##     ## ##     ## ##     ##    ##    ##       ##        ##     ## 
                                ########  ########  ##     ##    ##    ######   ##   #### ##     ## 
                                ##        ##   ##   ##     ##    ##    ##       ##    ##  ##     ## 
                                ##        ##    ##  ##     ##    ##    ##       ##    ##  ##     ## 
                                ##        ##     ##  #######     ##    ########  ######    #######  
                                +----------------------------------------------------------------+
                                               [+] A tool to generate your passwords

                                                   """,)


def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def sauvegarder_mot_de_passe(mot_de_passe):
    with open("passwords.txt", "a") as fichier:
        fichier.write(mot_de_passe + "\n")

nombre_mots_de_passe = int(input("How many passwords do you want to generate ? "))
longueur_mot_de_passe = int(input("Put the length for the password : "))

for _ in range(nombre_mots_de_passe):
    mot_de_passe_genere = generer_mot_de_passe(longueur_mot_de_passe)
    print("Generated password :", mot_de_passe_genere)
    sauvegarder_mot_de_passe(mot_de_passe_genere)

print("Passwords have been generated and saved to 'passwords.txt'.")
