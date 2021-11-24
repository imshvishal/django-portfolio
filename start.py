import os
check = {
    'r': 'runserver',
    'm': 'migrate',
    'mm': 'makemigrations'
}
while True:
    inp = input("Enter the command: ")
    os.system(f'python manage.py {check.get(inp, inp)}')