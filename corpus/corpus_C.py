# models = {
#     'list-method': 'method',
#     "'Guido Van Rossum'": 'person',
#     "'Python'": 'NN',
#     "'List'": 'NN'
# }

# person = {
#     'create': {
#         'python': 'Guido Van Rossum',
#         'foundation': 'Python Foundation'
#     },
# }
#
# date = {
#     'created': '1-1-2018',
#     'date': 'jan-1-2018'
# }
#
# location = {
#     'place': 'San Francisco',
#     'founded': 'New Delhi'
# }
#
# definition = {
#     'list': 'list is a data structure',
#     'dictionary': 'dictionary is a data structure'
# }
#
# reason = {
#     'list': 'yes, it can'
# }

person = {
    ("who created python", "who is the creator of python", "who made python",): "Guido van Rossum",
    ("who are developers", "who are python developers"): "Developers are coders. You can find details in https://www.python.org/dev/",
    ("who is guido van rossum","who guido van rossum"): "Creator of Python Programming Language"
}
date = {
    ("when was python created", "when was python founded"): "Python's implementation began in December 1989 by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands",
    ("when the next version of python will be released"): "You can find that on https://docs.python.org/3.7/whatsnew/3.7.html",
}
location_reference = {
    ("where was python created", "where was python founded"): "Netherlands",
    ("where can i find reference", "where can i find python documentations"): "At https://docs.python.org/",
    ("whom should i talk", "whom should i ask questions"): "Talk to the people at https://www.python.org/community/forums/"
}
definition = {
    ('what is python', 'what is python programming language', 'define python', 'explain python'): "Python is a high-level general-purpose programming language that can be applied to many different classes of problems.",
    # LISTS
    ("what is a list","what are lists", "define list", "what is list", "explain lists"): "List is a data structure. List store data in sequence and it is mutable.",
    ("what are list methods", "define list methods", "describe list methods"): "List methods are: append(), insert(), pop() and many more. To know more about list methods type dir(list)",
    ("what is the difference between list and tuple"): "Lists are mutable while tuples are immutable.",
    # TUPLE
    ("what is a tuple", "what are tuples", "define tuples", "what is tuple", "explain tuple"): "Tuple is a data structure in Python which is immutable.",
    ("what are tuple methods", "define tuple methods", "describe tuple methods"): "Tuples methods are count(), any(), filter() and many more. To know more about list mehods type dir(tuple)",
    # DICTIONARY
    ("what is a dictionary", "what is dictionary", 'define dictionary', "explain dictionary"): "Dictionary is a data structure that stores key value pairs.",
    ("what are dictionary methods", "define dictionary methods", "describe dictionary methods"): "Dictionary methods are keys(), values(), items(), and many more. To know more about dictionary type dir(dict)",
    ("what is list comprehension", "define list comprehension"): "List comprehension is process of creating a list using a for loop in the list",
    ("what is dictionary comprehension","define dictionary comprehension"): "Dictionary comprehension is process of creating a dictionary using a for loop in the list",
    ("what are modules","define modules"): "Modules are python packages",
}
methodology = {
    ("how is list implemented","how to implement list"): "List is implemented using list() function",
    ("how is dictionary implemented","how to implement dictionary"): "Dictionary is implemented using dict() function",
    ("how is tuple implemented","how to implement tuple"): "Tuple is implemented using tuple() function",
    ("how to implement list comprehension"): "List comprehension is implemented using for loop inside list",
    ("how to implement dictionary comprehension"): "Dictionary comprehension is implemented using for loop in dictionary",
    ("how is python object-oriented language"): "Python is object-oriented because it follows all the rules of OO-language"
}
numbers = {
    ("how many lists are there","how many"): "There are many list methods",
}
reason = {
    ("why is tuple immutable", "why are tuples immutable"): "Tuple is immutable to not allow any change in the data type",
    ("why"): "What do you want?",
}
ability = {
    ("can we implement inheritence in python"): "Yes we can.",
    ("can we"): "No. You can not."
}

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
              'yo','you', 'your', 'yours', 'yourself', 'yourselves', 'he',
              'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it',
              'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
              'this', 'that', 'these', 'those', 'having', 'doing', 'a', 'an', 'the',
              'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
              'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during',
              'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on',
              'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'all',
              'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
              'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'just', 'now', 'd', 'll', 'm', 'o']

action_verbs = ['created', 'founded', 'create', 'wrote', 'implemented']
