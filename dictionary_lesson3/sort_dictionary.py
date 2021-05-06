dict = {'Tim':18, 'Charlie':12, 'Tiffany':22, 'Robart':250}

students = list(dict.keys())

students.sort()

for key in students:

    print(":".join((key,str(dict[key]))))