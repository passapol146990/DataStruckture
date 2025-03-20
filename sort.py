import random
# test_array = random.choice()
# [7,4,6,9,1]
# [4,7,6,9,1]
# เริ่มต้น index = 1
# เป็นการเปรียบเทียบฝั่งซ้ายถ้าน้อยกว่าให้สลับกัน
# for loop ไปฝั่งขวา
# while loop ไปซ้าย loop ย่อย
def insertionSort(array):
    for i in range(1,len(array)):
        temp = array[i]
        j = i - 1
        while(j>=0 and array[j] > temp):
            array[j + 1] =  array[j]
            j-=1
        array[j + 1] = temp
    return array


# เริ่ม index = 0
# เป็นการตรวจสอบไปฝั่งขวา ค่าน้อยจะเอามาแทน index = i สลับกับ index j
# ค่าน้อยมาหน้า 
def selectionSort(array):
    for i in range(len(array)-1):
        minIndex = i
        for j in range(i,len(array)):
            minIndex = (array[j] < array[minIndex])and j or minIndex
            # if array[j] < array[minIndex]:
            #     minIndex = j
        temp = array[i]
        array[i] = array[minIndex]
        array[minIndex] = temp
    return array

# เปรียบเทียบ 2 ค่า
# [(7,4),6,9,1]
# [4,(7,6),9,1]
# [4,6,7,(9,1)]
# [4,6,7,(1,9)] จบรอบ 1
# [(4,6),7,1,9] 
# [4,(6,7),1,9] 
# [4,6,(7,1),9] 
# [4,6,1,7,9] จบรอบ 2
# เป็นการดันค่ามากสุดไปด้านขวา
# มันจะลดการตรวจสอบ index ขวาสุดลงเรื่อยๆเพราะมันเอาค่ามากสุดไปขวาสุดอยู่แล้วไม่ต้องไปตรวจสอบให้เสียเวลา
# การ isSwappen ในกรณีที่มันไม่มีค่ามากสลับเลย ก็คือมันเรียงมาแล้วจะ loop i แค่รอบเดียวจบ
# ลูป j คือการลดรอบการตรวจสอบลงมาส่วนมากเราจะตรวจสอบค่ามากที่ ลูป j
# สาเหตุที่ -1 loop j เพราะรอบแรกมันไม่มีค่าฝั่งขวา index มันเกิน
def bubbleSort(array):
    for i in range(len(array)-1):
        isSwappen = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
                isSwappen = False
        if isSwappen: break
    return array

# [7,4,6,9,10,5]-->[10,4,5,6,7,9]-->[4,5,6,7,9,10]
# หลักหน่วย		 หลักสิบ		
# 0	10	        0	4,5,6,7,9	
# 1		        1	10	
# 2		        2		
# 3		        3		
# 4	4	        4		
# 5	5	        5		
# 6	6	        6		
# 7	7	        7		
# 8		        8		
# 9	9	        9		
# เป็นการใช้ array 2D ในการมา sort
# ยิ่งหลักเยอะจะยิ่งลูปเยอะ ต้องหาค่ามากสุด
# การเก็บรวบรวมเลขซ้ายไปขวาบนลงล่าง
# มีความเร็วมากแต่กินเนื้อที่ แต่ถ้าใช้ arrayList จะแก้ปัญหากินเนื้อที่ได้
def radixSort(array):
    max_value = max(array)
    radix_array = [[],[],[],[],[],[],[],[],[],[]] # 2D 0-9
    exp = 1
    while max_value//exp>0:
        # เอาค่ามาใส่ 2D
        while len(array) > 0:
            val = array.pop()
            radixIndex = (val // exp) % 10 #หารเอา 5/1 % 10 ช
            radix_array[radixIndex].append(val)
        # เอา 2D มาคืนค่า array
        for i in radix_array:
            while len(i) > 0:
                val = i.pop()
                array.append(val)
        exp *= 10
    return array

# เป็นการเอามาเรียงเป็นแนวตั้งตามจำนวน
# จากนั้นก็จะเปรียบเทียบสลับเลขน้อยขึ้นบนด้วยระยะห่างลงล่าง k ช่อง
# [10,4,5,6], k = 4/2 = 2
# 0 10 10->5
# 1 4       
# 2 5  5->10
# 3 6
def shellSort(array):
    k = len(array)//2
    while k>=1:
        for i in range(k,len(array)):
            temp = array[i]
            j = i
            while j>k-1 and array[j-k] > temp:
                array[j] = array[j-k]
                j = j-k
            array[j] = temp
        k = k//2
    return array
# def shellSort(array):
#     [10,4,5,6]
#     k = 4//2 = 2
#     # 2>=1
#     while k>=1:
#         # i = 2 - 4
#         for i in range(k,len(array)):
#             temp = array[i] = 5
#             j = i = 2
#             # 2>(2-1) and array(2-2)=10 > 5
#             while j>k-1 and array[j-k] > temp:
#                 array[j] = array[j-k] #[10,4,5,6] --> 5 <> 10 -->[10,4,10,6]
#                 j = j-k = 2-2 = 0
#             array[j] = temp #[10,4,10,6] --> [5,4,10,6]
#         k = k//2 = 2/2=1
#     return array

def quickSort(array,start,end):
    f = start
    r = end
    if end>start:
        pivot = array[start]
        while r>f:
            while array[f] <= pivot and f <= end and r > f:
                f+=1
            while array[r] > pivot and r >= start and r >= f:
                r-=1
            if r > f:
                temp = array[f]
                array[f] = array[r]
                array[r] = temp
        temp = array[start]
        array[start] = array[r]
        array[r] = temp
        quickSort(array,start,r-1)
        quickSort(array,r+1,end)

# data = [5,1,2,3,4]
# print(data)
# quickSort(data,0,len(data)-1)
# print(data)



# print(insertionSort([7,4,6,9,1]))
# print(selectionSort([7,4,6,9,1]))
# print(bubbleSort([7,4,6,9,1]))
# print(radixSort([7,4,6,9,1]))
print(shellSort([7,4,6,9,1]))












