dict = {'Tim':18, 'Charlie':12, 'Tiffany':22, 'Robart':250}

boys = {'Tim':18, 'Charlie':12, 'Robart':25, 'Karlos':50}
girls = {'Tiffany':22}

for key in list(boys.keys()):
    if key in list (dict.keys()):
        print('True')
    else:
        print('False')