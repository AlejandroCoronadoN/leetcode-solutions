from random import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index_set = [list() for x in range(1000000)]
        self.block_size = round(2**32 //1000000)
        self.occupied_index = []
        self.index_set_len = 5000000
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the index_set. Returns True if the index_set did not already contain the specified element.
        """
        if val >=0:
          index = (val//self.block_size) + (self.index_set_len/2)
        else:
          index = (self.index_set_len/2)  - (val//self.block_size)

        if len(self.index_set[index]) ==0:
          self.index_set[index][0] == val 
          self.occupied_index.append(index)
          print(self.occupied_index)
          return True
        else:
          for i in range(len( self.index_set[index])):
            if self.index_set[index][i] == val:
              return False
          self.index_set[index][i+1]= val
          return True
          

        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the index_set. Returns True if the index_set contained the specified element.
        """
        
        if val >=0:
          index = val//self.block_size + 500000
        else:
          index = 500000  - val//self.block_size

          if len(self.index_set[index]) ==0:
            return False
          
          else:
            for i in range(len( self.index_set[index])):
              if self.index_set[index][i] == val:
                self.index_set[index].remove(self.index_set[index][i])
                return True
                if len(self.index_set[index]) == 0:
                  self.occupied_index.remove(index)
              
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the index_set.
        """
        occupied_index = self.occupied_index
        n_occupied = len(self.occupied_index)
        random_index =  int(random()*n_occupied//1)
        test =  self.index_set[random_index]
        random_number =  random()*self.index_set[random_index][int(random()*len(self.occupied_index[random_index]))]
        return random_number
                
        


# Your Randomizedindex_set object will be instantiated and called as such:
# obj = Randomizedindex_set()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()Insert Delete GetRandom O(1)