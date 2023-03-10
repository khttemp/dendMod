import struct
import codecs

index = 0
textList = []

def inputText(mode):
    global start
    global end
    
    while start <= end:
        try:
            if mode == 1:
                text = struct.pack(">B", start).decode("cp932")
            elif mode == 2:
                text = struct.pack(">H", start).decode("cp932")
                if len(text) != 1:
                    start += 1
                    continue
            #重複文字は除く
            if text not in textList:
                textList.append(text)
        except:
            pass
        finally:
            start += 1

def writeText():
    global textList
    
    count = 0
    w = codecs.open("text.txt", "w", "cp932", "strict")

    for text in textList:
        w.write(text)
        count += 1
        if count % 10 == 0:
            w.write("\n")
        else:
            w.write("\t")
    w.close()

#ASCII文字
start = 0x21
end = 0x7E
inputText(1)

#半角
start = 0xA1
end = 0xDF
inputText(1)

#全角
start = 0x8141
end = 0xFFFF
inputText(2)

def getName():
    global index
    global line

    nameChar4 = struct.unpack("<l", line[index:index+4])[0]
    nameChar4 = str(hex(nameChar4))[2:]
    index += 4
    nameList = [int(nameChar4[x:x+2], 16) for x in range(0, len(nameChar4), 2)]
    name = ""
    for n in nameList:
        name += chr(n)

    return name

f = open("FONT.SFF", "rb")
line = f.read()
f.close()

print("GUID:", getName())

fontSize = line[index]
index += 1
print("FontSize:", fontSize)

sheetMax = line[index];
index += 1
print("SheetMax:", sheetMax)

fontMax = struct.unpack("<h", line[index:index + 2])[0]
index += 2
print("FontMax:", fontMax)

indexTable = []
for i in range(len(textList)):
    idx = struct.unpack("<h", line[index:index + 2])[0]
    index += 2
    if idx != -1:
        indexTable.append(i)

for i in range(sheetMax):
    sheetName = struct.unpack("<32s", line[index:index + 32])[0]
    sheetName = sheetName.decode("shift-jis")
    index += 32

    print("SheetName:", sheetName)

for i in range(fontMax):
    print(hex(index), end=", ")
    sheetNo = line[index]

    print("【{0}】 -> ".format(textList[indexTable[i]]), end=" ")
    print(sheetNo, end=", ")
    index += 1

    # left padding?
    print(line[index], end=", ")
    index += 1

    # x1
    print(line[index], end=", ")
    index += 1

    # x2
    print(line[index], end=", | ")
    index += 1

    # y1
    print(line[index], end=", | ")
    index += 1

    # No, offset?
    print(line[index], end=", | ")
    index += 1
    print(line[index], end=", | ")
    index += 1

    # y2
    print(line[index], end=", | ")
    index += 1

    print()