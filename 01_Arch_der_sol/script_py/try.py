f = None
try:
    f = open("test.txt")
except IOError:
    print('Could not open file')
    pass
finally:
    if f is not None:
        f.close()
print('Program continue')