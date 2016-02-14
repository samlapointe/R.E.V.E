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
    print "ca fonctionne"
else:
    print "Tu a fais une erreur, il faudra faire attention"
    print "une fois dans le reve sa pourrait te tuer !"
print "Je crois que tu est pres on entre dans le reve ?"
play=raw_input("Oui: apuyez sur [a] - Non: apuyez sur [b] : ")
if play=="a":
    clear()
    print "C'est parti !"
else:
    clear()
    print "On a plus le temps de parler, de toutes facon tu ne peux plus reculer"
    print "C'est parti !"
