class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self._size += n
        if n > self._capacity or self._size > self._capacity:
            raise ValueError

    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar(4)
    jar.deposit(2)
    jar.withdraw(1)
    print(jar.capacity)
    print(jar.size)


if __name__ == "__main__":
    main()
