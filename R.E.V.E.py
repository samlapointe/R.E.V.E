# coding: utf-8

#Credits
print "______________________________________________________"
print "\033[1;0mCopyright 2016 - Tous Droits Réservés\033[1;m"
print "\033[1;0mEn jouant à ce jeu vous acceptez son contrat de licence.\033[1;m"
print
print "Histoire créée par Olivier Brassard, Camille Brassard & Sandrine Jodoin"
print "Développé par Olivier Brassard"
print "Modification et amélioration par Savannah Legault"
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
print
import time
print time.strftime('%d/%m/%y %H:%M',time.localtime())
print
nom=raw_input("Quel est votre nom : ")
print
print "BIENVENU " + nom.upper()
introqst=raw_input("POUR SAUTER L'INTRODUCTION APPUYEZ SUR [a] SINON SUR [ENTER] ")
if introqst=="a":
    True
else:
   clear()

   print "------------------"
   print "Je suis le Dr Robert Wonderstone;"
   print "Spécialiste des phénomènes psychiques du subconscient."
   print
   print "Ma spécialité ? Les rêves."
   print "Les rêves sont intimement liés à la vie du rêveur"
   print
   print "La plupart du temps, vous ne vous rappelez pas de vos rêves."
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
   print "de leurs rêves si on les réveille pendant le sommeil paradoxal. "
   print "C'est à ce moment qu'il devient possible de les extraire"
   print
   print "Cependant, il y a une faille."
   print
   print "Lors de l'extraction, le dernier sujet a fait une crise d'épilepsie..."
   print "J'ai voulu annuler le processus, mais il était trop tard..."
   print "Mort cérébrale"
   raw_input("Appuyez sur [ENTRER]")
   clear()
   print "Toutefois j'ai remarqué un phénomène étrange."
   print "Malgré le coma de type 5 de mon patient, le rêve ne s'est pas arrêté."
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
print "Allonge-toi ici " + nom
print "Je t'injecte un somnifère..."
print "Les effets se feront ressentir dans quelques minutes"

print "Tout à l'heure, il sera possible de communiquer ensemble,"
print "je te guiderai tout le long du périple."
print
print "Ton subconscient sera en lien avec le système et avec le rêve de mon ex-patient"
print "Je te donnerai plus de détails lorsque tu auras atteint le sommeil paradoxal"
print "TOUTEFOIS JE DOIS T'AVERTIR ..."
print "Tu ne dois JAMAIS avoir de contact physique avec lui, sinon"
print "cela créera des interférences entre ton subconscient et le sien."
print "Ça pourrait te TUER !!!"
print
print "Ahh, j'oubliais !"
print "Dans un rêve ordinaire où tu meurs, tu te réveilles, mais dans "
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
print "Rebonjour " + nom
print "Tu es désormais dans le R.E.V.E"
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Je dois t'avertir qu'il faudra être très vigilant lors"
print "de la saisie d'informations..."
print
print "Mon système n'étant pas très stable, une erreur pourrait être fatale"
print "Ainsi quand tu as le choix entre deux options, tu dois absolument choisir"
print "l'une ou l'autre, et ce, de façon exacte"
print
print "Testons-le tout de suite !"
a=raw_input("Fais un [a] et appuis sur [entrer]: ")
print
if a=="a":
    print "Ça fonctionne"
else:
    print "Tu as fait une erreur, il faudra faire attention"
    print "une fois dans le rêve, ça pourrait te tuer !"
print
print "Je crois que tu es prêt, on entre dans le rêve ?"
play=raw_input("Oui: Appuyez sur [a] - Non: Appuyez sur [b] : ")
if play=="a":
    clear()
    print "C'est parti !"
else:
    clear()
    print "On a plus le temps de parler, de toute façon, tu ne peux plus reculer"
    print "C'est parti !"

# Debut de l'histoire
# Labo
raw_input("Appuyez sur [ENTRER]")
clear()
print "Vous êtes dans une pièce sombre."
print "Vous ne voyez rien."
print "Vos yeux s'accommodent tranquillement à la noirceur"
print "Vous distinguez maintenant une grande porte et, au plafond, une bouche d'aération."
print "Pour sortir de cette pièce, voulez-vous vous :"
c1=raw_input("déplacer vers la porte [a] ou tenter de vous hisser vers les conduits [b]?: ")
if c1=="a":
    clear()
    print "Vous êtes face à la porte"
    print "Vous remarquez qu'elle est verrouillée"
    print "Il est possible d'ouvrir la porte à l'aide d'un mot de passe"
    c1a=raw_input("Essayer un mot de passe [a] ou rebrousser chemin [b]")
    if c1a=="a":
        clear()
        raw_input("Entrez le mot de passe, puis appuyer sur [ENTRER] : ")
        clear()
        print '\033[0;31m [ACCÈS REFUSÉ]\033[1;m'
        raw_input("Appuyez sur [ENTRER]")
        clear()
    else: True
    print "Vous rebroussez chemin"
    print "Vous prenez votre élan et vous vous agrippez à la tuyauterie du plafond"
    print "Vous poussez la grille et pénétrez dans le conduit."
else:
    clear()
    print "Vous prenez votre élan et vous vous agrippez à la tuyauterie du plafond"
    print "Vous poussez la grille et pénétrez dans le conduit."
print "Vous rampez tranquillement ..."
print "Vous arrivez finalement à une INTERSECTION !!!"
print "Dans quelle direction voulez-vous aller ?"
c2=raw_input("Droite [a] ou Gauche [b]")
if c2=="a":
    clear()
    print "Vous marchez vers le bout du conduit."
    print "Vous apercevez maintenant une pièce où vous pourriez descendre "
    c2a=raw_input("Descendre [a], rebrousser chemin [b]")
    if c2a=="a":
        clear()
        print "Vous atterrissez dans la pièce remplie d'étranges étagères"
        print "Elles sont remplies de nombreuses éprouvettes, béchers et bocaux"
        print "Vous apercevez qu'il y a, dans quelques bocaux, des cerveaux flottants"
        print "En panique, vous vous dirigez vers l'autre extrémité de la pièce"
        print "Vous tombez alors sur un sarrau et des lunettes "
        print "[Vous prenez  (et mettez) ces objets]"
        print "Vous sortez par la porte"
        raw_input("Appuyez sur [entrer]")
        clear()
        print "Vous arrivez alors au couloir"
        print "Celui-ci contient deux portes."
        print "la '501A' et la '502A'"
        print "Laquelle choisir ??"
        port=raw_input("501A [a], 502A [b]")
        if port=="a":
            clear()
            print "La salle est très grande."
            print "Vous entrez en toute discrétion grasse à votre fabuleux déguisement"
            print "Vous explorez tranquillement sous  le regard interrogé des scientifiques."
            print "Toutefois, ceux-ci ne semblent pas trop comprendre la situation"
            print "Ils n'ont  pas l'aire  d'être très sain d'esprit."
            print "Vous remarquez qu'il n'y a rien de vraiment intéressant alors vous sortez..."
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print
            print "Vous vous présentez alors devant l'autre salle."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ÉLECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'équipement informatique"
            print "Plus précisément, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNÉTIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit très étrange, vous vous dirigez"
            print "d'un pas pressé vers la porte du fond."
            raw_input("Appuyez sur [ENTRER]")
            clear()
        else:
            clear()
            print "Vous vous présentez alors devant la porte 502A."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ÉLECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'équipement informatique"
            print "Plus précisément, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNÉTIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit, vous vous dirigez"
            print "d'un pas pressé vers la porte du fond."
            raw_input("Appuyez sur [ENTRER]")
            clear()

        print "Vous atteignez un nouveau corridor, étrangement, c'est un"
        print "cul-de-sac... une seule porte coulissante..."
        print "Vous vous approchez de cette porte et tentez de l'ouvrir"
        print
        print "Au même moment, un scientifique au regard vide sort de la salle des serveurs."
        print "Il tente de vous attaquer par derrière, mais vous le poussez par terre."
        print "En tombant il tente de se retenir à vous."
        print "Ses ongles vous grafignent l'avant-bras."
        print "Vous ne saignez pas, mais la blessure est tout de même apparente."
        print "Aussi étrangement qu'il est arrivé, l'homme (fou), repart en criant"
        print
        print 'Vous revenez à votre objectif : la porte'
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
            print "Vous retentez..."
            print "La porte s'ouvre en un bruit sourd."
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous courrez vers l'extérieur"
            print "[La lumière blanche envahie l'espace...]"
            raw_input("Appuyez sur [ENTRER]")
            clear()
        else:
            clear()
            print "De retour dans la salle des serveurs..."
            print "Vous remarquez une console que vous n'aviez pas vue antérieurement"
            print "Vous tentez d'y accéder"
            raw_input("Entrez votre mot de passe: ")
            clear()
            print '\033[0;31m [ACCÈS REFUSÉ]\033[1;m'
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Une alarme retentis soudainement:"
            print '\033[0;31m [ALERTE 5 - INTRUSION AU SYSTÈME]\033[1;m'
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print
            print "Vous resortez, en courant, dans le corridor"
            print "Vous retentez d'ouvrir la porte"
            print "Elle s'ouvre en un bruit sourd."
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous courrez vers l'extérieur"
            print "[La lumière blanche envahie l'espace...]"
            raw_input("Appuyez sur [ENTRER]")
            clear()

    else:
        clear()
        print "Vous rebroussez chemin"
        print "Après un peu de marche, vous sautez dans la seconde pièce"
        print "Elle contient toute sorte de placards vitres"
        print "Vous choisissez une des portes de cette pièce ronde et peu éclairée"
        print "Vous examinez son contenu."
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print
        print "Vous remarquez qu'il s'agit d'une vaste collection"
        print "d'armes expérimentales."
        print "[Vous prenez une arme (au cas ou)]"
        print "Vous sortez par la porte principale"
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Vous arrivez alors a un couloir"
        print "Celui-ci contient deux portes."
        print "la '501A' et la '502A'"
        print "Laquelle choisir ??"
        port1=raw_input("501A [a], 502A [b]")
        if port1=="a":
            clear()
            print "La salle est très grande."
            print "Vous entrez en vitesse"
            print "Les scientifiques affolés se dirigent vers vous."
            print "Ils n'ont  pas l'aire  d'être très sain d'esprit."
            print "Vous prenez votre fusil au plasma et vous les désintégrez"
            print "Vous ne voulez pas être détecté alors vous sortez..."
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous vous présentez devant la salle 502A."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ÉLECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'équipement informatique"
            print "Plus précisément, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNÉTIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit très étrange, vous vous dirigez"
            print "d'un pas pressé vers la porte du fond."
            raw_input("Appuyez sur [ENTRER]")
            clear()

        else:
            clear()
            print "Vous vous présentez devant la salle 502A."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ÉLECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'équipement informatique"
            print "Plus précisément, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNÉTIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit très étrange, vous vous dirigez"
            print "d'un pas pressé vers la porte du fond."
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()

        print "Vous atteignez un nouveau corridor, étrangement, c'est un"
        print "cul-de-sac... une seule porte coulissante..."
        print "Vous vous approchez de cette porte et tentez de l'ouvrir"
        print
        print "Au même moment, un scientifique au regard vide sort de la salle des serveurs."
        print "Il tente de vous attaquer par derrière, mais vous le poussez par terre."
        print "En tombant il tente de se retenir à vous."
        print "Ses ongles vous grafignent l'avant-bras."
        print "Vous ne saignez pas, mais la blessure est tout de même apparente."
        print "Aussi étrangement qu'il est arrivé, l'homme (fou), repart en criant"
        print
        print 'Vous revenez à votre objectif : la porte'
        print "Vous approchez la carte du lecteur..."
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print
        print '\033[0;31m [ERREUR - LECTURE IMPOSSIBLE]\033[1;m'
        print
        card2=raw_input("Essayer une autre fois [a], retourner dans la salle des serveurs [b]")
        if card2=="a":
            clear()
            print "Vous retentez..."
            print "La porte s'ouvre en un bruit sourd."
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous courrez vers l'extérieur"
            print "[La lumière blanche envahie l'espace...]"
            raw_input("Appuyez sur [ENTRER]")
            clear()
        else:
            clear()
            print "De retour dans la salle des serveurs..."
            print "Vous remarquez une console que vous n'aviez pas vue antérieurement"
            print "Vous tentez d'y accéder"
            raw_input("Entrez votre mot de passe: ")
            clear()
            print '\033[0;31m [ACCÈS REFUSE]\033[1;m'
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Une alarme retentis soudainement:"
            print '\033[0;31m [ALERTE 5 - INTRUSION AU SYSTÈME]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous resortez, en courant, dans le corridor"
            print "Vous retentez d'ouvrir la porte"
            print "Elle s'ouvre en un bruit sourd."
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous courrez vers l'extérieur"
            print "[La lumière blanche envahie l'espace...]"
            raw_input("Appuyez sur [ENTRER]")
            clear()


else:
    clear()
    print "Vous marchez vers le bout du conduit."
    print "Vous apercevez maintenant une pièce où vous pourriez descendre "
    c2b=raw_input("Descendre [a], rebrousser chemin [b]")
    if c2b=="a":
       clear()
       print "Vous atterrissez dans la pièce"
       print "Elle contient toute sorte de placards vitres"
       print "Vous choisissez une des portes de cette pièce ronde et peu éclairée"
       print "Vous examinez son contenu."
       print
       raw_input("Appuyez sur [ENTRER]")
       clear()
       print "Vous remarquez qu'il s'agit d'une vaste collection"
       print "d'armes expérimentales."
       print "[Vous prenez une arme (au cas ou)]"
       print "Vous sortez par la porte principale"
       raw_input("Appuyez sur [ENTRER]")
       clear()
       print "Vous arrivez alors au couloir"
       print "Celui-ci contient deux portes."
       print "la '501A' et la '502A'"
       print "Laquelle choisir ??"
       port2=raw_input("501A [a], 502A [b]")
       if port2=="a":
           clear()
           print "La salle est très grande."
           print "Vous entrez en vitesse"
           print "Les scientifiques affolés se dirigent vers vous."
           print "Ils n'ont  pas l'aire  d'être très sain d'esprit."
           print "Vous prenez votre fusil au plasma et vous les désintégrez"
           print "Vous ne voulez pas être détecte alors vous sortez..."
           raw_input("Appuyez sur [ENTRER]")
           clear()
           print "Vous vous présentez alors devant l'autre salle."
           print "La porte coulissante s'ouvre automatiquement"
           print "[SON ÉLECTRONIQUE]"
           print "Il s'agit d'une salle pleine d'équipement informatique"
           print "Plus précisément, une salle des serveurs"
           print
           print "[VOUS TROUVEZ UNE CARTE MAGNÉTIQUE]"
           print
           print "Dans l'espoir de sortir de cet endroit très étrange, vous vous dirigez"
           print "d'un pas pressé vers la porte du fond."
           raw_input("Appuyez sur [ENTRER]")
           clear()
       else:
           clear
           print "Vous vous présentez alors devant l'autre salle."
           print "La porte coulissante s'ouvre automatiquement"
           print "[SON ÉLECTRONIQUE]"
           print "Il s'agit d'une salle pleine d'équipement informatique"
           print "Plus précisément, une salle des serveurs"
           print
           print "[VOUS TROUVEZ UNE CARTE MAGNÉTIQUE]"
           print
           print "Dans l'espoir de sortir de cet endroit très étrange, vous vous dirigez"
           print "d'un pas pressé vers la porte du fond."
           raw_input("Appuyez sur [ENTRER]")
           clear()

       print "Vous atteignez un nouveau corridor, étrangement, c'est un"
       print "cul-de-sac... une seule porte coulissante..."
       print "Vous vous approchez de cette porte et tentez de l'ouvrir"
       print
       print "Au même moment, un scientifique au regard vide sort de la salle des serveurs."
       print "Il tente de vous attaquer par derrière, mais vous le poussez par terre."
       print "En tombant il tente de se retenir à vous."
       print "Ses ongles vous grafignent l'avant-bras."
       print "Vous ne saignez pas, mais la blessure est tout de même apparente."
       print "Aussi étrangement qu'il est arrivé, l'homme (fou), repart en criant"
       print
       print 'Vous revenez à votre objectif : la porte'
       print "Vous approchez la carte du lecteur..."
       print
       raw_input("Appuyez sur [ENTRER]")
       clear()
       print '\033[0;31m [ERREUR - LECTURE IMPOSSIBLE]\033[1;m'
       print
       card3=raw_input("Essayer une autre fois [a], retourner dans la salle des serveurs [b]")
       if card3=="a":
           clear()
           print "Vous retentez..."
           print "La porte s'ouvre en un bruit sourd."
           print "Vous courrez vers l'extérieur"
           print "[La lumière blanche envahi l'espace...]"
           print
           print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
           print
           raw_input("Appuyez sur [ENTRER]")
           clear()
           print "Vous courrez vers l'extérieur"
           print "[La lumière blanche envahie l'espace...]"
           raw_input("Appuyez sur [ENTRER]")
           clear()

       else:
           clear()
           print "De retour dans la salle des serveurs..."
           print "Vous remarquez une console que vous n'aviez pas vue antérieurement"
           print "Vous tentez d'y accéder"
           raw_input("Entrez votre mot de passe: ")
           clear()
           print
           print '\033[0;31m [ACCÈS REFUSE]\033[1;m'
           raw_input("Appuyez sur [ENTRER]")
           clear()
           print
           print "Une alarme retentis soudainement:"
           print '\033[0;31m [ALERTE 5 - INTRUSION AU SYSTÈME]\033[1;m'
           print
           raw_input("Appuyez sur [ENTRER]")
           clear()
           print "Vous resortez, en courant, dans le corridor"
           print "Vous retentez d'ouvrir la porte"
           print "Elle s'ouvre en un bruit sourd."
           print
           print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
           print
           raw_input("Appuyez sur [ENTRER]")
           clear()
           print "Vous courrez vers l'extérieur"
           print "[La lumière blanche envahie l'espace...]"
           raw_input("Appuyez sur [ENTRER]")
           clear()
    else:
        clear()
        print "Vous rebroussez chemin"
        print "Après un peu de marche, vous sautez dans la seconde pièce"
        print "Vous atterrissez. Elle est remplie d'étrange étagère"
        print "Elles sont remplies de nombreuses eprouvettes, bechers et bocaux"
        print "Vous apercevez qu'il y a, dans quelques bocaux, des cerveaux flottants"
        print "En panique, vous vous dirigez vers l'autre extrémité de la pièce"
        print "Vous tombez alors sur un sarrau et des lunettes "
        print "[Vous prenez  (et mettez) ces objets]"
        print "Vous sortez par la porte"
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Vous arrivez alors au couloir"
        print "Celui-ci contient deux portes."
        print "la '501A' et la '502A'"
        print "Laquelle choisir ??"
        port3=raw_input("501A [a], 502A [b]")
        if port3=="a":
            clear()
            print "La salle est très grande."
            print "Vous entrez en toute discrétion grasse à votre fabuleux déguisement"
            print "Vous explorez tranquillement sous  le regard interroge des scientifiques."
            print "Toutefois, ceux-ci ne semblent pas trop comprendre la situation"
            print "Ils n'ont  pas l'aire  d'être très sain d'esprit."
            print "Vous remarquez qu'il n'y a rien de vraiment intéressant alors vous sortez..."
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous vous présentez donc devant l'autre salle."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ÉLECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'équipement informatique"
            print "Plus précisément, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNÉTIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit très étrange, vous vous dirigez"
            print "d'un pas pressé vers la porte du fond."
            raw_input("Appuyez sur [ENTRER]")
            clear()

        else:
            clear()
            print "Vous vous présentez devant la salle 502A."
            print "La porte coulissante s'ouvre automatiquement"
            print "[SON ÉLECTRONIQUE]"
            print "Il s'agit d'une salle pleine d'équipement informatique"
            print "Plus précisément, une salle des serveurs"
            print
            print "[VOUS TROUVEZ UNE CARTE MAGNÉTIQUE]"
            print
            print "Dans l'espoir de sortir de cet endroit très étrange, vous vous dirigez"
            print "d'un pas pressé vers la porte du fond."
            raw_input("Appuyez sur [ENTRER]")
            clear()

        print "Vous atteignez un nouveau corridor, étrangement, c'est un"
        print "cul-de-sac... une seule porte coulissante..."
        print "Vous vous approchez de cette porte et tentez de l'ouvrir"
        print
        print "Au même moment, un scientifique au regard vide sort de la salle des serveurs."
        print "Il tente de vous attaquer par derrière, mais vous le poussez par terre."
        print "En tombant il tente de se retenir à vous."
        print "Ses ongles vous grafignent l'avant-bras."
        print "Vous ne saignez pas, mais la blessure est tout de même apparente."
        print "Aussi étrangement qu'il est arrivé, l'homme (fou), repart en criant"
        print
        print 'Vous revenez à votre objectif : la porte'
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
            print "Vous courrez vers l'extérieur"
            print "[La lumière blanche envahi l'espace...]"
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous courrez vers l'extérieur"
            print "[La lumière blanche envahie l'espace...]"

        else:
            clear()
            print "De retour dans la salle des serveurs..."
            print "Vous remarquez une console que vous n'aviez pas vue antérieurement"
            print "Vous tentez d'y accéder"
            raw_input("Entrez votre mot de passe: ")
            clear()
            print '\033[0;31m [ACCÈS REFUSE]\033[1;m'
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print
            print "Une alarme retentis soudainement:"
            print '\033[0;31m [ALERTE 5 - INTRUSION AU SYSTÈME]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print "Vous resortez, en courant, dans le corridor"
            print "Vous retentez d'ouvrir la porte"
            print "Elle s'ouvre en un bruit sourd."
            print
            print '\033[0;32m [ACCES AUTHORIZE]\033[1;m'
            print
            raw_input("Appuyez sur [ENTRER]")
            clear()
            print
            print "Vous courrez vers l'extérieur"
            print "[La lumière blanche envahie l'espace...]"
            raw_input("Appuyez sur [ENTRER]")
            clear()

print "[Dr Wonderstone : ]"
print
print nom.upper() + "!"
print
print "Tu te demandes peut-être ce qu'il se passe..."
print
print "C'est ce qu'on appelle un 'bris de continuité'."
print
print "Tu as probablement déjà remarque que lorsqu'on "
print "arrive a se souvenir d'un rêve, il en manque souvent des parties."
print "En effet, c'est parce que les rêves sont à la base, décousus."
print
print "Il est normal, dans l'univers des rêves, de voyager dans le temps ou l'espace"
print "comme cela sans aucune raison valable... c'est ce qu'on appelle le bris de continuité"
print
print "C'est aussi pour cette raison, que lors d'un changement d'univers"
print "tous les objets que tu avais précédemment peuvent se réinitialiser."
print "C'est pour cette raison que tu n'es plus habillé comme il y a quelques minutes..."
print
print "Je te laisse, bonne chance!"
raw_input("Appuyez sur [ENTRER]")
clear()
print

# 2e monde
print "Vous arrivez alors dans une clairière ensoleillée."
print "D'un côté: une grande forêt de conifères, de l'autre: une rivière."
print "De quel côté voulez vous aller ?"
print
fb=raw_input("Foret [a] ou rivière [b]: ")
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
    print "Il commence a faire noir et vous n'avez toujours rien découvert"
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
        print "Vous décidez de vous arrêter pour dormir"
        print "Soudainement, vous entendez un craquement derrière vous."
        print "SURPISE ! UN OURS NOIR !"
        print
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Vous tentez de grimper à un arbre, mais vous glissez et vous vous"
        print "foulez la cheville."
        print
        print "L'ours affamé s'approche de vous avec appétit.."
        print "[SLURP !!] En se léchant les babines..."
        print "..."
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "..."
        print '\033[0;31m [VOUS ÊTES MORT]\033[1;m'
        print "\033[0;31m [L'OURS À TOUTEFOIS OBTENU UN SOMPTUEUX REPAS.] \033[1;m"
        import sys
        sys.exit("\033[0;31m [PARTIE TERMINÉE]\033[1;m")
    else:
        print "Vous retournez vers la rivière"
        raw_input("Appuyez sur [ENTRER]")
        True
else:
    True
clear()
print
print "Pres du cours d'eau, vous apercevez une vieille chaloupe."
print "Vous embarquez dans celle-ci."
print "Vous naviguez paisiblement sur l'eau calme de cette paisible rivière"
print
print "Vous relaxez..."
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Cependant, vous avez l'impression que le courant s'intensifie."
print "Vous vous levez debout..."
print
print "En plissant les yeux, vous avez l'impression que la "
print "rivière se termine au loin. Malheureusement, vous n'avez aucune pagaie"
print "et, comme pour confirmer vos pensées, le son de l'eau qui coule devient"
print "de plus en plus fort."
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Vous avez raison c'est une CASCADE !!!"
print "Vous vous agrippez de toutes vos forces"
print "[PAKLASH] Votre chaloupe éclate sous le choc ! "
print
print "Comme pour vous féliciter, une voix radiophonique resonne :"
print "[FÉLICITATION ! VOUS AVEZ SURVÉCU AU JEU TÉLÉVISÉ 'LA CHUTE DE LA MORT !']"
print "[VOUS GAGNEZ UN JAMBON ET UN FOURRE-TOUT PRATIQUE POUVANT CONTENIR N'IMPORTE QUOI ]"
print "Eh oui! Ce rêve contient vraiment  n'importe quoi !"
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Vous continuez votre périple avec votre prix.."
print "Heureusement (et étonnamment), vous n'avez aucune blessure."
print
raw_input("Appuyez sur [ENTRER]")
clear()
#changement d'encodage
print "Vous remarquez qu'il sera impossible de sortir par les côtés"
print "Ceux-ci sont trop haut..."
print "La nage est la seule issue possible..."
print "Aumoins, le courant vous aide !"
print
print "Vous apercevez au loin, devant,"
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
    pyr=raw_input("Tenter de sortir sur les cotés [a], Leur lancer votre jambon [b]")
    if pyr=="a":
        clear()
        print "Vous tentez de grimper sur les parois, mais la terre mouillée"
        print "s'effrite sous vos doigts."
        print
        print "Vous réessayez tout de même de grimper, mais c'est un échec"
        print "et vous mouvement brusque ne font qu'attirer plus de PIRANAHS"
        print "...Vous lâchez prise"
        print "[...]"
        print '\033[0;31m [VOUS ÊTES MORT.]\033[1;m'
        print '\033[0;31m [LES PIRANNAH ON TOUTEFOIS EU UN SOMPTUEUX REPAS.]\033[1;m'
        import sys
        sys.exit("\033[0;31m [PARTIE TERMINÉE]\033[1;m")

    else :
        clear()
        print "Vous utilisez ingénieusement votre jambon !"
        print "Vous le lancez d'une force surprenante de l'autre côté de la baie"
        print "Les PIRANNAHS s'en vont alors immédiatement !"
        print "Vous faites une petite danse de satisfaction"
        raw_input("Appuyez sur [ENTRER]")
        clear()
else:
    True

print "Après une dizaine de minutes de nage, vous apercevez une plage. "
print "Vous redoublez d'ardeur et arrivez finalement sur la terre ferme !"
print
print "Au loin, perdue dans la forêt, vous apercevez une petite maison."
raw_input("Appuyez sur [ENTRER]")
clear()

print "Le bâtiment est très petit et délabré."
print "La majorité des planches qui le constitue est moisie et plusieurs fenêtres sont brisées"
print "Vous décidez tout de même de pénétrer à l'intérieur de cette sombre demeure"
raw_input("Appuyez sur [ENTRER]")
clear()

#gare
print "Sans pouvoir l'expliquer, vous vous retrouver vraisemblablement dans"
print "un vaste hall bondé de monde."
print
print "Vous entendez soudainement :"
print "[Le train entre en gare]"
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

print "À cause de l'air déplacé par un nouveau train, "
print "vous apercevez un bout de papier qui ballote au vent sous"
print "la pâte du banc devant vous."
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

print "Assis sur une banquette, vous regardez à l'extérieur"
print "Le paysage défile devant vos yeux..."
print
print "C’est une magnifique vue vers une vallée entourée de montagne. "
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
print "Vous pouvez apercevoir de très grands immeubles et une circulation très dense."
print "Les portes s'ouvrent "
print "Plusieurs personnes descendent du train."
trn=raw_input("Voulez-vous faire de même ? Oui[a] Non, rester dans le train[b]: ")
if trn=="b":
    clear()
    print "Le train repart."
    print "La ville s'éloigne, les immeubles rapetissent petit à petit"
    print 'alors que vous vous dirigez vers les montagnes'
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous décidez d'explorer le train."
    print "Depuis votre place à l'avant, vous vous dirigez vers"
    print "le wagon restaurant."
    print "Le plan affiché sur les murs indique que celui-ci"
    print "ce situe à l'arrière du train."
    print "Vous vous y rendez et profitez de la vue vers la vallée."
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous vous assoyez à une table vide. "
    print "En fait, toutes les tables le sont."
    print "Vous remarquez qu'il n'y a personne à bord du wagon."
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print
    print "Vous vous relevez pour quitter l'endroit quand, soudainement,"
    print "train bascule vers la droite!"
    print
    print "Vous tombez avec celui-ci et vous vous écrasez contre le mur."
    print "La vaisselle fit de même dans un vacarme infernal."
    print "Allors que vous essayez d'éviter les éclats de verre qui glissent vers vous, "
    print "vous entendez une impitoyable détonation."
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Le wagon recommence à chuter !"
    print "Vous vous retrouvez projeté vers ce qui était, il y a quelques secondes, le plafond."
    print "Puis le sol."
    print "Puis le plafond."
    print "Puis le sol."
    print "..."
    print
    raw_input("Appuyez sur [ENTRER]")
    print "Après une dizaine de tonneaux"
    print "Le wagon se fracasse contre une paroi rocheuse de la montagne. "
    print "[...]"
    print '\033[0;31m [VOUS MOURREZ SUR LE COUP...]\033[1;m'
    import sys
    sys.exit("\033[0;31m [PARTIE TERMINÉE]\033[1;m")

else :
    True
clear()
print "Une fois sorti du train, vous vous retrouvez dans une gare semblable"
print "à celle où vous êtes monté."
print
print "Cependant, vous remarquez un petit café où vous pourriez enfin manger !"
print "Voulez-vous y acheter quelque chose?"
resto=raw_input("Oui[a], Non [b]")
if resto=="a":
    clear()
    print "Vous achetez un petit sandwich pour 5$"
    print "[Il ne vous reste plus d'argent.]"
    print "Vous vous régalez."
    print "Après ce magnifique encas, vous partez explorer la cité"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous marchez tranquillement dans la grande métropole..."
    print "Les gratte-ciel vous dominent de leur hauteur."
    print "Par cette chaude journée, vous êtes reconnaissant de l'ombre qu'ils vous procurent."
    print "À cette heure de la journée, les gens affluent en grand nombre sur les trottoirs."
    print "Vous vous faufilez habilement à travers cette marrée humaine."
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Après quelques minutes de marche, vous avez l'impression que quelqu'un vous observe."
    print "Vous regardez discrètement par-dessus votre épaule, mais vous ne voyez rien de suspect."
    print "Vous continuez donc d'avancer, mais vous avez VRAIMENT l'impression que quelqu'un vous suit. "
    print "Vos yeux sont soudainement attirés vers une magnifique vitrine colorée."
    print "Au même moment, une main se pose brusquement sur votre épaule !"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous vous retournez et constatez que le propriétaire de la main est un vieil"
    print "homme au regard paranoïaque."
    print
    print "Il vous tend frénétiquement un vieux journal roulé sur lui même."
    print "- Je sais pourquoi vous êtes ici !!!"
    print "Vous le regardez d'un regard interrogateur."
    print "- Vous devez vite vous rendre là-bas, vous dit-il tout en mettant le vieux papier en évidence. "
    print "SINON, ILS VOUS AURONT !"
    print
    print "Vous lui demandez plus d'information, mais l'homme s'obstine à ne pas répondre."
    print "Il vous lance le rouleau et quitte en claudiquant. "
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Sans trop comprendre, vous ramassez le journal et vous le déroulez"
    print "Sur la première page, vous découvrez une série de chiffres écrits à la main"
    print "La combinaison entourée de plusieurs traits de crayon ressemble à un numéro de téléphone."
    print
    print "{352-142-9977}"
    print
    print "Vous décidez ainsi de chercher une cabine téléphonique"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Après quelques minutes et une question à un chauffeur de Taxi,"
    print "Vous en trouvez une!"
    print "Toute rouge et vitrée; digne de l'Angleterre."
    print "Vous entrez."
    print "Vous décrochez"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "[<<ENFONCEZ BIEN VOTRE CARTE OU COMPOSEZ UN NUMÉRO>>]"
    print "Vous composez ..."
    print "[LES FRAIS D'APPEL VERS CE NUMÉRO SONT DE 2$]"
    print "OR! Vous n'avez plus un sou"
    print "Vous ressortez, bredouille, à la recherche d'une pièce de 2$"
    print "Vous pourriez;"
    print "Scruter le sol dans l'espoir de trouver par hasard quelques pièces [a]"
    print "Demander un peu d'argent à un passant [b]"
    mon=raw_input("Que voulez-vous faire?")
    if mon=="a":
        clear()
        print "Les yeux rivés au sol, vous recommencez votre marche"
        print "Sous les bancs, près des trottoirs, dans les machines distributrice,"
        print "dans un parc, dans plusieurs magasins..."
        print "Il n'y a pas un endroit où vous n'avez pas cherché!"
        print "Pourtant, vous n'avez rien trouvé... "
        print "Vous abandonnez donc les recherches et vous résignez à votre plan A"
        print
        raw_input("Appuyez sur [ENTRER]")
        True

    else :
        True
    clear()
    print "Vous cherchez donc une généreuse âme pour vous tirer d'affaire."
    print "Après un bref balayage visuel, vous apercevez un homme qui marche sur le trottoir"
    print "et une femme assise sur une terrasse. "
    print
    print "À qui voulez-vous demander de l'argent?"
    qst=raw_input("L'homme [a] ou la femme [b]")
    if qst=="a":
        clear()
        print "Vous accélérez le pas, pour rejoindre le monsieur de l'autre côté de la rue"
        print "Vous lui expliquez la situation et lui demandez 2$"
        print "Il refuse."
        print "Vous insistez en lui précisant que c'est très important"
        print "Il vous insulte et vous dit d'aller voir ailleur."
        print "Offencé, vous l'insultez à votre tour."
        print
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "L'homme se fâche et vous pousse vers la rue."
        print "À l'instant même une voiture tourne le coin."
        print "Tout se passe très rapidement:"
        print "Vous tombez par terre, les phares de la voiture vous aveuglent,"
        print "Vous entendez les crissements des pneus, mais il est déjà trop tard."
        print
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Le véhicule vous percute avant que vous n'ayez pu vous relever."
        print "Vous vous retrouvez projeté sur le trottoir, votre tête se"
        print "cogne sur la bordure. Vous perdez connaissance."
        print
        print '\033[0;31m [VOUS ÊTES MORT.]\033[1;m'
        print '\033[0;31m [LES SECOURS NE SONT PAS ARRIVÉS À TEMPS]\033[1;m'
        import sys
        sys.exit("\033[0;31m [PARTIE TERMINÉE]\033[1;m")
    else :
        clear()
        print "Vous accélérez le pas, pour rejoindre la jeune demoiselle"
        print "Vous lui expliquez la situation et lui demandez gentiment 2$"
        print "Vous lui faites votre plus beau sourire..."
        print "Elle accepte !"
        print '\033[0;32m [Vous avez maintenant 2$]\033[1;m'
        print
        print "Vous retournez, d'un pas vif, vers la cabine téléphonique"
        print "Vous recomposez le numéro et acceptez les frais."
        print
        raw_input("Appuyez sur [ENTRER]")
        True
else:
    clear()
    print "Vous continuez d'avoir faim, mais vous économisez 5$"
    print "Vous explorez ainsi la cité."
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous marchez tranquillement dans la grande métropole..."
    print "Les gratte-ciel vous dominent de leur hauteur."
    print "Par cette chaude journée, vous êtes reconnaissant de l'ombre qu'ils vous procurent."
    print "À cette heure de la journée, les gens affluent en grand nombre sur les trottoirs."
    print "Vous vous faufilez habilement à travers cette marrée humaine."
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Après quelques minutes de marche, vous avez l'impression que quelqu'un vous observe."
    print "Vous regardez discrètement par-dessus votre épaule, mais vous ne voyez rien de suspect."
    print "Vous continuez donc d'avancer, mais vous avez VRAIMENT l'impression que quelqu'un vous suit. "
    print "Vos yeux sont soudainement attirés vers une magnifique vitrine colorée."
    print "Au même moment, une main se pose brusquement sur votre épaule !"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous vous retournez et constatez que le propriétaire de la main est un vieil"
    print "homme au regard paranoïaque."
    print
    print "Il vous tend frénétiquement un vieux journal roulé sur lui même."
    print "- Je sais pourquoi vous êtes ici !!!"
    print "Vous le regardez d'un regard interrogateur."
    print "- Vous devez vite vous rendre là-bas, vous dit-il tout en mettant le vieux papier en évidence. "
    print "SINON, ILS VOUS AURONT !"
    print
    print "Vous lui demandez plus d'information, mais l'homme s'obstine à ne pas répondre."
    print "Il vous lance le rouleau et chite en claudiquant. "
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Sans trop comprendre, vous ramassez le journal et vous le déroulez"
    print "Sur la première page, vous découvrez une série de chiffres écrits à la main"
    print "La combinaison entourée de plusieurs traits de crayon ressemble à un numéro de téléphone."
    print
    print "{352-142-9977}"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous décidez ainsi de chercher une cabine téléphonique"
    print "Après quelques minutes et une question à un chauffeur de Taxi,"
    print "Vous en trouvez une!"
    print "Toute rouge et vitrée; digne de l'Angleterre."
    print "Vous entrez."
    print
    print "Vous décrochez"
    print "[<<ENFONCEZ BIEN VOTRE CARTE OU COMPOSEZ UN NUMÉRO>>]"
    print "Vous composez ..."
    print "[LES FRAIS D'APPEL VERS CE NUMÉRO SONT DE 2$]"
    print "Vous confirmez."
    print
    raw_input("Appuyez sur [ENTRER]")
    True

clear()
print "La tonalité retentit quelques secondes et s'arrête."
print "Une voix grave & mystérieuse résonne dans le combiné."
print "RENDEZ-VOUS AU 1367 BOULEVARD BROOK, vous n'avez plus beaucoup de temps"
print "JE RÉPÈTE, 1367 BOULEVARD BROOK [Clack]"
print "Sans que vous n'ayez même eu le temps placer un mot,"
print "la ligne fut coupée."
print "[...]"
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Vous sortez de la cabine."
print "Sans savoir dans quelle direction aller, vous vous remettez en route. "
print "Vous tournez à droite à une intersection, puis à gauche."
print "Vous apercevez un garage automobile "
print "Vous entrez."
print
print "À l'accueil vous demandez où se situe le boulevard Brook."
print "On vous explique qu'il est à l'autre bout de la ville."
print
raw_input("Appuyez sur [ENTRER]")
clear()
print
print "Vous ressortez du magasin."
print "À votre surprise, il fait maintenant nuit.."
print "Les bâtiments sont illuminés de partout."
print "En face du garage, vous apercevez un vélo accoté sur un arbre et à votre gauche,"
print "une rutilante Porsche blanche, les phares allumés, mais sans conducteur."
print
print "Sachant qu'il vous faut vous dépêcher, et qu'à pied, vous n'avez aucune chance"
print "d'arriver à temps, vous prenez la décision (bien que très peu légale) "
print "de commettre un vol."
print
print "Vous regardez autour de vous, il n'y a personne. "
print "Quel véhicule choisir ?"
auto=raw_input("La voiture [a] ou la bicyclette [b]")
if auto=="a":
    clear()
    print "Tant qu'à voler, vous voler la Porsche."
    True
else :
    clear()
    print "Vous vous dirigez vers le vélo."
    print "Mais à votre surprise il est cadenassé à l'arbre."
    print "Toutefois, la chaine est très mince, elle pourrait"
    print "Probablement être brisée en tirant fort sur le vélo."
    velo=raw_input("Voulez-vous essayer ? OUI[a] NON[b]")
    if velo=="a":
        clear()
        print "Vous tirrez d'un coup sec, mais sans succès."
        print "Vous réessayez une seconde fois. Toujours pas."
        print "Alors que vous retentez une 3e fois, une voiture de police"
        print "passe dans la rue."
        print
        print "Vous voyez du coin de l'oeil les lumières rouges & bleues."
        print "Effrayé, vous vous mettez à courir dans la direction opposée."
        print "La voiture de police vous pourchasse."
        print
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Vous regardez derrière vous tout en courant droit devant, mais "
        print "vous trébuchez dans un sac de poubelles oublié sur le trottoir."
        print "Vous tombez face première dans la rue."
        print
        print "À l'instant même une voiture grise tourne le coin."
        print "Tout se passe très rapidement:"
        print "Les phares de la voiture vous aveuglent,"
        print "Vous entendez les crissements des pneus, mais il est déjà trop tard."
        print
        raw_input("Appuyez sur [ENTRER]")
        clear()
        print "Le véhicule vous percute avant que vous n'ayez pu vous relever."
        print "Vous vous retrouvez projeté sur le trottoir, votre tête se"
        print "cogne sur la bordure. Vous perdez connaissance."
        print
        print '\033[0;31m [VOUS ÊTES MORT.]\033[1;m'
        print '\033[0;31m [MALGRÉ LA VOITURE DE POLICE DÉJÀ PRÉSENTE\033[1;m'
        print '\033[0;31m SUR PLACE, LES SECOURS MÉDICAUX NE SONT PAS\033[1;m'
        print '\033[0;31m ARRIVÉS À TEMPS.]\033[1;m'
        import sys
        sys.exit("\033[0;31m [PARTIE TERMINÉE]\033[1;m")
    else:
        clear()
        print "Vous retournez donc vers la Porsche."
        True
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Après un dernier coup d'oeil périphérique, vous vous asseyez "
print "derrière le volant. Le moteur tourne déjà."
print
print "Vous ne perdez pas de temps. Vous vous apprêtez à quitter le stationnement."
print "Au même moment, une voiture de police tourne le coin."
print "Vous paniquez légèrement, mais la voiture continue son chemin sans s'arrêter."
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Vous quittez la cour en vitesse."
print "Après quelques coins de rue, vous arrêtez en bordure de route."
print "Vous respirez un bon coup pour évacuer votre stress."
print "Vous analysez quelques secondes le tableau de bord."
print
print "Il y a une fonction GPS :"
print "Vous entrez l'adresse."
print "[DÉMARRAGE DE L'ITINÉRAIRE.]"
print "Vous repartez."
print
print "Votre automobile file à toute allure dans les rues de la métropole."
print "Les rues sont désormais vides pour la plupart."
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Alors que le GPS vous indique votre arrivée dans 2 minutes."
print "Vous apercevez dans votre rétroviseur, des lumières rouges & bleues"
print "Vous enfoncez l'accélérateur."
print "La sirène se fait entendre, mais vous ne vous arrêtez toujours pas."
print "D'autres véhicules se joignent la poursuite."
print "Vous tournez brusquement à gauche, puis encore à gauche."
print "Vous continuez 500 mètres tout droit."
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "[VOTRE DESTINATION SE TROUVE SUR VOTRE DROITE]"
print "Vous freinez brusquement devant un très grand immeuble effilé."
print "Sur la façade est écrit '1367 BROOK'S BOULLEVARD'. "
print
print "Vous descendez de votre véhicule alors que les policiers"
print "freinent à leurs tours quelques mètres derrière."
print "Sans réfléchir, vous courrez vers la grande porte vitrée de la tour."
print "Les policiers vous suivent, groupés, leur arme à la main."
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "À l'instant où vous pénétrez dans le hall, les portes dorées"
print "d'un ascenseur s'ouvrent devant vous. Vous y entrez. "
print "Au même moment les policiers pénêtrent dans l’immeuble."
print "Ceux-ci tentent de vous atteindre."
print "Ils courent dans votre direction..."
print "Cependant, les portes de l'ascenseur se ferment"
print "et vous montez..."
raw_input("Appuyez sur [ENTRER]")
clear()
print "L'ascenseur s'arrête brusquement, vous perdez pied."
print "Les portes restent fermées."
print "Vous avez le choix :"
print "> Patienter tranquillement (en comptant le nombre de carreaux sur le tapis) [a]"
print "> Vous acharner sur le tableau de commande (frappez dessus...) [b] "
asc=raw_input("Que faire ? : ")
if asc=="b":
    clear()
    print "Vous lacez de toutes vos forces un coup de poing sur le tableau de bord"
    print "Un bouton s'enfonce, mais aucun changement."
    print "Vous frappez une seconde fois, mais cette fois-ci avec votre pied."
    print "Les lumières s'éteignent subitement."
    print "Quelques étincelles vous éclairent toujours, mais ça ne dure pas."
    print "Vous êtes plongé dans le noir total."
    print "(EUH BRA-VO ! 'bruits d'applaudissement sarcastiques')"
    print "Vous criez à l'aide, mais personne ne vous entend"
    print "Vous vous asseyez en boule par terre"
    print "Tout ce qu'il vous reste à faire c'est d'attendre."
    print "[...]"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "[...]"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print
    print "[...]"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous ne savez pas depuis combien de temps vous êtes là."
    print "Vous commencez à trouver cela vraiment long."
    print "D'autant plus que vous êtes fatigué."
    print "Vous décidez d'essayer de dormir en attendant les secours."
    print "zzz"
    print "[...]"
    print
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "[...]"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print
    print "[...]"
    print
    raw_input("Appuyez sur [ENTRER]")
    clear()
    print "Vous vous réveillez après plusieurs heures."
    print "Vous êtes toujours dans l'ascenseur. Vous avez faim."
    print "Votre dos vous fait mal et il fait chaud."
    print "Vous criez encore, mais vous ne recevez aucune réponse"
    print "C'est peine perdue..."
    print
    print "[...]"
    print '\033[0;31m [VOUS MOURREZ DE SOIF]\033[1;m'
    print '\033[0;31m [MÊME APRÈS 3 JOURS, \033[1;m'
    print "\033[0;31m PERSONNE N'EST VENU VOUS CHERCHER...]\033[1;m"
    import sys
    sys.exit("\033[0;31m [PARTIE TERMINÉE]\033[1;m")
else :
    True
clear()
print "Vous gardez votre sang-froid et patientez gentiment dans l'ascenseur."
print "Vous criez à l'aide de temps en temps, mais, aucune réponse."
print "Après environ une heure (du moins selon vous)"
print "Vous apercevez un petit panneau sur le plafond"
print "Vous tentez de l'atteindre en grimpant sur la rampe"
print "qui fait le tour de l'ascenseur."
print
print "C'est un échec..."
print
print
raw_input("Appuyez sur [ENTRER]")
clear()
print "Vous commencez à perdre espoir quand vous entendez un bruit."
print "Le plancher vibre légèrement, les boutons du panneau"
print "de contrôle se rallument et l'ascenseur recommence son ascension."
print "C'EST UN MIRACLE !!"
print "Vous montez quelques secondes, puis l'ascenseur s'arrête."
print "Cette fois-ci par contre elle le fait de façon plus normale."
print "[Ping!] [100e ÉTAGE]"
print "Les portes coulissantes s'ouvrent doucement..."

#
print
print '\033[0;32m Le jeu est toujours en conception, revenez bientôt ! \033[1;m'

# >>> $ python -m py_compile script.py
# >>> 60% for printing accuracy
