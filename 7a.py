# hashit.py — minimal MD5 & SHA256 for string or file
import sys,hashlib,os
def h_str(s): return hashlib.md5(s).hexdigest(), hashlib.sha256(s).hexdigest()
def h_file(p):
    m,sha=hashlib.md5(),hashlib.sha256()
    with open(p,'rb') as f:
        for chunk in iter(lambda:f.read(8192), b''):
            m.update(chunk); sha.update(chunk)
    return m.hexdigest(), sha.hexdigest()

if __name__=='__main__':
    if len(sys.argv)<2:
        print("usage: python hashit.py <string_or_filepath>"); sys.exit(1)
    a=sys.argv[1]
    md5,sha = h_file(a) if os.path.isfile(a) else h_str(a.encode())
    print("MD5:   ", md5)
    print("SHA256:", sha)
