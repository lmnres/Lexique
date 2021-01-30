
# ! /usr/bin/env python
# Time-stamp: <2020-02-07 10:38:09 christophe@pallier.org>

""" Exemple de selection d'items dans la base Lexique382 """

import os
import os.path as op
import pandas as pd
import csv

text_input = "Les coiffeurs ont coupé les cheveux des clients"
text_output = "Les coiffeurs et coiffeuses ont coupé les cheveux des client-es "

LEXIQUE = op.join(os.getenv('HOME'), "/Users/mouneyres/Desktop/Lexique/Lexique383/Lexique383.tsv")
lex = pd.read_csv(LEXIQUE, sep="\t")

#print(lex.loc[(lex.ortho == "coiffeurs")])

# for word in text_input.split():
#     if lex['ortho'].str.contains(word).any():
#         ligne = lex.index[(lex.ortho == word)].tolist()
#         data_row = lex.loc[(lex.ortho == word)]
#
#         print(ligne)

for word in text_input.split():
    if lex['ortho'].str.contains(word).any():
        data_row = lex.loc[(lex.ortho == word)]
        if (data_row.iloc[0]["genre"] == "m") and (data_row.iloc[0]["nombre"] == "p"):
            lemme = data_row.iloc[0]["lemme"]
            print(word)
            complementaire = lex.loc[(lex.lemme == lemme) & (lex.genre == "f") & (lex.nombre == "p")]
            try :
                print(complementaire.iloc[0]["ortho"])
            except:
                pass

        elif (data_row.iloc[0]["genre"] == "f") and (data_row.iloc[0]["nombre"] == "p"):
            print(word)
        else:
            print(word)
    else:
        print(word)



