f = open('d:\\pyth\\thumbdata3.dat', 'rb')
tdata = f.read()
f.close()

ss = '\xff\xd8' # jpeg start byte
se = '\xff\xd9' # jpeg end byte

count = 0

while True:
    x1 = tdata.find(b'\xff\xd8')
    if x1 < 0:
        break
    x2 = tdata.find(b'\xff\xd9')
    jpg = tdata[x1:x2+1]
    count += 1
    fname = 'extracted%d03.jpg' % count
    fw = open(fname, 'wb')
    fw.write(jpg)
    fw.close()
    tdata = tdata[x2+2:]
