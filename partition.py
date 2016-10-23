def partition(seq):
    pivot_index, seq = seq[0], seq[1:]
    low_vals = [x for x in seq if x <= pivot_index]
    high_vals = [x for x in seq if x > pivot_index]
    return low_vals, high_vals, pivot_index


def quicksort(seq):
    if len(seq) < 1: return seq
    low, high, pivot_index = partition(seq) 
    return quicksort(low) + [pivot_index] + quicksort(right)

def merge_sort(seq):
    middle_index = len(seq)/2
    left, right = seq[:middle_index], seq[middle_index:]
    if len(left) > 1: merge_sort(left)
    if len(right) > 1: merge_sort(right)
    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(right.pop())
        else:
            result.append(left.pop())
    result.reverse()
    return (left or right) + result 


def merge_sorted(li):

    if len(li) < 2: return li 
    m = len(li) / 2 
    return sort_and_count(merge_sorted(li[:m]), merge_sorted(li[m:])) 

def sort_and_count(l, r):
    count = 0
    result = [] 
    i = j = 0 
    while i < len(l) and j < len(r): 
        if l[i] < r[j]: 
            result.append(l[i])
            i += 1 
        else: 
            result.append(r[j])
            count = count + (len(l) - i)
            j += 1
    result.extend(l[i:]) 
    result.extend(r[j:]) 
    return result

def merge(A,B):
    global c
    C=[]
    lenA=len(A)
    lenB=len(B)
    i=0
    j=0
    while i<lenA and j<lenB:
        if A[i]<=B[j]:
            C.append(A[i])
            i=i+1
        else:
            c=c+len(A)-i #the magic happens here
            C.append(B[j])
            j=j+1
    if i==lenA:#A get to the end
        C.extend(B[j:])
    else:
        C.extend(A[i:])
    return C

def mergeSort(L):
    N=len(L)
    if N>1:
        S1=mergeSort(L[0:N/2])
        S2=mergeSort(L[N/2:])
        return merge(S1,S2)
    else:
        return L


if __name__ == '__main__':
    NUMLIST_FILENAME = "integers.txt"
    inFile = open(NUMLIST_FILENAME, 'r')

    with inFile as f:
        numList = [int(integers.strip()) for integers in f.readlines()]


    # seq = [12,34534, 5346536, 2352525, 532525, 1313, 123, 232, 3212]
    # print merge_sorted(numList)
    c=0
    after=mergeSort(numList)
    print c






