
# coding: utf-8

import sys
import os
import os.path
import fnmatch
from lxml import etree
from collections import OrderedDict
import csv
import IPython
import argparse

print('This software generates a csv with basic statistics on a selected corpus \nusage: --dir path/to/your/source/dir --csv path/to/your/target/directory/for/csv')
parser = argparse.ArgumentParser()
parser.add_argument('--dir', help= '/your/directory/to/tagged/files/')
parser.add_argument('--csv', help= '/your/directory/to/your/csv/file/')
args = parser.parse_args()

path_to_folder=args.dir
files_list=fnmatch.filter(os.listdir(path_to_folder), '*.xml')

count_header=0
with open(args.csv+'global.csv', 'a') as f:
    for file in files_list:
        dic_stats=OrderedDict()
        tmpFile=file.replace("/",":")
        full_path=path_to_folder+tmpFile
        if os.path.isfile(full_path):
            tree=etree.parse(full_path)
            dic_stats['ref']=file
            dic_stats['title']=tree.find(".//title").text
            dic_stats['author']=tree.find(".//author").attrib['name']
            dic_stats['date']=tree.find(".//date").attrib['when']
            #dic_stats['genre']=tree.find(".//term").text
            dic_stats['canon_degree']="empty"
            dic_stats['word_count']=len(tree.findall(".//word"))
            dic_stats['book_count']=len(tree.findall(".//div[@type='book']"))
            dic_stats['part_count']=len(tree.findall(".//div[@type='part']"))
            dic_stats['chapter_count']=len(tree.findall(".//div[@type='chapter']"))
            dic_stats['paragraph_count']=len(tree.findall(".//p"))
            dic_stats['sentence_count']=len(tree.findall(".//word[@postag='PUNsent']"))
            dic_stats['verb_count']=len(tree.findall(".//word[@postag='VERB']"))
            titles_book=0
            num_book=0
            for element in tree.findall(".//div[@type='book'][@title]"):
                if len(element.attrib["title"])>3:
                    titles_book+=1
                if any(num in element.attrib["title"] for num in nums):
                    num_book+=1
                    print(element.attrib["title"])
            titles_part=0
            num_part=0
            for element in tree.findall(".//div[@type='part'][@title]"):
                if len(element.attrib["title"])>3:
                    titles_part+=1
                if any(num in element.attrib["title"] for num in nums):
                    num_part+=1
                    print(element.attrib["title"])
            titles_chap=0
            num_chap=0
            for element in tree.findall(".//div[@type='chapter'][@title]"):
                if len(element.attrib["title"])>3:
                    titles_chap+=1
                if any(num in element.attrib["title"] for num in nums):
                    num_chap+=1
                    print(element.attrib["title"])
            dic_stats['titled_book_count']=titles_book
            dic_stats['titled_part_count']=titles_part
            dic_stats['titled_chapter_count']=titles_chap
            dic_stats['numbered_book_count']=num_book
            dic_stats['numbered_part_count']=num_part
            dic_stats['numbered_chapter_count']=num_chap
            headers=list(dic_stats.keys())
            writer = csv.DictWriter(f, delimiter=',', lineterminator='\n',fieldnames=headers)
            if (count_header==0):
                writer.writeheader()
                count_header += 1
            writer2 = csv.writer(f)
            writer2.writerow(list(dic_stats.values()))
        print('File done : '+file)

