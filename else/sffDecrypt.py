import struct
import codecs

allHexTextList = []

f = open("KeyCodeTable.inc", encoding="cp932")
lines = f.readlines()
f.close()

for idx, line in enumerate(lines):
    if line.find("//") == 0 or "//" in line:
        continue
    arr = line.strip().split("\t")
    textIndex = int(arr[0].strip(","), 16)
    if textIndex != 0xFFFF:
        allHexTextList.append(idx)

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

def getName(line, index):
    nameChar4 = struct.unpack("<l", line[index:index+4])[0]
    nameChar4 = str(hex(nameChar4))[2:]
    index += 4
    nameList = [int(nameChar4[x:x+2], 16) for x in range(0, len(nameChar4), 2)]
    name = ""
    for n in nameList:
        name += chr(n)

    return name

def convertFontSheetData(lines):
    bitIndex = 0
    bitString = ""
    for line in lines:
        bitString = "{:08b}".format(line) + bitString

    y2 = bitString[bitIndex:bitIndex+11]
    bitIndex += 11

    x2 = bitString[bitIndex:bitIndex+11]
    bitIndex += 11

    y1 = bitString[bitIndex:bitIndex+11]
    bitIndex += 11

    x1 = bitString[bitIndex:bitIndex+11]
    bitIndex += 11

    right = bitString[bitIndex:bitIndex+6]
    bitIndex += 6

    left = bitString[bitIndex:bitIndex+6]
    bitIndex += 6

    sheetNo = bitString[bitIndex:bitIndex+8]
    bitIndex += 8

    fontSheetData = [
        int(sheetNo, 2),
        int(left, 2),
        int(right, 2),
        int(x1, 2),
        int(y1, 2),
        int(x2, 2),
        int(y2, 2)
    ]
    return fontSheetData

index = 0
f = open("FONT.SFF", "rb")
line = f.read()
f.close()

print("GUID:", getName(line, index))
index += 4

fontSize = line[index]
index += 1
print("FontSize:", fontSize)

sheetMax = line[index]
index += 1
print("SheetMax:", sheetMax)

fontMax = struct.unpack("<h", line[index:index + 2])[0]
index += 2
print("FontMax:", fontMax)

zenkakuIndex = 157
inputTableList = []
for i in range(len(allHexTextList)):
    idx = struct.unpack("<h", line[index:index + 2])[0]
    index += 2
    if idx != -1:
        if i < zenkakuIndex:
            text = struct.pack(">B", allHexTextList[i]).decode("cp932")
        else:
            text = struct.pack(">H", allHexTextList[i]).decode("cp932")
        inputTableList.append(text)

for i in range(sheetMax):
    sheetName = struct.unpack("<32s", line[index:index + 32])[0]
    sheetName = sheetName.decode("shift-jis")
    index += 32

    print("SheetName:", sheetName)

for i in range(fontMax):
    fontSheetData = convertFontSheetData(line[index:index + 8])
    index += 8
    print(inputTableList[i], fontSheetData)
