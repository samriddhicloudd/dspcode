import sys,os
from urllib.parse import urlparse

def is_phish(u):
    p=urlparse(u if '://' in u else 'http://'+u)
    return int( ('@' in u) or len(u)>70 or p.scheme!='https' )

def classify(path):
    for L in open(path,encoding='utf-8',errors='ignore'):
        u=L.strip()
        if u:
            print(f"{path}\t{0 if is_phish(u) else 1}\t{u}")

if __name__=='__main__':
    if len(sys.argv)<2:
        print("usage: python mini_phish_tiny.py <file_or_folder>"); 
        sys.exit(1)
    p=sys.argv[1]
    if os.path.isdir(p):
        for r,_,fs in os.walk(p):
            for fn in fs:
                if fn.lower().endswith('.txt'): 
                    classify(os.path.join(r,fn))
    else: 
        classify(p)