###############CHATBOT CORPUS#######################
greetings = [['hi', 'Hi', 'Hello', 'hello', 'hello there', 'hi there'],
             ['Hello', 'Hi']]

about = [['how are you', 'how do you do'],
         ['I am fine, thank you.', "I'm good. What about you?"]]

who = [['who are you', 'tell me about yourself'],
       ['I am PythonBot - a python programming guide', 'I am python programming assitant', 'I can help you with Python Programming.']]

create = [['who created you', 'who made you'],
          ['Jayant Kashyap']]

unknown = ["Sorry! This topic doesn't fall in my domain", "Sorry! I can't answer that."]
#####################################################

#####################################################

wh_qstn_words = ['who','whom','when','where','how','why','how much','how many','how long','how far','which']
wh_qstn_tags = ['WP','WRB','JJ','NN','WDT']

ab_qstn_words = ['can','could','would','should','shall','will','do','does','did','am','is','had','have','has','are']
ab_qstn_tags = ['VB','VBZ','VBD','VBP','VBN','MD']

desc_qstn_words = ['what','tell','explain','give','describe','illustrate','define','inform','say']

verb_tags = ['VB','VBD','VBG','VBN','VBP','VBZ']

######################################################

######################################################
replacement_patterns = [
    # replacement for clitic
    (r'won\'t', 'will not'),
    (r'can\'t', 'can not'),
    (r'i\'m', 'i am'),
    (r'ain\'t', 'is not'),
    (r'(\w+)\'ll', '\g<1> will'),
    (r'(\w+)n\'t', '\g<1> not'),
    (r'(\w+)\'ve', '\g<1> have'),
    (r'(\w+)\'s', '\g<1> is'),
    (r'(\w+)\'re', '\g<1> are'),
    (r'(\w+)\'d', '\g<1> would'),

    # named entity replacement
    (r'[nN]ew [yY]ork', 'newyork'),

    # abbreviation
    (r'[dD]r\.', 'Doctor'),

    # data structures
    (r'(\w+)\(\)', '\g<1>-method'),

    # Named Entities
    (r'[gG]uido [vV]an [rR]ossum', "'Guido Van Rossum'"),
    (r'[pP]ython', "'Python'"),
    (r'[Ll]ist', "'List'")
]
######################################################
