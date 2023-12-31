class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
      def __init__(self,value):
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            self.length = 1
  
      def printList(self):
            temp = self.head
            while temp is not None:
                  print(temp.value)
                  temp = temp.next

      def append(self, value):
            newNode = Node(value)
           
            if self.length == 0:
                self.head = newNode   
                self.tail = newNode
                
            else:
                 self.tail.next =newNode
                 self.tail = newNode
            self.length+=1
            return True
      
      # first we check that linkedlist is empty then return none
      # then set 2 variables temp and pre 
      # after that we will run the while loop which will check next is none or not if not while loop will run 
      # make temp equals to pre and assign temp.next  to temp for next iteration of while loop
      def pop(self):
            temp = self.head
            pre = self.tail
            if self.length == 0:
                  return None
            
            while(temp.next) :
                 pre = temp
                 temp = temp.next
            
            self.tail = pre
            self.tail.next = None
            self.length -=1

            if(self.length == 0):
                 self.head = None
                 self.tail = None
            
            return temp
                 
           

                  
      

myLinkedList = LinkedList(4)
myLinkedList.append(55)
myLinkedList.pop()
myLinkedList.printList()