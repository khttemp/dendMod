import struct
import codecs
import os

def search(file, ext):
    folders = [
        "Patch_4th_7",
        "Patch_4th_6",
        "Patch_4th_4",
        "Patch_4th_3",
        "Patch_4th_2",
        "Patch_4th_1",
        "Patch_4th_0",
        "DenD_RS_Data",
        "CStoRS007",
        "CStoRS006",
        "CStoRS005",
        "CStoRS004",
        "CStoRS003",
        "CStoRS002",
        "CStoRS001",
        "CStoRS000",
        "CStoRS_Data"
    ]

    for folder in folders:
        path = folder
        if ext == "smf":
            path += "/MDL/"
        else:
            path += "/"

        path += file

        if os.path.exists(path):
            return path

    return "-"

f = open("Patch_4th_4/MDLINFO.BIN", "rb")
line = f.read()
f.close()

index = 16
allcnt = struct.unpack("<h", line[index:index+2])[0]
index += 2

printFlag = False
w = codecs.open("MDLINFO.csv", "w", "utf-8", "ignore")
w.write("SMF,smf_path,bin,bin_path\n")

for c in range(allcnt):
    #if c >= mdlIdx:
    #    printFlag = True
    smfLen = line[index]
    index += 1
    smfName = line[index:index+smfLen].decode("shift-jis")
    index += smfLen
    print("No.{0}->{1}".format(c, smfName))

    mdlcnt = line[index]
    index += 1
    for i in range(mdlcnt):
        if printFlag:
            print("mdl No.{0}".format(i))
        b = struct.unpack("<b", line[index].to_bytes(1, "big"))[0]
        if printFlag:
            print(b)
        index += 1
        if "AMB_" not in smfName and b > 0:
            for j in range(b):
                imgLen = line[index]
                index += 1
                imgName = line[index:index+imgLen].decode("shift-jis")
                index += imgLen
                if printFlag:
                    print(imgName)
            
        for j in range(6):
            b = struct.unpack("<b", line[index].to_bytes(1, "big"))[0]
            if printFlag:
                print(b, end=", ")
            index += 1
        if printFlag:
            print()
        for j in range(4):
            f = struct.unpack("<f", line[index:index+4])[0]
            if printFlag:
                print(f, end=", ")
            index += 4
        if printFlag:
            print()

        if printFlag:
            print(line[index])
        index += 1
        
        for j in range(3):
            f = struct.unpack("<f", line[index:index+4])[0]
            if printFlag:
                print(f, end=", ")
            index += 4
        if printFlag:
            print()

        for j in range(3):
            b = struct.unpack("<b", line[index].to_bytes(1, "big"))[0]
            if printFlag:
                print(b, end=", ")
            index += 1
        if printFlag:
            print()
            
    if printFlag:
        print("mdl End!")

    mdlcnt2 = struct.unpack("<b", line[index].to_bytes(1, "big"))[0]
    index += 1
    if mdlcnt2 > 0:
        for i in range(mdlcnt2):
            imgLen = line[index]
            index += 1
            imgName = line[index:index+imgLen].decode("shift-jis")
            index += imgLen
            if printFlag:
                print(imgName)
        if printFlag:
            print("mdl2 End!")

    mdlcnt3 = line[index]
    index += 1
    for i in range(mdlcnt3):
        mdlLen = line[index]
        index += 1
        mdlName = line[index:index+mdlLen].decode("shift-jis")
        index += mdlLen
        if printFlag:
            print(mdlName)

        for j in range(6):
            f = struct.unpack("<f", line[index:index+4])[0]
            if printFlag:
                print(f, end=", ")
            index += 4
        if printFlag:
            print()
    if printFlag:
        print("mdl3 End!")
    
    binFileLen = line[index]
    index += 1
    binFileName = line[index:index+binFileLen].decode("shift-jis")
    index += binFileLen
    if printFlag:
        print("binFile:{0}".format(binFileName))
    temp = struct.unpack("<h", line[index:index+2])[0]
    index += 2
    if printFlag:
        print(temp)

    if printFlag:
        print("No.{0}->{1}".format(c, smfName))
        input()

    w.write("{0},".format(smfName))
    w.write("{0},".format(search(smfName, "smf")))
    if binFileName:
        w.write("{0},".format(binFileName))
        w.write("{0}\n".format(search(binFileName, "bin")))
    else:
        w.write("-,-\n")

w.close()

    
