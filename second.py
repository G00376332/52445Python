#Program that reads in text file.

txt = open('Aladdin.txt', 'r')
m = []
txt_lenght = len(txt.readlines())
print(txt_lenght)
lines = txt.readline()
row = lines.split()
for x in range(txt_lenght):
    m.append(row[1])
print(m)
txt.close()
