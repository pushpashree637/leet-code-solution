class MedianFinder:
    def __init__(self):
        self.arr = []
    def addNum(self, num):
        self.arr.append(num)
        return None
    def findMedian(self):
        temp = self.arr[:]
        for i in range(len(temp)):
            for j in range(i + 1, len(temp)):
                if temp[i] > temp[j]:
                    temp[i], temp[j] = temp[j], temp[i]
        n = len(temp)
        if n % 2 == 1:
            return temp[n // 2]
        else:
            return (temp[n // 2 - 1] + temp[n // 2]) / 2
mf = MedianFinder()
output = []
output.append(None)            
output.append(mf.addNum(1))
output.append(mf.addNum(2))     
output.append(mf.findMedian())  
output.append(mf.addNum(3))     
output.append(mf.findMedian())  
print(output)
