# No.622 Design circular Queue
***
https://leetcode.com/problems/design-circular-queue/  
</br>

## 문제 설명
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".
One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
* MyCircularQueue(k) Initializes the object with the size of the queue to be k.
* int Front() Gets the front item from the queue. If the queue is empty, return -1.
* int Rear() Gets the last item from the queue. If the queue is empty, return -1.
* boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
* boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
* boolean isEmpty() Checks whether the circular queue is empty or not.
* boolean isFull() Checks whether the circular queue is full or not.  
</br>

## 제한 사항
* 1 <= k <= 1000
* 0 <= value <= 1000
* At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.  
</br>

## 입출력 예
**Input**  
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]  
[[3], [1], [2], [3], [4], [], [], [], [4], []]  
**Output**  
[null, true, true, true, false, 3, true, true, true, 4]  
</br>
