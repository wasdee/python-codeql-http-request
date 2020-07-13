# https://help.semmle.com/QL/learn-ql/python/ql-for-python.html
error = True
if error: pass

x = None

def reset_this_world():
    return 123

for var in range(123):
    pass
else:
    x = 12