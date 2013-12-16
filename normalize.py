def Normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers   
    
try:
      Normalize([0, 0, 0])
except ZeroDivisionError, e:
      print 'Invalid maximum element'    
