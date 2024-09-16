n = int(input())
s = input()
my_list = s.split(" ")
f_list = [int(i) for i in my_list]

if set([1, 2, 3]).issubset(set(f_list)):
    num_list = set()
    final_list = []

    def find_indices(lst, num_set, count):
        indices = []
        for i, val in enumerate(lst):
            if val in num_set and (i + 1) not in num_list:
                indices.append(i + 1)
                num_set.add(i + 1)
                count -= 1
                if count == 0:
                    break
        return indices, num_set, count

    for _ in range(3):
        m_list, num_list, count = find_indices(f_list, num_list, 3)
        if count == 0:
            final_list.append(m_list)
    if len(final_list) == 0:
        print("0")
    else:
        print(len(final_list))
        for k in final_list:
            print(*k)
else:
    print("0")
