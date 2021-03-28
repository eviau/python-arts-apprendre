import os

if __name__ == "__main__":
    sourcedir = "projets"
    destdir = "html/"
    files = [f for f in os.listdir(sourcedir) if os.path.isfile(os.path.join(sourcedir,f))]
    for f in files:
        with open( destdir + f[0:-4] + ".html", "w") as projet:
            with open("preambule.txt", "r") as preambule:
                row = preambule.readline()
                while (len(row) >0):
                    print(row, file=projet, end='')
                    row = preambule.readline()

            with open(sourcedir+ "/" + f, "r") as contenu:
                row = contenu.readline()
                while (len(row) >0):
                    print(row, file=projet, end='')
                    row = contenu.readline()

            with open("fin.txt", "r") as end:
                row = end.readline()
                while (len(row) >0):
                    print(row, file=projet, end='')
                    row = end.readline()
