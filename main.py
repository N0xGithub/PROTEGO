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

longueur_mot_de_passe = int(input("Put the length for the password : "))
mot_de_passe_genere = generer_mot_de_passe(longueur_mot_de_passe)
print("Generated password :", mot_de_passe_genere)
