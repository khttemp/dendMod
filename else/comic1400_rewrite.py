import struct

f = open("origin/COMIC1400.BIN", "rb")

lines = f.read()
byteArr = bytearray(lines)

index = 0x2EF

oggCntIndex = index
oggCnt = byteArr[oggCntIndex]

index += 0x122

#ogg Insert
oggList = [
    'P143_00.ogg',
    'P143_01.ogg',
    'P143_02.ogg',
    'P144_00.ogg',
    'P144_01.ogg',
    'P144_02.ogg',
    'KAN_CLASH.ogg',
]

for ogg in oggList:
    length = len(ogg)
    byteStr = bytearray()
    byteStr.extend(map(ord, ogg))
    byteArr.insert(index, length)
    index += 1
    for arr in byteStr:
        byteArr.insert(index, arr)
        index += 1
    byteArr.insert(index, 1)
    index += 1
    oggCnt += 1
    byteArr[oggCntIndex] = oggCnt

del byteArr[index+0x68:index+0x68+0x1E]

index += 0x1B
cmdCntIndex = index
cmdCnt = struct.unpack("<h", byteArr[index:index+2])[0]
index += 0x25

#Fill_BG
num = struct.pack("<hcf", 56, b'\x01', 1.0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#SkipEventFlg
num = struct.pack("<hcf", 73, b'\x01', 1.0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#PlayComicBGM
num = struct.pack("<hcfff", 76, b'\x03', 0, -1, 100)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 0, 0, 0, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 0, 0, 0, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 0, 0, 255, 90, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#VolComicBGM
num = struct.pack("<hcfff", 78, b'\x03', 0, 70, 30)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#WaitFrame
num = struct.pack("<hcf", 67, b'\x01', 30)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 22, 0, 0, 1, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#BtnWait
num = struct.pack("<hc", 60, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 1, 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 348, 455, 60, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 1, 348, 455, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 1, 0, 255, 90, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 23, 0, 0, 1, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#BtnWait
num = struct.pack("<hc", 60, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 2, 2)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -145, 455, 60, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 2, -145, 455, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 2, 0, 255, 90, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 24, 0, 0, 1, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#BtnWait
num = struct.pack("<hc", 60, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 3, 3)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 208, 958, 60, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 3, 208, 1020, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 3, 0, 255, 90, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#BtnWait
num = struct.pack("<hc", 60, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 4, 4)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -355, 958, 60, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 4, -355, 958, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 4, 0, 255, 90, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#BtnWait
num = struct.pack("<hc", 60, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#WaitMoveEye
num = struct.pack("<hcf", 66, b'\x01', 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#HideALLComic
num = struct.pack("<hc", 79, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 5)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 0, 0, 0, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 0, 0, 0, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 0, 0, 255, 90, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 28, 0, 0, 1, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#BtnWait
num = struct.pack("<hc", 60, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 1, 6)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 398, 850, 60, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 1, 398, 850, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 1, 0, 255, 90, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 25, 0, 0, 1, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#BtnWait
num = struct.pack("<hc", 60, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 2, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -155, 780, 60, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 2, -155, 780, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 2, 0, 255, 90, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 26, 0, 0, 1, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 27, 0, 0, 1, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#BtnWait
num = struct.pack("<hc", 60, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#HideALLComic
num = struct.pack("<hc", 79, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

cmdNum = struct.pack("<h", cmdCnt)
byteArr[cmdCntIndex] = cmdNum[0]
byteArr[cmdCntIndex+1] = cmdNum[1]


w = open("COMIC1400.BIN", "wb")
w.write(byteArr)
w.close()

f.close()
