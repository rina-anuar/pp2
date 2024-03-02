f = open('demofile3.txt', 'w')#Write – перезапишет любой существующий контент.
#Write - создаст файл, если указанный файл не существует

f.write('Woops! I have deleted the content!')
f.close()

f = open('demofile3.txt', 'r')
print(f.read())
