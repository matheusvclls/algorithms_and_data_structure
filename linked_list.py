
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None


    def append(self, element):
        '''
        Append an element in the end of the linked list
        '''

        # create the new node with element inputed by the user
        new_node=Node(element)

        # when you already have the head element
        if self.head != None:
            current_node=self.head
            while current_node.next!=None:
                current_node=current_node.next
            current_node.next=new_node

        # first insert
        else:
            self.head = new_node


    def lenght(self) -> int:
        '''
        Return total elements of linked list
        '''

        count_elements=0
        current_node = self.head
        while current_node!=None:
            count_elements+=1
            current_node=current_node.next
        return count_elements


    def _get_node(self, index):
        '''
        Return the node especified by the index passed
        '''
        if index >=self.lenght():
            print('List index out of range')

        elif index < 0:
            print('Index must be greater than zero')

        else:
            current_node=self.head
            node_index =0
            while node_index!=index:
                current_node=current_node.next
                node_index+=1
            return current_node


    def _set_node_value(self, value, index):
        '''
        Set a new value in a node that already exist
        '''
        if index >=self.lenght():
            print('List index out of range')

        elif index < 0:
            print('Index must be greater than zero')

        else:
            current_node=self.head
            node_index =0
            while node_index!=index:
                current_node=current_node.next
                node_index+=1
            current_node.data = value


    def _get_index(self, element):
        '''
        Return index of the first time element appears
        '''
        current_node=self.head
        node_index =0
        while current_node!=None:
            if current_node.data == element:
                return node_index

            current_node=current_node.next
            node_index+=1
        
        raise ValueError("{} is not in linked list".format(element))      

    
    def insert(self, element, index: int):
        '''
        Insert a new node based on an index and an element passed by the user
        '''
        if index > self.lenght():
            print('List index out of range')

        elif index < 0:
            print('Index must be greater than zero')

        elif index==0:
            new_node=Node(element)
            new_node.next=self.head
            self.head = new_node

        else:
            new_node = Node(element)
            previous_node = self._get_node(index -1)
            new_node.next=previous_node.next
            previous_node.next = new_node

    def remove(self, element):
        '''
        Remove a node based on his value
        '''
        if self.head == None:
            print('list is empty')
        
        elif self.head.data == element:
            self.head = self.head.next
            return True

        else:
            previous_node=self.head
            current_node=self.head.next
            while current_node!=None:
                if current_node.data==element:
                    previous_node.next=current_node.next
                    current_node.next=None # remove the next node reference of node removed
                    return True
                previous_node = current_node
                current_node=current_node.next
        print('element {} is not in the linked list'.format(element))


    def __repr__(self):
        '''
        Customize way python prints
        '''
        current_node = self.head

        if self.lenght() == 0:
            print('linked list is empty')

        elif self.lenght() == 1:
            print(self.head.data)

        else:
            string_linked_list = ""
            while current_node!=None:
                string_linked_list = string_linked_list + str(current_node.data) 
                current_node = current_node.next
                if current_node!=None:
                    string_linked_list = string_linked_list + '-->'
            return string_linked_list


if __name__ == '__main__':
    ll1 = Linked_list()
    ll1.append(1)
    ll1.append(2)
    ll1.append(3)
    ll1.append(5)
    print(ll1)
    ll1.remove(2)
    print(ll1)