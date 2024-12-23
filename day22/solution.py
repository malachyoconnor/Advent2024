from functools import cache

current_dir = "/".join(__file__.split("\\")[:-1])
secrets = open(f"{current_dir}/input.txt", "r").read()
secrets = [int(sec) for sec in secrets.split("\n")[:-1]]

@cache
def next_secret(secret):
    secret = mix(secret, secret << 6)
    secret = prune(secret)

    secret = mix(secret, secret // 32)
    secret = prune(secret)

    secret = mix(secret, secret << 11)
    secret = prune(secret)

    return secret

def mix(secret, other):
    return secret ^ other

def prune(secret):
    return secret % 16777216

def get_price(secret):
    return secret % 10

def update_sequence(price_sequence: list[int], price_change: int):
    if len(price_sequence) < 4:
        price_sequence.append(price_change)
        return
    
    price_sequence[0], price_sequence[1], price_sequence[2], price_sequence[3] = price_sequence[1], price_sequence[2], price_sequence[3], price_change

monkey_sequences = [dict() for _ in secrets]

def update_stored_best_sequences(sequence, monkey_id, price):    
    seq_tup = tuple(sequence)

    if seq_tup in monkey_sequences[monkey_id]:
        return
    
    monkey_sequences[monkey_id][seq_tup] = price


total = 0
for monkey_id, secret in enumerate(secrets):

    prev_price = get_price(secret)
    
    price_sequence = []

    for i in range(2000):
        secret = next_secret(secret)
        new_price = get_price(secret)

        price_change = new_price - prev_price
        update_sequence(price_sequence, price_change)
        update_stored_best_sequences(price_sequence, monkey_id, new_price)
        
        prev_price = new_price

    total += secret


all_sequences = set()

for sequence_dict in monkey_sequences:
    all_sequences.update(sequence_dict.keys())

best_price = 0

for sequence_tup in all_sequences:

    total = 0

    for sequence_dict in monkey_sequences:

        total += sequence_dict.get(sequence_tup, 0)

    best_price = max(best_price, total)

print(best_price)