#hacker rank solution for merge tool.
def merge_the_tools(string, k):
    for i in range(0,len(string)+1-k,k):
        l=[]
        for a in string[i:i+k]:
           if a not in l:
                l.append(a)
        print("".join(l))
        del l 

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
