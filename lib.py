class Transaction:
   def __init__(self, sender, destination, amount): 
      self.sender = sender
      self.destination = destination
      self.amount = amount
   def __str__(self):
      return str(self.sender) + " ---> " + str(self.destination) + " : " + str(self.amount)

class Block:

     def __init__(self, transactions, nonce, previous_hash): 
        self.transactions = transactions
        self.nonce = nonce
        self.previous_hash = previous_hash

     def __str__(self):
        block_str = "Nonce: " + str(self.nonce) +"\nPrevious Hash: "+ str(self.previous_hash) +"\n"

        block_str += "Transactions:\n"

        for t in self.transactions:
            block_str+= "\t"+str(t) +"\n"

        
        return block_str

