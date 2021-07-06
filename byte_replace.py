import struct

f = open("COMIC1300.BIN", "rb")

lines = f.read()
cam1_index = 0xA88
cam2_1_index = 0
cam2_2_index = 0
cam3_1_index = 0
cam3_2_index = 0
cam4_1_index = 0
cam4_2_index = 0
cam5_1_index = 0
cam5_2_index = 0
cam6_1_index = 0
cam6_2_index = 0
cam7_1_index = 0
cam7_2_index = 0
cam8_1_index = 0
cam8_2_index = 0
cam9_1_index = 0
cam9_2_index = 0

index = cam1_index

Cam1 = []
Cam2_1 = []
Cam2_2 = []
Cam3_1 = []
Cam3_2 = []
Cam4_1 = []
Cam4_2 = []
Cam5_1 = []
Cam5_2 = []
Cam6_1 = []
Cam6_2 = []
Cam7_1 = []
Cam7_2 = []
Cam8_1 = []
Cam8_2 = []
Cam9_1 = []
Cam9_2 = []

for i in range(8):
    Cam1.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4

index += 0x228
cam2_1_index = index
for i in range(8):
    Cam2_1.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4
index += 3
cam2_2_index = index
for i in range(8):
    Cam2_2.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4

index += 0x3DF
cam3_1_index = index
for i in range(8):
    Cam3_1.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4
index += 3
cam3_2_index = index
for i in range(8):
    Cam3_2.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4
    
index += 0x310
cam4_1_index = index
for i in range(8):
    Cam4_1.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4
index += 3
cam4_2_index = index
for i in range(8):
    Cam4_2.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4

index += 0x310
cam5_1_index = index
for i in range(8):
    Cam5_1.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4
index += 3
cam5_2_index = index
for i in range(8):
    Cam5_2.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4

index += 0x310
cam6_1_index = index
for i in range(8):
    Cam6_1.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4
index += 3
cam6_2_index = index
for i in range(8):
    Cam6_2.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4

index += 0x310
cam7_1_index = index
for i in range(8):
    Cam7_1.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4
index += 3
cam7_2_index = index
for i in range(8):
    Cam7_2.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4

index += 0x421
cam8_1_index = index
for i in range(8):
    Cam8_1.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4
index += 0x1CA
cam8_2_index = index
for i in range(8):
    Cam8_2.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4

index += 0x186
cam9_1_index = index
for i in range(8):
    Cam9_1.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4
index += 0x1D2
cam9_2_index = index
for i in range(8):
    Cam9_2.append(struct.unpack("<f", lines[index:index+4])[0])
    index += 4

temp = cam1_index
templine = bytearray(lines)

for byte in struct.pack("<f", 1.0):
    templine[temp] = byte
    temp += 1

w = open("update.BIN", "wb")
w.write(templine)
w.close()

f.close()
