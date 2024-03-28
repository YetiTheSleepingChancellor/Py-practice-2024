# WAP to find the class of ip address A, B, C, D, E.

# steps:

# A = 1-126
# B = 128 - 191
# C = 192 - 223
# D = 224 - 239
# E = 240 - 254

ip_address = ["192.168.1.20", "220.10.14.1", "150.20.10.10","1.10.10.1","20.20.20.20","140.150.20.1"]



size =  len(ip_address)

i = 0
while i < size:
        
    classes = ip_address[i] 
    newip =  classes.split('.')
    finalip = int(newip[0])
        
    if finalip >= 1 and finalip <= 126:
        print(classes,"-> Class A")
    elif finalip >= 128 and finalip <= 191:
        print(classes,"-> Class B")
    elif finalip >= 192 and finalip <= 223:
        print(classes,"-> Class C")
    elif finalip >= 224 and finalip <= 239:
        print(classes,"-> Class D")
    elif finalip >= 249 and finalip <= 254:
        print(classes,"-> Class E")
    else:
        print("NOT an ip address.")
    i += 1






