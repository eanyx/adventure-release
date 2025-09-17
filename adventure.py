import csv

pos = "chemin"
cle = "0"
briquet = "0"
pomme = "0"
vie = 5
cheminee_allumee = False
diamant = "0"
coquillage="0"

print ("Vous êtes sur un bateau qui vient de couler, vous vous retrouvez sur une plage déserte.")

while True:
    choix = input ("Que voulez-vous faire ? ")

    match choix:

        case "aide":
            print("Choix possible: dormir, boire, manger, creuser, allumer, ouvrir, descendre, monter, aller, regarder, prendre, sauvegarder, restaurer")

        case "inventaire" | "inv":
            print (cle + " clé")
            print (briquet + " briquet")
            print(pomme + " pomme")
            print(str(vie) + " points de vie")
            print(diamant +  " diamant")
            print(coquillage + " coquillage")
        case "creuser":
            if (pos == "plage"):
                print ("Vous creusez dans le sable")
                print ("Vous trouvez une clé")
                cle = "1"
            elif (pos=="foret"):
                print("Vous trouvez un diamant")
                diamant = "1"
            elif (pos=="riviere"):
                print("vous creusez dans la boue")
                print("Vous trouvez un coquillage")
                coquillage="1"
            else:
                print ("Vous ne pouvez creuser ici")



        case "aller":
            direction = input ("Dans quelle direction : N|S|O|E ? ")
            match direction:
                case "N":
                    print ("Vous allez vers une plage")
                    pos = "plage"
                case "S":
                    print ("Vous allez vers une rivière")
                    pos = "riviere"
                case "E":
                    print ("Vous allez vers une maison")
                    pos = "devant_maison"
                case "O":
                    print ("Vous allez dans une fôret")
                    pos = "foret"
                case _:
                    print ("Vous ne pouvez aller par là")

        case "ouvrir":

            match pos:
                case "dedans_maison":
                    print("Vous trouvez un briquet")
                    briquet = "1"

                case "devant_maison":
                    if (cle == "1"):
                        print ("Vous ouvrez la porte de la maison")
                        cle = "0"
                        pos = "dedans_maison"
                    else:
                        print ("Vous n'avez pas de clé")
                case _:
                    print ("Vous ne pouvez rien ouvrir ici")

        case "allumer":
            if (pos == "dedans_maison"):
                if (briquet == "1"):
                    print("Vous allumez la cheminée, il fait froid dehors")
                    cheminee_allumee = True
                else:
                    print ("Vous n'avez rien pour allumer la cheminée")
            else:
                    print ("Vous ne pouvez rien n'allumer ici")

        case "manger":
            if (pomme == "1"):
                print("Vous mangez une pomme")
                pomme = "0"
                vie = vie + 1
            else:
                print("Vous n'avez rien à manger")

        case "prendre":
            if (pos == "foret"):
                print("Vous ceuillez une pomme")
                pomme = "1"

        case "boire":
            if (pos == "riviere"):
                print("Vous vous désaltérez")
                if (vie < 10):
                    vie = vie + 1
            else:
                print("Il n'y a rien à boire ici")
        case "dormir":
            if (pos == "dedans_maison"):
                if (cheminee_allumee ==  True):
                    print ("Vous vous allongez sur le canapé et vous vous endormez")
                else:
                    print("il fait trop froid")
            else:
                print("Vous ne pouvez dormir ici")

        case "sauvegarder":

            with open('sauvegarde.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['pos', pos])
                writer.writerow(['cle', cle])
                writer.writerow(['briquet', briquet])
                writer.writerow(['pomme', pomme])
                writer.writerow(['vie', vie])

            print ("Sauvegarde en cours")

        case "restaurer":
            with open('sauvegarde.csv', 'r') as file:
                tableau=[]
                reader = csv.reader(file)
                for row in reader:
                    tableau.append(row)
                pos = tableau[0][1]
                cle = tableau[1][1]
                briquet = tableau[2][1]
                pomme = tableau[3][1]
                vie = int(tableau[4][1])
        case "regarder":
            if (pos == "foret"):
                print("Voici une très belle forêt. Verdoyante.")