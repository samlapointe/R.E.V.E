#Credits
print "Histoire créée par Olivier Brassard & Camille Brassard"
print "Developpé par Olivier Brassard"
import sys
def clear():
   sys.stdout.write('\033[2J')
   sys.stdout.write('\033[H')
   sys.stdout.flush()

raw_input("Appuyez sur [ENTRER] pour executer le script du jeu")
clear()

#warning
print "*** POUR LE BON FONCTIONNEMENT DU JEU, VERIFIEZ QUE "
print " VOTRE TOUCHE VER.MAJ EST DESACTIVE  ***"
print "-----------------------------------"
import sys
def clear():
   sys.stdout.write('\033[2J')
   sys.stdout.write('\033[H')
   sys.stdout.flush()

raw_input("Appuyez sur [ENTRER] pour demmarer")
clear()

#INTRODUCTION
import time
print time.strftime('%d/%m/%y %H:%M',time.localtime())
print
nom=raw_input("Quel est votre nom : ")
print
print "BIENVENUE " + nom.upper()
introqst=raw_input("POUR SAUTER L'INTRODUCTION APPUYEZ SUR [a] SINON SUR [ENTER] ")
if introqst=="a":
    True
else:
   clear()

   print "------------------"
   print "Je suis le Dr. Robet Wonderstone;"
   print "Specialiste des phenomenes psychiques du suconscient."
   print
   print "Ma specialite ? Les reves."
   print "Les reves sonts intimement lies a la vie du reveur"
   print
   print "Pourtant, dans la majorite du temps, vous ne vous rappellez pas de vos reves."
   print "Ils ne sont qu'un produit de notre imagination ..."
   rev=raw_input("N'est-ce pas ? (oui/non): ")
   clear()
   print "------------------- "
   print "Peu importe..."
   print "J'ai decouvert que les reves, meme s'ils parraissent anodins,"
   print "sont bien plus que des films qui jouent dans nos tetes."
   print "..."
   print "ILS SONT REELS !"
   print
   print "Desole, je m'emporte.."
   print
   print "En fait, j'ai developpe un systeme qui permet de revivre ses reves."
   print "L'etude du cerveau a montre que beaucoup de personnes se souviennent"
   print "de leurs reves si on les reveillent pendant le sommeil paradoxal. "
   print "C'est a ce moment qu'il devient possible de les extraires"
   print
   print "Cependant il y a une faille."
   print
   print "Le dernier sujet a eu une crise d'epillepsie au moment critique de l'extraction..."
   print "J'ai voulu annuler le processus, mais il etait trop tard.."
   print "Mort Cerebrale"
   raw_input("Appuyez sur [ENTRER]")
   clear()
   print "Toutefois j'ai remarque un phenomene etrange."
   print "Malgre le coma de type 5 de mon patient, le reve ne s'est pas arrete."
   print "C'est comme si son esprit s'etait detache. "
   print "Comme s'il etait toujours vivant, mais dans son reve "
   print
   print "Apres etude, j'en suis venu a une theorie. Si on arrive a "
   print "retourner dans le reve et a retrouver son esprit"
   print "... ou quelque chose du genre,"
   print "il sera probablement possible de le faire revenir.."
   print


#start
print "J'ai alors modifie la machine pour pouvoir introduire"
print "un second sujet dans le reve en cours."
jouer=raw_input("et pour cela j'ai besoin de votre aide. [o/n]: ")
if jouer=="o":
   print
   print "Tres biens " + nom + " !"
   print "Nous n'avons pas de temps a perdre."
   print "Debutont..."
   True
elif jouer=="n":
   print "Etes-vous certain ? :"
   quit=raw_input("[o/n] : ")
   if quit=="o":
       print "Au revoirs, alors"
       import sys
       sys.exit("[FIN DE LA PARTIE]")
   elif quit=="n":
       print
       print "Nous n'avons pas de temps a perdre."
       print "Debutont..."
print "==============="

#Debut
raw_input("Appuyez sur [ENTRER]")
clear()
print ".............................."
print "[Une heure plus tard]"
print ".............................."
print "Allonge toi ici " + nom
print "Je t'injecte un somnifere.."
print "Il fera effet dans quelques minutes"

print "Tout a l'heure il sera possbile de comuniquer enssemble,"
print "je te guiderai tous le long du periple."
print
print "Ton subconcient sera en lien avec le systeme et avec le reve de mon ex-patient"
print "Je te donnerai plus de detail lorsque tu aura atteint le sommeil paradoxal"
print
print "Ah et j'oubliais !"
print "Dans un reve normal, si tu meurt tu te reveille, mais dans "
print "celui d'un autre ce n'est p...."
print
print "(VOUS VOUS ETES ENDORMI)"
print
raw_input("Appuyez sur [ENTRER]")
clear()
print
print '\033[0;32m [CONSOLE R.E.V.E -  BETA 2.1.4 :]\033[1;m'
print '\033[0;32m [EN ATTENTE DU SOMMEIL PARADOXAL...]\033[1;m'
print '\033[0;32m [...]\033[1;m'
print '\033[0;32m [TEMPS ECOULE : 270 MIN]\033[1;m'
print '\033[0;32m [DEMARAGE DE LA SEQUENCE R.E.V.E]\033[1;m'
print '\033[0;32m        ....\033[1;m'
print '\033[0;32m       ......\033[1;m'
print '\033[0;32m     ..........\033[1;m'
print '\033[0;32m   ..............\033[1;m'
print '\033[0;32m  ................\033[1;m'
print '\033[0;32m ...................\033[1;m'
print '\033[0;32m [Connexion etablie]\033[1;m'
print
raw_input("Appuyez sur [ENTRER]")
clear()
print
print "(VOUS ETES DANS UNE PIECES BLANCHE, VOUS NE POUVEZ RIEN DISTINGUER"
print "MEME PAS LES MUR OU LE PLANCHE. RIENQUE CETTE LUMIERE ENVOUTANTE)"
print
print "RE-Bonjour " + nom
print "Tu est desormais dans le R.E.V.E"
print "Tu n'a malheureusement pas la capacite physique de te deplacer."
print "Dans le reve, tu pourra toutefois choisir quoi faire."
print
raw_input("appuyez sur [ENTRER]")
clear()
print
print "J'entrerai les donnes dans la console pour que tu puisse interagir."
print "Je dois par contre t'avertir qu'il faudra etre tres vigillant lors"
print "de la saisie d'information..."
print
print "Mon systeme n'etant pas tres stable, une erreur pourrais etre fatale"
print "Ainsi quand tu a le choix entre deux option, tu dois absolument choisir"
print "l'une ou l'autre et ce de facon exacte"
print
print "Testons tout de suite !"
a=raw_input("Fais un [a] puis apuis sur [entrer]: ")
print
if a=="a":
    print "Ca fonctionne"
else:
    print "Tu a fais une erreur, il faudra faire attention"
    print "une fois dans le reve sa pourrait te tuer !"
print
print "Je crois que tu est pres on entre dans le reve ?"
play=raw_input("Oui: apuyez sur [a] - Non: apuyez sur [b] : ")
if play=="a":
    clear()
    print "C'est parti !"
else:
    clear()
    print "On a plus le temps de parler, de toutes facon tu ne peux plus reculer"
    print "C'est parti !"

# Debut de l'histoire
# Labo
raw_input("appuyez sur [ENTRER]")
clear()
print "Vous etes dans une piece sombre."
print "Vous ne voyez rien."
print "Vos yeux s'accomodent tranquillement a la noirceur"
print "Vous distinguez maintenant une grande porte et, au plafond, une bouche d'aeration."
print "Pour sortir de cette piece, voulez vous vous :"
c1=raw_input("deplacer vers la porte [a] ou tenter de vous hisser vers les conduits [b]?: ")
if c1=="a":
    print "Vous etes face a la porte"
    print "Vous remarquez qu'elle est verouille"
    print "Il est possible d'ouvrir la porte a l'aide d'un mot de passe"
    c1a=raw_input("essayer un mot de passse [a] ou rebrousser chemin [b]")
    if c1a=="a":
        print
        raw_input("Entrez le mot de passe (puis faites entrer) : ")
        print "[MOT DE PASSE INCORECT]"
    else: True
    print "Vous rebroussez chemin"
else:
    print "Vous prenez vorte elan et vous vous agrippez a la tuyauterie du plafond"
    print "Vous poussez la grille et penetrez dans le conduit."
print "Vous rempez tranquillement ..."
print "Vous arrivez finalement a une INTERSECTION !!!"
print "Dans quelle direction voulez-vous aller ?"
c2=raw_input("Droite [a] ou Gauche [b]")
if c2=="a":
    print "Vous marchez vers le bout du conduit."
    print "Vous appercevez maintenant une piece ou vous pourriez descedre "
    c2a=raw_input("Descendre [a], rebrousser chemin [b]")
    if c2a=="a":
        print "Vous atterissez dans la piece remplie d'etrange etagere"
        print "Elles sont remplies de nombreuses eprouvettes, bechers et bocaux"
        print "Vous appercevez qu'il y a, dans quelques bocaux, des cerveaux flottants"
        print "En panique, vous vous dirigez vers l'autre extremite de la piece"
        print "Vous tombez alors sur un sarrau et des lunettes "
        print "[Vous prenez  (et mettez) ces objets]"
        print "Vous sortez par la porte"
        raw_input("Appuyez sur [entrer]")
        print "Vous arrivez alors au couloir"
        print "Celui-ci contient deux portes."
        print "la '501A' et la '502A'"
        print "Laquelle Choisir ??"
        port=raw_input("501A [a], 502A [b]")
        if port=="a":
            print "La salle est tres grande."
            print "Vous entrez en toute discretion grace a votre fabuleux deguisement"
            print "Vous explorez tranquillement sous  le regard interoge des scientifiques."
            print "Toutefois, ceux ci ne semble pas trop comprendre la situation"
            print "Ils n'ont  pas l'aire  d'etre tres sains d'esprit."
            print "Vous remarquez qu'il n'y a rien de vraiment interessant alors vous sortez..."
            print
            print "Vous vous presentez alors devant l'autre salle."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ELECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'equipement informatique"
            print "Plus precisement, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNETIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit tres etrange, vous vous dirigez"
            print "d'un pas presse vers la porte du fond."
        else:
            print "Vous vous presentez alors devant la porte 502A."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ELECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'equipement informatique"
            print "Plus precisement, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNETIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit, vous vous dirigez"
            print "d'un pas presse vers la porte du fond."

        print "Vous atteignez un nouveau corridor, etrangement, c'est un"
        print "cul de sac... une seule porte coulissante..."
        print "Vous vous approchez de cette porte et tentez de l'ouvrir"
        print "Vous approchez la carte du lecteur..."
        print
        print "[ERREUR 351 - LECTURE IMPOSSIBLE]"
        print
        card=raw_input("Essayer une autre fois [a], retourner dans la salle des serveurs [b]")
        if card=="a":
            print "Vous re-tentez..."
            print "La porte s'ouvre en un bruit sourd."
            print
            print "[ACCES AUTHORIZE]"
            print
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahi l'espace...]"
        else:
            print "De retour dans la salle des serveurs..."
            print "Vous remarquez une console que vous n'aviez pas vue anterieurement"
            print "Vous tentez d'y acceder"
            raw_input("Entrez votre mot de passe: ")
            print "[ACCES REFUSE]"
            print
            print "Une alarme retentis soudainement:"
            print "[ALERTE 5 - INTRUSION AU systeme]"
            print
            print "Vous re-sortez, en courant, dans le corridor"
            print "Vous re-tentez d'ouvrir la porte"
            print "Elle s'ouvre en un bruit sourd."
            print
            print "[ACCES AUTHORIZE]"
            print
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahi l'espace...]"

    else:
        print "Vous rebroussez chemin"
        print "Apres un peu de marche, vous sautez dans la seconde piece"
        print "Elle contient toute sortes de placards vitres"
        print "Vous choisissez une des portes de cette piece ronde et peu eclairee"
        print "Vous examinez son contenu."
        print
        print "Vous remaqrquez qu'il s'agit d'une vaste collection"
        print "d'arme experimentale."
        print "[Vous prenez une arme, (au cas ou)]"
        print "Vous sortez par la porte principale"
        raw_input("Apuyez sur [entrer]")
        print "Vous arrivez alors a un couloir"
        print "Celui-ci contient deux portes."
        print "la '501A' et la '502A'"
        print "Laquelle Choisir ??"
        port1=raw_input("501A [a], 502A [b]")
        if port1=="a":
            print "La salle est tres grande."
            print "Vous entrez en vitesse"
            print "Les scientifiques affoles se dirigent vers vous."
            print "Ils n'ont  pas l'aire  d'etre tres sains d'esprit."
            print "Vous prenez votre fusil au plasma et vous les desintegrez"
            print "Vous ne voulez pas etre detecte alors vous sortez..."
            print
            print "Vous vous presentez devant la salle 502A."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ELECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'equipement informatique"
            print "Plus precisement, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNETIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit tres etrange, vous vous dirigez"
            print "d'un pas presse vers la porte du fond."

        else:
            print "Vous vous presentez devant la salle 502A."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ELECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'equipement informatique"
            print "Plus precisement, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNETIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit tres etrange, vous vous dirigez"
            print "d'un pas presse vers la porte du fond."
            print
        print "Vous atteignez un nouveau corridor, etrangement, c'est un"
        print "cul de sac... une seule porte coulissante..."
        print "Vous vous approchez de cette porte et tentez de l'ouvrir"
        print "Vous approchez la carte du lecteur..."
        print
        print "[ERREUR 351 - LECTURE IMPOSSIBLE]"
        print
        card2=raw_input("Essayer une autre fois [a], retourner dans la salle des serveurs [b]")
        if card2=="a":
            print "Vous re-tentez..."
            print "La porte s'ouvre en un bruit sourd."
            print
            print "[ACCES AUTHORIZE]"
            print
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahi l'espace...]"
        else:
            print "De retour dans la salle des serveurs..."
            print "Vous remarquez une console que vous n'aviez pas vue anterieurement"
            print "Vous tentez d'y acceder"
            raw_input("Entrez votre mot de passe: ")
            print "[ACCES REFUSE]"
            print
            print "Une alarme retentis soudainement:"
            print "[ALERTE 5 - INTRUSION AU systeme]"
            print
            print "Vous re-sortez, en courant, dans le corridor"
            print "Vous re-tentez d'ouvrir la porte"
            print "Elle s'ouvre en un bruit sourd."
            print
            print "[ACCES AUTHORIZE]"
            print
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahi l'espace...]"


else:
    print "Vous marchez vers le bout du conduit."
    print "Vous appercevez maintenant une piece ou vous pourriez descendre "
    c2b=raw_input("Descendre [a], rebrousser chemin [b]")
    if c2b=="a":
       print "Vous atterissez dans la piece"
       print "Elle contient toute sortes de placards vitres"
       print "Vous choisissez une des portes de cette piece ronde et peu eclairee"
       print "Vous examinez son contenu."
       print
       print "Vous remaqrquez qu'il s'agit d'une vaste collection"
       print "d'arme experimentale."
       print "[Vous prenez une arme, (au cas ou)]"
       print "Vous sortez par la porte principale"
       raw_input("Apuyez sur [entrer]")
       print "Vous arrivez alors au couloir"
       print "Celui-ci contient deux portes."
       print "la '501A' et la '502A'"
       print "Laquelle Choisir ??"
       port2=raw_input("501A [a], 502A [b]")
       if port2=="a":
           print "La salle est tres grande."
           print "Vous entrez en vitesse"
           print "Les scientifiques affoles se dirigent vers vous."
           print "Ils n'ont  pas l'aire  d'etre tres sains d'esprit."
           print "Vous prenez votre fusil au plasma et vous les desintegrez"
           print "Vous ne voulez pas etre detecte alors vous sortez..."
           print "Vous vous presentez alors devant l'autre salle."
           print "La porte coulissante s'ouvre automatiquement"
           print "[SON ELECTRONIQUE]"
           print "Il s'agit d'une salle pleine d'equipement informatique"
           print "Plus precisement, une salle des serveurs"
           print
           print "[VOUS TROUVEZ UNE CARTE MAGNETIQUE]"
           print
           print "Dans l'espoir de sortir de cet endroit tres etrange, vous vous dirigez"
           print "d'un pas presse vers la porte du fond."
       else:
           print "Vous vous presentez alors devant l'autre salle."
           print "La porte coulissante s'ouvre automatiquement"
           print "[SON ELECTRONIQUE]"
           print "Il s'agit d'une salle pleine d'equipement informatique"
           print "Plus precisement, une salle des serveurs"
           print
           print "[VOUS TROUVEZ UNE CARTE MAGNETIQUE]"
           print
           print "Dans l'espoir de sortir de cet endroit tres etrange, vous vous dirigez"
           print "d'un pas presse vers la porte du fond."

       print "Vous atteignez un nouveau corridor, etrangement, c'est un"
       print "cul de sac... une seule porte coulissante..."
       print "Vous vous approchez de cette porte et tentez de l'ouvrir"
       print "Vous approchez la carte du lecteur..."
       print
       print "[ERREUR 351 - LECTURE IMPOSSIBLE]"
       print
       card3=raw_input("Essayer une autre fois [a], retourner dans la salle des serveurs [b]")
       if card3=="a":
           print "Vous re-tentez..."
           print "La porte s'ouvre en un bruit sourd."
           print "Vous courrez vers l'exterieur"
           print "[La lumiere blanche envahi l'espace...]"
           print
           print "[ACCES AUTHORIZE]"
           print "Vous courrez vers l'exterieur"
           print "[La lumiere blanche envahi l'espace...]"

       else:
           print "De retour dans la salle des serveurs..."
           print "Vous remarquez une console que vous n'aviez pas vue anterieurement"
           print "Vous tentez d'y acceder"
           raw_input("Entrez votre mot de passe: ")
           print "[ACCES REFUSE]"
           print
           print "Une alarme retentis soudainement:"
           print "[ALERTE 5 - INTRUSION AU systeme]"
           print
           print "Vous re-sortez, en courant, dans le corridor"
           print "Vous re-tentez d'ouvrir la porte"
           print "Elle s'ouvre en un bruit sourd."
           print
           print "[ACCES AUTHORIZE]"
           print
           print "Vous courrez vers l'exterieur"
           print "[La lumiere blanche envahi l'espace...]"
    else:
        print "Vous rebroussez chemin"
        print "Apres un peu de marche, vous sautez dans la seconde piece"
        print "Vous atterissez. Elle est remplie d'etrange etagere"
        print "Elles sont remplies de nombreuses eprouvettes, bechers et bocaux"
        print "Vous appercevez qu'il y a, dans quelques bocaux, des cerveaux flottants"
        print "En panique, vous vous dirigez vers l'autre extremite de la piece"
        print "Vous tombez alors sur un sarrau et des lunettes "
        print "[Vous prenez  (et mettez) ces objets]"
        print "Vous sortez par la porte"
        raw_input("Apuyez sur [entrer]")
        print "Vous arrivez alors au couloir"
        print "Celui-ci contient deux portes."
        print "la '501A' et la '502A'"
        print "Laquelle Choisir ??"
        port3=raw_input("501A [a], 502A [b]")
        if port3=="a":
            print "La salle est tres grande."
            print "Vous entrez en toute discretion grace a votre fabuleux deguisement"
            print "Vous explorez tranquillement sous  le regard interoge des scientifiques."
            print "Toutefois, ceux ci ne semble pas trop comprendre la situation"
            print "Ils n'ont  pas l'aire  d'etre tres sains d'esprit."
            print "Vous remarquez qu'il n'y a rien de vraiment interessant alors vous sortez..."
            print "Vous vous presentez alors devant l'autre salle."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ELECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'equipement informatique"
            print "Plus precisement, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNETIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit tres etrange, vous vous dirigez"
            print "d'un pas presse vers la porte du fond."

        else:
            print "Vous vous presentez devant la salle 502A."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ELECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'equipement informatique"
            print "Plus precisement, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNETIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit tres etrange, vous vous dirigez"
            print "d'un pas presse vers la porte du fond."
        print "Vous atteignez un nouveau corridor, etrangement, c'est un"
        print "cul de sac... une seule porte coulissante..."
        print "Vous vous approchez de cette porte et tentez de l'ouvrir"
        print "Vous approchez la carte du lecteur..."
        print
        print "[ERREUR 351 - LECTURE IMPOSSIBLE]"
        print
        card4=raw_input("Essayer une autre fois [a], retourner dans la salle des serveurs [b]")
        if card4=="a":
            print "La porte s'ouvre en un bruit sourd."
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahi l'espace...]"
            print
            print "[ACCES AUTHORIZE]"
            print
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahi l'espace...]"

        else:
            print "De retour dans la salle des serveurs..."
            print "Vous remarquez une console que vous n'aviez pas vue anterieurement"
            print "Vous tentez d'y acceder"
            raw_input("Entrez votre mot de passe: ")
            print "[ACCES REFUSE]"
            print
            print "Une alarme retentis soudainement:"
            print "[ALERTE 5 - INTRUSION AU systeme]"
            print
            print "Vous re-sortez, en courant, dans le corridor"
            print "Vous re-tentez d'ouvrir la porte"
            print "Elle s'ouvre en un bruit sourd."
            print
            print "[ACCES AUTHORIZE]"
            print
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahi l'espace...]"
