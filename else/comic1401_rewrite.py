import struct

f = open("origin/COMIC1401.BIN", "rb")

lines = f.read()
byteArr = bytearray(lines)

index = 0x885

oggCntIndex = index
oggCnt = byteArr[oggCntIndex]

index += 0x269

#ogg Insert
oggList = [
    'P171_00.ogg',
    'P171_01.ogg',
    'P171_02.ogg',
    'P171_03.ogg',
    'P171_04.ogg',
    'P171_05.ogg',
    'P172_00_I.ogg',
    'P172_00_T.ogg',
    'P172_01_I.ogg',
    'P172_01_T.ogg',
    'P172_02_I.ogg',
    'P172_02_T.ogg',
    'P172_03.ogg',
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


index += 0x47
cmdCntIndex = index
cmdCnt = struct.unpack("<h", byteArr[index:index+2])[0]

debug = False
if debug:
    index += 2
    #Fill_BG
    num = struct.pack("<hcf", 56, b'\x01', 1.0)
    for n in num:
        byteArr.insert(index, n)
        index += 1
    cmdCnt += 1
    
    #GOTO
    num = struct.pack("<hcf", 194, b'\x01', 4435)
    for n in num:
        byteArr.insert(index, n)
        index += 1
    cmdCnt += 1

    index += 0x1DAB
    #FROM
    num = struct.pack("<hcf", 193, b'\x01', 4435)
    for n in num:
        byteArr.insert(index, n)
        index += 1
    cmdCnt += 1

else:
    index += 0x1DAD

#HideALLComic
num = struct.pack("<hc", 79, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#StopComicBGM
num = struct.pack("<hcff", 77, b'\x02', 2, 0)
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

#VolComicBGM
num = struct.pack("<hcfff", 78, b'\x03', 0, 100, 30)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###
    
#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 49)
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
num = struct.pack("<hcfffff", 52, b'\x05', 0, 0, 255, 30, 0)
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

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 50)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 0, 52, 0, 7)
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
num = struct.pack("<hcfffff", 52, b'\x05', 0, 0, 255, 30, 0)
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

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 47, 0, 0, 1, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 1, 51)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -525, 52, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 1, -525, 52, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 1, 0, 255, 30, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 48, 0, 0, 1, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 49, 0, 0, 1, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 2, 52)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 40, 532, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 2, 40, 535, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 2, 0, 255, 30, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 50, 0, 0, 1, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 3, 53)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -457, 532, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 3, -457, 532, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 3, 0, 255, 30, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 51, 0, 0, 1, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 52, 0, 0, 1, 0)
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

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 54)
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
num = struct.pack("<hcfffff", 52, b'\x05', 0, 0, 255, 30, 0)
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

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 55)
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
num = struct.pack("<hcfffff", 52, b'\x05', 0, 0, 255, 30, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 53, 0, 0, 0, 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 54, 0, 0, 0, 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#WaitFrame
num = struct.pack("<hcf", 67, b'\x01', 210)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 1, 56)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 0, 450, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 1, 0, 450, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 1, 0, 255, 30, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 55, 0, 0, 0, 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 56, 0, 0, 0, 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#WaitFrame
num = struct.pack("<hcf", 67, b'\x01', 210)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 57, 0, 0, 0, 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 58, 0, 0, 0, 1)
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

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 57)
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
num = struct.pack("<hcfffff", 52, b'\x05', 0, 0, 255, 30, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 59, 0, 0, 1, 0)
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

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 58)
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
num = struct.pack("<hcfffff", 52, b'\x05', 0, 0, 255, 30, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 1, 59)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 167, 385, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 1, 167, 388, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 1, 0, 255, 30, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 2, 60)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -325, 385, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 2, -325, 385, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 2, 0, 255, 30, 0)
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

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 61)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 275, 0, 0, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 0, 275, 0, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 0, 0, 255, 30, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 1, 62)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -275, 0, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 1, -275, 45, 0, 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 1, 0, 255, 30, 0)
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

cmdNum = struct.pack("<h", cmdCnt)
byteArr[cmdCntIndex] = cmdNum[0]
byteArr[cmdCntIndex+1] = cmdNum[1]


w = open("COMIC1401.BIN", "wb")
w.write(byteArr)
w.close()

f.close()
