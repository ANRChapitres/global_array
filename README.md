# global_array
Tableau global de stats sur le corpus, soit via jupyter notebook, soit via la commande suivante (depuis le dossier où se trouve le script) : </br></br>
```python3 global_table.py --dir 'chemin/vers/le/dossier/source/de/fichiers/taggés/' --csv 'chemin/vers/le/dossier/pour/le/csv/'```

## Légende pour chaque colonne :

ref : la référence du fichier dans le dossier</br>
title : le titre</br>
author : l'auteur</br>
date : la date</br>
canon_degree : canonique ou non (to do)</br>

### Pour les calculs sur l'ensemble de l'oeuvre :
glob_words : nombre de mots dans l'ensemble de l'oeuvre</br>
glob_book : nombre de livres dans l'oeuvre</br>
glob_part : nombre de parties dans l'oeuvre</br>
glob_chapter : nombre de chapitres dans l'oeuvre</br>
glob_paragraph : nombre de paragraphes dans l'oeuvre</br>
glob_sentence : nombre de phrases dans l'oeuvre</br>
glob_av_word_per_sent : nombre de mots moyen par phrase dans l'oeuvre</br>
glob_verb : nombre de verbes dans l'oeuvre</br>
glob_adverb : nombre d'adverbes dans l'oeuvre</br>
glob_adj : nombre d'adjectifs dans l'oeuvre</br>
glob_coord : nombre de coordinations dans l'oeuvre</br>
glob_sub : nombre de subordinations dans l'oeuvre</br>
glob_il : nombre de formes "il" dans l'oeuvre</br>
glob_ils : nombre de formes "ils" dans l'oeuvre</br>
glob_elle : nombre de formes "elle" dans l'oeuvre</br>
glob_elles : nombre de formes "elles" dans l'oeuvre</br>
glob_je : nombre de formes "je" dans l'oeuvre</br>
glob_nous : nombre de formes "nous" dans l'oeuvre</br>
glob_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester)</br>
glob_voc : variété du vocabulaire (combien de lemmes différents) pour toute l'oeuvre</br>

### Pour les calculs sur le premier chapitre :
first_words : nombre de mots dans le premier chapitre</br>
first_paragraph : nombre de paragraphes dans le premier chapitre</br>
first_sentence : nombre de phrases dans le premier chapitre</br>
first_av_word_per_sent : nombre de mots moyen par phrase dans le premier chapitre</br>
first_verb : nombre de verbes dans le premier chapitre</br>
first_adverb : nombre d'adverbes dans le premier chapitre</br>
first_adj : nombre d'adjectifs dans le premier chapitre</br>
first_coord : nombre de coordinations dans le premier chapitre</br>
first_sub : nombre de subordinations dans le premier chapitre</br>
first_il : nombre de formes "il" dans le premier chapitre</br>
first_ils : nombre de formes "ils" dans le premier chapitre</br>
first_elle : nombre de formes "elle" dans le premier chapitre</br>
first_elles : nombre de formes "elles" dans le premier chapitre</br>
first_je : nombre de formes "je" dans le premier chapitre</br>
first_nous : nombre de formes "nous" dans le premier chapitre</br>
first_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester) dans le premier chapitre</br>
first_voc : variété du vocabulaire (combien de lemmes différents) dans le premier chapitre</br>

### Pour les calculs sur les 10 premiers % :
first_ten_words : nombre de mots dans les premiers 10% des mots</br>
first_ten_sentence : nombre de phrases dans les premiers 10% des mots</br>
first_ten_av_word_per_sent : nombre de mots moyen par phrase dans les premiers 10% des mots</br>
first_ten_verb : nombre de verbes dans les premiers 10% des mots</br>
first_ten_adverb : nombre d'adverbes dans les premiers 10% des mots</br>
first_ten_adj : nombre d'adjectifs dans les premiers 10% des mots</br>
first_ten_coord : nombre de coordinations dans les premiers 10% des mots</br>
first_ten_sub : nombre de subordinations dans les premiers 10% des mots</br>
first_ten_il : nombre de formes "il" dans les premiers 10% des mots</br>
first_ten_ils : nombre de formes "ils" dans les premiers 10% des mots</br>
first_ten_elle : nombre de formes "elle" dans les premiers 10% des mots</br>
first_ten_elles : nombre de formes "elles" dans les premiers 10% des mots</br>
first_ten_je : nombre de formes "je" dans les premiers 10% des mots</br>
first_ten_nous : nombre de formes "nous" dans les premiers 10% des mots</br>
first_ten_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester) dans les premiers 10% des mots</br>
first_ten_voc : variété du vocabulaire (combien de lemmes différents) dans les premiers 10% des mots</br>

### Pour les calculs sur le chapitre du milieu :
mid_words : nombre de mots dans le chapitre du milieu</br>
mid_paragraph : nombre de paragraphes dans le chapitre du milieu</br>
mid_sentence : nombre de phrases dans le chapitre du milieu</br>
mid_av_word_per_sent : nombre de mots moyen par phrase dans le chapitre du milieu</br>
mid_verb : nombre de verbes dans le chapitre du milieu</br>
mid_adverb : nombre d'adverbes dans le chapitre du milieu</br>
mid_adj : nombre d'adjectifs dans le chapitre du milieu</br>
mid_coord : nombre de coordinations dans le chapitre du milieu</br>
mid_sub : nombre de subordinations dans le chapitre du milieu</br>
mid_il : nombre de formes "il" dans le chapitre du milieu</br>
mid_ils : nombre de formes "ils" dans le chapitre du milieu</br>
mid_elle : nombre de formes "elle" dans le chapitre du milieu</br>
mid_elles : nombre de formes "elles" dans le chapitre du milieu</br>
mid_je : nombre de formes "je" dans le chapitre du milieu</br>
mid_nous : nombre de formes "nous" dans le chapitre du milieu</br>
mid_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester) dans le chapitre du milieu</br>
mid_voc : variété du vocabulaire (combien de lemmes différents) dans le chapitre du milieu</br>

### Pour les calculs sur le dernier chapitre :
last_words : nombre de mots dans le dernier chapitre</br>
last_paragraph : nombre de paragraphes dans le dernier chapitre</br>
last_sentence : nombre de phrases dans le dernier chapitre</br>
last_av_word_per_sent : nombre de mots moyen par phrase dans le dernier chapitre</br>
last_verb : nombre de verbes dans le dernier chapitre</br>
last_adverb : nombre d'adverbes dans le dernier chapitre</br>
last_adj : nombre d'adjectifs dans le dernier chapitre</br>
last_coord : nombre de coordinations dans le dernier chapitre</br>
last_sub : nombre de subordinations dans le dernier chapitre</br>
last_il : nombre de formes "il" dans le dernier chapitre</br>
last_ils : nombre de formes "ils" dans le dernier chapitre</br>
last_elle : nombre de formes "elle" dans le dernier chapitre</br>
last_elles : nombre de formes "elles" dans le dernier chapitre</br>
last_je : nombre de formes "je" dans le dernier chapitre</br>
last_nous : nombre de formes "nous" dans le dernier chapitre</br>
last_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester) dans le dernier chapitre</br>
last_voc : variété du vocabulaire (combien de lemmes différents) dans le dernier chapitre</br>

### Pour les calculs sur les 10 derniers % :
last_ten_words : nombre de mots dans les derniers 10% des mots</br>
last_ten_sentence : nombre de phrases dans les derniers 10% des mots</br>
last_ten_av_word_per_sent : nombre de mots moyen par phrase dans les derniers 10% des mots</br>
last_ten_verb : nombre de verbes dans les derniers 10% des mots</br>
last_ten_adverb : nombre d'adverbes dans les derniers 10% des mots</br>
last_ten_adj : nombre d'adjectifs dans les derniers 10% des mots</br>
last_ten_coord : nombre de coordinations dans les derniers 10% des mots</br>
last_ten_sub : nombre de subordinations dans les derniers 10% des mots</br>
last_ten_il : nombre de formes "il" dans les derniers 10% des mots</br>
last_ten_ils : nombre de formes "ils" dans les derniers 10% des mots</br>
last_ten_elle : nombre de formes "elle" dans les derniers 10% des mots</br>
last_ten_elles : nombre de formes "elles" dans les derniers 10% des mots</br>
last_ten_je : nombre de formes "je" dans les derniers 10% des mots</br>
last_ten_nous : nombre de formes "nous" dans les derniers 10% des mots</br>
last_ten_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester) dans les derniers 10% des mots</br>
last_ten_voc : variété du vocabulaire (combien de lemmes différents) dans les derniers 10% des mots
