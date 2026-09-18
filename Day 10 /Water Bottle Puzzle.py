bottles = 10
exchange = 3
drunk = 0

while bottles >= exchange:
    drunk += bottles
    bottles = bottles // exchange + bottles % exchange

print("Bottles:", drunk + bottles)
