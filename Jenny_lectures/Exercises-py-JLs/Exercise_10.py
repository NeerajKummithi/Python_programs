# EXERCISE 10 - (LOVE CALCULATOR)

B=input("Enter the boy name = ")
G=input("Enter the girl name = ")

b=B.lower()
g=G.lower()

T=b.count("t")+g.count("t")
R=b.count("r")+g.count("r")
U=b.count("u")+g.count("u")
E1=b.count("e")+g.count("e")
L=b.count("l")+g.count("l")
O=b.count("o")+g.count("o")
V=b.count("v")+g.count("v")
E2=b.count("e")+g.count("e")

true=T+R+U+E1
love=L+O+V+E2

print(f"Percentage of love between {B} and {G} is {true}{love}%")