import struct

name = input("input comic binFile:")
index = 16
f = open(name, "rb")
line = f.read()
index += 1

#ReadComicImg
imgCnt = line[index]
index += 1
for i in range(imgCnt):
    b = line[index]
    index += 1
    text = line[index:index+b].decode()
    print(text)
    index += b
print()

#ReadComicSize

b = line[index]
index += 1
for i in range(b):
    index += 1
    for j in range(4):
        text = line[index:index+4]
        if struct.unpack("<f", text)[0] != -1:
            print("ReadComicSize Error!")
        index += 4
print()
#ReadSE

secnt = line[index]
index += 1
for i in range(secnt):
    b = line[index]
    index += 1
    text = line[index:index+b].decode()
    print(text)
    index += b
    index += 1
print()

#ReadBGM
bgmcnt = line[index]
index += 1
for i in range(bgmcnt):
    b = line[index]
    index += 1
    text = line[index:index+b].decode()
    print(text)
    index += b
    index += 1
    index += 4
    index += 4
print()

#ReadComicData
index += 1
num = struct.unpack("<H", line[index:index+2])[0]
index += 2
for i in range(num):
    num2 = struct.unpack("<H", line[index:index+2])[0]
    index += 2
    print("num2", num2)
    b = line[index]
    print("float array length", b)
    index += 1
    p_str = []
    for j in range(b):
        if j == 0 and num2 == 193:
            p_str.append(struct.unpack("<f", line[index:index+4])[0])
        print(struct.unpack("<f", line[index:index+4])[0], end=" ")
        index += 4

    if len(p_str) > 0:
        print(p_str, end=" ")
    print("No."+ str(i))
    
f.close()
