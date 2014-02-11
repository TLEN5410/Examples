names = ['Flynn', 'Tron', 'Dumont']

# dont
the_names = ''
for name in names:
    the_names += name

# do
the_names = ''.join(names)
print the_names

the_names = ' '.join(names)
print the_names

the_names = ' '.join([name for name in names if name.endswith('n')])
print the_names

# Signature in my e-mail, what is going on here?
''.join([chr(i) for i in [67,105,97,111,33]])
