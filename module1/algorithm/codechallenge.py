#question 1
def getOnlyEvens(arr):
    result = []
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
            result.append(arr[i])
    print(result)

#test
getOnlyEvens([9,12,14.17,16,18]) 
getOnlyEvens([20,24,27,34,12,16])

#question 2
def reverseCompare(num):
    reverse_num = int(str(num)[::-1])
    if num >= reverse_num:
        print("ok")
    else:
        print("not ok")
#test 
reverseCompare(123)
reverseCompare(23)
reverseCompare(32)

#question 3
def returnFactorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * returnFactorial(num -1)
 #test
print(returnFactorial(6))
#question 4
def checkMeera(arr):
    for n in arr:
        if n * 2 in arr: 
            print("I am NOT a Meera array")
            return
    print("I am a Meera array")

#tests
checkMeera([22, 40, 30, 49,7])  
checkMeera([7, 4, 9,8])        

#question 5
def isDual(arr):
    counts = {}
    for n in arr:
        counts[n] = counts.get(n, 0) + 1     
    
    for val in counts.values():
        if val != 2:   
            return 0
    return 1

#tests
print(isDual([1, 2, 1, 3, 3, 2]))  
print(isDual([2, 5, 2, 5, 5]))     
print(isDual([3, 1, 1, 2, 2]))

#question 6
def digitalClock(seconds):
    hrs = (seconds // 3600) % 24       
    mins = (seconds % 3600) // 60      
    secs = seconds % 60                
    return f"{hrs:02}:{mins:02}:{secs:02}"

#tests
print(digitalClock(5425)) 
print(digitalClock(8699))
print(digitalClock(9843))
