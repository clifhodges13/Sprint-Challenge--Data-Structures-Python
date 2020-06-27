class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.oldest = None

    def append(self, item):
        # if buffer is empty,
        if len(self.buffer) == 0:
            # add item to list and
            self.buffer.append(item)
            # make new item the "oldest"
            self.oldest = item
            return self.oldest
        # if buffer is at capacity, replace oldest item with new item
        elif len(self.buffer) == self.capacity:
            # get the index of the oldest item
            index_oldest = self.buffer.index(self.oldest)
            # replace the oldest with the new item
            self.buffer[index_oldest] = item
            if (index_oldest+1) >= len(self.buffer):
                self.oldest = self.buffer[0]
            else:
                self.oldest = self.buffer[index_oldest+1]
        # if buffer is not at capacity, add item to end of buffer
        elif len(self.buffer) < self.capacity:
            self.buffer.append(item)
            return item

    def get(self):
        return self.buffer
