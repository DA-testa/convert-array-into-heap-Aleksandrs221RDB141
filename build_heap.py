# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range (n// 2 -1,-1,-1):
        while True:
            mx = i
            l=2*i+1
            r=2*i+2
            if l<n and data[l]<data[mx]:
                mx = l
            if l<n and data[l]<data[mx]:
                mx = r
            if i != mx:
                (data[i],data[mx])=(data[mx],data[i])
                swaps.append((i,mx))
                i=mx
            else:
                break
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text = input()
    if "F" in text :
        file=input()
        with open(f"tests/{file}") as f:
            length = int(f.readline())
            n = f.readline().split()
    elif "I" in text:
        length = int(input())
        n = input().split()
    # input from keyboard
    data = list(map(int, n))
    # checks if lenght of data is the same as the said lenght
    assert len(data) == length
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
