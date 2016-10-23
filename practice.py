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

def make_change(amount, denominations):
    denominations = sorted(denominations, reverse = True)
    coin_count = 0
    if amount < 0:
        return 0
    elif max(denominations) > amount:
        return 0
    else:
        for coin in denominations:
            amount = amount - coin
            coin_count += 1
    print coin_count

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


if __name__ == '__main__':
    coinsOptions = [1, 2, 3]
    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    meeting_times =   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

    p1 = Point(1,1)
    p2 = Point(3,3)
    r1 = Rect(p1,p2)
    p3 = Point(2,2)
    p4 = Point(4,4)
    r2 = Rect(p3,p4)
    # make_change(10, coinsOptions)
    # merged_meeting_times(meeting_times)
    # get_products_of_all_ints_except_at_index(stock_prices_yesterday)
    # get_max_profit(stock_prices_yesterday)
    # highest_product_of_three(stock_prices_yesterday)
    # overlap(r1,r2)

