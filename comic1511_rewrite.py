import struct

f = open("origin/COMIC1511.BIN", "rb")

lines = f.read()
byteArr = bytearray(lines)

index = 0x11

imgCntIndex = index
imgCnt = byteArr[imgCntIndex]

#img Insert
imgList = [
    'ED00.bmp',
    'ED01.bmp',
    'ED02.bmp',
    'ED03.bmp',
    'ED04.bmp',
    'ED05.bmp',
    'ED06.bmp',
    'ED07.bmp',
    'P3_033_00.bmp',
    'P3_033_01.bmp',
    'P3_033_03.bmp',
    'P3_033_04.bmp',
    'P3_033_05.bmp',
    'P3_033_06.bmp',
    'P3_033_07.bmp',
    'P3_034_00.bmp',
    'P3_034_01.bmp',
    'P3_034_02.bmp',
    'P3_034_03.bmp',
    'P3_035_00.bmp',
    'P3_035_01.bmp',
    'P3_035_02.bmp',
    'P3_035_03.bmp',
    'P3_035_04.bmp',
    'P3_036_00.bmp',
    'P3_036_01.bmp',
    'P3_036_02.bmp',
    'P3_036_03.bmp',
]

index += 0x143

for img in imgList:
    length = len(img)
    byteStr = bytearray()
    byteStr.extend(map(ord, img))
    byteArr.insert(index, length)
    index += 1
    for arr in byteStr:
        byteArr.insert(index, arr)
        index += 1
    imgCnt += 1
    byteArr[imgCntIndex] = imgCnt

imgSizeIndex = index
imgSizeCnt = byteArr[imgSizeIndex]

index += 0x188

for img in imgList:
    indexNum = imgSizeCnt
    byteArr.insert(index, indexNum)
    index += 1
    num = struct.pack("<f", -1)
    for i in range(4):
        for n in num:
            byteArr.insert(index, n)
            index += 1
    imgSizeCnt += 1
    byteArr[imgSizeIndex] = imgSizeCnt


oggCntIndex = index
oggCnt = byteArr[oggCntIndex]

index += 0x120

#ogg Insert
oggList = [
    'ED00.ogg',
    'ED01.ogg',
    'ED02.ogg',
    'ED03.ogg',
    'ED04.ogg',
    'ED05.ogg',
    'ED06.ogg',
    'ED07.ogg',
    'P3_033_00.ogg',
    'P3_034_00.ogg',
    'P3_034_01.ogg',
    'P3_034_02.ogg',
    'P3_034_03.ogg',
    'P3_034_04.ogg',
    'P3_035_00.ogg',
    'P3_035_01.ogg',
    'P3_035_02.ogg',
    'P3_035_3.ogg',
    'P3_036_01.ogg',
    'P3_036_02.ogg',
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
    byteArr.insert(index, 0)
    index += 1
    oggCnt += 1
    byteArr[oggCntIndex] = oggCnt

bgmCntIndex = index
bgmCnt = byteArr[bgmCntIndex]

bgmList = [
    'summeryray.ogg'
]

index += 0x1A

for bgm in bgmList:
    length = len(bgm)
    byteStr = bytearray()
    byteStr.extend(map(ord, bgm))
    byteArr.insert(index, length)
    index += 1
    for arr in byteStr:
        byteArr.insert(index, arr)
        index += 1
    byteArr.insert(index, 1)
    index += 1
    for i in range(8):
        byteArr.insert(index, 0)
        index += 1
    bgmCnt += 1
    byteArr[bgmCntIndex] = bgmCnt

index += 1
cmdCntIndex = index
cmdCnt = struct.unpack("<h", byteArr[index:index+2])[0]
print(cmdCnt)


debug = False
if debug:
    index += 2

    #Stage_BGM_Vol
    num = struct.pack("<hcfff", 80, b'\x03', 0, 60, 0)
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
    
    index += 0xA23

    #FROM
    num = struct.pack("<hcf", 193, b'\x01', 4435)
    for n in num:
        byteArr.insert(index, n)
        index += 1
    cmdCnt += 1

    index += 0x66
else:
    index += 0xA8B

###

#HideALLComic
num = struct.pack("<hc", 79, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 23)
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
num = struct.pack("<hcfffff", 74, b'\x05', 20, 0, 0, 1, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 0, 24)
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
num = struct.pack("<hcfffff", 74, b'\x05', 21, 0, 0, 1, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 0, 25)
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
num = struct.pack("<hcff", 50, b'\x02', 0, 26)
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
num = struct.pack("<hcff", 50, b'\x02', 0, 27)
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
num = struct.pack("<hcff", 50, b'\x02', 0, 28)
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
num = struct.pack("<hcff", 50, b'\x02', 0, 29)
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
num = struct.pack("<hcfffff", 74, b'\x05', 26, 0, 0, 1, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 0, 30)
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

######

#STOP_STAGE_BGM
num = struct.pack("<hcff", 299, b'\x02', 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicBGM
num = struct.pack("<hcfff", 76, b'\x03', 1, -1, 100)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#VolComicBGM
num = struct.pack("<hcfff", 78, b'\x03', 1, 100, 30)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 31)
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
num = struct.pack("<hcff", 50, b'\x02', 1, 32)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 0, 370, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 1, 0, 370, 0, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 2, 33)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 335, 675, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 2, 335, 675, 0, 0)
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

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 3, 34)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 103, 675, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 3, 103, 675, 0, 0)
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
    
#BtnWait
num = struct.pack("<hc", 60, b'\x00')
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 4, 35)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -232, 675, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 4, -232, 675, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 4, 0, 255, 30, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#VolComicBGM
num = struct.pack("<hcfff", 78, b'\x03', 1, 70, 30)
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
num = struct.pack("<hcff", 50, b'\x02', 5, 36)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 270, 1085, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 5, 270, 1085, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 5, 0, 255, 30, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 6, 37)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -215, 1085, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 6, -215, 1083, 0, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicAlpha
num = struct.pack("<hcfffff", 52, b'\x05', 6, 0, 255, 30, 0)
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

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 38)
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
num = struct.pack("<hcfffff", 74, b'\x05', 29, 0, 0, 1, 0)
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

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 39)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 0, 550, 0, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 0, 0, 550, 0, 0)
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
num = struct.pack("<hcfffff", 74, b'\x05', 30, 0, 0, 1, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 31, 0, 0, 1, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 1, 40)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -490, 550, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 1, -490, 580, 0, 0)
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
num = struct.pack("<hcfffff", 74, b'\x05', 32, 0, 0, 1, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 2, 41)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -170, 990, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 2, -170, 990, 0, 0)
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
num = struct.pack("<hcfffff", 74, b'\x05', 33, 0, 0, 1, 0)
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

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 42)
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
num = struct.pack("<hcfffff", 74, b'\x05', 34, 0, 0, 1, 0)
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

#VolComicBGM
num = struct.pack("<hcfff", 78, b'\x03', 1, 0, 0)
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
num = struct.pack("<hcfff", 78, b'\x03', 0, 100, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 43)
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

#VolComicBGM
num = struct.pack("<hcfff", 78, b'\x03', 0, 70, 30)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 44)
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
num = struct.pack("<hcfffff", 74, b'\x05', 35, 0, 0, 1, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 1, 45)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 177, 530, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 1, 177, 530, 0, 0)
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
num = struct.pack("<hcfffff", 74, b'\x05', 36, 0, 0, 0, 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#PlayComicSE
num = struct.pack("<hcfffff", 74, b'\x05', 37, 0, 0, 0, 1)
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
num = struct.pack("<hcff", 50, b'\x02', 2, 46)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -310, 530, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 2, -310, 530, 0, 0)
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

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 47)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', 0, -30, 0, 7)
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
num = struct.pack("<hcff", 50, b'\x02', 1, 48)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -500, -30, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 1, -500, -30, 0, 0)
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
num = struct.pack("<hcfffff", 74, b'\x05', 38, 0, 0, 1, 0)
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
num = struct.pack("<hcff", 50, b'\x02', 2, 49)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#EyeMove
num = struct.pack("<hcffff", 61, b'\x04', -287, 335, 30, 7)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1
    
#ComicPos
num = struct.pack("<hcfffff", 51, b'\x05', 2, -287, 335, 0, 0)
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

#SetComic
num = struct.pack("<hcff", 50, b'\x02', 0, 50)
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
num = struct.pack("<hcfffff", 74, b'\x05', 39, 0, 0, 1, 0)
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

cmdNum = struct.pack("<h", cmdCnt)
byteArr[cmdCntIndex] = cmdNum[0]
byteArr[cmdCntIndex+1] = cmdNum[1]


w = open("COMIC1511.BIN", "wb")
w.write(byteArr)
w.close()

f.close()
