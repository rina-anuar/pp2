f = open('demofile2.txt', 'a')#Append – добавит в конец файла
#Append – создаст файл, если указанный файл не существует.
f.write('Now the file has more content!')#Откройте файл «demofile2.txt» и добавьте в него содержимое:
f.close()

f = open('demofile2.txt', 'r')
         
print(f.read())
f.close()