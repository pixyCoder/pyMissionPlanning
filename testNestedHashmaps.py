Dict = { }
print("Initial nested hashmap :-")
print(Dict)
 
Dict['Brentwood'] = {}
Dict['Downtown']  = {}
 
# Adding elements one at a time for Brentwood hashmap
Dict['Brentwood']['Torrance'] = 31
Dict['Brentwood']['Irvine'] = 81
print("\nAfter adding hashmap Brentwood")
print(Dict)
 
# Adding elements one at a time for Downtown
Dict['Downtown']['Torrance'] = 41
Dict['Downtown']['Irvine']   = 71
print("\nAfter adding hashmap Downtown")
print(Dict)
