import chardet
f = open('tt.txt','r')
f1=open('file.txt','r')
data = f.read()
print chardet.detect(data)
print chardet.detect(f1.read())