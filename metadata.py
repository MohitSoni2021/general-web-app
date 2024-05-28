import random

Dashboard_options = {
    'Notepad': 'notepad_page',
    'List': 'list_page',
    'Cash Manager': 'cash_manager_page',
    'WebPage Links': 'webpage_link_page'
}

query = {
    'user_password' : 'SELECT password from {tablename} WHERE username = "{username}"'
}

user_notes = {
    'Python':"coding",
    'Javascript':'coding',
    'Java':'coding',
    'C++':'coding',
    'C':'coding',
    'HTML':'coding',
    'CSS':'coding',
    'SQL':'coding',
    'PHP':'coding',
    'C#':'coding',
    'Swift':'coding',
    'Ruby':'coding',
    'Kotlin':'coding'
}

def generate_code(length):
    code = ''
    for i in range(length):
        code += chr(random.randint(45,122))
        
    return code

print(generate_code(50))