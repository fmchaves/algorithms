# Create a Stack Classpython
# In the last section, we talked about what a stack is and how we can use
# an array to represent a stack. In this section, we will be creating our own stack class.
# Although you can use arrays to create stacks, sometimes it is best to limit the amount
# of control we have with our stacks. Apart from the push and pop method,
# stacks have other useful methods. Let's add a peek, isEmpty, and clear method to our stack class.

class Stack(object):

    """A class used to implement a stack, Last-In-First-Ourt"""

    def __init__(self, *args):
        """
        Stack constructor
        
        Parameters
        ----------       
        *args : any
            items to be added to the stack
        """
        self._stack = list(args) if args else []

    def push(self, arg):
        """This method pushes an item on the top of the stack

        Parameters
        ----------
        arg : any
            the item to be added to the stack
        """
        self._stack.append(arg)

    def pop(self):
        """This method pops the top item of the stack

        Returns
        -------
        any
            the item on the top of the stack
        """
        ans = self._stack[-1]
        del self._stack[-1]
        return ans

    def peek(self):
        """This method looks on the top of the stack

        Returns
        -------
        any
            the item on the top of the stack
        """
        return self._stack[-1]

    def isEmpty(self) -> bool:
        """This method checks whether the stack is empty

        Returns
        -------
        boolean
            a boolean value that indicates whether a stack is empty
        """
        return len(self._stack) == 0

    def clear(self):
        """This method clears the stack by instantiating a new object

        Returns:
            object (Stack)
                an object of Stack class
        """
        return self.__init__()

    def __str__(self) -> str:
        """This magic method returns a string representing the stack.

        Returns:
            str
                a string representing the stack.
        """
        return str(self._stack)


s = Stack(1, 2, 3, 4)
print('Stack:', s)
s.push(5)
print('Push:', s)
print('Peek:', s.peek())
s.pop()
print('Pop:', s)
print('Is empty:', s.isEmpty())
s.clear()
print(s)
print('Is empty:', s.isEmpty())