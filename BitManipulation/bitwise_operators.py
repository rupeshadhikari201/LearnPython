# cook your dish here
user_input = map(int, input().split())
n, l, r = user_input
# print(n, l, r)
# Right Shift 
n= n>>r    # 7 >> 2 i.e 111 >> 2 ==> 001 ie. 7/2^shift_amount ie. 7/4 = 1
print(n)
n = n<<l    # 1 << 2 i.e 001 << 2 ==> 100 ie. 1*2*shift_amount ie. 1*4 = 4
print(n)