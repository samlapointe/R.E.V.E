# coding: utf-8

#Credits
print "______________________________________________________"
print
print "\033[1;0mCopyright 2016 - Tous Droits Réservés\033[1;m"
print "Histoire créée par Olivier Brassard & Camille Brassard"
print "Développée par Olivier Brassard"
print 'Corrections effectuées par Samuel Lapointe'
import sys
def clear():
   sys.stdout.write('\033[2J')
   sys.stdout.write('\033[H')
   sys.stdout.flush()

print
raw_input("Appuyez sur [ENTRER] pour exécuter le script du jeu")
clear()

#warning
print "*** POUR LE BON FONCTIONNEMENT DU JEU, VÉRIFIEZ QUE "
print " VOTRE TOUCHE VER.MAJ EST DÉSACTIVÉE  ***"
print "-----------------------------------"

raw_input("Appuyez sur [ENTRER] pour démarrer")
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
   print "Je suis le Dr. Robert Wonderstone;"
   print "Spécialiste des phénomènes psychiques du subconscient."
   print
   print "Ma spécialité ? Les rêves."
   print "Les rêves sont intimement liés à la vie du rêveur"
   print
   print "La plupart du temps, vous ne vous rappellez pas de vos rêves."
   print "Ils ne sont que le fruit de votre imagination ..."
   rev=raw_input("N'est-ce pas ? (oui/non): ")
   clear()
   print "------------------- "
   print "Peu importe..."
   print "J'ai découvert que les rêves, même s'ils paraissent anodins,"
   print "sont bien plus que des films qui jouent dans nos têtes."
   print "..."
   print "ILS SONT RÉELS !"
   print
   print "Désolé, je m'emporte.."
   print
   print "En fait, j'ai développé un système qui permet de revivre ses rêves."
   print "L'étude du cerveau a démontré que beaucoup de personnes se souviennent"
   print "de leurs rêves si on les réveillent pendant le sommeil paradoxal. "
   print "C'est à ce moment qu'il devient possible de les extraire"
   print
   print "Cependant, il y a une faille."
   print
   print "Lors de l'extraction, le dernier sujet a fait une crise d'épillepsie..."
   print "J'ai voulu annuler le processus, mais il était trop tard..."
   print "Mort cérébrale"
   raw_input("Appuyez sur [ENTRER]")
   clear()
   print "Toutefois j'ai remarqué un phénomène étrange."
   print "Malgré le coma de type 5 de mon patient, le rêve ne s'est pas arreté."
   print "C'est comme si son esprit s'était détaché. "
   print "Comme s'il était toujours vivant, mais dans son rêve "
   print
   print "Après étude, j'en suis venu à une théorie. Si on arrive à "
   print "retourner dans le rêve et à retrouver son esprit"
   print "... ou quelque chose du genre,"
   print "il sera probablement possible de le faire revenir.."
   print
   print "J'ai alors modifié la machine pour pouvoir introduire"
   print "une seconde personne dans le rêve en cours."


#start

jouer=raw_input("Pour cela, j'ai besoin de votre aide. [o/n]: ")
if jouer=="o":
   clear()
   print "Très bien " + nom + " !"
   print "Nous n'avons pas de temps à perdre."
   print "Débutons..."
   True
elif jouer=="n":
   clear()
   print "Êtes-vous certain ? :"
   quit=raw_input("[o/n] : ")
   if quit=="o":
       print "Au revoir, alors"
       import sys
       sys.exit("\033[0;31m [PARTIE TERMINÉE]\033[1;m")
   elif quit=="n":
       clear()
       print "Nous n'avons pas de temps à perdre."
       print "Débutons..."


#Debut
raw_input("Appuyez sur [ENTRER]")
clear()
print ".............................."
print "[Une heure plus tard]"
print ".............................."
print "Allonge toi ici " + nom
print "Je t'injecte un somnifère..."
print "Les effets se feront ressentir dans quelques minutes"

print "Tout a l'heure, il sera possible de communiquer ensemble,"
print "je te guiderai tout le long du périple."
print
print "Ton subconcient sera en lien avec le système et avec le rêve de mon ex-patient"
print "Je te donnerai plus de détails lorsque tu auras atteint le sommeil paradoxal"
print "TOUTEFOIS JE DOIS T'AVERTIR ..."
print "Tu ne dois JAMAIS avoir de contact physique avec lui, sinon"
print "cela créera des interférances entre ton subconscient et le sien."
print "Ça pourrait te TUER !!!"
print
print "Ahh, j'oubliais !"
print "Dans un rêve ordinaire où tu meurs, tu te réveille, mais dans "
print "celui d'un autre ce n'est p... Zzzzh!"
print
print "(VOUS VOUS ÊTES ENDORMI)"
print
raw_input("Appuyez sur [ENTRER]")
clear()
print
print '\033[0;32m [CONSOLE R.E.V.E -  BETA 2.1.4 :]\033[1;m'
print '\033[0;32m [EN ATTENTE DU SOMMEIL PARADOXAL...]\033[1;m'
print '\033[0;32m [...]\033[1;m'
print '\033[0;32m [TEMPS ÉCOULÉ : 270 MIN.]\033[1;m'
print '\033[0;32m [DÉMARRAGE DE LA SÉQUENCE R.E.V.E]\033[1;m'
print '\033[0;32m        ....\033[1;m'
print '\033[0;32m       ......\033[1;m'
print '\033[0;32m     ..........\033[1;m'
print '\033[0;32m   ..............\033[1;m'
print '\033[0;32m  ................\033[1;m'
print '\033[0;32m ...................\033[1;m'
print '\033[0;32m [Connexion établie]\033[1;m'
print
raw_input("Appuyez sur [ENTRER]")
clear()
print
print "(VOUS ÊTES DANS UNE PIÈCE BLANCHE, VOUS NE POUVEZ RIEN DISTINGUER"
print "MÊME PAS LES MURS OU LE PLANCHER. RIEN QUE CETTE LUMIÈRE ENVOUTANTE)"
print
print "Re-bonjour " + nom
print "Tu est désormais dans le R.E.V.E"
print "Tu n'a malheureusement pas la capacité physique de te déplacer."
print "Dans le rêve, tu pourra toutefois choisir quoi faire."
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
raw_input("Appuyez sur [ENTRER]")
clear()
print "Vous etes dans une piece sombre."
print "Vous ne voyez rien."
print "Vos yeux s'accomodent tranquillement a la noirceur"
print "Vous distinguez maintenant une grande porte et, au plafond, une bouche d'aeration."
print "Pour sortir de cette piece, voulez vous vous :"
c1=raw_input("deplacer vers la porte [a] ou tenter de vous hisser vers les conduits [b]?: ")
if c1=="a":
    clear()
    print "Vous etes face a la porte"
    print "Vous remarquez qu'elle est verouille"
    print "Il est possible d'ouvrir la porte a l'aide d'un mot de passe"
    c1a=raw_input("essayer un mot de passse [a] ou rebrousser chemin [b]")
    if c1a=="a":
        clear()
        raw_input("Entrez le mot de passe (puis faites entrer) : ")
        clear()
        print '\033[0;31m [ACCES REFUSE]\033[1;m'
        raw_input("Appuyez sur [ENTRER]")
        clear()
    else: True
    print "Vous rebroussez chemin"
    print "Vous prenez vorte elan et vous vous agrippez a la tuyauterie du plafond"
    print "Vous poussez la grille et penetrez dans le conduit."
else:
    clear()
    print "Vous prenez vorte elan et vous vous agrippez a la tuyauterie du plafond"
    print "Vous poussez la grille et penetrez dans le conduit."
print "Vous rempez tranquillement ..."
print "Vous arrivez finalement a une INTERSECTION !!!"
print "Dans quelle direction voulez-vous aller ?"
c2=raw_input("Droite [a] ou Gauche [b]")
if c2=="a":
    clear()
    print "Vous marchez vers le bout du conduit."
    print "Vous appercevez maintenant une piece ou vous pourriez descedre "
    c2a=raw_input("Descendre [a], rebrousser chemin [b]")
    if c2a=="a":
        clear()
        print "Vous atterissez dans la piece remplie d'etrange etagere"
        print "Elles sont remplies de nombreuses eprouvettes, bechers et bocaux"
        print "Vous appercevez qu'il y a, dans quelques bocaux, des cerveaux flottants"
        print "En panique, vous vous dirigez vers l'autre extremite de la piece"
        print "Vous tombez alors sur un sarrau et des lunettes "
        print "[Vous prenez  (et mettez) ces objets]"
        print "Vous sortez par la porte"
        raw_input("Appuyez sur [entrer]")
        clear()
        print "Vous arrivez alors au couloir"
        print "Celui-ci contient deux portes."
        print "la '501A' et la '502A'"
        print "Laquelle Choisir ??"
        port=raw_input("501A [a], 502A [b]")
        if port=="a":
            clear()
            print "La salle est tres grande."
            print "Vous entrez en toute discretion grace a votre fabuleux deguisement"
            print "Vous explorez tranquillement sous  le regard interoge des scientifiques."
            print "Toutefois, ceux ci ne semble pas trop comprendre la situation"
            print "Ils n'ont  pas l'aire  d'etre tres sains d'esprit."
            print "Vous remarquez qu'il n'y a rien de vraiment interessant alors vous sortez..."
            raw_input("Appuyez sur [ENTRER]")
            clear()
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
            raw_input("Appuyez sur [ENTRER]")
            clear()
        else:
            clear()
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
            raw_input("Appuyez sur [ENTRER]")
            clear()

        print "Vous atteignez un nouveau corridor, etrangement, c'est un"
        print "cul de sac... une seule porte coulissante..."
        print "Vous vous approchez de cette porte et tentez de l'ouvrir"
        print "Vous approchez la carte du lecteur..."
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print
        print '\033[0;31m [ERREUR - LECTURE IMPOSSIBLE]\033[1;m'
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print
        card=raw_input("Essayer une autre fois [a], retourner dans la salle des serveurs [b]")
        if card=="a":
            print "Vous re-tentez..."
            print "La porte s'ouvre en un bruit sourd."
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahie l'espace...]"
            raw_input("Appuyez sur [ENTRER]")
            clear()
        else:
            clear()
            print "De retour dans la salle des serveurs..."
            print "Vous remarquez une console que vous n'aviez pas vue anterieurement"
            print "Vous tentez d'y acceder"
            raw_input("Entrez votre mot de passe: ")
            clear()
            print '\033[0;31m [ACCES REFUSE]\033[1;m'
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Une alarme retentis soudainement:"
            print '\033[0;31m [ALERTE 5 - INTRUSION AU SYSTEME]\033[1;m'
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print
            print "Vous re-sortez, en courant, dans le corridor"
            print "Vous re-tentez d'ouvrir la porte"
            print "Elle s'ouvre en un bruit sourd."
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahie l'espace...]"
            raw_input("Appuyez sur [ENTRER]")
            clear()

    else:
        clear()
        print "Vous rebroussez chemin"
        print "Apres un peu de marche, vous sautez dans la seconde piece"
        print "Elle contient toute sortes de placards vitres"
        print "Vous choisissez une des portes de cette piece ronde et peu eclairee"
        print "Vous examinez son contenu."
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print
        print "Vous remarquez qu'il s'agit d'une vaste collection"
        print "d'arme experimentale."
        print "[Vous prenez une arme, (au cas ou)]"
        print "Vous sortez par la porte principale"
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Vous arrivez alors a un couloir"
        print "Celui-ci contient deux portes."
        print "la '501A' et la '502A'"
        print "Laquelle Choisir ??"
        port1=raw_input("501A [a], 502A [b]")
        if port1=="a":
            clear()
            print "La salle est tres grande."
            print "Vous entrez en vitesse"
            print "Les scientifiques affoles se dirigent vers vous."
            print "Ils n'ont  pas l'aire  d'etre tres sains d'esprit."
            print "Vous prenez votre fusil au plasma et vous les desintegrez"
            print "Vous ne voulez pas etre detecte alors vous sortez..."
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
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
            raw_input("Appuyez sur [ENTRER]")
            clear()

        else:
            clear()
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
            raw_input("Appuyez sur [ENTRER]")
            clear()

        print "Vous atteignez un nouveau corridor, etrangement, c'est un"
        print "cul de sac... une seule porte coulissante..."
        print "Vous vous approchez de cette porte et tentez de l'ouvrir"
        print "Vous approchez la carte du lecteur..."
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print
        print '\033[0;31m [ERREUR - LECTURE IMPOSSIBLE]\033[1;m'
        print
        card2=raw_input("Essayer une autre fois [a], retourner dans la salle des serveurs [b]")
        if card2=="a":
            clear()
            print "Vous re-tentez..."
            print "La porte s'ouvre en un bruit sourd."
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahie l'espace...]"
            raw_input("Appuyez sur [ENTRER]")
            clear()
        else:
            clear()
            print "De retour dans la salle des serveurs..."
            print "Vous remarquez une console que vous n'aviez pas vue anterieurement"
            print "Vous tentez d'y acceder"
            raw_input("Entrez votre mot de passe: ")
            clear()
            print '\033[0;31m [ACCES REFUSE]\033[1;m'
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Une alarme retentis soudainement:"
            print '\033[0;31m [ALERTE 5 - INTRUSION AU SYSTEME]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous re-sortez, en courant, dans le corridor"
            print "Vous re-tentez d'ouvrir la porte"
            print "Elle s'ouvre en un bruit sourd."
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahie l'espace...]"
            raw_input("Appuyez sur [ENTRER]")
            clear()


else:
    clear()
    print "Vous marchez vers le bout du conduit."
    print "Vous appercevez maintenant une piece ou vous pourriez descendre "
    c2b=raw_input("Descendre [a], rebrousser chemin [b]")
    if c2b=="a":
       clear()
       print "Vous atterissez dans la piece"
       print "Elle contient toute sortes de placards vitres"
       print "Vous choisissez une des portes de cette piece ronde et peu eclairee"
       print "Vous examinez son contenu."
       print
       raw_input("Appuyez sur [ENTRER]")
       clear()
       print "Vous remarquez qu'il s'agit d'une vaste collection"
       print "d'arme experimentale."
       print "[Vous prenez une arme, (au cas ou)]"
       print "Vous sortez par la porte principale"
       raw_input("Appuyez sur [ENTRER]")
       clear()
       print "Vous arrivez alors au couloir"
       print "Celui-ci contient deux portes."
       print "la '501A' et la '502A'"
       print "Laquelle Choisir ??"
       port2=raw_input("501A [a], 502A [b]")
       if port2=="a":
           clear()
           print "La salle est tres grande."
           print "Vous entrez en vitesse"
           print "Les scientifiques affoles se dirigent vers vous."
           print "Ils n'ont  pas l'aire  d'etre tres sains d'esprit."
           print "Vous prenez votre fusil au plasma et vous les desintegrez"
           print "Vous ne voulez pas etre detecte alors vous sortez..."
           raw_input("Appuyez sur [ENTRER]")
           clear()
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
           raw_input("Appuyez sur [ENTRER]")
           clear()
       else:
           clear
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
           raw_input("Appuyez sur [ENTRER]")
           clear()

       print "Vous atteignez un nouveau corridor, etrangement, c'est un"
       print "cul de sac... une seule porte coulissante..."
       print "Vous vous approchez de cette porte et tentez de l'ouvrir"
       print "Vous approchez la carte du lecteur..."
       print
       raw_input("Appuyez sur [ENTRER]")
       clear()
       print '\033[0;31m [ERREUR - LECTURE IMPOSSIBLE]\033[1;m'
       print
       card3=raw_input("Essayer une autre fois [a], retourner dans la salle des serveurs [b]")
       if card3=="a":
           clear()
           print "Vous re-tentez..."
           print "La porte s'ouvre en un bruit sourd."
           print "Vous courrez vers l'exterieur"
           print "[La lumiere blanche envahi l'espace...]"
           print
           print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
           print
           raw_input("Appuyez sur [ENTRER]")
           clear()
           print "Vous courrez vers l'exterieur"
           print "[La lumiere blanche envahie l'espace...]"
           raw_input("Appuyez sur [ENTRER]")
           clear()

       else:
           clear()
           print "De retour dans la salle des serveurs..."
           print "Vous remarquez une console que vous n'aviez pas vue anterieurement"
           print "Vous tentez d'y acceder"
           raw_input("Entrez votre mot de passe: ")
           clear()
           print
           print '\033[0;31m [ACCES REFUSE]\033[1;m'
           raw_input("Appuyez sur [ENTRER]")
           clear()
           print
           print "Une alarme retentis soudainement:"
           print '\033[0;31m [ALERTE 5 - INTRUSION AU SYSTEME]\033[1;m'
           print
           raw_input("Appuyez sur [ENTRER]")
           clear()
           print "Vous re-sortez, en courant, dans le corridor"
           print "Vous re-tentez d'ouvrir la porte"
           print "Elle s'ouvre en un bruit sourd."
           print
           print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
           print
           raw_input("Appuyez sur [ENTRER]")
           clear()
           print "Vous courrez vers l'exterieur"
           print "[La lumiere blanche envahie l'espace...]"
           raw_input("Appuyez sur [ENTRER]")
           clear()
    else:
        clear()
        print "Vous rebroussez chemin"
        print "Apres un peu de marche, vous sautez dans la seconde piece"
        print "Vous atterissez. Elle est remplie d'etrange etagere"
        print "Elles sont remplies de nombreuses eprouvettes, bechers et bocaux"
        print "Vous appercevez qu'il y a, dans quelques bocaux, des cerveaux flottants"
        print "En panique, vous vous dirigez vers l'autre extremite de la piece"
        print "Vous tombez alors sur un sarrau et des lunettes "
        print "[Vous prenez  (et mettez) ces objets]"
        print "Vous sortez par la porte"
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Vous arrivez alors au couloir"
        print "Celui-ci contient deux portes."
        print "la '501A' et la '502A'"
        print "Laquelle Choisir ??"
        port3=raw_input("501A [a], 502A [b]")
        if port3=="a":
            clear()
            print "La salle est tres grande."
            print "Vous entrez en toute discretion grace a votre fabuleux deguisement"
            print "Vous explorez tranquillement sous  le regard interoge des scientifiques."
            print "Toutefois, ceux ci ne semble pas trop comprendre la situation"
            print "Ils n'ont  pas l'aire  d'etre tres sains d'esprit."
            print "Vous remarquez qu'il n'y a rien de vraiment interessant alors vous sortez..."
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous vous presentez donc devant l'autre salle."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ELECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'equipement informatique"
            print "Plus precisement, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNETIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit tres etrange, vous vous dirigez"
            print "d'un pas presse vers la porte du fond."
            raw_input("Appuyez sur [ENTRER]")
            clear()

        else:
            clear()
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
            raw_input("Appuyez sur [ENTRER]")
            clear()

        print "Vous atteignez un nouveau corridor, etrangement, c'est un"
        print "cul de sac... une seule porte coulissante..."
        print "Vous vous approchez de cette porte et tentez de l'ouvrir"
        print "Vous approchez la carte du lecteur..."
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print
        print '\033[0;31m [ERREUR - LECTURE IMPOSSIBLE]\033[1;m'
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print
        card4=raw_input("Essayer une autre fois [a], retourner dans la salle des serveurs [b]")
        if card4=="a":
            clear()
            print "La porte s'ouvre en un bruit sourd."
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahi l'espace...]"
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahie l'espace...]"

        else:
            clear()
            print "De retour dans la salle des serveurs..."
            print "Vous remarquez une console que vous n'aviez pas vue anterieurement"
            print "Vous tentez d'y acceder"
            raw_input("Entrez votre mot de passe: ")
            clear()
            print '\033[0;31m [ACCES REFUSE]\033[1;m'
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print
            print "Une alarme retentis soudainement:"
            print '\033[0;31m [ALERTE 5 - INTRUSION AU SYSTEME]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous re-sortez, en courant, dans le corridor"
            print "Vous re-tentez d'ouvrir la porte"
            print "Elle s'ouvre en un bruit sourd."
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print
            print "Vous courrez vers l'exterieur"
            print "[La lumiere blanche envahie l'espace...]"
            raw_input("Appuyez sur [ENTRER]")
            clear()

print "[Dr. Wonderstone : ]"
print
print nom.upper() + "!"
print
print "Tu te demande peut-etre ce qu'il se passe..."
print
print "C'est ce qu'on appelle un 'bris de continuite'."
print
print "Tu a probablement deja remarque que lorsqu'on "
print "arrive a se souvenir d'un reve, il en manque souvent des parties."
print "En effet, c'est parceque les reves sont a la base, decousus."
print
print "Il est normal, dans l'univers des reves, de voyager dans le temps ou l'espace"
print "comme cela sans aucune raison valable... c'est ce qu'on appelle le bris de continuite"
print
print "C'est aussi pour cette raison, que lors d'un changement d'univers"
print "tous les objets que tu avais precedement peuvent se reinitialiser."
print "C'est pour cette raison que tu n'est plus habille comme il y a quelques minutes..."
print
print "Je te laisse, bonne chance!"
raw_input("Appuyez sur [ENTRER]")
clear()
print

# 2e monde
print "Vous arrivez alors dans une clairiere ensoleillee."
print "D'un cote: une grande foret de coniferes, de l'autre: une riviere."
print "De quel cote voulez vous aller ?"
print
fb=raw_input("Foret [a] ou riviere [b]: ")
if fb=="a":
    clear()
    print "Vous partez donc d'un pas confiant vers la foret."
    print
    print "Vous marchez..."
    print
    print "Vous marchez..."
    print
    print "Vous marchez..."
    print
    print "Il commence a faire noir et vous n'avez toujours rien decouvert"
    fr=raw_input("Voulez vous continuer [a] ou rebrousser chemin avant la nuit [b]")
    if fr=="a":
        clear()
        print "Vous marchez toujours..."
        print
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Vous marchez..."
        print
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Et il fait toujours plus noir..."
        print
        print "Vous desidez de vous arreter pour dormir"
        print "Soudainement, vous entendez un craquement derriere vous."
        print "SURPISE ! UN OURS NOIR !"
        print
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Vous tentez de grimper a un arbre, mais vous glissez et vous vous"
        print "la cheville."
        print
        print "L'ours affame s'approche de vous avec appetit.."
        print "[SLURP !!] En se laichant les babines..."
        print "..."
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "..."
        print '\033[0;31m [VOUS ETES MORT]\033[1;m'
        print "\033[0;31m [L'OURS À TOUTEFOIS OBTENU UN SOMPTUEUX REPAS.] \033[1;m"
        import sys
        sys.exit("\033[0;31m [PARTIE TERMINE]\033[1;m")
    else:
        print "Vous retournez vers la riviere"
        raw_input("Appuyez sur [ENTRER]")
        True
else:
    True
clear()
print
print "Pres du cours d'eau, vous appercevez une vieille chalouppe."
print "Vous embarquez dans celle-ci."
print "Vous naviguez paisiblement sur l'eau calme de cette paisible riviere"
print
print "Vous relaxez..."
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Cependant, vous avez l'imppression que le courant s'intensifie."
print "Vous vous levez debout..."
print
print "En plissant les yeux, vous avez l'impression que la "
print "rivière se termine au loin. Malheureusement vous n'avez aucune paguaie"
print "et, comme pour confirmer vos pensees, le son de l'eau qui coule devient"
print "de plus en plus fort."
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Vous avez raison c'est une CASCADE !!!"
print "Vous vous aggripez de toutes vos force"
print "[PAKLASH] Votre chaloupe eclate sous le choc ! "
print
print "Comme pour vous feliciter, une vois radiophonique resonne :"
print "[FELICITATION ! VOUS AVEZ SURVECU AU JEU TELEVISE 'LA CHUTE DE LA MORT !']"
print "[VOUS GAGNEZ UN JAMBON ET UN FOURRE-TOUT PRATIQUE POUVANT CONTENIR N'IMPORTE QUOI ]"
print "Et oui! Ce reve contient vraiment du n'importe quoi !"
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Vous continuez votre periple avec votre prix.."
print "Heureusement (et etonnament), vous n'avez aucune blessure."
print
raw_input("Appuyez sur [ENTRER]")
clear()
#changement d'encodage
print "Vous remarquez qu'il sera impossible de sortir par les côtés"
print "Ceux-ci sont trop haut..."
print "La nage est la seule issue possible..."
print "Aumoins, le courrant vous aide !"
print
print "Vous apercevez au loins, devant,"
print "un embranchement à la rivière..."
print
nag=raw_input("Aller à droite [a] à gauche [b]: ")
if nag=="a":
    clear()
    print "Vous arrivez vers une baie"
    print "Le courant qui vous portait se calme soudainement"
    print "Un poisson s'approche de vous.."
    print "Vous tenter de le toucher, mais il vous mord soudainement !"
    print
    print "C'est un PIRANAH !"
    print "Vous nagez frénétiquement dans l'autre direction"
    print "Mais il y en beaucoup d'autres.."
    print "Comment vous échapper ?"
    print
    pyr=raw_input("Tenter de sortir sur les cotés [a], Leurs lancer votre jambon [b]")
    if pyr=="a":
        clear()
        print "Vous tentez de grimper sur les parrois, mais la terre mouillée"
        print "s'éffrite sous vos doigt."
        print
        print "Vous réésayez tout de même de grimper, mais c'est un échec"
        print "et vous mouvement brusque ne font qu'attirer plus de PIRANAHS"
        print "...Vous lachez prise"
        print "[...]"
        print '\033[0;31m [VOUS ÊTES MORT.]\033[1;m'
        print '\033[0;31m [LES PIRANNAH ON TOUTEFOIS EU UN SOMPTUEUX REPAS.]\033[1;m'
        import sys
        sys.exit("\033[0;31m [PARTIE TERMINE]\033[1;m")

    else :
        clear()
        print "Vous utilisez ingénieusement votre jambon !"
        print "Vous le lancez d'une force surprenante de l'autre côté de la baie"
        print "Les PIRANAHS s'en vont alors immédiatement !"
        print "Vous faites une petite danse de satisfaction"
        raw_input("Appuyez sur [ENTRER]")
        clear()
else:
    True

print "Après une dizaine de minute de nage, vous appercevez une plage. "
print "Vous redoublez d'ardeur et arrivez finalement sur la terre ferme !"
print
print "Au loin, perdue dans la forêt, vous appercevez une petite maison."
raw_input("Appuyez sur [ENTRER]")
clear()

print "Le bâtiment est très petit et déllabré."
print "La majorité des planches qui le constitue est moisie et plusieurs fenêtres sont brisées"
print "Vous décidez tout de même de pénétrer à l'inerieur de cette sombre demeure"
raw_input("Appuyez sur [ENTRER]")
clear()

#garre
print "Sans pouvoir l'expliquer, vous vous retrouver vraisemblablement dans"
print "un vaste loby bondé de monde."
print
print "Vous entendez soudainement :"
print "[Le train entre en garre]"
print "Fatigué de votre périple et affamé, vous décidez de vous reposer sur un banc."
print
raw_input("Appuyez sur [ENTRER]")
clear()

print "Vous observez les environs "
print "[...]"
print
raw_input("Appuyez sur [ENTRER]")
clear()

print "Une billetterie..."
print
raw_input("Appuyez sur [ENTRER]")
clear()

print "Beaucoup beaucoup beaucoup de monde..."
print
raw_input("Appuyez sur [ENTRER]")
clear()


print "Pas de restaurant..."
print
raw_input("Appuyez sur [ENTRER]")
clear()

print "À cause de l'air déplacée par un nouveau train, "
print "vous apercevez un bout de papier qui balote au vent sous"
print "la pate du banc devant vous."
print
print "Vous vous approchez et vous découvrez qu'il s'agit en fait"
print "d'un billet de 20 dollars"
print
raw_input("Appuyez sur [ENTRER]")
clear()

print "Vous vous dirigez donc vers la billetterie."
print "Il est possible d'acheter un billet pour 15 dollars."
print
print "C'est donc ce que vous faites"
print "et vous montez dans ce train qui va dieux sais où..."
print
print "Il vous reste ainsi 5$"
print
raw_input("Appuyez sur [ENTRER]")
clear()

print "Assis sur une banquette, vous regardez à l'exterieur"
print "Le paysage défile devant vos yeux..."
print
print "C’est une magnifique vue vers une vallée entourées de montagne. "
print "On peut apercevoir de superbes rayons de soleil se coucher sur la vallée."
print "Vous fermez les yeux..."
print "et sombrez dans un profond sommeil."
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Vous vous réveillez en sursaut."
print "On annonce l'arrivée du train à un arrêt."
print
print "Vous n'avez cependant aucune idée du temps que vous avez dormis."
print "Il s'agit d'une grande métropole..."
print "Vous pouvez apercevoir de très grands buildings et une circultaion très dense."
print "Les portes s'ouvrent "
print "Plusieurs personnes décendent du train."
trn=raw_input("Voulez vous faire de même ? Oui[a] Non, rester dans le train[b]: ")
if trn=="b":
    print "Le train repart."
    print "La ville s'éloigne, les buildings rapetissent petit à petit"
    print 'alors que vous vous dirigez vers les montagnes'
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous décidez d'explorer le train."
    print "Depuis votre placce à l'avant, vous vous dirigez vers"
    print "le wagon restaurant."
    print "Le plan affiché sur les murs indique que celui-ci"
    print "ce situe à l'arrière du train."
    print "Vous vous y rendez et profitez de la vue vers la vallée."
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous vous assoyez à une table vide. "
    print "En fait, toutes les tables le sont."
    print "Vous remarquez qu'il n'y a personne abord du wagon."
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print
    print "Vous vous relevez pour quitter l'endroit quand, soudainement,"
    print "train bascule vers la droite!"
    print
    print "Vous tombez avec celui-ci et vous vous écrasez contre le mur."
    print "La vaissele fait de même dans un vacarme infernal."
    print "Allors que vous essayez d'éviter les éclats de verre qui glissent vers vous, "
    print "vous entendez un impitoyable détonation."
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Le wagon recommence à chuter !"
    print "Vous vous retrouvez projeté vers ce qui était, il y a quelques secondes, le plafond."
    print "Puis le sol."
    print "Puis le plafond."
    print "Puis le sol."
    print "..."
    print "Après une dizaine de tonnaux"
    print "Le wagon se fracasse contre un parrois rocheuse de la montagne. "
    print "[...]"
    print '\033[0;31m [VOUS MOURREZ SUR LE COUPS...]\033[1;m'
    import sys
    sys.exit("\033[0;31m [PARTIE TERMINE]\033[1;m")

else :
    True

#une fois débarqué choix petit resto / sortir de la garre (economiser...)


#conception
print '\033[0;32m Le jeu est toujours en conception, revenez bientôt ! \033[1;m'

#print '\033[0;31m ROUGE\033[1;m'
