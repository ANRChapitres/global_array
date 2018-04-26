
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
                middle_chap = tree.findall(".//div[@type='chapter']")[int(len(tree.findall(".//div[@type='chapter']"))/2)]
                last_chap = tree.findall(".//div[@type='chapter']")[len(tree.findall(".//div[@type='chapter']"))-1]
            elif tree.findall(".//div[@type='book']"):
                first_chap = tree.findall(".//div[@type='book']")[0]
                middle_chap = tree.findall(".//div[@type='book']")[int(len(tree.findall(".//div[@type='book']"))/2)]
                last_chap = tree.findall(".//div[@type='book']")[len(tree.findall(".//div[@type='book']"))-1]
            elif tree.findall(".//div[@type='part']"):
                first_chap = tree.findall(".//div[@type='part']")[0]
                middle_chap = tree.findall(".//div[@type='part']")[int(len(tree.findall(".//div[@type='part']"))/2)]
                last_chap = tree.findall(".//div[@type='part']")[len(tree.findall(".//div[@type='part']"))-1]
            
            dic_stats['ref']=file
            dic_stats['title']=re.sub(u'\n','',tree.find(".//title").text).replace("     ","")
            dic_stats['author']=tree.find(".//author").attrib['name']
            dic_stats['date']=tree.find(".//date").attrib['when']
            #dic_stats['genre']=tree.find(".//term").text
            dic_stats['canon_degree']="empty"
            total_words = tree.findall(".//word")
            nb_words = len(total_words)
            dic_stats['glob_word']= nb_words
            first_ten = etree.Element("first")
            for word in total_words[0:int(((10*nb_words)/100))]:
                first_ten.append(deepcopy(word))
            last_ten = etree.Element("last")
            for word in total_words[nb_words-int(((10*nb_words)/100)):nb_words]:
                last_ten.append(deepcopy(word))
            
            dic_stats['glob_book']=len(tree.findall(".//div[@type='book']"))
            dic_stats['glob_part']=len(tree.findall(".//div[@type='part']"))
            dic_stats['glob_chapter']=len(tree.findall(".//div[@type='chapter']"))
            dic_stats['glob_paragraph']=len(tree.findall(".//p"))
            dic_stats['glob_sentence']=len(tree.findall(".//word[@postag='PUNsent']"))
            dic_stats['glob_av_word_per_sent']= average_words_sent(tree)
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
            dic_stats['first_ten_words']=len(first_ten.findall(".//word"))
            dic_stats['first_ten_sentence']=len(first_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['first_ten_av_word_per_sent']= average_words_sent(first_ten)
            dic_stats['first_ten_name']=len(set(first_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['first_ten_verb']=len(first_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['first_ten_adverb']=len(first_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['first_ten_adj']=len(first_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['first_ten_coord']=len(first_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['first_ten_sub']=len(first_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['first_ten_il']=len(first_ten.findall(".//word[@form='il']"))
            dic_stats['first_ten_ils']=len(first_ten.findall(".//word[@form='ils']"))
            dic_stats['first_ten_elle']=len(first_ten.findall(".//word[@form='elle']"))
            dic_stats['first_ten_elles']=len(first_ten.findall(".//word[@form='elles']"))
            dic_stats['first_ten_je']=len(first_ten.findall(".//word[@form='je']"))
            dic_stats['first_ten_nous']=len(first_ten.findall(".//word[@form='nous']"))
            dic_stats['first_ten_etat']=len(first_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['first_ten_voc']=len(set(first_ten.xpath(".//word/@lemma")))
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
            dic_stats['last_ten_word']=len(last_ten.findall(".//word"))
            dic_stats['last_ten_sentence']=len(last_ten.findall(".//word[@postag='PUNsent']"))
            dic_stats['last_ten_av_word_per_sent']= average_words_sent(last_ten)
            dic_stats['last_ten_name']=len(set(last_ten.xpath(".//word[starts-with(@postag, 'NAME')]/@lemma")))
            dic_stats['last_ten_verb']=len(last_ten.xpath(".//word[starts-with(@postag,'VERB')]"))
            dic_stats['last_ten_adverb']=len(last_ten.xpath(".//word[starts-with(@postag, 'ADV')]"))
            dic_stats['last_ten_adj']=len(last_ten.xpath(".//word[starts-with(@postag, 'ADJ')]"))
            dic_stats['last_ten_coord']=len(last_ten.findall(".//word[@postag='CONJcoord']"))
            dic_stats['last_ten_sub']=len(last_ten.findall(".//word[@postag='CONJsubord']"))
            dic_stats['last_ten_il']=len(last_ten.findall(".//word[@form='il']"))
            dic_stats['last_ten_ils']=len(last_ten.findall(".//word[@form='ils']"))
            dic_stats['last_ten_elle']=len(last_ten.findall(".//word[@form='elle']"))
            dic_stats['last_ten_elles']=len(last_ten.findall(".//word[@form='elles']"))
            dic_stats['last_ten_je']=len(last_ten.findall(".//word[@form='je']"))
            dic_stats['last_ten_nous']=len(last_ten.findall(".//word[@form='nous']"))
            dic_stats['last_ten_etat']=len(last_ten.xpath(".//word[@lemma='être' or @lemma='sembler' or @lemma='devenir' or @lemma='demeurer' or @lemma='rester' ]"))
            dic_stats['last_ten_voc']=len(set(last_ten.xpath(".//word/@lemma")))
            titles_book=0
            num_book=0
            for element in tree.findall(".//div[@type='book'][@title]"):
                if len(element.attrib["title"])>3:
                    titles_book+=1
                if any(num in element.attrib["title"] for num in nums):
                    num_book+=1
            titles_part=0
            num_part=0
            for element in tree.findall(".//div[@type='part'][@title]"):
                if len(element.attrib["title"])>3:
                    titles_part+=1
                if any(num in element.attrib["title"] for num in nums):
                    num_part+=1
            titles_chap=0
            num_chap=0
            for element in tree.findall(".//div[@type='chapter'][@title]"):
                if len(element.attrib["title"])>3:
                    titles_chap+=1
                if any(num in element.attrib["title"] for num in nums):
                    num_chap+=1
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

