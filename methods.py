def bestFit(block_num, block_size, process_num, process_size):
    ans0 = []
    ans1 = []
    ans2 = []
    block_size = sorted(block_size)
    for k in range(0, process_num, 1):
        for i in range(0, block_num, 1):
            if block_size[i] >= process_size[k]:
                if i not in ans0:
                    ans0.append(i)
                    ans1.append(block_size[i])
                    ans2.append(k)
                    break
    return ans1, ans2
