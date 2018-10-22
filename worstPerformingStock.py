import sys

# Complete the worstPerformingStock function below.
def worstPerformingStock(prices):
    if len(prices) == 0:
        return 0
    worst_rate = sys.maxsize  # will update if lower than worst_rate
    for stock in prices:
        id = stock[0]
        opening = stock[1]
        closing = stock[2]
        rate = (closing-opening)/opening
        if rate < worst_rate:
            worst_rate = rate
            min_id = id
    return min_id
        

if __name__== "__main__":
	print worstPerformingStock([[1200,100,105],[1400,50,55]])