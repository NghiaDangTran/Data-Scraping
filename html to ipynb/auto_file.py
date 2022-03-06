from bs4 import BeautifulSoup
import urllib.request
import codecs
import codecs
import io
import re





url = 'https://imic.edu.vn/training/basic-python/Phan-03-Kien-thuc-Python-co-ban-2022.html'
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response.read(), 'html.parser')


file = codecs.open("notebook.txt", "w+", "utf-8")
file.write(soup.get_text())
file.close()


f = io.open("notebook.txt", mode="r", encoding="utf-8")
data = f.readlines()
count = 0
curr1 = 0
curr2 = 0


while count < len(data):

    if "In" in data[count] and "[" in data[count] and "]" in data[count]:

        data.pop(count)
        data.insert(count, "## %% \n")
        count += 1
        while data[count] == "\n":
            data.remove(data[count])
            count += 1
        curr1 = count

        while data[count] != "\n":
            count += 1
        curr2 = count
        for i in range(curr1, curr2-1):
            if re.match(r'\s', data[i]):
                data[i] = data[i][4:]
            data[i] = "#"+data[i]
        data.pop(curr2-1)
        data[curr2] = '## %% [markdown]\n'

    elif data[count] == '\n':
        data.pop(count)

    else:
        count += 1


print(data)
file = codecs.open("File_PY.py", "w+", "utf-8")
file.writelines("\n# %% [markdown]\n")
for line in data:
    if line[0] == "#":
        file.write(line[1:])

    elif line[len(line)-2] == '¶':
        file.write(" # "+line+"\n")
    else:
        file.write("#"+line+"\n")

file.close()
