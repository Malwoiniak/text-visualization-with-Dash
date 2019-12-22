#Import dash, csv module
import csv
import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.graph_objs as go

def sen_content_chap1(a):
	"""Appends every 8th element a[i] starting from 1st element to empty list

	Parameters:
	a (list): List of elements to perform above

	Returns: List of appended elements 
	""" 
	sen_content=[]
	for i in range(1,len(a),8):
		sen_content.append(a[i]) 
	return(sen_content)

def sen_content_chap2(a):
	"""Appends every 8th element a[i] starting from 5th element to empty list

	Parameters:
	a (list): List of elements to perform above

	Returns: List of appended elements 
	""" 
	sen_content=[]
	for i in range(5,len(a),8):
		sen_content.append(a[i]) 
	return(sen_content)

def sen_length_chap1(a):
	"""Converts every 8th element a[i] to int and appends it to empty list

	Parameters:
	a (list): List of elements to perform above

	Returns: List of appended elements 
	"""
	sen_content=[]
	for i in range(0,len(a),8):
		sen_content.append(int(a[i]))
	return(sen_content)

def sen_length_chap2(a):
	"""Converts every 8th element a[i] to int (starting from 4th element) and appends it to empty list

	Parameters:
	a (list): List of elements to perform above

	Returns: List of appended elements 
	"""
	sen_content=[]
	for i in range(4,len(a),8):
		sen_content.append(int(a[i]))
	return(sen_content)

def list_to_dict_sen_chap1(a):
	"""Converts list to dict of sentence_length-ranking pairs (starting from 0 element of (a) list)

	Parameters:
	a (list): List of elements to perform above

	Returns: Dictionary of sentence_length-ranking pairs
	"""
	d = {int(a[i+3]): int(a[i]) for i in range(0,len(a),8)}
	return(d)

def list_to_dict_sen_chap2(a):
	"""Converts list to dict of sentence_length-ranking pairs (starting from 4th element of (a) list)

	Parameters:
	a (list): List of elements to perform above

	Returns: Dictionary of sentence_length-ranking pairs
	"""
	d = {int(a[i+3]): int(a[i]) for i in range(4,len(a),8)}
	return(d)

def list_to_dict_freq_chap1(a):
	"""Converts list to dict of word-frequency pairs (starting from 0 element of (a) list)

	Parameters:
	a (list): List of elements to perform above

	Returns: Dictionary of word-frequency pairs pairs
	"""
	d = {a[i]: int(a[i+1]) for i in range(0,len(a),8)}
	return(d)

def list_to_dict_freq_chap2(a):
	"""Converts list to dict of word-frequency pairs (starting from 4th element of (a) list)

	Parameters:
	a (list): List of elements to perform above

	Returns: Dictionary of word-frequency pairs pairs
	"""
	d = {a[i]: int(a[i+1]) for i in range(4,len(a),8)}
	return(d)

def list_to_dict_len_chap1(a):
	"""Converts list to dict of word-length pairs (starting from 0 element of (a) list)

	Parameters:
	a (list): List of elements to perform above

	Returns: Dictionary of word-length pairs pairs
	"""
	d = {a[i]: int(a[i+2]) for i in range(0,len(a),8)}
	return(d)

def list_to_dict_len_chap2(a):
	"""Converts list to dict of word-length pairs (starting from 4th element of (a) list)

	Parameters:
	a (list): List of elements to perform above

	Returns: Dictionary of word-length pairs pairs
	"""
	d = {a[i]: int(a[i+2]) for i in range(4,len(a),8)}
	return(d)


#Read sentences.csv with csv module; define var reader_sen
file_sen = open('sentences.csv', encoding='utf-8', newline='') 
reader_sen = csv.reader(file_sen, quotechar="'", delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)

#Append rows from sentences.csv to empty list (creates list of strings)
header_sen=next(reader_sen) #First line is a header
sen=[]
for row in reader_sen:
	sen=sen + row

#Get content of sentences (list of strings) from 'sen' list of strings for chapter 1,2
sen_content_chap1=sen_content_chap1(sen)
sen_content_chap2=sen_content_chap2(sen)

#Gets lenght of sentences (list of int) from 'sen' list of strings for chapter 1,2
sen_len_chap1=sen_length_chap1(sen)
sen_len_chap2=sen_length_chap2(sen)

#Get dictionary of sentence_length-ranking pairs for chapter 1,2
sen_rank_chap1=list_to_dict_sen_chap1(sen)
sen_rank_chap2=list_to_dict_sen_chap2(sen)


#Create list of tuples to iterate for bubble chart (sentences visualization)
data_for_scatter=[(sen_rank_chap1,'Chapter 1', sen_content_chap1, sen_len_chap1),(sen_rank_chap2,'Chapter 2', sen_content_chap2, sen_len_chap2)]

#Read words.csv with csv module, define var reader_words 
file_words = open('words.csv', encoding='utf-8', newline='')
reader_words = csv.reader(file_words)

#Append rows from words.csv to empty list (creates list of strings)
header=next(reader_words) #First line is a header
words=[]
for row in reader_words:
	words=words + row

#Get dictionary of word-frequency pairs for chapter 1,2
keyword_freq_chap1=list_to_dict_freq_chap1(words)
keyword_freq_chap2=list_to_dict_freq_chap2(words)

#Get dictionary of word-length pairs for chappter 1,2
keyword_len_chap1=list_to_dict_len_chap1(words)
keyword_len_chap2=list_to_dict_len_chap2(words)

#Create list of tuples to iterate for stacked bar chart (words visualization)
data_for_stackbar=[(keyword_len_chap1,'Lenght, chapter 1'),(keyword_len_chap2,'Lenght, chapter 2'),(keyword_freq_chap1, 'Frequency, chapter 1'), (keyword_freq_chap2,'Frequency, chapter 2')]

#Configuration for dcc.Graph (fixes size of downloaded .pdf)
config={"toImageButtonOptions": {"width": None, "height": None}}

#Create dash visualization
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
	html.H1(children='Visualization of ten longest sentences and ten most frequent words in Muller, Sapir'),
	dcc.Graph(
		id='keyword-frequency',
		config=config,
		style={'height':600},
		figure={
			'data': [
				go.Scatter(
					x=list(keyword_freq_chap1.keys()),
					y=list(keyword_freq_chap1.values()),
					name='Chapter 1',
					mode='markers',
					opacity=1,
					marker={
						'color': 'Lime',
						'size':30,
						'line':{'width':2, 'color': 'Black'}
						}),
				go.Scatter(
					x=list(keyword_freq_chap2.keys()),
					y=list(keyword_freq_chap2.values()),
					name='Chapter 2',
					mode='markers',
					opacity=1,
					marker={
						'color': 'Magenta',
						'size':30,
						'line':{'width':2, 'color': 'Black'}
						}),	
					
			],
			'layout': {

				'title': 'word/(frequency|length)',
				'yaxis' : {'title': 'frequency [occurrence in text]', 'showline':True, 'linewidth':0.7, 'linecolor':'DarkSlateGrey', 'gridcolor': 'LightSlateGrey', 'mirror':True
				},
				'xaxis' : {'showticklabels':False, 'showline':True, 'linewidth':0.7, 'linecolor':'DarkSlateGrey', 'gridcolor': 'LightSlateGrey', 'mirror':True},

				'font': {'color':'black', 'size':14},
				


			}


		}),
	dcc.Graph(
		id='keyword-length',
		config=config,
		style={'height':600},
		figure={
			'data': [
				go.Scatter(
					x=list(keyword_len_chap1.keys()),
					y=list(keyword_len_chap1.values()),
					name='Chapter 1',
					mode='markers',
					opacity=1,
					marker={
						'color': 'Lime',
						'size':30,
						'line':{'width':2, 'color': 'Black'}
						}),
				go.Scatter(
					x=list(keyword_len_chap2.keys()),
					y=list(keyword_len_chap2.values()),
					name='Chapter 2',
					mode='markers',
					opacity=1,
					marker={
						'color': 'Magenta',
						'size':30,
						'line':{'width':2, 'color': 'Black'}
						}),				
			],
			'layout': {
				'yaxis' : {'title': 'length [number of letters]', 'showline':True, 'linewidth':0.7, 'linecolor':'DarkSlateGrey', 'gridcolor': 'LightSlateGrey', 'mirror':True

				},
				'xaxis' : {'title': 'word', 'showline':True, 'linewidth':0.7, 'linecolor':'DarkSlateGrey', 'automargin':True, 'gridcolor': 'LightSlateGrey', 'mirror':True}, 
				'font': {'color':'black', 'size':14},
				
				
			}
		}),
	dcc.Graph(
		id='keyword-length-stack',
		config=config,
		style={'height':600},
		figure={
			'data': [
				go.Bar(
					x=list(i[0].keys()),
					y=list(i[0].values()),
					name=i[1],					
					opacity=1,
					marker={
						'line':{'width':2, 'color': 'Black'}
						})for i in data_for_stackbar
				
			],
			'layout': {
			'title':'word/(frequency|length)',
				'barmode':'stack',
				'yaxis' : {'title': 'length | frequency', 'showline':True, 'linewidth':0.7, 'linecolor':'DarkSlateGrey', 'gridcolor': 'LightSlateGrey', 'mirror':True

				},
				'xaxis' : {'title': 'word', 'showline':True, 'linewidth':0.7, 'linecolor':'DarkSlateGrey', 'automargin':True, 'gridcolor': 'LightSlateGrey', 'mirror':True}, 
				'font': {'color':'black', 'size':14},
				
			}


		}),
		dcc.Graph(
		id='sentence_length-ranking',
		style={'height':800},
		config=config,
		figure={
			'data': [
				go.Scatter(
					x=list(i[0].keys()),
					y=list(i[0].values()),

					text=i[2],
					name=i[1],
					mode='markers',
					hoverlabel=dict(namelength=190),
					opacity=1,
					marker={
						
						'size':i[3],
						'sizemode':'area',
						'sizeref':2.*max(i[3])/(90.**2),
						'sizemin':10,
						'opacity':1,
						'line':{'width':5, 'color': 'Black'},
						})for i in data_for_scatter
					
			],
			'layout': {

				'title': 'sentence length/ranking',
				'yaxis' : {'title': 'length [number of words]', 'showline':True, 'linewidth':0.7, 'linecolor':'DarkSlateGrey', 'gridcolor': 'LightSlateGrey', 'mirror':True
				},
				'xaxis' : {'title':'ranking','showticklabels':True, 'showline':True, 'linewidth':0.7, 'linecolor':'DarkSlateGrey', 'gridcolor': 'LightSlateGrey', 'mirror':True},

				'font': {'color':'black', 'size':14},
				


			}


		})
	])
	

if __name__ == '__main__':
	app.run_server(debug=True)