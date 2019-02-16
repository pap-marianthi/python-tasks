def sumIntervals(list) :
    #input = list
    #classify list
    list2 = list.copy()
    #print("list2=",list2)
    list = sorted(list, key = lambda x: (x[0], -x[1]))
    #print("list=",list)
    #create new empty list = result
    result = []
    #for each item in list
    for item in list :
        #add item if list is blank
        if not result:
            result.append(item)
        else:
            #lastitem = last item of result list
            lastitem = result[-1]
            #spaces that don't have common numbers
            if item[0] > lastitem[1]:
                #add item in result
                result.append(item)
            elif item[1] > lastitem[1]:
                #merge 2 items
                (result[-1])[1]=item[1]
    #print("result=", result)
    sum = 0
    for item in result:
        sum = sum + item[1] - item[0]
    print("sumIntervals(" ,list2, ")=" ,sum)

def main():
    print("", end="")
   
main()
#sumIntervals( [[1,2], [6, 10], [11, 15] ] )
#sumIntervals( [[1,4], [7, 10], [3, 5] ] )
#sumIntervals( [[1,5], [10, 20], [1, 6], [16, 19], [5, 11]] )
