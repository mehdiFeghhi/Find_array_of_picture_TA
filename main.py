def isTheSame(coral1, coral2):

    return coral1 == coral2


def remove_duplicate(dic1, dic2):
    duplicate = dic2["duplicate"].copy()
    duplicate += [item for item in dic1["duplicate"] if item not in dic2["duplicate"]]
    # for item in dic1.get("duplicate"):
    #     if item not in dic2.get("duplicate"):
    #         duplicate.append(item)
    print(dic1)
    print(dic2)
    print("///////")

    for i in dic1["happen_once"]:

        for j in duplicate:

            if isTheSame(i,j):
                dic1["happen_once"].remove(i)
                print("_______________________________________________")
                print(dic1)
                break

    for c in dic2["happen_once"]:

        for d in duplicate:

            if isTheSame(c,d):
                dic2["happen_once"].remove(c)
                print("_______________________________________________")
                print(dic2)
                break

    for k in dic1["happen_once"]:

        for h in dic2["happen_once"]:

            if isTheSame(k,h):
                duplicate.append(k)
                dic1["happen_once"].remove(k)
                dic2["happen_once"].remove(h)
                print("_______________________________________________")
                print(dic1)
                print(dic2)
                break

    print("***************************************************************8")

    return  {"happen_once":dic1["happen_once"]+dic2["happen_once"],"duplicate":duplicate}







def Single_memeber(list_of_input):
    if  len(list_of_input) == 1:
        return {"happen_once": list_of_input, "duplicate": []}
    elif len(list_of_input) == 2:
            if isTheSame(list_of_input[0],list_of_input[1]):
                return {"happen_once": [], "duplicate": [list_of_input[0]]}
            else:
                return {"happen_once": list_of_input, "duplicate": []}

    else:
        size_of_list = len(list_of_input)
        print(size_of_list//2)
        result_list = remove_duplicate(Single_memeber(list_of_input[:size_of_list // 2]), Single_memeber(list_of_input[size_of_list // 2:]))
        return result_list


def main():

    list_of_input = input().split()
    x = Single_memeber(list_of_input)
    print(".......................................................")
    print(x)

if __name__ == '__main__':

    main()

