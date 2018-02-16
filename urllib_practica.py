import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://github.com/ralsina/python-no-muerde/blob/master/intro.txt')
for line in fhand:
    print(line.decode().strip())