def power_set(set, set_size):
 power_set_s = 2**set_size
 outer = 0
 inner = 0
 for outer in range(0, power_set_s):
  for inner in range(0, set_size):
   if outer & (1 << inner)>0:
    print(set[inner], end="")
arraysize = int(input("Size: "))
i = 0
set = []
while i < arraysize:
 askuser = int(input("Enter element: "))
 set.append(askuser)
 i = i+1
power_set(set, len(set))
 


