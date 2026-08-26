def best_chocolates(prices,window_size):
    current_total = sum(prices[0:window_size])
    best_total = current_total
    print(f"window : {prices[0:window_size]} = {current_total}")

    for i in range(window_size,len(prices)):
        left_choclate = prices[i-window_size]
        right_chocolate = prices[i]

        current_total = current_total - left_choclate + right_chocolate

        wiindow = prices[i-window_size+1 : i+1 ]
        print(f"window: {wiindow} = {current_total}")

        if current_total>best_total:
            best_total=current_total

    return best_total

prices = [2,4,6,1,7,3,5]
answer = best_chocolates(prices,3)
print("best totl",answer)
