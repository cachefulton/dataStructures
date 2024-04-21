class HashMap: # I did this with a list of lists
    def __init__(self):
        self.buckets = 7 # initial capacity
        self.table = []
    def get(self, key):
        '''Return the value for key if key is in the dictionary.
        If key is not in the dictionary, raise a KeyError.
        '''
        key_index = 0
        val_index = 1
        hash_val = (key[0] * key[1]) % self.buckets
        count = 0
        while self.table and self.table[hash_val + count] is not None: # not empty and not none value
            if self.table[hash_val + count][key_index] == key:
                return self.table[hash_val + count][val_index]
            count += 1
            if hash_val + count > len(self.table) - 1:
                #start count again from beginning of table/list
                count = 0
                hash_val = 0
        raise KeyError
    def set(self, key, value):
        '''Add the (key,value) pair to the hashMap. 
        After adding, if the load-factor>= 80%, rehash the map into a map 2k - 1 its current capacity.
        '''
        def add(table, key, value):
            '''Hash value is row * column % buckets. Collision res. is linear'''
            hash_val = (key[0] * key[1]) % self.buckets #row times column
            count = 0
            while table[hash_val + count] is not None and table[hash_val + count][0] != key:
                count += 1
                if hash_val + count > len(table) - 1:
                    #start count again from beginning of table/list
                    count = 0
                    hash_val = 0
            table[hash_val + count] = [key, value]
        def rehash():
            new_table = []
            for i in range(self.buckets):
                new_table.append(None)
            for item in self.table:
                if item is None: # None item
                    continue
                kee, val = item
                add(new_table, kee, val)
            self.table = new_table
        if not self.table: # make the list the right size
            rehash()
        # add the item to my hash map.
        add(self.table, key, value)
        # calculate load factor, number of items (self.size()) / number of buckets
        load = self.size() / self.buckets
        # if greater >= .8 increase buckets and re-insert values into new hash buckets
        if load >= 0.8:
            self.buckets = self.buckets * 2 - 1
            rehash()
    def remove(self, key):
        '''Remove the key and its associated value from the map.
        If the key does not exist, nothing happens.
        Do not rehash the table after deleting keys.
        '''
        try:
            self.get(key) #see if key exists
            index = -1
            for item in self.table:
                index += 1
                if item and item[0] == key:
                   break
            self.table[index] = None 
        except: #if it doesn't do nothing
            pass
    def clear(self):
        '''Empty the HashMap'''
        # restart hash tabled
        self.table = []
        self.buckets = 7
    def capacity(self):
        '''Return the current capacity--number of buckets--in the map.'''
        return self.buckets
    def size(self):
        '''Return the number of key-value pairs in the map.'''
        count = 0
        for item in self.table:
            if item is not None:
                count += 1
        return count
    def keys(self):
        '''Return a list of keys.'''
        key_list = []
        for item in self.table:
            if item is not None:
                key_list.append(item[0])
        return key_list