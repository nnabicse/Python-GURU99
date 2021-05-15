#(:d): binary to decimal

print('The binary to decimal is: {:d}'.format(0b0011))

#(:b): decimal to binary

print('Decimal to binary is: {:b}'.format(50))

#(:e): decimal to scientific lower

print('Decimal to scientific: {:e}'.format(50))

#(:E): decimal to scientific Upper

print('Decimal to scientific: {:E}'.format(50))

#(:f) decimal to floating point

print('Decimal to floating: {:f}'.format(50))
print('Decimal to floating: {:.2f}'.format(50))

#(:o): decimal to octal

print('Decimal to Octal: {:o}'.format(500))

#(:x): decimnal to hex lower

print('Decimal to hex lower: {:x}'.format(500))

#(:X): decimnal to hex upper

print('Decimal to hex Upper: {:X}'.format(500))

#(:n)float to integer number

print('Float to integer number: {:n}'.format(500.00))

#(:%) percenrtage output

print('percentage is: {:.0%}'.format(0.8))

#(:_) underscore as thousand

print('Value is: {:_}'.format(1000000000))

#(:,) comma as thousand

print('value is: {:,}'.format(1000000000))

#(:) space before intiger

print('Value is: {:5}'.format(560))

#(:-) minus before negetive number

print('Value is {:-}'.format(-40))

#(:+) plus before positive number

print('Value is {:+}'.format(+50))

#(:=) use plus or minus before intiger

print('The value is: {:=}'.format(-40))

#(:^) align text center

print('The Value {:^10} Is positive Value'.format(50))

#(:>) right alligned text

print('This value {:>10} is Positive Number'.format(50))

#(:<) left alligned text

print('This value {:<10} is a positive value'.format(50))

#Padding space using placeholder

print('I have {0:5} dogs and {1:5} cats'.format(2,3))