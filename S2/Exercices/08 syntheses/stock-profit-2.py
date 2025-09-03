def stock_profit(stock: list) -> int:
    res,minimum=0,stock[0]
    for st in stock:
        res=max(res,st-minimum)
        minimum=min(st,minimum)
    return res

#**********

def stock_profit(stock: list) -> int:
    return max([0] + [max([x - stock[i] for x in stock[i+1:]]) for i in range(len(stock)-1)])

#**********

def stock_profit(stock: list) -> int:
    n=1
    profits=[0]
    for buy in stock:
        
        for sell in stock[n:]:
            profits.append(sell-buy)
        n+=1
    return max(profits)

