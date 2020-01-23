#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #find profit
  profit = prices[1] - prices[0]
#loop throu prices
  for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
   # If the diff of prices[j] - prices[i] is greater
      # than profit. Update profit to
         # new profit.
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
  return profit


print(find_max_profit([44, 30, 24, 32, 35, 30, 40, 38, 15]))
print(find_max_profit([1050, 270, 1540, 3800, 2]))
        


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))