#4.MATRIX DIAGONAL SUM
#given a matrix print the largest of the sums of the two triangles split by diagonal from top right to bottom left

r=int(input("Enter no. of rows: "))
c=int(input("Enter no. of columns: "))
matrix=[]

for i in range(r):
    row=[]
    for j in range(c):
        x=int(input())
        row.append(x)
    matrix.append(row)

print(matrix)        

sum1=0
sum2=0

for i in range(r):
    for j in range(c):
        if i<=j:
            sum1+=matrix[i][j]
        if i>=j:
            sum2+=matrix[i][j]        
print(max(sum1,sum2))            
