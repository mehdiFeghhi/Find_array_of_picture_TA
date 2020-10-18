class Rec:

    def __init__(self, x1, x2, h):
        self.left = x1
        self.right = x2
        self.high = h

    @classmethod
    def make_rec(cls, list):
        return cls(list[0], list[1], list[2])

    def __str__(self):
        return "Rectangel :\n" + "Left = " + str(self.left) + "\nRight = " + str(self.right) + "\nHigh = " + str(self.high)


def marege(list1, list2):
    i = j = 0
    result = []
    while i < len(list2):

        while j < len(list1):

            if i == len(list2):
                result.append(list1[j])
                j += 1

            elif list1[j].right > list2[i].left:
                result.append(Rec.make_rec([list1[j].left, list2[i].left, list1[j].high]))

                if list2[i].right >= list1[j].right:
                    result.append(Rec.make_rec([list2[i].left, list1[j].right, max(list1[j].high, list2[i].high)]))
                    if list2[i].right != list1[j].right:
                        list2[i] = Rec.make_rec([list1[j].right, list2[i].right, list2[i].high])
                        j += 1

                    else:
                        j += 1
                        i += 1
                else:
                    result.append(Rec.make_rec([list2[i].left, list2[i].right, max(list1[j].high, list2[i].high)]))
                    list1[j] = Rec.make_rec([list2[i].right, list1[j].right, list1[j].high])
                    i += 1
            else:

                result.append(list1[j])
                j += 1

        if i < len(list2):
            result.append(list2[i])
            i += 1

    return result


def find_all_rectangle(list_rec):
    size = len(list_rec)
    if size == 1:
        return list_rec
    elif size == 2:  # اگر دوتا مستطیل از هم جدا بودند
        if list_rec[0].right <= list_rec[1].left:
            return list_rec
        else:  # اگر دوتا مستطیل با هم تداخل داشتند

            if list_rec[0].right <= list_rec[1].right:
                return [Rec.make_rec([list_rec[0].left, list_rec[1].left, list_rec[0].high]),
                        Rec.make_rec([list_rec[1].left, list_rec[0].right, max(list_rec[0].high, list_rec[1].high)]),
                        Rec.make_rec([list_rec[0].right, list_rec[1].right, list_rec[1].high])]
            else:
                return [Rec.make_rec([list_rec[0].left, list_rec[1].left, list_rec[0].high]),
                        Rec.make_rec([list_rec[1].left, list_rec[1].right, max(list_rec[0].high, list_rec[1].high)]),
                        Rec.make_rec([list_rec[1].right, list_rec[0].right, list_rec[0].high])]

    else:

        return marege(find_all_rectangle(list_rec[:(size // 2)+1]), find_all_rectangle(list_rec[(size // 2)+1:]))


def calculate_area(all_rectangle):
    result = 0
    for i in all_rectangle:
        print(i)
        print((i.right - i.left) * i.high)
        print("__________________________________")
        result += (i.right - i.left) * i.high

    return result


def print_all_Rec(all_rectangle):
    for obj in all_rectangle:
        print(obj)
        print("__________________________________")


def main():
    number_rectangle = int(input())

    list_rectangle = []
    for i in range(number_rectangle):
        list_rectangle.append(list(map(float, input().split())))

    list_Rec_Object = list(map(Rec.make_rec, list_rectangle))
    list_Rec_Object.sort(key=lambda x: x.left)
    print_all_Rec(list_Rec_Object)
    all_rectangle = find_all_rectangle(list_Rec_Object)
    # print_all_Rec(all_rectangle)
    result = calculate_area(all_rectangle)

    print(result)


if __name__ == '__main__':
    main()
