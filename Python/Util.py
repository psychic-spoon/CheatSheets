import time

s="psychic-spoon"

'''Reversing a String'''
# start=time.time()
# time.sleep(2)
# print(s[::-1])
# elapsed=time.time()-start
# print("Slice Method:"+str(elapsed))

# start=time.time()
# time.sleep(2)
# print(''.join(reversed(s)))
# elapsed=time.time()-start
# print("Reversed Method:"+str(elapsed))

# start=time.time()
# time.sleep(2)
# chars=list(s)
# length=len(s)
# for i in range(int(length/2)):
#     chars[i],chars[length-1-i]=chars[length-1-i],chars[i]
# s=''.join(chars)
# print(s)    
# elapsed=time.time()-start
# print("Inplace Method:"+str(elapsed))


'''Filter null strings'''
# s='A B  C'

# start=time.time()
# time.sleep(1)
# lst=list(filter(None,s.split(' ')))
# elapsed=time.time()-start
# print("List Filter:"+str(elapsed))
# print(str(lst))

# start=time.time()
# time.sleep(1)
# lst=[x for x in s.split(' ') if x]
# elapsed=time.time()-start
# print("List If Filter:"+str(elapsed))
# print(str(lst))

'''Reversing a list'''
#Slice
# s="2 3 4 5 6"
# lst=[int(x) for x in s.split()]
# print(str(lst))

# start=time.time()
# time.sleep(1)
# print(lst[::-1])
# elapsed=time.time()-start
# print("Slice Method:"+str(elapsed))

# #Method
# start=time.time()
# time.sleep(1)
# lst.reverse()
# print(str(lst))
# elapsed=time.time()-start
# print("Slice Method:"+str(elapsed))
# lst.reverse()

# #List Reversed
# start=time.time()
# time.sleep(1)
# lst=list(reversed(lst))
# print(str(lst))
# elapsed=time.time()-start
# print("Slice Method:"+str(elapsed))

# def remove_prefix(f,prefix):
#     rsl = f[len(prefix):] if f.startswith(prefix) else f
#     return rsl

