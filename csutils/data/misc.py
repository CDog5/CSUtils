import time

ranseed = int(time.time()) % 11
#generates fake random numbers
def semirandom():
    global ranseed
    ranseed = (ranseed * 8) % 11
    return ranseed

def clamp(val,clamp):
    if not of_type([(clamp,[tuple])]):
        return None
    val = float(val)
    low = float(clamp[0])
    high = float(clamp[1])
    if val > high:
        return high
    elif val < low:
        return low
    else:
        return val
def negative_normalise(val):
    val = float(val)
    if val > 0:
        return -1 * val
    else:
        return val
#turn negative values into positive ones
def normalise(val):
    return math.sqrt(val**2)
#sticky caps is where parts of a sentence are randomly capitalised, e.g. hElLo PeRsoN
def sticky_caps(mystr):
    newstr=""
    for i in range(len(mystr)):
        r = random.randint(0,1)
        if r == 0:
            newstr += mystr[i].lower()
        else:
            newstr += mystr[i].upper()

    return newstr
def keepcase(string):
    out=[]
    lowers= "abcdefghijklmnopqrstuvwxyz"
    for i,char in enumerate(string):
        if char in lowers:
            out.append((i,False))
        elif char in lowers.upper():
            out.append((i,True))
        else:
            out.append((i,None))
    return out

            

def owoify(mystr):
    cases = keepcase(mystr)
    mystr = mystr.lower()
    replacers = [["r", "w"],["l", "w"],
    ["no", "nu"],["has", "haz"],["have", "haz"],
    ["you", "uu"],["the ", "da "]]
    for repl in replacers:
        mystr = mystr.replace(repl[0],repl[1])
    newstr=""
    for k in cases:
        if k[0] < len(mystr):
            if k[1] == True:
                newstr += mystr[k[0]].upper()
            elif k[1] == False:
                newstr += mystr[k[0]].lower()
            else:
                newstr += mystr[k[0]]
    return newstr
def myrstrip(string,detect):
    mystr = str(string)
    mystr = mystr[::-1]
    outstr=''
    found = 0
    finding = True
    for char in mystr:
        if char == detect and finding:
            found += 1
            continue
        finding = False
        outstr += char

    outstr = outstr[::-1]
    return string,found
