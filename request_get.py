import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://www.wp.pl/')

#print the response text (the content of the requested file):
# print(x.text)

f = open("test.txt", "w")
f.write(x.text)
f.close()

print('close')
