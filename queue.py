from node import Node

class Queue:
    """
    Here, in this class we will deep dive and implement by 
    ourserlves the queue structure.

    Queue follows the rule of first in first out (FIFO). In other words,
    the first element inserted in queue, will be the first to be removed from list.

    Use cases: how your Vscode works when you press ctrl + z/
    """

    def __init__(self):
        self.top_item = None
        self.bottom_item = None


    def lenght(self) -> int:
        '''
        Return total elements of linked list
        '''

        count_elements=0
        current_node = self.top_item
        while current_node!=None:
            count_elements+=1
            current_node=current_node.next
        return count_elements


    def push(self, elem):
        '''
        Insert an element on the top of the list
        '''
        new_node = Node(elem)
        if self.bottom_item == None:
            self.bottom_item = new_node
        
        else:
            self.bottom_item.next = new_node
            self.bottom_item = new_node

        if self.top_item == None:
            self.top_item = new_node


    def pop(self):
        '''
        Remove the top element of the queue
        '''
        if self.lenght() != 0:
            elem = self.top_item
            self.top_item = self.top_item.next
            return elem
        else:
            print('Queue is empty')


    def peek(self):
        '''
        Return the top element of the stack
        '''
        if self.lenght() != 0:
            return self.top_item.data

        else:
            print('Queue is empty')


    def __repr__(self):
        '''
        Customize way python prints
        '''
        current_node = self.top_item

        if self.lenght() == 0:
            print('Queue is empty')

        elif self.lenght() == 1:
            print(str(self.top_item.data))

        else:
            string_linked_list = ""
            while current_node!=None:
                string_linked_list = string_linked_list + str(current_node.data) + " "
                current_node = current_node.next
            return string_linked_list


if __name__ == '__main__':
    ll1 = Queue()
    ll1.push(1)
    ll1.push(2)
    ll1.push(3)
    ll1.push(5)
    print(ll1)
    ll1.pop()
    print(ll1)
    print(ll1.peek())
   