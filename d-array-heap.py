import sys
import re


class DArrayMaxHeap:
    def __init__(self, num_child):
        """
        Initializes a d-array max heap.
            - num_child: The number of children each node has.
        """
        self.heap = []
        self.d = num_child  # Child per node

    def insert(self, value):
        """
        Inserts a value into the d-array max heap.
            - value: The value to be inserted.
        """
        self.heap.append(value)  # add value to end of the array
        self.heapify_up()  # correct the heap

    def heapify_up(self, index=0):
        """
        Correct the heap upwards, from a given index.
            - index: The index to do the heapify up from (default the last element).
        """
        if index == 0:
            index = len(self.heap) - 1  # index of the last element
        # While the index isn't the root index
        while index > 0:
            parent_index = (index - 1) // self.d  # Recalculate parent index for the current index
            if self.heap[index] > self.heap[parent_index]:
                # swap child and parent (if child is bigger)
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            # if child's value is less than parent's value done the heapify up successfully.
            else:
                break

    def extract_max(self):
        """
        Extract the maximum value of the d-array.
             - heap: The d-array to extract the maximum value from.
        """
        # if the heap is empty
        if not self.heap:
            return None
        last_index = len(self.heap) - 1
        # Insert the last element into the root and deleting the last element (the maximum)
        self.heap[0] = self.heap[last_index]
        del self.heap[last_index]
        # correct the heap downwards from the root
        self.heapify_down()

    def heapify_down(self, index=0):
        """
        Correct the heap downwards, from a given index.
            - index: The index to do heapify down from (default the root).
        """
        while True:
            max_child_index = self.max_child(index)  # Save the maxed child's index of current index
            # if the max child is in the heap, and greater from the parent, swap them.
            if max_child_index < len(self.heap) and self.heap[max_child_index] > self.heap[index]:
                self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]
                index = max_child_index  # Update to the subtree downwards
            else:
                break

    def max_child(self, parent_index):
        """
        Get the index of the maximum child of the d-array.
            - heap: The d-array heap.
            - parent_index: The index of the parent.
        returns: The index of the maximum child of the parent index.
        """
        max_child_index = parent_index * self.d + 1  # Initialize with the index of the first child
        # Run along all child and find the max value (save his index) in complexity of O(d).
        for i in range(1, self.d):
            current_child_index = parent_index * self.d + i + 1
            if current_child_index < len(self.heap) and self.heap[current_child_index] > self.heap[max_child_index]:
                max_child_index = current_child_index
        return max_child_index

    def print_heap(self):
        """
        Prints the element of the d-array heap for each level.
        """
        if not self.heap:
            print("Heap is empty")
            return
        n = len(self.heap)
        current_level = 0
        nodes_at_level = 1
        for i in range(n):
            # Print each element for current level with space separates them
            print(self.heap[i], end=" ")
            # If all elements for current level have been printed move to the next line
            if i + 1 == nodes_at_level:
                print()
                current_level += 1
                nodes_at_level += self.d ** current_level
        # Print new line at the end
        print()

    def increase_key(self, current_key, value):
        """
        Increase the key of an index (current_key) in the d-array if <value> is greater.
            - current_key: The index to increase the key of.
            - value: The new value
        """
        if current_key >= len(self.heap):
            print("Invalid current key.")
            return None
        # Update the key with the maximum value
        self.heap[current_key] = max(self.heap[current_key], value)
        # Restore the max heap property by performing heapify_up
        self.heapify_up(current_key)

    def delete_key(self, current_key):
        """
        Delete an element from the d-array.
            - current_key: Index of the element to delete.
        """
        if current_key >= len(self.heap):
            print("Invalid current key")
        # Swap current key with the last leaf, then delete the last and fix the heap
        else:
            last_index = len(self.heap) - 1
            self.heap[current_key], self.heap[last_index] = self.heap[last_index], self.heap[current_key]
            del self.heap[last_index]
            self.heapify_down(current_key)


def read_numbers(heap_, filename):
    """
    Reads integers from a file and inserts them into a heap.
    The numbers in the file must be seperated by whitespaces or comma.
        - heap_: An instance of the heap data structure.
        - filename: The name of the file containing integers.
    """
    try:
        with open(filename, 'r') as file:
            values = [int(value) for value in re.split(r'[,\s]+', file.read().strip())]
            for value in values:
                heap_.insert(value)
    except ValueError as e:
        print(f"Error: {e}")
        exit()


def get_d_array():
    """
    Gets the d-array value from the user.
    :return: The d-array value.
    """
    while True:
        try:
            D = int(input("Enter d-array (an integer greater than 0): "))
            if D > 0:
                return D
            else:
                print("Invalid input. Please enter an integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python.py file_name.txt")
        exit()
    else:
        file_name = sys.argv[1]
        d = get_d_array()
        print(f"Generate a {d}-array maxed heap.")
        heap = DArrayMaxHeap(d)
        print("Read numbers from the file...")
        read_numbers(heap, file_name)
        print("Print the heap:")
        heap.print_heap()
        print("Extracting max value.")
        heap.extract_max()
        print(f"Now heap looks like this: {heap.heap}")
        print("Increase 3 key to 100.")
        heap.increase_key(3, 100)
        print(f"Now heap looks like this: {heap.heap}")
        print("Deleting 3 key from heap.")
        heap.delete_key(3)
        print(f"Now heap looks like this: {heap.heap}")
        print("Print the heap after deleting:")
        heap.print_heap()
