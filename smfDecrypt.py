import os
import struct

f = open("DenD_RS_Data/MDL/H2000_TRACK.SMF", "rb")
line = f.read()
f.close()

index = 0
MAX_BONE_COUNT = 40
MAX_NAME_SIZE = 64

def getStructNameAndLength():
    global line
    global index

    nameChar4 = struct.unpack("<4c", line[index:index+4])
    index += 4
    name = bytearray()
    for i in range(3, -1, -1):
        if nameChar4[i] == b'\x00':
            continue
        name.append(ord(nameChar4[i]))
    name = name.decode("shift-jis")

    structLen = struct.unpack("<I", line[index:index+4])[0]
    index += 4
    
    return (name, structLen)

### SMF_FILEHEAD ###

nameAndLength = getStructNameAndLength()
print(nameAndLength[0], nameAndLength[1])

guid = struct.unpack("<L", line[index:index+4])[0]
index += 4
print("バージョン識別子", hex(guid))

meshCount = struct.unpack("<l", line[index:index+4])[0]
index += 4
print("メッシュの数", meshCount)

frameCount = struct.unpack("<l", line[index:index+4])[0]
index += 4
print("フレームの数", frameCount)

animationSetCount = struct.unpack("<l", line[index:index+4])[0]
index += 4
print("アニメーションの数", animationSetCount)

### SMF_FRAMEDATA ###

for frame in range(frameCount):
    print("Frame.No.{0}/{1}".format(frame+1, frameCount))
    print("="*30)
    nameAndLength = getStructNameAndLength()
    print(nameAndLength[0], nameAndLength[1])

    print("フレーム用変換行列")
    for i in range(4):
        for j in range(4):
            matrix = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            print(matrix, end=", ")
        print()
    print()

    print("フレームの名前", end=", ")
    fName = struct.unpack("<64s", line[index:index+MAX_NAME_SIZE])[0]
    fName = fName.decode("shift-jis")
    index += MAX_NAME_SIZE
    print(fName)

    print("所持しているメッシュのインデックス", end=", ")
    meshNo = struct.unpack("<l", line[index:index+4])[0]
    index += 4
    print(meshNo)

    print("親のフレームのインデックス", end=", ")
    parentFrameNo = struct.unpack("<l", line[index:index+4])[0]
    index += 4
    print(parentFrameNo)

    if nameAndLength[1] > 136:
        ### SMF_OBBDATA ###
        obbNameAndLength = getStructNameAndLength()
        print(obbNameAndLength[0], obbNameAndLength[1])

        vCenter = []
        for i in range(3):
            vec = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            vCenter.append(vec)
        print("中心座標", vCenter)

        for i in range(3):
            vAxis = []
            for j in range(3):
                axis = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                vAxis.append(axis)
            print("ローカルXYZ軸", vAxis)

        fLength = []
        for i in range(3):
            fLen = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            fLength.append(fLen)
        print("XYZ軸の長さ", fLength)


### SMF_MESHDATA ###

for mesh in range(meshCount):
    print("Mesh.No.{0}/{1}".format(frame+1, frameCount))
    print("="*30)

    nameAndLength = getStructNameAndLength()
    print(nameAndLength[0], nameAndLength[1])

    print("メッシュの名前", end=", ")
    mName = struct.unpack("<64s", line[index:index+MAX_NAME_SIZE])[0]
    mName = mName.decode("shift-jis")
    index += MAX_NAME_SIZE
    print(mName)

    materialCount = struct.unpack("<l", line[index:index+4])[0]
    index += 4
    print(materialCount)

    nextNameAndLength = getStructNameAndLength()
    print(nextNameAndLength[0], nextNameAndLength[1])
    input()
