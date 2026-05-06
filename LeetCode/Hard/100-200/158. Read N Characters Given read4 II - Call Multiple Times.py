# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:

    def __init__(self):
        self.buf4 = ['']*4
        self.i = 0
        self.size = 0
    def read(self, buf: List[str], n: int) -> int:
        idx = 0

        while idx<n:

            if self.i==self.size:
                self.size = read4(self.buf4)
                self.i = 0 

                if self.size == 0:
                    break
            
            while idx<n and self.i<self.size:
                buf[idx] = self.buf4[self.i]
                idx+=1
                self.i+=1
        return idx