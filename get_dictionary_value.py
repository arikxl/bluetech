courses= {
    'js': 'Javascript 101',
    'python': 'Python 101',
    'html': 'HTML 201'
}

print(courses.get('js', None))
print(courses.get('css', None))
print(courses.get('css', 'CSS 301'))

if courses.get('css', None):
    print('You are enrolled to CSS 101')

if courses.get('js', None):
    print('You are enrolled to JS 101')


