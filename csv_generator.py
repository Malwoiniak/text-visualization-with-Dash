#Import regex library
import re

def ten_longest_sen(a):
	"""Returns element [0:10] of list of string sorted by length splitted by whitespace in descending order 

	Parameters:
	a (list): The list of strings to perform above

	Returns: Element [0:10] of list of string sorted by length splitted by whitespace in descending order
	""" 
	longest_sentence = sorted(a,key=lambda x: len(x.split()), reverse=True)[:10]
	return(longest_sentence)

def strip_delimiters(a):
	""" Removes delimiters from the list of strings

	Parameters:
	a (list): The list of strings to remove delimiters 

	Returns: List of strings without delimiters 
	""" 
	a=[item.lower() for item in a]
	words_strip=[]
	for item in a:
		words_strip.append(item.strip(delimiters))
	return(words_strip)

def remove_stopwords(a,b):
	"""Removes elements listed in (b) from list (a) 

	Parameters:
	a (list): List of elements to perform above
	b (list): List of elements to be removed from (a)

	Returns: List of elements (a) without elements (b)
	""" 
	stopwords_removed=[word for word in a if word not in b]
	return stopwords_removed

def freq_dict(a):
	"""Convert a list of words into a dictionary of word-frequency pairs 

	Parameters:
	a (list): The list of strings to perform above

	Returns: Dictionary of word-frequency pairs 
	""" 
	word_freq = [a.count(item) for item in a]
	d = dict(zip(a,word_freq))
	return d

def sort_freq_dict(a):
	"""Turns a dictionary of word-frequency pairs to list and sorts by descending order

	Parameters:
	a (dict): The dictionary of word-frequency pairs to perform above

	Returns: List of word-frequency pairs sorted by descending order
	""" 
	freq_sort = [(a[key], key) for key in a]
	freq_sort.sort()
	freq_sort.reverse()
	return freq_sort

#Open and read files with encoding utf-8
f=open('Sapir1921_chapter1.txt', encoding='utf-8')
Sapir=f.read()
f1=open('Muller1861_lecture1.txt', encoding='utf-8')
Muller=f1.read()
f2=open('stopwordlist.txt')
stop_words=f2.read()
f.close()
f1.close()
f2.close()

#Process stopwords file: create list of stopwords 
stop_words=(re.sub("\s+", " ", stop_words)).split()

#Replace ellipsis by a period in Muller, Sapir
Muller_process = re.sub(r'\.+', ".", Muller)
Sapir_process = re.sub(r'\.+', ".", Sapir)

#Replace whitespace by a space in Muller, Sapir
Muller_process = re.sub("\s+", " ", Muller_process)
Sapir_process = re.sub("\s+", " ", Sapir_process)

#Replace more than two hypens by a space in Muller
Muller_process = re.sub(r'\‐{3,}', " ", Muller_process)

#Define acronyms at the end of sentences and replace with ||acronym|| in Muller, Sapir
acronyms_end = r'(\b[A-Z][a-zA-Z\.]*[A-Z]\b\.?) +(?=[A-Z0-9]|["\'])'
Muller_process1 = re.sub(acronyms_end, "||\\1||. ", Muller_process)
Sapir_process1 = re.sub(acronyms_end, "||\\1||. ", Sapir_process)

#Split Muller into sentences 
Muller_sentences = re.split(r'(?<=[^A-Z.].[.?!"\')\]\”]) +(?=[A-Z0-9]|[\|"\'_\“])', Muller_process1)

#Split Sapir into sentences 
Sapir_sentences = re.split(r'(?<=[^A-Z.].[.?!"\')\]\”]) +(?=[A-Z0-9]|[\|"\'_\“])', Sapir_process1)

#Get ten longest sentences in Muller, Sapir
Muller_longest=ten_longest_sen(Muller_sentences)
Sapir_longest=ten_longest_sen(Sapir_sentences)

#Iterate over ten longest sentences in Muller, Sapir and assign necessary data to 'header','data' string variables 
header='length, sentence, chapter, ranking\n'
data=''
for i in range(0, 10, 1):
	data=data + str(len(Sapir_longest[i].split()))  + ',' + "'" + Sapir_longest[i] + "'" + ',1,' + str(i+1) + '\n'

	data=data +str(len(Muller_longest[i].split()))  + ',' + "'" + Muller_longest[i] + "'" +',2,' + str(i+1) + '\n'

#Write and save CSV_sentences file 
CSV_sentences=header+data
fw = open('sentences.csv', 'w+', encoding='utf-8')
fw.write(CSV_sentences)

#Define delimiters
delimiters = '\<\"\'\[\{\(\@.,;:?!>]})&=/\“\”—_'
 
#Replace two hypens/em dash by a period and space in Muller, Sapir
Sapir_words = re.sub("--", ". ", Sapir_process)
Muller_words = re.sub("--", ". ", Muller_process)
Sapir_words = re.sub("—", ". ", Sapir_words)
Muller_words = re.sub("—", ". ", Muller_words)

#Create list of words in Muller, Sapir
Sapir_words = Sapir_words.split()
Muller_words = Muller_words.split()

#Remove delimiters from list of words in Muller, Sapir
Sapir_stripped = strip_delimiters(Sapir_words)
Muller_stripped = strip_delimiters(Muller_words)
Muller_stripped=strip_delimiters(Muller_stripped)

#Remove stopwords from list of words stripped by delimiters in Muller, Sapir
Sapir_stopwords_removed=remove_stopwords(Sapir_stripped, stop_words)
Muller_stopwords_removed=remove_stopwords(Muller_stripped, stop_words)

#Create a dict of word-frequency pairs from word list without stopwords in Muller, Sapir
Sapir_words_freq=freq_dict(Sapir_stopwords_removed)
Muller_words_freq=freq_dict(Muller_stopwords_removed)

#Turn a dict of word-frequency pairs into list and sort by descending order in Muller, Sapir
Sapir_freq_sorted=sort_freq_dict(Sapir_words_freq)
Muller_freq_sorted=sort_freq_dict(Muller_words_freq)

#Get ten most frequent words with frequencies in Muller, Sapir
Sapir_ten_freq=Sapir_freq_sorted[:10]
Muller_ten_freq=Muller_freq_sorted[:10]

#Iterate over ten most frequent words in Muller, Sapir and assign necessary data to 'header1','data1' string variables
header1='keyword, frequency, length, chapter\n'
data1=''
for i in range(0, 10, 1):
	data1=data1 + str(Sapir_ten_freq[i][1]) + ',' + str(Sapir_ten_freq[i][0]) + ',' + str(len(str(Sapir_ten_freq[i][1]))) + ',1\n'

	data1=data1 + str(Muller_ten_freq[i][1]) + ',' + str(Muller_ten_freq[i][0]) + ',' + str(len(str(Muller_ten_freq[i][1]))) + ',2\n'

#Write and save CSV_words file 
CSV_words=header1+data1

fw1 = open('words.csv', 'w+', encoding='utf-8')
fw1.write(CSV_words)


