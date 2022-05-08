with open("file1.txt") as f1:
    content1 = f1.readlines()

with open("file2.txt") as f2:
    content2 = f2.readlines()


result = [int(n) for n in content1 if n in content2]
print(result)