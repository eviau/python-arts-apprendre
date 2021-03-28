# Générer un site web personnel avec Python

Si vous connaissez déjà le HTML et Python, vous pouvez apprendre à générer votre propre site web personnel avec Python - et ce, sans framework ! 

**Attention**: cette façon de faire est adaptée pour de petits sites statiques, et n'est pas testée ou recommandée pour des sites non-artisanaux. Le but de cet atelier est de démontrer l'idée générale derrière une technique spécifique de génération de fichiers.

## Les bases du HTML

Si vous ne savez pas le HTML, sachez que toute l'information pour bien débuter est disponible sur le site du Mozilla Developer Network, en français: [lien vers Mozilla Developer Network, page Les bases du HTML](https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/HTML_basics).

Nous allons utiliser le fichier HTML qui est rédigé dans le tutoriel de Mozilla, que vous pouvez visualiser ici: [lien vers la page HTML obtenue par le tutorial de Mozilla](https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/HTML_basics).

Vous trouverez une copie de ce fichier HTML dans le dépôt que vous êtes en train de consulter: [lien vers le fichier HTML dans le dépôt de cet atelier](lien).

## Étapes de l'atelier

Dans cet atelier, nous allons:

* Séparer le contenu du fichier `index.html` en trois partie: le préambule, le contenu et la fermeture du fichier
* Rédiger plusieurs fichiers textes avec le contenu souhaité
* Programmer un script Python pour assembler les pages finales, générées à partir de la combinaison du préambule, des contenus et des balises de fermeture du fichier

## Séparation du fichier `index.html`

Le fichier `index.html` situé dans le dossier `00_debut` est structuré par trois balises principales: les balises `<html>, <head>` et `<body>`. Celles-ci apparaissent dans l'ordre suivant:

    <html>
    
        <head>
        ....
        </head>
       
        <body>
        ....
        </body>
        
   </html>

Ainsi, les balises `<head>` et `<body>` sont imbriquées dans la balise `<html>`.

### Création de `preambule.txt`

Pour séparer le contenu de `index.html` de façon à pouvoir le réutiliser plus tard, nous allons placer l'entièreté du contenu de la balise ouvrante `<html>` à la balise ouvrante `<body>` dans un fichier texte à part, nommé `preambule.txt`.

### Création de `fermeture.txt`

Ensuite, nous placerons la fin du fichier `index.html`, soit le contenu de la balies `</body>` à la balise </html> dans un fichier texte à part, nommé `fermeture.txt`.

Vous trouverez ces deux fichiers dans le dossier `01_separation_contenu`.
  
### Et le contenu ?

Nous allons oublier le contenu issu de l'atelier de départ pour le moment. La prochaine section portera sur la création de nouveau contenu.

## Rédaction de nouveau contenu

Supposons que nous souhaitons réaliser un site organisé de façon à ce que chaque page du site corresponde à la description d'un seul projet artistique.

Dans la partie deux de cet atelier, nous allons expliquer comment générer chacune de ces pages à partir d'un fichier `.csv` contenant l'information souhaitée. Pour le moment, j'ai rédigé pour vous trois descriptions de trois projets artistiques fictifs, situé dans le dossier `02_redaction_contenu`.

Notez que j'ai sauvegardé les fichiers en format `.txt`, et que j'ai inclu les balies HTML nécessaires.

## ÉCriture d'un script Python pour assembler les pages des projets

Maintenant que j'ai tous les ingrédients pour le script, programmons-le ensemble !

L'idée du script est d'utiliser les différents fichiers textes comme morceaux à assembler dans des pages nouvellement créées, intitulées `projeta.html`, `projetb.html`, `projetc.html`.

Vous trouverez le script final dans `03_programmer_script_py`, sous le nom de `assemblage.py`. Notez que j'ai copié tous les fichiers nécessaires à `assemblage.py` dans le dossier parent. 

### Explications du script

Regardons ligne par ligne ce qui se passe dans le script...

Au début, nous importons le module `os`, qui nous permettra de naviguer au travers les dossiers situés sur notre ordinateur:

    import os

Le programme principal suit. Les lignes de code suivant le `if __name__ == "__main__"` seront exécutées si le fichier `assemblage.py` est appelé à partir de la ligne de commande.

    if __name__ == "__main__":
    
Nous allons définir deux variables pour garder en mémoire l'endroit où sont situés les fichiers qui serviront à l'assemblage, ainsi que pour indiquer au script à quel endroit nous voulons enregistrer les fichiers obtenus.

        sourcedir = "projets"
        destdir = "html/"

Nous allons créer une liste nommée `files` contenant les chemins pour se rendre aux fichiers inclus dans le dossier `sourcedir`.

        files = [f for f in os.listdir(sourcedir) if os.path.isfile(os.path.join(sourcedir,f))]

Commençons l'assemblage ! Pour chaque fichier dans le dossier `sourcedir`...

        for f in files:
        
Nous allons créer avec des droits d'écriture ( l'option "w" pour *write* ) des fichiers HTML ayant le même nom que le fichier où est enregistré le contenu. C'est-à-dire que la page `projeta.txt` sera assemblée en la page `projeta.html`.

            with open( destdir + f[0:-4] + ".html", "w") as projet:

Première étape de l'assemblage: lire le contenu de `preambule.txt` et copier son contenu, ligne par ligne, dans le nouveau fichier HTML que nous venons de créer.

Nous commençons par ouvrir le fichier `preambule.txt` avec des droits d'écriture ( l'options "r" pour *read* ):

                with open("preambule.txt", "r") as preambule:

Dans `row`, nous allons enregistrer la première ligne du fichier:

                    row = preambule.readline()

Nous allons maintenant boucler sur le fichier, ligne par ligne.

Nous commençons par vérifier que la ligne `row` contient quelque chose:

                    while (len(row) >0):
                    
Comme cette ligne est valide, nous allons l'imprimer dans le fichier `projet` défini ci-haut:

                        print(row, file=projet, end='')

Puis, nous passons à la ligne suivante et recommençons, c'est-à-dire que nous allons de nouveau vérifier si la ligne contient quelque chose, l'imprimer dans `projet` si c'est le cas, et passer à la ligne suivante, puis recommencer...

                        row = preambule.readline()

Le principe pour le contenu est le même. Notez que nous avons toujours le fichier `projet` ouvert en mode écriture. 

Nous lisons le fichier source dans `contenu`, puis nous allons itérer sur les lignes du fichier afin d'en copier chaque ligne et de les imprimer une à la fois dans `projet`.

                with open(sourcedir+ "/" + f, "r") as contenu:
                    row = contenu.readline()
                    while (len(row) >0):
                        print(row, file=projet, end='')
                        row = contenu.readline()

Puis, nous réalisons le même manège pour le fichier `fin.txt`

                with open("fin.txt", "r") as end:
                    row = end.readline()
                    while (len(row) >0):
                        print(row, file=projet, end='')
                        row = end.readline()

## Exécution du script

Pour exécuter le script, naviguez dans une fenêtre Terminal jusqu'au dossier `03_programmer_script_py` puis exécutez la ligne de commande suivante:

    python3 assemblage.py

Les fichiers HTML résultants seront dans le dossier `html/`. Vous pouvez les visualiser dans un navigateur web de votre choix.

## Exercice

Pouvez-vous réaliser une fonction d'ordre général, qui reprend les trois instructions de copie et d'écriture et peut s'exécuter sur n'importe quel duo de fichier ?


