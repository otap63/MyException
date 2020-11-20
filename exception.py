######## BRAND NEW new_branch #################
################ exception.py #################
#C:\Users\admin\AppData\Local\Programs\Python\workspace\exception.py

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