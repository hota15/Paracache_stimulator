MAIN_MEMORY_SIZE = 256
CACHE_SIZE = 32 
BLOCK_SIZE = 1 
ASSOCIATIVITY = 1

# Initialize the cache with '0' for each block
cache = [['0'] * BLOCK_SIZE for _ in range(CACHE_SIZE)]

def input_memory_addresses():
    addresses = input("Enter memory addresses separated by space: ").split()
    return [int(address) for address in addresses]

def calculate_tag(address):
    # for fully , entire adress is tag
    if ASSOCIATIVITY == 0:
        return address
    # for set tag= address/no of set for dm set=1 
    return address // (BLOCK_SIZE * CACHE_SIZE // ASSOCIATIVITY)

def calculate_index(address):
    #index =0 for fully
    if ASSOCIATIVITY == 0:
        return 0
    # remainder of address/no of sets for dm and set
    return (address // BLOCK_SIZE) % (CACHE_SIZE // ASSOCIATIVITY)

def cache_operation(address):
    if address >= MAIN_MEMORY_SIZE:
        print(f"Address {address} is out of main memory range.")
        return False

    tag = calculate_tag(address)
    index = calculate_index(address)
    
    if ASSOCIATIVITY == 0: # Fully 
        for i, block in enumerate(cache):
            if block[0] == '0' or block[0] == str(address):
                if block[0] == '0':
                    print(f"Cache miss for address {address}")
                    cache[i] = [str(address)] * BLOCK_SIZE
                    return False
                else:
                    print(f"Cache hit for address {address}")
                    return True
    else: # Direct mapped or set associative
        if cache[index] == ['0'] * BLOCK_SIZE:
            print(f"Cache miss for address {address}")
            cache[index] = [str(address)] * BLOCK_SIZE
            return False
        elif cache[index][0] == str(address):
            print(f"Cache hit for address {address}")
            return True
        else:
            print(f"Cache miss for address {address}")
            cache[index] = [str(address)] * BLOCK_SIZE
            return False

def main():
    addresses = input_memory_addresses()
    hits = 0
    misses = 0
    for address in addresses:
        hit = cache_operation(address)
        if hit:
            hits += 1
        else:
            misses += 1
    print(f"Total hits: {hits}")
    print(f"Total misses: {misses}")

if __name__ == "__main__":
    main()
