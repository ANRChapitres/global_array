
# coding: utf-8
# author: odysseuspolymetis


import sys
import os
import os.path
import fnmatch
from lxml import etree
from collections import OrderedDict
import csv
import IPython
import argparse
import re
from copy import deepcopy


nums=['I ','V ','X ','C ','L ','I.','V.','X.','C.','L.','1','2','3','4','5','6','7','8','9','0']


print('This software generates a csv with basic statistics on a selected corpus \nusage: --dir path/to/your/source/dir --csv path/to/your/target/directory/for/csv')
parser = argparse.ArgumentParser()
parser.add_argument('--dir', help= '/your/directory/to/tagged/files/')
parser.add_argument('--csv', help= '/your/directory/to/your/csv/file/')
args = parser.parse_args()

if len(sys.argv) == 1:
    sys.exit()


argsdir= os.path.join(args.dir, '')
argscsv= os.path.join(args.csv, '')
files_list=fnmatch.filter(os.listdir(argsdir), '*.xml')

def average_words_chap (tree):
    average = 0
    words=list()
    if tree.findall(".//div[@type='chapter']"):
        for chapter in tree.findall(".//div[@type='chapter']"):
            numWords=len(chapter.findall(".//word"))
            words.append(numWords)
    
    average=sum(words)/len(words)
    return average

def average_words_sent(tree):
    average = 0
    indexes=list()
    for sent in tree.findall(".//word[@postag='PUNsent']"):
        indexes.append(sent.getparent().index(sent))
                #print(sent.getparent().index(sent))
    words_between=list()
    for idx, index in enumerate(indexes):
        if idx == 0:
            if len(indexes) == 1:
                words_between.append(index)
            elif len(indexes) > 1:
                words_between.append(indexes[idx+1]-index-1)
        elif idx < len(indexes)-1 :
            if index<indexes[idx+1]:
                words_between.append(indexes[idx+1]-index-1)
    if len(words_between) > 0:
        average = int(sum(words_between)/len(words_between))
    else :
        print("No sentence found in this section")
    return average

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

count_header=0
with open(argscsv+'rest.csv', 'w') as f:
    for file in files_list:
        print("File being processed : "+file)
        dic_stats=OrderedDict()
        tmpFile=file.replace("/",":")
        full_path=argsdir+tmpFile
        if os.path.isfile(full_path):
            tree=etree.parse(full_path)
            if tree.findall(".//div[@type='chapter']"):
                first_chap = tree.findall(".//div[@type='chapter']")[0]
                second_chap = tree.findall(".//div[@type='chapter']")[1]
                middle_chap = tree.findall(".//div[@type='chapter']")[int(len(tree.findall(".//div[@type='chapter']"))/2)]
                last_chap = tree.findall(".//div[@type='chapter']")[len(tree.findall(".//div[@type='chapter']"))-1]
            elif tree.findall(".//div[@type='book']"):
                first_chap = tree.findall(".//div[@type='book']")[0]
                second_chap = tree.findall(".//div[@type='book']")[1]
                middle_chap = tree.findall(".//div[@type='book']")[int(len(tree.findall(".//div[@type='book']"))/2)]
                last_chap = tree.findall(".//div[@type='book']")[len(tree.findall(".//div[@type='book']"))-1]
            elif tree.findall(".//div[@type='part']"):
                first_chap = tree.findall(".//div[@type='part']")[0]
                second_chap = tree.findall(".//div[@type='part']")[1]
                middle_chap = tree.findall(".//div[@type='part']")[int(len(tree.findall(".//div[@type='part']"))/2)]
                last_chap = tree.findall(".//div[@type='part']")[len(tree.findall(".//div[@type='part']"))-1]
            
            dic_stats['ref']=file
            dic_stats['title']=re.sub(u'\n','',tree.find(".//title").text).replace("     ","")
            dic_stats['author']=tree.find(".//author").attrib['name']
            dic_stats['date']=tree.find(".//date").attrib['when']
            if tree.find(".//profileDesc[@tag]"):
                dic_stats['canon_degree']=tree.find(".//profileDesc").attrib['tag']
            elif tree.find(".//profiledesc[@tag]"):
                dic_stats['canon_degree']=tree.find(".//profiledesc").attrib['tag']
            else:
                dic_stats['canon_degree']="non-canon"
            total_words = tree.findall(".//word")
            nb_words = len(total_words)
            dic_stats['glob_word']= nb_words
            first_ten = etree.Element("first")
            second_ten = etree.Element("second")
            third_ten = etree.Element("third")
            fourth_ten = etree.Element("fourth")
            fifth_ten = etree.Element("fifth")
            sixth_ten = etree.Element("sixth")
            seventh_ten = etree.Element("seventh")
            eigth_ten = etree.Element("eigth")
            ninth_ten = etree.Element("ninth")
            last_ten = etree.Element("tenth")
            
            percents=list(chunks(total_words,round(((10*nb_words)/100))))
            
            if len(percents)>10:
                percents[9].extend(percents[10])
                percents.pop(10)
            
            for word in percents[0]:
                first_ten.append(deepcopy(word))
            for word in percents[1]:
                second_ten.append(deepcopy(word))
            for word in percents[2]:
                third_ten.append(deepcopy(word))
            for word in percents[3]:
                fourth_ten.append(deepcopy(word))
            for word in percents[4]:
                fifth_ten.append(deepcopy(word))
            for word in percents[5]:
                sixth_ten.append(deepcopy(word))
            for word in percents[6]:
                seventh_ten.append(deepcopy(word))
            for word in percents[7]:
                eigth_ten.append(deepcopy(word))
            for word in percents[8]:
                ninth_ten.append(deepcopy(word))
            for word in percents[9]:
                last_ten.append(deepcopy(word))
            
            dic_stats['glob_book']=len(tree.findall(".//div[@type='book']"))
            dic_stats['glob_part']=len(tree.findall(".//div[@type='part']"))
            dic_stats['glob_chapter']=len(tree.findall(".//div[@type='chapter']"))
            dic_stats['glob_paragraph']=len(tree.findall(".//p"))
            dic_stats['glob_sentence']=len(tree.findall(".//word[@postag='PUNsent']"))
            dic_stats['glob_av_word_per_sent']= average_words_sent(tree)
            dic_stats['glob_av_word_per_chap']= average_words_chap(tree)
            dic_stats['glob_name']=len(set(tree.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['glob_verb']=len(tree.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['glob_adverb']=len(tree.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['glob_adj']=len(tree.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['glob_coord']=len(tree.findall(".//word[@postag='CONJcoord']"))
            dic_stats['glob_sub']=len(tree.findall(".//word[@postag='CONJsubord']"))
            dic_stats['glob_il']=len(tree.findall(".//word[@form='il']"))
            dic_stats['glob_ils']=len(tree.findall(".//word[@form='ils']"))
            dic_stats['glob_elle']=len(tree.findall(".//word[@form='elle']"))
            dic_stats['glob_elles']=len(tree.findall(".//word[@form='elles']"))
            dic_stats['glob_je']=len(tree.findall(".//word[@form='je']"))
            dic_stats['glob_nous']=len(tree.findall(".//word[@form='nous']"))
            dic_stats['glob_etat']=len(tree.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['glob_voc']=len(set(tree.xpath(".//word/@lemma")))
            
            dic_stats['first_word']=len(first_chap.findall(".//word"))
            dic_stats['first_paragraph']=len(first_chap.findall(".//p"))
            dic_stats['first_sentence']=len(first_chap.findall(".//word[@postag='PUNsent']"))
            dic_stats['first_av_word_per_sent']= average_words_sent(first_chap)
            dic_stats['first_name']=len(set(first_chap.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['first_verb']=len(first_chap.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['first_adverb']=len(first_chap.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['first_adj']=len(first_chap.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['first_coord']=len(first_chap.findall(".//word[@postag='CONJcoord']"))
            dic_stats['first_sub']=len(first_chap.findall(".//word[@postag='CONJsubord']"))
            dic_stats['first_il']=len(first_chap.findall(".//word[@form='il']"))
            dic_stats['first_ils']=len(first_chap.findall(".//word[@form='ils']"))
            dic_stats['first_elle']=len(first_chap.findall(".//word[@form='elle']"))
            dic_stats['first_elles']=len(first_chap.findall(".//word[@form='elles']"))
            dic_stats['first_je']=len(first_chap.findall(".//word[@form='je']"))
            dic_stats['first_nous']=len(first_chap.findall(".//word[@form='nous']"))
            dic_stats['first_etat']=len(first_chap.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['first_voc']=len(set(first_chap.xpath(".//word/@lemma")))

            dic_stats['second_word']=len(second_chap.findall(".//word"))
            dic_stats['second_paragraph']=len(second_chap.findall(".//p"))
            dic_stats['second_sentence']=len(second_chap.findall(".//word[@postag='PUNsent']"))
            dic_stats['second_av_word_per_sent']= average_words_sent(second_chap)
            dic_stats['second_name']=len(set(second_chap.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['second_verb']=len(second_chap.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['second_adverb']=len(second_chap.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['second_adj']=len(second_chap.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['second_coord']=len(second_chap.findall(".//word[@postag='CONJcoord']"))
            dic_stats['second_sub']=len(second_chap.findall(".//word[@postag='CONJsubord']"))
            dic_stats['second_il']=len(second_chap.findall(".//word[@form='il']"))
            dic_stats['second_ils']=len(second_chap.findall(".//word[@form='ils']"))
            dic_stats['second_elle']=len(second_chap.findall(".//word[@form='elle']"))
            dic_stats['second_elles']=len(second_chap.findall(".//word[@form='elles']"))
            dic_stats['second_je']=len(second_chap.findall(".//word[@form='je']"))
            dic_stats['second_nous']=len(second_chap.findall(".//word[@form='nous']"))
            dic_stats['second_etat']=len(second_chap.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['second_voc']=len(set(second_chap.xpath(".//word/@lemma")))
            
            dic_stats['1/10_words']=len(first_ten.findall(".//word"))
            dic_stats['1/10_sentence']=len(first_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['1/10_av_word_per_sent']= average_words_sent(first_ten)
            dic_stats['1/10_name']=len(set(first_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['1/10_verb']=len(first_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['1/10_adverb']=len(first_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['1/10_adj']=len(first_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['1/10_coord']=len(first_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['1/10_sub']=len(first_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['1/10_il']=len(first_ten.findall(".//word[@form='il']"))
            dic_stats['1/10_ils']=len(first_ten.findall(".//word[@form='ils']"))
            dic_stats['1/10_elle']=len(first_ten.findall(".//word[@form='elle']"))
            dic_stats['1/10_elles']=len(first_ten.findall(".//word[@form='elles']"))
            dic_stats['1/10_je']=len(first_ten.findall(".//word[@form='je']"))
            dic_stats['1/10_nous']=len(first_ten.findall(".//word[@form='nous']"))
            dic_stats['1/10_etat']=len(first_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['1/10_voc']=len(set(first_ten.xpath(".//word/@lemma")))
            
            dic_stats['2/10_word']=len(second_ten.findall(".//word"))
            dic_stats['2/10_sentence']=len(second_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['2/10_av_word_per_sent']= average_words_sent(second_ten)
            dic_stats['2/10_name']=len(set(second_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['2/10_verb']=len(second_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['2/10_adverb']=len(second_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['2/10_adj']=len(second_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['2/10_coord']=len(second_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['2/10_sub']=len(second_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['2/10_il']=len(second_ten.findall(".//word[@form='il']"))
            dic_stats['2/10_ils']=len(second_ten.findall(".//word[@form='ils']"))
            dic_stats['2/10_elle']=len(second_ten.findall(".//word[@form='elle']"))
            dic_stats['2/10_elles']=len(second_ten.findall(".//word[@form='elles']"))
            dic_stats['2/10_je']=len(second_ten.findall(".//word[@form='je']"))
            dic_stats['2/10_nous']=len(second_ten.findall(".//word[@form='nous']"))
            dic_stats['2/10_etat']=len(second_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['2/10_voc']=len(set(second_ten.xpath(".//word/@lemma")))
            
            dic_stats['3/10_word']=len(third_ten.findall(".//word"))
            dic_stats['3/10_sentence']=len(third_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['3/10_av_word_per_sent']= average_words_sent(third_ten)
            dic_stats['3/10_name']=len(set(third_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['3/10_verb']=len(third_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['3/10_adverb']=len(third_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['3/10_adj']=len(third_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['3/10_coord']=len(third_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['3/10_sub']=len(third_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['3/10_il']=len(third_ten.findall(".//word[@form='il']"))
            dic_stats['3/10_ils']=len(third_ten.findall(".//word[@form='ils']"))
            dic_stats['3/10_elle']=len(third_ten.findall(".//word[@form='elle']"))
            dic_stats['3/10_elles']=len(third_ten.findall(".//word[@form='elles']"))
            dic_stats['3/10_je']=len(third_ten.findall(".//word[@form='je']"))
            dic_stats['3/10_nous']=len(third_ten.findall(".//word[@form='nous']"))
            dic_stats['3/10_etat']=len(third_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['3/10_voc']=len(set(third_ten.xpath(".//word/@lemma")))
            
            dic_stats['4/10_word']=len(fourth_ten.findall(".//word"))
            dic_stats['4/10_sentence']=len(fourth_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['4/10_av_word_per_sent']= average_words_sent(fourth_ten)
            dic_stats['4/10_name']=len(set(fourth_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['4/10_verb']=len(fourth_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['4/10_adverb']=len(fourth_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['4/10_adj']=len(fourth_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['4/10_coord']=len(fourth_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['4/10_sub']=len(fourth_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['4/10_il']=len(fourth_ten.findall(".//word[@form='il']"))
            dic_stats['4/10_ils']=len(fourth_ten.findall(".//word[@form='ils']"))
            dic_stats['4/10_elle']=len(fourth_ten.findall(".//word[@form='elle']"))
            dic_stats['4/10_elles']=len(fourth_ten.findall(".//word[@form='elles']"))
            dic_stats['4/10_je']=len(fourth_ten.findall(".//word[@form='je']"))
            dic_stats['4/10_nous']=len(fourth_ten.findall(".//word[@form='nous']"))
            dic_stats['4/10_etat']=len(fourth_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['4/10_voc']=len(set(fourth_ten.xpath(".//word/@lemma")))
            
            dic_stats['5/10_word']=len(fifth_ten.findall(".//word"))
            dic_stats['5/10_sentence']=len(fifth_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['5/10_av_word_per_sent']= average_words_sent(fifth_ten)
            dic_stats['5/10_name']=len(set(fifth_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['5/10_verb']=len(fifth_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['5/10_adverb']=len(fifth_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['5/10_adj']=len(fifth_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['5/10_coord']=len(fifth_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['5/10_sub']=len(fifth_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['5/10_il']=len(fifth_ten.findall(".//word[@form='il']"))
            dic_stats['5/10_ils']=len(fifth_ten.findall(".//word[@form='ils']"))
            dic_stats['5/10_elle']=len(fifth_ten.findall(".//word[@form='elle']"))
            dic_stats['5/10_elles']=len(fifth_ten.findall(".//word[@form='elles']"))
            dic_stats['5/10_je']=len(fifth_ten.findall(".//word[@form='je']"))
            dic_stats['5/10_nous']=len(fifth_ten.findall(".//word[@form='nous']"))
            dic_stats['5/10_etat']=len(fifth_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['5/10_voc']=len(set(fifth_ten.xpath(".//word/@lemma")))
            
            dic_stats['6/10_word']=len(sixth_ten.findall(".//word"))
            dic_stats['6/10_sentence']=len(sixth_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['6/10_av_word_per_sent']= average_words_sent(sixth_ten)
            dic_stats['6/10_name']=len(set(sixth_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['6/10_verb']=len(sixth_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['6/10_adverb']=len(sixth_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['6/10_adj']=len(sixth_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['6/10_coord']=len(sixth_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['6/10_sub']=len(sixth_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['6/10_il']=len(sixth_ten.findall(".//word[@form='il']"))
            dic_stats['6/10_ils']=len(sixth_ten.findall(".//word[@form='ils']"))
            dic_stats['6/10_elle']=len(sixth_ten.findall(".//word[@form='elle']"))
            dic_stats['6/10_elles']=len(sixth_ten.findall(".//word[@form='elles']"))
            dic_stats['6/10_je']=len(sixth_ten.findall(".//word[@form='je']"))
            dic_stats['6/10_nous']=len(sixth_ten.findall(".//word[@form='nous']"))
            dic_stats['6/10_etat']=len(sixth_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['6/10_voc']=len(set(sixth_ten.xpath(".//word/@lemma")))
            
            dic_stats['7/10_word']=len(seventh_ten.findall(".//word"))
            dic_stats['7/10_sentence']=len(seventh_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['7/10_av_word_per_sent']= average_words_sent(seventh_ten)
            dic_stats['7/10_name']=len(set(seventh_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['7/10_verb']=len(seventh_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['7/10_adverb']=len(seventh_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['7/10_adj']=len(seventh_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['7/10_coord']=len(seventh_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['7/10_sub']=len(seventh_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['7/10_il']=len(seventh_ten.findall(".//word[@form='il']"))
            dic_stats['7/10_ils']=len(seventh_ten.findall(".//word[@form='ils']"))
            dic_stats['7/10_elle']=len(seventh_ten.findall(".//word[@form='elle']"))
            dic_stats['7/10_elles']=len(seventh_ten.findall(".//word[@form='elles']"))
            dic_stats['7/10_je']=len(seventh_ten.findall(".//word[@form='je']"))
            dic_stats['7/10_nous']=len(seventh_ten.findall(".//word[@form='nous']"))
            dic_stats['7/10_etat']=len(seventh_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['7/10_voc']=len(set(seventh_ten.xpath(".//word/@lemma")))
            
            dic_stats['8/10_word']=len(eigth_ten.findall(".//word"))
            dic_stats['8/10_sentence']=len(eigth_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['8/10_av_word_per_sent']= average_words_sent(eigth_ten)
            dic_stats['8/10_name']=len(set(eigth_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['8/10_verb']=len(eigth_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['8/10_adverb']=len(eigth_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['8/10_adj']=len(eigth_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['8/10_coord']=len(eigth_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['8/10_sub']=len(eigth_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['8/10_il']=len(eigth_ten.findall(".//word[@form='il']"))
            dic_stats['8/10_ils']=len(eigth_ten.findall(".//word[@form='ils']"))
            dic_stats['8/10_elle']=len(eigth_ten.findall(".//word[@form='elle']"))
            dic_stats['8/10_elles']=len(eigth_ten.findall(".//word[@form='elles']"))
            dic_stats['8/10_je']=len(eigth_ten.findall(".//word[@form='je']"))
            dic_stats['8/10_nous']=len(eigth_ten.findall(".//word[@form='nous']"))
            dic_stats['8/10_etat']=len(eigth_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['8/10_voc']=len(set(eigth_ten.xpath(".//word/@lemma")))
            
            dic_stats['9/10_word']=len(ninth_ten.findall(".//word"))
            dic_stats['9/10_sentence']=len(ninth_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['9/10_av_word_per_sent']= average_words_sent(ninth_ten)
            dic_stats['9/10_name']=len(set(ninth_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['9/10_verb']=len(ninth_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['9/10_adverb']=len(ninth_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['9/10_adj']=len(ninth_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['9/10_coord']=len(ninth_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['9/10_sub']=len(ninth_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['9/10_il']=len(ninth_ten.findall(".//word[@form='il']"))
            dic_stats['9/10_ils']=len(ninth_ten.findall(".//word[@form='ils']"))
            dic_stats['9/10_elle']=len(ninth_ten.findall(".//word[@form='elle']"))
            dic_stats['9/10_elles']=len(ninth_ten.findall(".//word[@form='elles']"))
            dic_stats['9/10_je']=len(ninth_ten.findall(".//word[@form='je']"))
            dic_stats['9/10_nous']=len(ninth_ten.findall(".//word[@form='nous']"))
            dic_stats['9/10_etat']=len(ninth_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['9/10_voc']=len(set(ninth_ten.xpath(".//word/@lemma")))
            
            dic_stats['10/10_word']=len(last_ten.findall(".//word"))
            dic_stats['10/10_sentence']=len(last_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['10/10_av_word_per_sent']= average_words_sent(last_ten)
            dic_stats['10/10_name']=len(set(last_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['10/10_verb']=len(last_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['10/10_adverb']=len(last_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['10/10_adj']=len(last_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['10/10_coord']=len(last_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['10/10_sub']=len(last_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['10/10_il']=len(last_ten.findall(".//word[@form='il']"))
            dic_stats['10/10_ils']=len(last_ten.findall(".//word[@form='ils']"))
            dic_stats['10/10_elle']=len(last_ten.findall(".//word[@form='elle']"))
            dic_stats['10/10_elles']=len(last_ten.findall(".//word[@form='elles']"))
            dic_stats['10/10_je']=len(last_ten.findall(".//word[@form='je']"))
            dic_stats['10/10_nous']=len(last_ten.findall(".//word[@form='nous']"))
            dic_stats['10/10_etat']=len(last_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['10/10_voc']=len(set(last_ten.xpath(".//word/@lemma")))
            
            dic_stats['mid_word']=len(middle_chap.findall(".//word"))
            dic_stats['mid_paragraph']=len(middle_chap.findall(".//p"))
            dic_stats['mid_sentence']=len(middle_chap.findall(".//word[@postag='PUNsent']"))
            dic_stats['mid_av_word_per_sent']= average_words_sent(middle_chap)
            dic_stats['mid_name']=len(set(middle_chap.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['mid_verb']=len(middle_chap.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['mid_adverb']=len(middle_chap.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['mid_adj']=len(middle_chap.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['mid_coord']=len(middle_chap.findall(".//word[@postag='CONJcoord']"))
            dic_stats['mid_sub']=len(middle_chap.findall(".//word[@postag='CONJsubord']"))
            dic_stats['mid_il']=len(middle_chap.findall(".//word[@form='il']"))
            dic_stats['mid_ils']=len(middle_chap.findall(".//word[@form='ils']"))
            dic_stats['mid_elle']=len(middle_chap.findall(".//word[@form='elle']"))
            dic_stats['mid_elles']=len(middle_chap.findall(".//word[@form='elles']"))
            dic_stats['mid_je']=len(middle_chap.findall(".//word[@form='je']"))
            dic_stats['mid_nous']=len(middle_chap.findall(".//word[@form='nous']"))
            dic_stats['mid_etat']=len(middle_chap.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['mid_voc']=len(set(middle_chap.xpath(".//word/@lemma")))
            
            dic_stats['last_word']=len(last_chap.findall(".//word"))
            dic_stats['last_paragraph']=len(last_chap.findall(".//p"))
            dic_stats['last_sentence']=len(last_chap.findall(".//word[@postag='PUNsent']"))
            dic_stats['last_av_word_per_sent']= average_words_sent(last_chap)
            dic_stats['last_name']=len(set(last_chap.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['last_verb']=len(last_chap.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['last_adverb']=len(last_chap.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['last_adj']=len(last_chap.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['last_coord']=len(last_chap.findall(".//word[@postag='CONJcoord']"))
            dic_stats['last_sub']=len(last_chap.findall(".//word[@postag='CONJsubord']"))
            dic_stats['last_il']=len(last_chap.findall(".//word[@form='il']"))
            dic_stats['last_ils']=len(last_chap.findall(".//word[@form='ils']"))
            dic_stats['last_elle']=len(last_chap.findall(".//word[@form='elle']"))
            dic_stats['last_elles']=len(last_chap.findall(".//word[@form='elles']"))
            dic_stats['last_je']=len(last_chap.findall(".//word[@form='je']"))
            dic_stats['last_nous']=len(last_chap.findall(".//word[@form='nous']"))
            dic_stats['last_etat']=len(last_chap.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['last_voc']=len(set(last_chap.xpath(".//word/@lemma")))
            
            dic_stats['mid_word']=len(middle_chap.findall(".//word"))
            dic_stats['mid_paragraph']=len(middle_chap.findall(".//p"))
            dic_stats['mid_sentence']=len(middle_chap.findall(".//word[@postag='PUNsent']"))
            dic_stats['mid_av_word_per_sent']= average_words_sent(middle_chap)
            dic_stats['mid_name']=len(set(middle_chap.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['mid_verb']=len(middle_chap.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['mid_adverb']=len(middle_chap.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['mid_adj']=len(middle_chap.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['mid_coord']=len(middle_chap.findall(".//word[@postag='CONJcoord']"))
            dic_stats['mid_sub']=len(middle_chap.findall(".//word[@postag='CONJsubord']"))
            dic_stats['mid_il']=len(middle_chap.findall(".//word[@form='il']"))
            dic_stats['mid_ils']=len(middle_chap.findall(".//word[@form='ils']"))
            dic_stats['mid_elle']=len(middle_chap.findall(".//word[@form='elle']"))
            dic_stats['mid_elles']=len(middle_chap.findall(".//word[@form='elles']"))
            dic_stats['mid_je']=len(middle_chap.findall(".//word[@form='je']"))
            dic_stats['mid_nous']=len(middle_chap.findall(".//word[@form='nous']"))
            dic_stats['mid_etat']=len(middle_chap.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['mid_voc']=len(set(middle_chap.xpath(".//word/@lemma")))
            
            dic_stats['last_word']=len(last_chap.findall(".//word"))
            dic_stats['last_paragraph']=len(last_chap.findall(".//p"))
            dic_stats['last_sentence']=len(last_chap.findall(".//word[@postag='PUNsent']"))
            dic_stats['last_av_word_per_sent']= average_words_sent(last_chap)
            dic_stats['last_name']=len(set(last_chap.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['last_verb']=len(last_chap.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['last_adverb']=len(last_chap.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['last_adj']=len(last_chap.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['last_coord']=len(last_chap.findall(".//word[@postag='CONJcoord']"))
            dic_stats['last_sub']=len(last_chap.findall(".//word[@postag='CONJsubord']"))
            dic_stats['last_il']=len(last_chap.findall(".//word[@form='il']"))
            dic_stats['last_ils']=len(last_chap.findall(".//word[@form='ils']"))
            dic_stats['last_elle']=len(last_chap.findall(".//word[@form='elle']"))
            dic_stats['last_elles']=len(last_chap.findall(".//word[@form='elles']"))
            dic_stats['last_je']=len(last_chap.findall(".//word[@form='je']"))
            dic_stats['last_nous']=len(last_chap.findall(".//word[@form='nous']"))
            dic_stats['last_etat']=len(last_chap.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['last_voc']=len(set(last_chap.xpath(".//word/@lemma")))
            titles_book=0
            num_book=0
            for element in tree.findall(".//div[@type='book'][@title]"):
                if re.match(r'(Livre)*(LIVRE)*\s*\b[IVXCL0-9]+\b',element.attrib["title"]):
                    num_book+=1
                elif re.match(r"(Livre)*(LIVRE)*\s*\b[IVXCL]+[:,. ]*[A-Za-zéèếôîâûùÙÉÈïëüçÇ']+"):
                    titles_book+=1
                    num_book+=1
                else:
                    titles_book+=1
                
            titles_part=0
            num_part=0
            for element in tree.findall(".//div[@type='part'][@title]"):
                if re.match(r'(Partie)*(PARTIE)*\s*\b[IVXCL0-9]+\b',element.attrib["title"]):
                    num_part+=1
                elif re.match(r"(Partie)*(PARTIE)*\s*\b[IVXCL]+[:,. ]*[A-Za-zéèếôîâûùÙÉÈïëüçÇ']+"):
                    titles_part+=1
                    num_part+=1
                else:
                    titles_part+=1
            titles_chap=0
            num_chap=0
            for element in tree.findall(".//div[@type='chapter'][@title]"):
                if re.match(r'(Chapitre)*(CHAPITRE)*\s*\b[IVXCL0-9]+\b',element.attrib["title"]):
                    num_chap+=1
                elif re.match(r"(Chapitre)*(CHAPITRE)*\s*\b[IVXCL]+[:,. ]*[A-Za-zéèếôîâûùÙÉÈïëüçÇ']+"):
                    titles_chap+=1
                    num_chap+=1
                else:
                    titles_chap+=1
            dic_stats['titled_books']=titles_book
            dic_stats['titled_parts']=titles_part
            dic_stats['titled_chapters']=titles_chap
            dic_stats['numbered_books']=num_book
            dic_stats['numbered_parts']=num_part
            dic_stats['numbered_chapters']=num_chap
            headers=list(dic_stats.keys())
            writer = csv.DictWriter(f, delimiter=',', lineterminator='\n',fieldnames=headers)
            if (count_header==0):
                writer.writeheader()
                count_header += 1
            writer2 = csv.writer(f)
            writer2.writerow(list(dic_stats.values()))
        print('File done : '+file)

