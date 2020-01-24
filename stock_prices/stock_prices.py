#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #find profit
  profit = prices[1] - prices[0]
#loop throu prices
  for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
   # If the diff of prices[j] - prices[i] is greater than profit. Update profit to new profit.
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
  return profit


print(find_max_profit([10, 7, 5, 8, 11, 9]))
print(find_max_profit([1050, 270, 1540, 3800, 2]))

# Flow of this function:
# j = 1, i = 0,  7 - 10 = -3 initialized
# j = 2, i = 0,  5 -10 = -5, max_prof doesnt change
# j = 2, i= 1,   5 - 7 = -2 so max_prof is now -2
# j = 3, i = 0,  8 - 10 = -2, max_prof no change
# j = 3, i = 1,  8 - 7 = 1, max_prof = 1
# j = 3, i = 2,  8 - 5 = 3, max_prof = 3
# j = 4, i = 0,  11 - 10 = 1, max_prof no change
# j = 4, i = 1,  11 - 7 = 4, max_prof = 4
# j = 4, i = 2,  11 - 5 = 6, max_prof = 6



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))