n=int(input())
s=input()
my_list=s.split(" ")
f_list=[]
num_list=[]
initial_list=[]
final_list=[]
num="123"
flag=False
for i in my_list:
    f_list.append(int(i))
if (1 in f_list) and (2 in f_list) and (3 in f_list):
    flag=True
if flag==False:
    print("0")
elif n<=2:
    print("0")
elif flag==True:
    def list(a_list,b_list):
        c_list=[]
        d_list=b_list
        num="123"
        for i in num:
            for j in range(len(a_list)):
                if i==str(a_list[j]) and ((j+1) not in d_list):
                    c_list.append(j+1)
                    d_list.append(j+1)
                    break
        return c_list,d_list
    for i in f_list:
        m_list,n_list=list(f_list,num_list)
        if len(m_list)==3:
            final_list+=[m_list]
            num_list+=n_list
    print(len(final_list))
    for k in final_list:
        for j in k:
            print(j,end=" ")
        print()









