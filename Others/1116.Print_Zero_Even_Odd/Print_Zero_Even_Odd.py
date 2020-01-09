from threading import Semaphore

class ZeroEvenOdd:
    # Use three 0-value Semaphores to lock and unlock each thread
    def __init__(self, n):
        self.n = n
        self.num = 0
        self.gates = [Semaphore(), Semaphore(), Semaphore()]
        self.gates[0].acquire()
        self.gates[1].acquire()
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.gates[2].acquire()
            printNumber(0)
            self.num += 1
            self.gates[self.num % 2].release()        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.gates[0].acquire()
            printNumber(self.num)
            self.gates[2].release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):
            self.gates[1].acquire()
            printNumber(self.num)
            self.gates[2].release()
        
        