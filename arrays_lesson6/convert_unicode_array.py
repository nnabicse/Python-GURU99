import array as arr

a = arr.array('u', [u'\u0054',u'\u0041',u'\u004D',u'\u0049',u'\u004D'])
b = a.tounicode()

print(b)

