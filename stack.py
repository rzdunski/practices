from unittest import TestCase

ELEMENT = 'element'


class Stack(object):
    def __init__(self, capacity=99):
        self.elements = [None] * capacity
        self.size = 0

    pass

    def push(self, element):
        if self.is_full():
            raise StackOverflowException()
        self.elements[self.size] = element
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise StackUnderflowException()
        self.size -= 1
        return self.elements[self.size]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return len(self.elements) == self.size


class StackUnderflowException(Exception):
    pass


class StackOverflowException(Exception):
    pass


class StackTest(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        self.assert_stack_size(0)

    def test_stack_size_after_push_is_one(self):
        self.stack.push(ELEMENT)
        self.assert_stack_size(1)

    def test_stack_size_after_push_and_pop_is_zero_again(self):
        self.stack.push(ELEMENT)
        self.stack.pop()

        self.assert_stack_size(0)

    def test_cannot_pop_an_empty_stack(self):
        with self.assertRaises(StackUnderflowException):
            self.stack.pop()

    def test_cannot_push_a_full_stack(self):
        self.stack = Stack(0)
        with self.assertRaises(StackOverflowException):
            self.stack.push(ELEMENT)

    def test_pops_pushed_element(self):
        self.stack.push(ELEMENT)
        popped = self.stack.pop()

        self.assertEqual(ELEMENT, popped)

    def test_pops_elements_in_reverse_order(self):
        self.stack.push("first pushed")
        self.stack.push("second pushed")

        first_popped = self.stack.pop()
        second_popped = self.stack.pop()

        self.assertEqual("second pushed", first_popped)
        self.assertEqual("first pushed", second_popped)

    def assert_stack_size(self, expected_size):
        self.assertEqual(expected_size, self.stack.size)