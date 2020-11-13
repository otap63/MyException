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
	    print('Exception RAISED!', exc, sep='***', flush=True, end='........')