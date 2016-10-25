import math

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    print max(a, b)
    """if a>b:
        print a
    else:
        print b
    """

    #
    ####################################################

    fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!'  # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
print round(1.5)