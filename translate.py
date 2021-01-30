
# ! /usr/bin/env python
# Time-stamp: <2020-02-07 10:38:09 christophe@pallier.org>

""" Exemple de selection d'items dans la base Lexique382 """

import os
import os.path as op
import pandas as pd

text_input = " Les coiffeurs ont coupé les cheveux des clients"
text_output = ""

# location of Lexique383.tsv file (adapt to your case!)
LEXIQUE = op.join(os.getenv('HOME'), "/Users/mouneyres/Desktop/Lexique/Lexique383/Lexique383.tsv")

lex = pd.read_csv(LEXIQUE, sep="\t")

lex.head()

# restreint la recherche à des mots de longueur comprises entre 5 et 8 lettres
#subset = lex.loc[(lex.nblettres >= 5) & (lex.nblettres <= 8)]

# separe les noms et les verbes dans deux dataframes:
#noms = subset.loc[subset.cgram == 'NOM']
#verbs = subset.loc[subset.cgram == 'VER']

# sectionne sur la bases de la fréquence lexicale
#noms_hi = noms.loc[noms.freqlivres > 50.0]
#noms_low = noms.loc[(noms.freqlivres < 10.0) & (noms.freqlivres > 1.0)]

#verbs_hi = verbs.loc[verbs.freqlivres > 50.0]
#verbs_low = verbs.loc[(verbs.freqlivres < 10.0) & (verbs.freqlivres > 1.0)]

for word in text_input.split():
    #subset_word = lex.loc[(lex.ortho == word)]
    #subset_word.lemme.to_csv('text_output.txt', index=False)
    subset_word = (lex.loc[(lex.ortho == word)]).lemme
    print(subset_word)



    #lemme = lex.loc[lex.lemme == str(subset_word.lemme) ]
    #print(lemme)
    #if subset_word :
        #if subset_word.genre == "m" & subset_word.nombre == "p" :
            #supplement = lex.loc(lex.ortho == word)
