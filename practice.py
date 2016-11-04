def get_max_profit(prices):

    max_profit = 0

    # every time 
    for outer_time in xrange(len(stock_prices_yesterday)):
        for inner_time in xrange(len(stock_prices_yesterday)):

            # find max and minimum times
            earlier_time = min(outer_time, inner_time)
            later_time = max(outer_time, inner_time)

            # find the earlier and price
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price = stock_prices_yesterday[later_time]

            potential_profit = later_price - earlier_time

            max_profit = max(max_profit, potential_profit)   

    return max_profit


def get_products_of_all_ints_except_at_index(int_list):

    # we make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    i = 0
    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    product_so_far = 1
    i  = len(int_list) - 1
    while i > 0:
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i -= 1


    print products_of_all_ints_except_at_index



from itertools import islice

def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # we could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest =  min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

    # except this one--we pre-populate it for the first /3/ items.
    # this means in our first pass it'll check against itself, which is fine.
    highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # walk through items, starting at index 2 --> thanks itertools
    for current in islice(list_of_ints, 2, None):

        # do we have a new highest product of 3?
        # it's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        # do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    print highest_product_of_three

def merged_meeting_times(tuples):
    sorted_times = sorted(tuples)
    start_time, end_time = tuples[0]
    condensed_times = []
    for i in tuples:
        if end_time > i[0]:
            end_time = max(end_time, i[1])
        else:
            condensed_times.append((start_time, end_time))
            start_time, end_time = i 
    condensed_times.append((start_time, end_time))
    print condensed_times

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect(object):
    def __init__(self, p1, p2):
        '''Store the top, bottom, left and right values for points 
               p1 and p2 are the (corners) in either order
        '''
        self.left   = min(p1.x, p2.x)
        self.right  = max(p1.x, p2.x)
        self.bottom = min(p1.y, p2.y)
        self.top    = max(p1.y, p2.y)

def overlap(r1, r2):
    '''Overlapping rectangles overlap both horizontally & vertically
    '''
    h_overlaps = (r1.left <= r2.right) and (r1.right >= r2.left)
    v_overlaps = (r1.bottom <= r2.top) and (r1.top >= r2.bottom)
    print h_overlaps and v_overlaps

def count_change(money, coins):
    if money < 0:
        return 0
    if money == 0:
        return 1
    if money > 0 and not coins:
        return 0
    return count_change(money-coins[-1], coins) + count_change(money, coins[:-1])

class TreeNode(object):
    """Node of a Binary tree."""
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
    def __str__(self):
        return "{0}".format(self.key)


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def is_root(self, node):
        return node.key == self.root.key

    def is_leaf(self, node):
        if node is None or self.is_root(node):
            return False
        return node.left is None and node.right is None

    def is_internal(self, node):
        return not self.is_leaf(node)

    def is_full(self):

        def recurse(node):
            if node is None:
                return True
            if self.is_leaf(node):
                return True
            if node.left is not None and node.right is not None:
                return recurse(node.left) and recurse(node.right)
            return False
        return recurse(self.root)

    def height(self):
        return self.node_height(self.root)

    def node_height(self, node):
        if node is None or self.is_leaf(node):
            return 0
        return max(self.node_height(node.left), self.node_height(node.right)) + 1
    
    def is_super_balanced(self):
        def recurse(node):
            if node is None:
                return True
            left_height = node_height(node.left)
            right_height = node_height(node.right)
            return abs(left_height - right_height) < 1
        return recurse

class TempTracker:
    
    def __init__(self):
        # initialize instance variables
        self.temps = list(0 for x in xrange(111))
        self.max_temp = None
        self.min_temp = None
        self.mean_temp = None
        self.temp_sum = 0
        self.temp_num = 0

    def insert(self, temperature):        
        self.temps[temperature] += 1        
        self.temp_sum += temperature
        self.temp_num += 1
        if self.min_temp == None or temperature < self.min_temp:
            self.min_temp = temperature
        if self.max_temp == None or temperature > self.max_temp:
            self.max_temp = temperature
  
    def get_max(self):        
        # return max temp ever added
        return self.max_temp
  
    def get_min(self):
        # return min temp ever added
        return self.min_temp
  
    def get_mean(self):
        # return mean of all temps added
        if self.temp_num > 0:
            return self.temp_sum/float(self.temp_num)
        else:
            return None
  
    def get_mode(self):
        # return mode of all temps added        
        if self.temp_num:
            return self.temps.index(max(self.temps))
        else:
            return None


class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def findKthLargest(self, root, k):
        global count
        if root is None:
            return
        findKthLargest(root.right, k)
        count += 1
        if count == k:
            print root.value
            return
        findKthLargest(root.left, k)

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.q.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        

    def empty(self):
        """
        :rtype: bool
        """
        len(self.q) == 0

class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: 
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items: 
            return None
        return self.items[-1]


class MaxStack(Stack):

    # initialize an empty list
    def __init__(self):
        self.items = []

    def get_max(self):
        return max(items)

def kth_smallest_element(arr1, arr2, k):
    temp = []
    i = 0
    for i in arr1:
        temp[i] = arr1[i]
    for j in arr2:
        temp[i] = arr2[j]
        i += 1
    return sorted(temp, reverse=False)[k+1]


def mergeSort(seq):
    if len(seq) == 0:
        return 0
    elif len(seq) < 2:
        return seq
    m = len(seq) / 2
    return merge(merge_sort(seq[:m]), merge_sort(seq[m:]))
        
def merge(left, right):
    result = []
    i, j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def findComplementingWeights(arr, limit):
    hashtable = {}
    for index, mass in enumerate(arr):
        if mass in hashtable:
            print hashtable[mass], index
            return hashtable[mass], index
        else:
            hashtable[limit - mass] = index
    return -1

def findKth(A, B, k):
    if len(A) > len(B):
        A, B = (B,A)

    if not A:
        return B[k]

    if k == len(A) + len(B) - 1:
        return max(A[-1], B[-1])

    i = min(len(A) -1, k/2)
    j = min(len(B) - 1, k -i)

    if A[i] > A[j]:
        return findKth(A[:i], B[j:], i)
    else:
        return findKth(A[i:], B[:j], j)

def preOrderTraversal(root):
    result = []
    node = []
    if not root:
        return res
    node.append(root)
    while node:
        temp = node.pop()
        result.append(temp)
        if temp.right:
            node.append(temp.right)
        else:
            result.append(temp.left)
    return result

def inorderTraversal(self, root):
    if not root:
        return []
        
    stack = [root]
    ans = []
    
    while stack:
        node = stack.pop()
        if isinstance(node, int):
            ans.append(node)
            continue
        if node.right:  # if has right node, push into stack
            stack.append(node.right)
        stack.append(node.val)  # Push VALUE into stack, in between left and right
        if node.left:  # if has left node, push into stack
            stack.append(node.left)
            
    return ans



def max_duffel_bag_value(cake_tuples, weight_capacity):

    # we make a list to hold the maximum possible value at every
    # duffel bag weight capacity from 0 to weight_capacity
    # starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in xrange(weight_capacity + 1):

        # set a variable to hold the max monetary value so far for current_capacity
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples:

            # if a cake weighs 0 and has a positive value the value of our duffel bag is infinite!
            if (cake_weight == 0 and cake_value != 0):
                return float('inf')

            # if the current cake weighs as much or less than the current weight capacity
            # it's possible taking the cake would give get a better value
            if (cake_weight <= current_capacity):

                # so we check: should we use the cake or not?
                # if we use the cake, the most kilograms we can include in addition to the cake
                # we're adding is the current capacity minus the cake's weight. we find the max
                # value at that integer capacity in our list max_values_at_capacities
                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]

                # now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake, current_max_value)

        # add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight_capacity]



class LinkedListNode:

def __init__(self, value):
    self.value = value
    self.next  = None

def check_cycle(first_node):

# start both runners at the beginning
slow_runner = first_node
fast_runner = first_node

# until we hit the end of the list
while fast_runner is not None and fast_runner.next is not None:
    slow_runner = slow_runner.next
    fast_runner = fast_runner.next.next

    # case: fast_runner is about to "lap" slow_runner
    if fast_runner is slow_runner:
        return True

# case: fast_runner hit the end of the list
return False

def is_single_riffle_recursive_optimized(half1, half2, shuffled_deck, shuffled_deck_index=0, half1_index=0, half2_index=0):

    # base case we've hit the end of shuffled_deck
    if shuffled_deck_index == len(shuffled_deck):
        return True

    # if we still have cards in half1
    # and the "top" card in half1 is the same
    # as the top card in shuffled_deck
    if (half1_index < len(half1)) and \
            half1[half1_index] == shuffled_deck[shuffled_deck_index]:
        half1_index += 1

    # if we still have cards in half2
    # and the "top" card in half2 is the same
    # as the top card in shuffled_deck
    elif (half2_index < len(half2)) and \
            half2[half2_index] == shuffled_deck[shuffled_deck_index]:
        half2_index += 1

    # if the top card in shuffled_deck doesn't match the top
    # card in half1 or half2, this isn't a single riffle.
    else:
        return False

    # the current card in shuffled_deck has now been "accounted for"
    # so move on to the next one
    shuffled_deck_index += 1

    return is_single_riffle_recursive_optimized(half1, half2, shuffled_deck, shuffled_deck_index, half1_index, half2_index)



if __name__ == '__main__':
    coinsOptions = [1, 2, 3]
    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    meeting_times =   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    limit = 2
    # findComplementingWeights(stock_prices_yesterday, limit)
    # p1 = Point(1,1)
    # p2 = Point(3,3)
    # r1 = Rect(p1,p2)
    # p3 = Point(2,2)
    # p4 = Point(4,4)
    # r2 = Rect(p3,p4)
    # count_change(10, coinsOptions)
    # merge_sort(seq)


    # merged_meeting_times(meeting_times)
    # get_products_of_all_ints_except_at_index(stock_prices_yesterday)
    # get_max_profit(stock_prices_yesterday)
    # highest_product_of_three(stock_prices_yesterday)
    # overlap(r1,r2)

