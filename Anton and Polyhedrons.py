n=int(input())
my_dict={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
sum=0
for i in range(n):
    s=input()
    sum+=my_dict[s]
print(sum)
