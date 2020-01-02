# text-visualization-with-Dash
> Text processing and visualization with Python. First steps with Dash.

## Table of contents
* [General info](#general-info)
* [Illustrations](#illustrations)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Contact](#contact)

## General info
Created as training project to practice Dash and process text without external natural language processing tools.

Part of this script is reused from [text-processing-with-regex](https://github.com/Malwoiniak/text-processing-with-regex)

**Text source:** *Lectures on The Language: An Introduction to the Study of Speech* by Edward Sapir, 1921, 
[www.gutenberg.org/Sapir](http://www.gutenberg.org/cache/epub/12629/pg12629.txt) **|** *Lectures on the Science of Language* by Max Müller, 1862, [www.gutenberg.org/Muller](http://www.gutenberg.org/files/32856/32856-0.txt)

**Actions**

*csv_generator.py:* extracts ten most frequent words and ten longest sentences for each input text file, generates .csv files (*words.csv, sentences.csv*)

*dash_visualization.py:* gets .csv files and generates visualization with Dash

## Illustrations
**Interactive charts generated with script actions:**

Scatterplot matrix of words and their frequency|length pairs 
![scatter](https://github.com/Malwoiniak/text-visualization-with-Dash/blob/master/scatter.jpg)

Stacked bar chart of word and their frequency|length pairs
![stackbar](https://github.com/Malwoiniak/text-visualization-with-Dash/blob/master/stackbar.png)

Bubble chart of sentences with respect to their length|ranking
![bubble](https://github.com/Malwoiniak/text-visualization-with-Dash/blob/master/bubble.png)

## Technologies
* Python 3.7
* Dash 1.4.0


## Setup
To run this project, install dash with pip: 

`pip install dash==1.4.0`

Input data: *Lectures on The Language: An Introduction to the Study of Speech* by Edward Sapir, 1921 *(Sapir1921_chapter1.txt)*, *Lectures on the Science of Language* by Max Müller, 1862 *(Muller1861_lecture1.txt)*, stopwords list *(stopwordlist.txt)*

## Status
Project is _in progress_. TODO: 
- [ ] .csv files manipulation with pandas for Dash visualization
- [ ] restructuring *sentences.csv* 
- [ ] bubble chart scaling correction
## Contact
Created by [@mal](https://www.linkedin.com/in/malwina-kotowicz/) - feel free to contact me!
