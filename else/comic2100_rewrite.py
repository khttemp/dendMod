import struct

f = open("origin/COMIC2100.BIN", "rb")

lines = f.read()
byteArr = bytearray(lines)

index = 0

index += 0x5E0
cmdCntIndex = index
cmdCnt = struct.unpack("<h", byteArr[index:index+2])[0]
print(cmdCnt)

index += 0x175C

###

#CHK_TRAIN_TYPE
num = struct.pack("<hcffff", 195, b'\x04', 0, 2, 100, 200)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#FROM
num = struct.pack("<hcf", 193, b'\x01', 100)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#SET_CAM_TARGET_OFFSET
num = struct.pack("<hcffffff", 301, b'\x06', 0, 11, 1, 0, 7, 30)
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


#TRAIN_ANIME_CHANGE
num = struct.pack("<hcffff", 420, b'\x04', 0, 0, 0, 3)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#TRAIN_ANIME_CHANGE
num = struct.pack("<hcffff", 420, b'\x04', 0, 7, 0, 3)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1


#GOTO
num = struct.pack("<hcf", 194, b'\x01', 300)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#FROM
num = struct.pack("<hcf", 193, b'\x01', 200)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#CHK_TRAIN_TYPE
num = struct.pack("<hcffff", 195, b'\x04', 0, 11, 100, 200)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#FROM
num = struct.pack("<hcf", 193, b'\x01', 100)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#SET_CAM_TARGET_OFFSET
num = struct.pack("<hcffffff", 301, b'\x06', 0, 11, 1, 0, 7, 30)
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


#TRAIN_ANIME_CHANGE
num = struct.pack("<hcffff", 420, b'\x04', 0, 0, 8, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#TRAIN_ANIME_CHANGE
num = struct.pack("<hcffff", 420, b'\x04', 0, 3, 8, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1


#GOTO
num = struct.pack("<hcf", 194, b'\x01', 300)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#FROM
num = struct.pack("<hcf", 193, b'\x01', 200)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#CHK_TRAIN_TYPE
num = struct.pack("<hcffff", 195, b'\x04', 0, 12, 100, 200)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#FROM
num = struct.pack("<hcf", 193, b'\x01', 100)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#SET_CAM_TARGET_OFFSET
num = struct.pack("<hcffffff", 301, b'\x06', 0, 11, 1, 0, 7, 30)
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


#TRAIN_ANIME_CHANGE
num = struct.pack("<hcffff", 420, b'\x04', 0, 0, 8, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#TRAIN_ANIME_CHANGE
num = struct.pack("<hcffff", 420, b'\x04', 0, 3, 8, 0)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1


#GOTO
num = struct.pack("<hcf", 194, b'\x01', 300)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#FROM
num = struct.pack("<hcf", 193, b'\x01', 200)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

#CHK_TRAIN_TYPE
num = struct.pack("<hcffff", 195, b'\x04', 0, 16, 100, 200)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#FROM
num = struct.pack("<hcf", 193, b'\x01', 100)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#SET_CAM_TARGET_OFFSET
num = struct.pack("<hcffffff", 301, b'\x06', 0, 11, 1, 0, 7, 30)
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


#GOTO
num = struct.pack("<hcf", 194, b'\x01', 300)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#FROM
num = struct.pack("<hcf", 193, b'\x01', 200)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

index += 0x62

#GOTO
num = struct.pack("<hcf", 194, b'\x01', 300)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

index += 0x84

#GOTO
num = struct.pack("<hcf", 194, b'\x01', 300)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

index += 0x7

#CHK_TRAIN_TYPE
num = struct.pack("<hcffff", 195, b'\x04', 0, 0, 100, 200)
for n in num:
    byteArr[index] = n
    index += 1

index += 0x4F

#GOTO
num = struct.pack("<hcf", 194, b'\x01', 300)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#FROM
num = struct.pack("<hcf", 193, b'\x01', 200)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#SET_CAM_TARGET_OFFSET
num = struct.pack("<hcffffff", 301, b'\x06', 0, 11, 1, 0, 7, 30)
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

#TRAIN_ANIME_CHANGE
num = struct.pack("<hcffff", 420, b'\x04', 0, 0, 8, 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#TRAIN_ANIME_CHANGE
num = struct.pack("<hcffff", 420, b'\x04', 0, 3, 8, 1)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

#FROM
num = struct.pack("<hcf", 193, b'\x01', 300)
for n in num:
    byteArr.insert(index, n)
    index += 1
cmdCnt += 1

###

cmdNum = struct.pack("<h", cmdCnt)
byteArr[cmdCntIndex] = cmdNum[0]
byteArr[cmdCntIndex+1] = cmdNum[1]


w = open("COMIC2100.BIN", "wb")
w.write(byteArr)
w.close()

f.close()
