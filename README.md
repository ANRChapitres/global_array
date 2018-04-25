# global_array
Tableau global de stats sur le corpus (soit à utiliser via jupyter notebook, soit faire la commande suivante (depuis le dossier où se trouve le script) :
	python3 global_table.py --dir 'chemin/vers/le/dossier/source/de/fichiers/taggés/' --csv 		'chemin/vers/le/dossier/pour/le/csv/')

## Légende pour chaque colonne :

ref : la référence du fichier dans le dossier<lb>
title : le titre
author : l'auteur
date : la date
canon_degree : canonique ou non (to do)

### Pour les calculs sur l'ensemble de l'oeuvre :
glob_words : nombre de mots dans l'ensemble de l'oeuvre
glob_book : nombre de livres dans l'oeuvre
glob_part : nombre de parties dans l'oeuvre
glob_chapter : nombre de chapitres dans l'oeuvre
glob_paragraph : nombre de paragraphes dans l'oeuvre
glob_sentence : nombre de phrases dans l'oeuvre
glob_av_word_per_sent : nombre de mots moyen par phrase dans l'oeuvre
glob_verb : nombre de verbes dans l'oeuvre
glob_adverb : nombre d'adverbes dans l'oeuvre
glob_adj : nombre d'adjectifs dans l'oeuvre
glob_coord : nombre de coordinations dans l'oeuvre
glob_sub : nombre de subordinations dans l'oeuvre
glob_il : nombre de formes "il" dans l'oeuvre
glob_ils : nombre de formes "ils" dans l'oeuvre
glob_elle : nombre de formes "elle" dans l'oeuvre
glob_elles : nombre de formes "elles" dans l'oeuvre
glob_je : nombre de formes "je" dans l'oeuvre
glob_nous : nombre de formes "nous" dans l'oeuvre
glob_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester)
glob_voc : variété du vocabulaire (combien de lemmes différents) pour toute l'oeuvre

### Pour les calculs sur le premier chapitre :
first_words : nombre de mots dans le premier chapitre
first_paragraph : nombre de paragraphes dans le premier chapitre
first_sentence : nombre de phrases dans le premier chapitre
first_av_word_per_sent : nombre de mots moyen par phrase dans le premier chapitre
first_verb : nombre de verbes dans le premier chapitre
first_adverb : nombre d'adverbes dans le premier chapitre
first_adj : nombre d'adjectifs dans le premier chapitre
first_coord : nombre de coordinations dans le premier chapitre
first_sub : nombre de subordinations dans le premier chapitre
first_il : nombre de formes "il" dans le premier chapitre
first_ils : nombre de formes "ils" dans le premier chapitre
first_elle : nombre de formes "elle" dans le premier chapitre
first_elles : nombre de formes "elles" dans le premier chapitre
first_je : nombre de formes "je" dans le premier chapitre
first_nous : nombre de formes "nous" dans le premier chapitre
first_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester) dans le premier chapitre
first_voc : variété du vocabulaire (combien de lemmes différents) dans le premier chapitre

### Pour les calculs sur les 10 premiers % :
first_ten_words : nombre de mots dans les premiers 10% des mots
first_ten_sentence : nombre de phrases dans les premiers 10% des mots
first_ten_av_word_per_sent : nombre de mots moyen par phrase dans les premiers 10% des mots
first_ten_verb : nombre de verbes dans les premiers 10% des mots
first_ten_adverb : nombre d'adverbes dans les premiers 10% des mots
first_ten_adj : nombre d'adjectifs dans les premiers 10% des mots
first_ten_coord : nombre de coordinations dans les premiers 10% des mots
first_ten_sub : nombre de subordinations dans les premiers 10% des mots
first_ten_il : nombre de formes "il" dans les premiers 10% des mots
first_ten_ils : nombre de formes "ils" dans les premiers 10% des mots
first_ten_elle : nombre de formes "elle" dans les premiers 10% des mots
first_ten_elles : nombre de formes "elles" dans les premiers 10% des mots
first_ten_je : nombre de formes "je" dans les premiers 10% des mots
first_ten_nous : nombre de formes "nous" dans les premiers 10% des mots
first_ten_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester) dans les premiers 10% des mots
first_ten_voc : variété du vocabulaire (combien de lemmes différents) dans les premiers 10% des mots

### Pour les calculs sur le chapitre du milieu :
mid_words : nombre de mots dans le chapitre du milieu
mid_paragraph : nombre de paragraphes dans le chapitre du milieu
mid_sentence : nombre de phrases dans le chapitre du milieu
mid_av_word_per_sent : nombre de mots moyen par phrase dans le chapitre du milieu
mid_verb : nombre de verbes dans le chapitre du milieu
mid_adverb : nombre d'adverbes dans le chapitre du milieu
mid_adj : nombre d'adjectifs dans le chapitre du milieu
mid_coord : nombre de coordinations dans le chapitre du milieu
mid_sub : nombre de subordinations dans le chapitre du milieu
mid_il : nombre de formes "il" dans le chapitre du milieu
mid_ils : nombre de formes "ils" dans le chapitre du milieu
mid_elle : nombre de formes "elle" dans le chapitre du milieu
mid_elles : nombre de formes "elles" dans le chapitre du milieu
mid_je : nombre de formes "je" dans le chapitre du milieu
mid_nous : nombre de formes "nous" dans le chapitre du milieu
mid_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester) dans le chapitre du milieu
mid_voc : variété du vocabulaire (combien de lemmes différents) dans le chapitre du milieu

### Pour les calculs sur le dernier chapitre :
last_words : nombre de mots dans le dernier chapitre
last_paragraph : nombre de paragraphes dans le dernier chapitre
last_sentence : nombre de phrases dans le dernier chapitre
last_av_word_per_sent : nombre de mots moyen par phrase dans le dernier chapitre
last_verb : nombre de verbes dans le dernier chapitre
last_adverb : nombre d'adverbes dans le dernier chapitre
last_adj : nombre d'adjectifs dans le dernier chapitre
last_coord : nombre de coordinations dans le dernier chapitre
last_sub : nombre de subordinations dans le dernier chapitre
last_il : nombre de formes "il" dans le dernier chapitre
last_ils : nombre de formes "ils" dans le dernier chapitre
last_elle : nombre de formes "elle" dans le dernier chapitre
last_elles : nombre de formes "elles" dans le dernier chapitre
last_je : nombre de formes "je" dans le dernier chapitre
last_nous : nombre de formes "nous" dans le dernier chapitre
last_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester) dans le dernier chapitre
last_voc : variété du vocabulaire (combien de lemmes différents) dans le dernier chapitre

### Pour les calculs sur les 10 derniers % :
last_ten_words : nombre de mots dans les derniers 10% des mots
last_ten_sentence : nombre de phrases dans les derniers 10% des mots
last_ten_av_word_per_sent : nombre de mots moyen par phrase dans les derniers 10% des mots
last_ten_verb : nombre de verbes dans les derniers 10% des mots
last_ten_adverb : nombre d'adverbes dans les derniers 10% des mots
last_ten_adj : nombre d'adjectifs dans les derniers 10% des mots
last_ten_coord : nombre de coordinations dans les derniers 10% des mots
last_ten_sub : nombre de subordinations dans les derniers 10% des mots
last_ten_il : nombre de formes "il" dans les derniers 10% des mots
last_ten_ils : nombre de formes "ils" dans les derniers 10% des mots
last_ten_elle : nombre de formes "elle" dans les derniers 10% des mots
last_ten_elles : nombre de formes "elles" dans les derniers 10% des mots
last_ten_je : nombre de formes "je" dans les derniers 10% des mots
last_ten_nous : nombre de formes "nous" dans les derniers 10% des mots
last_ten_etat : nombre de verbes d'état (être, sembler, devenir, demeurer, rester) dans les derniers 10% des mots
last_ten_voc : variété du vocabulaire (combien de lemmes différents) dans les derniers 10% des mots
