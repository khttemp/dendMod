import struct
import sys

f = open("DEND/CS_RS/CStoRS_Data/MDL/H2000_PANTA00.smf", "rb")
line = f.read()
f.close()

index = 0
MAX_BONE_COUNT = 40
MAX_NAME_SIZE = 64

meshCount = 0
frameCount = 0
animationSetCount = 0

printFRM = True
printMTRL = True
printMESH = True


def getStructNameAndLength():
    global line
    global index

    if index >= len(line):
        return ('SMF READ END!', 0)
    nameAndLength = struct.unpack("<ll", line[index:index+8])
    nameChar4 = str(hex(nameAndLength[0]))[2:]
    index += 4
    index += 4
    nameList = [int(nameChar4[x:x+2], 16) for x in range(0, len(nameChar4), 2)]
    name = ""
    for n in nameList:
        name += chr(n)

    structLen = nameAndLength[1]

    return (name, structLen)


def readSMF():
    global line
    global index
    global meshCount
    global frameCount
    global animationSetCount

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
    print("="*30)


def readFRM(frame):
    global line
    global index
    global frameCount

    if printFRM:
        print("Frame No.{0}/{1}".format(frame, frameCount-1))

    nameAndLength = getStructNameAndLength()
    if printFRM:
        print(nameAndLength[0], nameAndLength[1])
    allReadCount = nameAndLength[1]

    if printFRM:
        print("フレーム用変換行列")
    for i in range(4):
        for j in range(4):
            matrix = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printFRM:
                print(matrix, end=", ")
        if printFRM:
            print()
    if printFRM:
        print()

    if printFRM:
        print("フレームの名前", end=", ")
    fName = struct.unpack("<64s", line[index:index+MAX_NAME_SIZE])[0]
    fName = fName.decode("shift-jis")
    index += MAX_NAME_SIZE
    allReadCount -= MAX_NAME_SIZE
    if printFRM:
        print(fName)

    if printFRM:
        print("所持しているメッシュのインデックス", end=", ")
    meshNo = struct.unpack("<l", line[index:index+4])[0]
    index += 4
    allReadCount -= 4
    if printFRM:
        print(meshNo)

    if printFRM:
        print("親のフレームのインデックス", end=", ")
    parentFrameNo = struct.unpack("<l", line[index:index+4])[0]
    index += 4
    allReadCount -= 4
    if printFRM:
        print(parentFrameNo)
        print()

    if allReadCount > 0:
        obbNameAndLength = getStructNameAndLength()
        if printFRM:
            print(obbNameAndLength[0], obbNameAndLength[1])

        vCenter = []
        for i in range(3):
            vec = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            vCenter.append(vec)
        if printFRM:
            print("中心座標", vCenter)

        for i in range(3):
            vAxis = []
            for j in range(3):
                axis = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                vAxis.append(axis)
            if printFRM:
                print("ローカルXYZ軸", vAxis)

        fLength = []
        for i in range(3):
            fLen = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            fLength.append(fLen)
        if printFRM:
            print("XYZ軸の長さ", fLength)
    elif allReadCount < 0:
        print("FRM Error!", allReadCount)
        sys.exit(1)
    if printFRM:
        print("="*30)


def readANIS(anime):
    global line
    global index
    global animationSetCount

    print("No Info ANIS!")
    return


def readMESH(mesh):
    global line
    global index
    global meshCount
    global nextNameAndLength
    global subName
    global allReadCount

    print("="*30)
    print("Mesh No.{0}/{1}".format(mesh, meshCount-1))

    print(hex(index))
    nameAndLength = getStructNameAndLength()
    if printMESH:
        print(nameAndLength[0], nameAndLength[1])
    allReadCount = nameAndLength[1]

    if printMESH:
        print("メッシュの名前", end=", ")
    mName = struct.unpack("<64s", line[index:index+MAX_NAME_SIZE])[0]
    mName = mName.decode("shift-jis")
    index += MAX_NAME_SIZE
    allReadCount -= MAX_NAME_SIZE
    if printMESH:
        print(mName)

    if printMESH:
        print("所持しているマテリアルの数", end=", ")
    materialCount = struct.unpack("<l", line[index:index+4])[0]
    index += 4
    allReadCount -= 4
    if printMESH:
        print(materialCount)

    if allReadCount <= 0:
        return

    nextNameAndLength = getStructNameAndLength()
    if printMESH:
        print(nextNameAndLength[0], nextNameAndLength[1])
    subName = nextNameAndLength[0]
    allReadCount -= 8

    if subName == "OBB":
        vCenter = []
        for i in range(3):
            vec = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            vCenter.append(vec)
        if printMESH:
            print("中心座標", vCenter)

        for i in range(3):
            vAxis = []
            for j in range(3):
                axis = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                allReadCount -= 4
                vAxis.append(axis)
            if printMESH:
                print("ローカルXYZ軸", vAxis)

        fLength = []
        for i in range(3):
            fLen = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            fLength.append(fLen)
        if printMESH:
            print("XYZ軸の長さ", fLength)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "BONE":
        if printMESH:
            print("ボーンのローカルオフセット行列")
        for i in range(4):
            for j in range(4):
                matrix = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                allReadCount -= 4
                if printMESH:
                    print(matrix, end=", ")
            if printMESH:
                print()
        if printMESH:
            print()

        if printMESH:
            print("骨の対象となるフレームのインデックス", end=", ")
        frameNo = struct.unpack("<l", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMESH:
            print(frameNo)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "V_PC":
        count = nextNameAndLength[1] // 16
        for i in range(count):
            vPC = []
            for i in range(3):
                vec = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                vPC.append(vec)
            if printMESH:
                print("頂点の位置", vPC)

            if printMESH:
                print("頂点の色", end=", ")
            vPCcolor = struct.unpack("<l", line[index:index+4])[0]
            index += 4
            if printMESH:
                print(vPCcolor)
        if printMESH:
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "V_N":
        count = nextNameAndLength[1] // 12
        for i in range(count):
            vN = []
            for i in range(3):
                vec = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                allReadCount -= 4
                vN.append(vec)
            if printMESH:
                print("頂点の法線", vN)
        if printMESH:
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "V_B":
        count = nextNameAndLength[1] // 12
        for i in range(count):
            vB = []
            for i in range(3):
                vec = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                allReadCount -= 4
                vB.append(vec)
            if printMESH:
                print("頂点の接線", vB)
        if printMESH:
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "V_A":
        count = nextNameAndLength[1] // 8
        for i in range(count):
            f = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printMESH:
                print(f, end=", ")

            charList = []
            for j in range(4):
                charList.append(line[index])
                index += 1
                allReadCount -= 1
            if printMESH:
                print(charList)
        if printMESH:
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "V_UV":
        count = nextNameAndLength[1] // 16
        for i in range(count):
            if printMESH:
                print("頂点のテクスチャUV", end=", ")
            list1 = []
            for j in range(2):
                f = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                allReadCount -= 4
                list1.append(f)
            if printMESH:
                print(list1)

            if printMESH:
                print("頂点のライトマップ用テクスチャUV", end=", ")
            list2 = []
            for j in range(2):
                f = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                allReadCount -= 4
                list2.append(f)
            if printMESH:
                print(list2)

        if printMESH:
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "IDX2":
        count = nextNameAndLength[1] // 2
        for i in range(count):
            if printMESH:
                print("頂点インデックス", end=", ")
            h = struct.unpack("<h", line[index:index+2])[0]
            index += 2
            allReadCount -= 2
            if printMESH:
                print(h)

        if printMESH:
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "IDX4":
        count = nextNameAndLength[1] // 4
        for i in range(count):
            if printMESH:
                print("頂点インデックス", end=", ")
            l = struct.unpack("<l", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printMESH:
                print(l)
        if printMESH:
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "MTRL":
        for i in range(materialCount):
            readMTRL()

            if materialCount > 1:
                nextNameAndLength = getStructNameAndLength()
                if printMESH:
                    print(nextNameAndLength[0], nextNameAndLength[1])
                subName = nextNameAndLength[0]
                allReadCount -= 8

    if subName == "C_AT":
        count = nextNameAndLength[1] // 12
        for i in range(count):
            if printMESH:
                print("面の開始位置", end=", ")
            colStart = struct.unpack("<l", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printMESH:
                print(colStart)

            if printMESH:
                print("面の数", end=", ")
            colCount = struct.unpack("<l", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printMESH:
                print(colCount)

            if printMESH:
                print("面の属性", end=", ")
            colAttribute = struct.unpack("<l", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printMESH:
                print(colAttribute)

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "C_FC":
        count = nextNameAndLength[1] // 32
        for i in range(count):
            if printMESH:
                print("面の属性", end=", ")
            colAttribute = struct.unpack("<l", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printMESH:
                print(colAttribute)

            if printMESH:
                print("面を構成する頂点のインデックス", end=", ")
            indexList = []
            for i in range(3):
                iindex = struct.unpack("<l", line[index:index+4])[0]
                index += 4
                allReadCount -= 4
                indexList.append(iindex)
            if printMESH:
                print(indexList)

            if printMESH:
                print("面データ", end=", ")
            planeList = []
            for i in range(4):
                f = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                allReadCount -= 4
                planeList.append(f)
            if printMESH:
                print(planeList)

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if printMESH:
            print(nextNameAndLength[0], nextNameAndLength[1])
        subName = nextNameAndLength[0]
        allReadCount -= 8

    if subName == "C_VX":
        count = nextNameAndLength[1] // 28
        for i in range(count):
            if printMESH:
                print("頂点の位置", end=", ")
            vecList = []
            for i in range(3):
                vec = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                allReadCount -= 4
                vecList.append(iindex)
            if printMESH:
                print(vecList)

            if printMESH:
                print("頂点の色", end=", ")
            colColor = struct.unpack("<l", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printMESH:
                print(colColor)

            if printMESH:
                print("頂点の法線", end=", ")
            vecList = []
            for i in range(3):
                vec = struct.unpack("<f", line[index:index+4])[0]
                index += 4
                allReadCount -= 4
                vecList.append(iindex)
            if printMESH:
                print(vecList)


def readMTRL():
    global line
    global index
    global nextNameAndLength
    global subName
    global allReadCount

    if printMTRL:
        print("マテリアル名", end=", ")
    mName = struct.unpack("<64s", line[index:index+MAX_NAME_SIZE])[0]
    mName = mName.decode("shift-jis")
    index += MAX_NAME_SIZE
    allReadCount -= 4
    if printMTRL:
        print(mName)

    if printMTRL:
        print("ポリゴン開始位置", end=", ")
    l = struct.unpack("<l", line[index:index+4])[0]
    index += 4
    allReadCount -= 4
    if printMTRL:
        print(l)

    if printMTRL:
        print("ポリゴン数", end=", ")
    l = struct.unpack("<l", line[index:index+4])[0]
    index += 4
    allReadCount -= 4
    if printMTRL:
        print(l)

    if printMTRL:
        print("頂点開始位置", end=", ")
    l = struct.unpack("<l", line[index:index+4])[0]
    index += 4
    allReadCount -= 4
    if printMTRL:
        print(l)

    if printMTRL:
        print("頂点数", end=", ")
    l = struct.unpack("<l", line[index:index+4])[0]
    index += 4
    allReadCount -= 4
    if printMTRL:
        print(l)
        print()

    if allReadCount <= 0:
        return

    nextNameAndLength = getStructNameAndLength()
    if printMTRL:
        print(nextNameAndLength[0], nextNameAndLength[1])
    subName = nextNameAndLength[0]
    allReadCount -= 8

    if subName == "TEXC":
        if printMTRL:
            print("テクスチャ名チャンク(通常)", end=", ")
        mName = struct.unpack("<64s", line[index:index+MAX_NAME_SIZE])[0]
        mName = mName.decode("shift-jis")
        index += MAX_NAME_SIZE
        allReadCount -= MAX_NAME_SIZE
        if printMTRL:
            print(mName)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "TEXL":
        if printMTRL:
            print("テクスチャ名チャンク(ライトマップ)", end=", ")
        mName = struct.unpack("<64s", line[index:index+MAX_NAME_SIZE])[0]
        mName = mName.decode("shift-jis")
        index += MAX_NAME_SIZE
        allReadCount -= MAX_NAME_SIZE
        if printMTRL:
            print(mName)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "TEXE":
        if printMTRL:
            print("テクスチャ名チャンク(DDS)", end=", ")
        mName = struct.unpack("<64s", line[index:index+MAX_NAME_SIZE])[0]
        mName = mName.decode("shift-jis")
        index += MAX_NAME_SIZE
        allReadCount -= MAX_NAME_SIZE
        if printMTRL:
            print(mName)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "TEXS":
        if printMTRL:
            print("テクスチャ名チャンク(スペキュラー用)", end=", ")
        mName = struct.unpack("<64s", line[index:index+MAX_NAME_SIZE])[0]
        mName = mName.decode("shift-jis")
        index += MAX_NAME_SIZE
        allReadCount -= MAX_NAME_SIZE
        if printMTRL:
            print(mName)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "TEXN":
        if printMTRL:
            print("テクスチャ名チャンク(法線マップ用)", end=", ")
        mName = struct.unpack("<64s", line[index:index+MAX_NAME_SIZE])[0]
        mName = mName.decode("shift-jis")
        index += MAX_NAME_SIZE
        allReadCount -= MAX_NAME_SIZE
        if printMTRL:
            print(mName)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "DRAW":
        if printMTRL:
            print("マテリアルの描画属性", end=", ")
        l = struct.unpack("<l", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMTRL:
            print(l)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "ZTES":
        if printMTRL:
            print("Zテスト", end=", ")
        l = struct.unpack("<l", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMTRL:
            print(l)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "ZWRI":
        if printMTRL:
            print("Z書き込み", end=", ")
        l = struct.unpack("<l", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMTRL:
            print(l)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "ATES":
        if printMTRL:
            print("アルファテスト", end=", ")
        l = struct.unpack("<l", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMTRL:
            print(l)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "ABND":
        if printMTRL:
            print("アルファテスト(閾値)", end=", ")
        l = struct.unpack("<l", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMTRL:
            print(l)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "CULL":
        if printMTRL:
            print("背面カリング", end=", ")
        l = struct.unpack("<l", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMTRL:
            print(l)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "LGT":
        if printMTRL:
            print("ライティング", end=", ")
        l = struct.unpack("<l", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMTRL:
            print(l)
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "DIFF":
        if printMTRL:
            print("拡散反射の色")
        for i in range(4):
            vec = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printMTRL:
                print(vec, end=", ")
        if printMTRL:
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "EMIS":
        if printMTRL:
            print("自己発光の色")
        for i in range(3):
            vec = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printMTRL:
                print(vec, end=", ")
        if printMTRL:
            print()

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "SPEC":
        if printMTRL:
            print("スペキュラーの色", end=", ")
        for i in range(3):
            vec = struct.unpack("<f", line[index:index+4])[0]
            index += 4
            allReadCount -= 4
            if printMTRL:
                print(vec, end=", ")
        if printMTRL:
            print()

        if printMTRL:
            print("反射率（大きいほど強い反射）", end=", ")
        fRefractive = struct.unpack("<f", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMTRL:
            print(fRefractive)

        if printMTRL:
            print("荒さ（大きいほどソフトな反射）", end=", ")
        fRoughly = struct.unpack("<f", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMTRL:
            print(fRoughly)

        if allReadCount <= 0:
            return

        nextNameAndLength = getStructNameAndLength()
        if nextNameAndLength[0] in ["MESH", "MTRL"]:
            index -= 8
        else:
            if printMTRL:
                print(nextNameAndLength[0], nextNameAndLength[1])
            subName = nextNameAndLength[0]
            allReadCount -= 8

    if subName == "BUMP":
        if printMTRL:
            print("視差マップ用の視差", end=", ")
        fParallaxDepth = struct.unpack("<f", line[index:index+4])[0]
        index += 4
        allReadCount -= 4
        if printMTRL:
            print(fParallaxDepth)

        if allReadCount <= 0:
            return

    print("="*20)
    print()

###

nameAndLength = getStructNameAndLength()
print(nameAndLength[0], nameAndLength[1])
readSMF()

for frame in range(frameCount):
    readFRM(frame)

for anime in range(animationSetCount):
    readANIS(anime)

for mesh in range(meshCount):
    readMESH(mesh)
