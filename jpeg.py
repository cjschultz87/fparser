import sys

try:
    foxtrot = open(sys.argv[1],"r")
except:
    print "File does not exist"
    
    
bytes = []

bytes_L = 0

while True:
    alpha = foxtrot.readline()
    
    if alpha == "":
        break
        
    bytes_L += 1
    
    bytes.append(alpha[0:2])
    
m16 = "cdef"

tags = []

hex = "0123456789abcdef"

for element in m16:
    for element_1 in hex:
        tags.append(element + element_1)
        
tags.pop(len(tags)-1)

index = 0

alpha = 0

while alpha == 0 and index < bytes_L:
    print bytes[index]
    
    if bytes[index] == "ff":
        index += 1
        
        segment_val = 0
        
        if bytes[index] in tags[16:26]:
            index += 1
            
        elif (bytes[index] in tags) and not(bytes[index] in tags[16:26]):
            if bytes[index] == "da":
                print "start of scan: byte " + str(index)
                bravo = 0
                
                while bravo == 0:
                    index += 1
                    
                    if bytes[index] == "ff":
                        index += 1
                        
                        if bytes[index] in tags and not(bytes[index] in tags[16:26]):
                            index -= 1
                            bravo = 1
                            
                        if bytes[index] == "d9":
                            alpha = 1
                            
                            break
                
            else:
                print bytes[index-1] + bytes[index] + ": byte " + str(index)
            
                def sierraF(bravo):
                    sierra_0 = hex.index(bravo[0])
                    sierra_1 = hex.index(bravo[1])
                    return sierra_0*16 + sierra_1
            
                index += 1
            
                segment_val += 256 * sierraF(bytes[index])
            
                index += 1
            
                segment_val += sierraF(bytes[index])
            
                segment_val -= 1
            
        index += segment_val
        
        print index

    else:
        print "Tagged length not congruent with bytes!"
        
        while not(bytes[index] == "ff"):
            index += 1
        
print str(index + 1) + " bytes"
