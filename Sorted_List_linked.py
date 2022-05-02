"""
-------------------------------------------------------
Linked version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    Spring 2021
__updated__ = "2022-02-09"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_SL_Node)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """

        # your code here

        return self._count ==0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """

        # your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new = _SL_Node(value, None)
        if self._front is None:
            self._front = new
            self._rear = self._front
        else:
            current = self._front
            previous = None
            index = 0
            while index < self._count and current._value <= value:
                previous = current
                current = current._next
                index += 1
            if previous is None:
                self._front = new
            new._next = current
            if previous is not None:
                previous._next = new
            if previous == self._rear:
                self._rear =  new
        self._count += 1
        return

        # your code here

        

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        index=0
        
        while index<self._count and current._value!=key:
            previous = current
            current = current._next
            index+=1
            
        if index==self._count:
            index = -1
            
        # your code here
        return previous,current,index

        # your code here


    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, i = self._linear_search(key)
        
        if i>-1:
            self._count -= 1
            if i>0:
                previous._next = current._next
            elif i==0:
                self._front = current._next
            if i == self._count:
                self._rear = previous
            
            value = current._value
        else:
            value = None
                
        # your code here
        return value

        # your code here

        

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        if self._count==1:
            value = self._front._value
            self._rear = None
            self._front = None
            self._count-=1
        else:
            value = self._front._value
            self._front = self._front._next
            self._count-=1
            
        return value


        # your code here

        

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """
        previous, current, i = self._linear_search(key)
        while i!=-1:
            if i>-1:
                self._count -= 1
                if i>0:
                    previous._next = current._next
                elif i==0:
                    self._front = current._next
                if i == self._count:
                    self._rear = previous
                
                value = current._value
            else:
                value = None
            previous, current, i = self._linear_search(key)   
        # your code here
        
        # your code here
        return

        # your code here

        

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None
        p,c,i = self._linear_search(key)
        if i!=-1:
            value = deepcopy(key)

        # your code here

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"
        value = deepcopy(self._front._value)

        # your code here
        return value


        # your code here

        

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        p,c,i = self._linear_search(key)

        # your code here

        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """

        # your code here

        return (-1 * self._count) <= i < self._count

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        curr_node = self._front
        end = i
        if i<0:
            start = self._count*-1
        else:
            start = 0
        for x in range(start,end):
            curr_node = curr_node._next
            
        value = deepcopy(curr_node._value)   

        # your code here
        return value

        # your code here
       

        

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _, c, i = self._linear_search(key)
        
        

        # your code here

        return i!=-1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        value = deepcopy(self._front)
        
        
        return value
      
        # your code here


       

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"
        value = deepcopy(self._rear)
        
        
        return value

        # your code here

        

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        n= 0
        _, c, _ = self._linear_search(key)
        while c is not None and c._value == key:
            n += 1
            c = c._next
        return n

        # your code here

        

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        current = self._front
        previous = None
        while current is not None:
            _, c, _ = self._linear_search(current._value)
            if c != current:
                previous._next = current._next
                self._count -= 1
                if current == self._rear:
                    self._rear = previous
            else:
                previous = current
            current = current._next
        return
        
        
        
        
        

        # your code here

        

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:
            i = args[0]

            if i < 0:
                # index is negative
                i = self._count + i
            j = 0

            while j < i:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
            # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                # Value does not appear in target list.
                    self.insert(value)

            source1_node = source1_node._next

        # your code here
        return

        # your code here

        

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
            # Value does not exist in new list.
                self.insert(value)
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
            # Value does not exist in current list.
                self.insert(value)

            source2_node = source2_node._next
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish self is empty.
        Use: target1, target2 = lst.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        index = 0
        curr = self._front
        while curr is not None and curr._value<key:
            index+=1
            curr = curr._next
        
        
        target1 = Sorted_List()
        target2 = Sorted_List()
        
        middle = index
        prev = None
        curr = self._front
        
        if index!=-1:

            for _ in range(middle):
                prev = curr
                curr = curr._next
    
            if prev is not None:
                # Break the source list between prev and curr
                prev._next = None
    
            # Define target1
            target1._count = middle
            target1._front = self._front
            target1._rear = prev
    
            # Define target2
            target2._count = self._count - middle
            target2._front = curr
    
            if target2._count > 0:
                target2._rear = self._rear
    
            # Clean up source
            self._front = None
            self._rear = None
            self._count = 0
            
        return target1, target2

        # your code here

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node

        node._next = None
        self._rear = node
        self._count += 1
        return    

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty. Order of even and odd is not significant.
        (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left

        return target1, target2
                
                

        # your code here

        

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        
        middle = self._count // 2 + self._count % 2
        prev = None
        curr = self._front

        for _ in range(middle):
            prev = curr
            curr = curr._next

        if prev is not None:
            # Break the source list between prev and curr
            prev._next = None

        # Define target1
        target1._count = middle
        target1._front = self._front
        target1._rear = prev

        # Define target2
        target2._count = self._count - middle
        target2._front = curr

        if target2._count > 0:
            target2._rear = self._rear

        # Clean up source
        self._front = None
        self._rear = None
        self._count = 0
        return target1, target2
            
            
            

        # your code here

        

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (iterative version)
        Use: b = l.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """
        target = other
        if self._count != target._count:
            identical = False
        else:
            source_node = self._front
            target_node = target._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical

        # your code here

        

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """
        new_list = Sorted_List()
        curr = self._front
        while curr is not None:
            node =  _SL_Node(curr._value,None)
        
            if new_list._front is None:
                new_list._front = node
            
            #if list is empty, rear has no 'next' so we only do if there is a rear    
            if new_list._rear is not None:
                new_list._rear._next = node
                
            new_list._rear = node
            new_list._count +=1
            curr = curr._next
        
            
        # your code here
        return new_list

        # your code here

        

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"
        
        while source1._front is not None or source2._front is not None:
            if source1._front is not None:
                
                if self._front is None:
                    
                    self._front = source1._front
          
                else:   
                    self._rear._next = source1._front
            
                self._rear = source1._front
                source1._front = source1._front._next
                source1._count-=1
                self._count+=1
                
                
            if source2._front is not None:
       
                if self._front is None:
                    
                    self._front = source2._front
          
                else:   
                    self._rear._next = source2._front
            
                self._rear = source2._front
                source2._front = source2._front._next
                source2._count-=1
                self._count+=1
        
        source1._rear = None
        source2._rear = None
            
           
        # your code here
        return
    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        # your code here

        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        # your code here

        return

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (recursive version)
        Use: b = l.identical_r(rs)
        -------------------------------------------------------
        Parameters:
            rs - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """

        # your code here

        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"

        # your code here

        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = l.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -----------------------------------------------------------
        """

        # your code here

        return

    def combine_r(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(rs)
        -------------------------------------------------------
        Parameters:
            rs- an linked-based List (Sorted_List)
        Returns:
            new_list - the contents of the current Sorted_List and rs
            are interlaced into new_list - current Sorted_List and rs
            are empty (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"

        # your code here

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next