class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
      def __init__(self,value):
            newNode = Node(value)
            print(newNode)
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
      

      

myLinkedList = LinkedList(4)
myLinkedList.append(55)
myLinkedList.printList()

