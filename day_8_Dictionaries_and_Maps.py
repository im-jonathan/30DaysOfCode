if __name__ == "__main__":
    n = int(input())
    directory = dict()
    for _ in range(n):
        value = list(map(str, input().split()))
        directory[value[0]] = value[1]
    
    for _ in range(n):
        search = str(input())
        if search not in directory:
            print("Not found")
        else:
            print("{}={}".format(search, directory[search]))
