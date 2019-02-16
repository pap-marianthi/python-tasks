def sumIntervals(list) :
  list2 = list.copy()
  print("list2=",list2)
  list = sorted(list, key = lambda x: (x[0], -x[1]))
  print("list=",list)
  result = []
  for item in list :
    if not result:
      result.append(item)
    else:
      lastitem = result[-1]
      if item[0] > lastitem[1]:
        result.append(item)
      elif item[1] > lastitem[1]:
        (result[-1])[1]=item[1]
  sum = 0
  for item in result:
    sum = sum + item[1] - item[0]
  print("sumIntervals(" ,list2, ")=" ,sum)
