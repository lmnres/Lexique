# Database : Lexique382
import os
import os.path as op
import pandas as pd

text_input = "le cinéma a changé depuis que les acteurs ont montré leurs convictions sur les droits de la femme et l'égalité homme femme"
text_output = []

LEXIQUE = op.join(os.getenv('HOME'), "/Users/mouneyres/Desktop/Lexique/Lexique383/Lexique383.tsv")
lex = pd.read_csv(LEXIQUE, sep="\t")

for word in text_input.split():
    if lex['ortho'].str.contains(word).any():
        data_row = lex.loc[(lex.ortho == word)]
        if (data_row.iloc[0]["genre"] == "m") and (data_row.iloc[0]["nombre"] == "p") and (data_row.iloc[0]["cgram"]=="NOM"):
            lemme = data_row.iloc[0]["lemme"]
            text_output.append(word)
            complementaire = lex.loc[(lex.lemme == lemme) & (lex.genre == "f") & (lex.nombre == "p")]
            try :
                text_output.append("et " + complementaire.iloc[0]["ortho"])
            except:
                pass
        elif (data_row.iloc[0]["genre"] == "f") and (data_row.iloc[0]["nombre"] == "p") and (data_row.iloc[0]["cgram"]=="NOM"):
            lemme = data_row.iloc[0]["lemme"]
            text_output.append(word)
            complementaire = lex.loc[(lex.lemme == lemme) & (lex.genre == "m") & (lex.nombre == "p")]
            try:
                text_output.append("et " + complementaire.iloc[0]["ortho"])
            except:
                pass
        else:
            text_output.append(word)
    else:
        text_output.append(word)
# Conditions homme femme replacé par femmme homme
    for i in range(len(text_output)-1):
        if text_output[i] == "homme" and text_output[i+1] == "femme":
            text_output[i]="femme"
            text_output[i+1]="homme"
        # remplace l'homme par l'humain
        if (text_output[i]== "l'homme" or text_output[i]== "l'Homme" or text_output[i]== "L'Homme" or text_output[i]== "L'homme"):
            text_output[i]="l'humain"

print(text_output)



