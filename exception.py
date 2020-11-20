#C:\Users\admin\AppData\Local\Programs\Python\workspace\exception.py
#This comment is added on PYCHARM!!!
# 2) THIS LINE IS ADDED to exception.py AFTER new_branch IS PUSHED
class UpperCaseException(Exception):
	 print('UpperCaseException raised')

l=['hi', 'THERE']

def myException():
    try:
        for w in l:
            if w.isupper():
                raise UpperCaseException(w)
    except Exception as exc:
	    print('Exception RAISED in %s!', __file__, exc, sep='***', flush=True, end='........')