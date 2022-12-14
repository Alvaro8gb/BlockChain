import hashlib as hl
from sys import maxsize
import time

from lib import Block, Transaction

NUMBER_of_CHARACTER = 4 # 6 -> 30 segs
CHARACTER = '0'

def good_hash(hash):
    """
    cheching if a hash meet some conditions

    """

    if str(hash[:NUMBER_of_CHARACTER]) == CHARACTER * NUMBER_of_CHARACTER :
        print('Found!')
        return True
    
    return False
    
def mining(block_name, transactions, previus_hash, cycles = maxsize):
    """
    Mining a block up to n cycles.
    
    """
        
    for nonce in range(cycles):
        
        hash_alg = hl.sha256()
        block = str(Block(transactions, nonce, previus_hash))
        hash_alg.update(block.encode())
        hash = hash_alg.hexdigest()

        if good_hash(hash):
            print('Hash : ', hash)
            f = open(block_name ,'w', encoding="utf-8")
            print(block)
            f.write(block)
            f.close()
            break

    print("Not mine")


if __name__ == '__main__':
    previus_hash = "0000d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79"
    transactions = [Transaction("Dani","Alvaro","100 ₿"),
                     Transaction("Alvaro","Julia","50 ₿"), 
                     Transaction("Julia","Maria","25 ₿")]
    
    start = time.time()
    mining("block_content_file", transactions, previus_hash, 1000000000)
    end = time.time()

    print("Time mining: ", end-start)


