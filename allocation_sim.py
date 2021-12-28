import methods

# Total number of memory blocks
print("Enter the total number of memory blocks: ")
bn = input()
while bn.isdigit() == False or (bn.isdigit() == True and int(bn) == 0):
    bn = input("Please enter a valid number for number of memory blocks:")
block_num = int(bn)


# block sizes
print("Enter the block sizes: ")
block_size = []
for i in range(0, block_num, 1):
    bin = input()
    while bin.isdigit() == False or int(bin) == 0:
        bin = input("Please enter a valid number for block size: ")
    block_size.append(int(bin))


# Number of processes
print("Enter the total number of processes: ")
pn = input()
while pn.isdigit() == False or (pn.isdigit() == True and int(pn) == 0):
    pn = input("Please enter a valid number for number of processes: ")
process_num = int(pn)


# Processes sizes
print("Enter the processes sizes: ")
process_size = []
for i in range(0, process_num, 1):
    pin = input()
    while pin.isdigit() == False or int(pin) == 0:
        pin = input("Please enter a valid number for process size: ")

    process_size.append(int(pin))

# Allocation method (choices)
print("Choose an allocation method (1 for First fit, 2 for Best fit & 3 for Worst fit): ")
option = input()
while option.isdigit() == False or (option.isdigit() == True and (int(option) < 1 or int(option) > 3)):
    option = input("Please enter a valid choice: ")
choice = int(option)
if choice == 1:
    ans1, ans2 = methods.firstFit(
        block_num, block_size, process_num, process_size)
elif choice == 2:
    ans1, ans2 = methods.bestFit(
        block_num, block_size, process_num, process_size)
elif choice == 3:
    ans1, ans2 = methods.worstFit(
        block_num, block_size, process_num, process_size)

if choice == 2 or choice == 3:
    index = []
    for w in range(0, len(ans1), 1):
        for l in range(0, len(block_size), 1):
            if ans1[w] == block_size[l]:
                index.append(l)
    ans1 = index
# prints info in tabular form
print("Process no.  Process size    Block no.   Block size")
for i in range(0, len(ans2), 1):
    print("      "+str(ans2[i]+1)+"           "+str(process_size[ans2[i]]
                                                    )+"             "+str(ans1[i]+1)+"             "+str(block_size[ans1[i]])+"                   "+str(block_size[ans1[i]]-process_size[ans2[i]])+" units of block no. "+str(ans1[i]+1)+" is wasted")

    # prints the process that'll need to wait
print("Processes of the below sizes will have to wait:")
for z in range(0, process_num, 1):
    if z not in ans2:
        print("p"+str(z+1)+" : "+str(process_size[z]))

    # when num>num2 or vice versa
    # if i have 2 processes of the same size
