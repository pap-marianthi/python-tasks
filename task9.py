def maxSequence2(list):
    max_sum = current_sum = 0
    current_position = start_position = last_position =  0
    #enumerate: j=counter & i=value
    for j, i in enumerate(list):
        if current_sum+i > 0:
            current_sum += i
        else:
            # reset start position
            current_sum= 0
            current_position = j+1
        if current_sum > max_sum:
            #set first list position
            start_position = current_position
            #set last list position
            last_position = j+1
            max_sum = current_sum        
    print("maxSequence(", list ,")=", max_sum ,":", list[current_position:last_position])
  
def maxSequence(list):
    #if all elements in list are negative
    max_sum = 0
    max_num = list[0]
    for a in list:
        if a > max_num:
            max_num = a
    
    if max_num < 0 :
        list2 = []
        list2.append(max_num)
        print("maxSequence2(", list ,")=", max_num, ":", list2)
    else:
        maxSequence2(list)

def main():
    print("",end="")
    
main()
#maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
