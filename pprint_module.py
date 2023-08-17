from pprint import pprint
my_dict = {
    'name': 'Dhruv',
    'age': 30,
    'address': {
    'Village': 'Govindpur',
    'District': 'Amreli',
    'Postal': 365640
    },
    'Hobbies': ['reading', 'coding']
}
print(my_dict)   # this will print direct straight line of the entire dictionary,
                 # which is not quite readeable.

pprint(my_dict)  # Wihle this will print the proper, as we have written, dictionary,
                 # which looks pretty much readeable...

''' Output of normal print function 
    {'name': 'Dhruv', 'age': 30, 'address': {'Village': 'Govindpur', 'District': 'Amreli', 'Postal': 365640}, 'Hobbies': ['reading', 'coding']}
    
    Output of pprint (pretty print) function
    {'Hobbies': ['reading', 'coding'],
     'address': {'District': 'Amreli', 'Postal': 365640, 'Village': 'Govindpur'},
     'age': 30,
     'name': 'Dhruv'}
    '''
