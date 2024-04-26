import math
def log2(x):
    return math.log(x, 2)

MAIN_MEMORY_SIZE =int(input("Enter main memory size"))
CACHE_SIZE = int(input("Enter cache memory size"))
BLOCK_SIZE = int(input("Enter block size"))
ASSOCIATIVITY = int(input("Enter associativity"))

# Initialize the cache with '0' for each block
no_of_blocks = CACHE_SIZE//BLOCK_SIZE
cache = [['0'] * BLOCK_SIZE for _ in range(CACHE_SIZE)]


def binary_representation(address, total_bits):
    # Convert the address to binary string
    binary_str = bin(address)[2:]
    
    # Check if the binary string needs padding
    if len(binary_str) < total_bits:
        # Calculate the padding length
        padding_length = total_bits - len(binary_str)
        # Pad the binary string with zeros
        binary_str = '0' * padding_length + binary_str
    
    return binary_str
def calculate_bits():
    tagbits = int(log2((MAIN_MEMORY_SIZE/CACHE_SIZE)))
    indexbits = int(log2((no_of_blocks)))
    wordbits = int(log2(BLOCK_SIZE))
    total_bits = tagbits + indexbits + wordbits
    
    print("no of tag bits" , tagbits)
    print("no of index bits" , indexbits)
    print("no of word bits" , wordbits)    
    return tagbits, indexbits, wordbits, total_bits

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
    tagbits, indexbits, wordbits, total_bits = calculate_bits()  
    for address in addresses:
        print(binary_representation(address, total_bits))  
        hit = cache_operation(address)
        if hit:
            hits += 1
        else:
            misses += 1

    total_accesses = hits + misses
    hit_ratio = hits / total_accesses if total_accesses > 0 else 0
    miss_ratio = misses / total_accesses if total_accesses > 0 else 0
    print(f"Total hits: {hits}")
    print(f"Total misses: {misses}")
    print(f"Hit ratio: {hit_ratio:.2f}")
    print(f"Miss ratio: {miss_ratio:.2f}")

if __name__ == "__main__":
    main()
