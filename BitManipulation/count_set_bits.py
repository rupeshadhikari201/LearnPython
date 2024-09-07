# cook your dish here
# number = 15, 1110
# pos    = 4
# mask   = 1 << pos, ie. 001 << 4 ==> 1000
# ans    = num & mask i.e 1110 & 10000 => 

def is_set_bits(number, position):
    mask = 1 << position
    print(mask&number)
    print(bin(mask,), bin(number))
    if mask & number == 1:
        print("SET BIT")
    else:
        print("NOT SET BIT")
        

number = 15
position = 3
is_set_bits(number, position)
