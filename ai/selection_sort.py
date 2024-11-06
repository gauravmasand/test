#selection sort

def selection_sort(a):
    for i in range(len(a)):
        min_index=i
        for j in range(i,len(a)):
            if a[min_index]>a[j]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]
        print(f"Pass {i+1}=",a)

a=[]
n=int(input("Enter the size of array= "))
for i in range(n):
    mark=int(input("Enter the Numbers= "))
    a.append(mark)
print("Unsorted Array=",a)
selection_sort(a)
print("Sorted Array=",a)

#o(n^2)
