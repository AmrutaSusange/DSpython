import random
import random
import string

class Executor:
    def __init__(self, core, memory):
        self.core = core
        self.memory = memory
        self.id = ''.join(random.sample(list(set(string.printable) - set(['\n', '\t', '\r', '\x0b', '\x0c', '\\'])), 9))


class worker:
    def __init__(self, num_of_executors, core_per_executor, memory_per_executor):
        self.num_of_executors = num_of_executors
        self.core_per_executor = core_per_executor
        self.memory_per_executor = memory_per_executor

        self.create_executors()

    def create_executors(self):
        self.executors = [Executor(self.core_per_executor, self.memory_per_executor) for i in range(self.num_of_executors)]


    def add_executor(self, c, m):
        new_exe = Executor(c,m)
        self.executors.append(new_exe)
        self.num_of_executors += 1
        return new_exe.id

    def delete_executor(self, id):
        self.executors = [executor for executor in self.executors if executor.id != id]

    def __add__(self, other):

        return worker(
            num_of_executors=self.num_of_executors + other.core_per_executor,
            core_per_executor=self.core_per_executor + other.core_per_executor,
            memory_per_executor=self.memory_per_executor + other.memory_per_executor
        )












if __name__ == '__main__':
    w1 = worker(4, 4, 8)


    for executor in w1.executors:
        print("\n id=", executor.id)

    print("Additing new execut", w1.add_executor(4, 8))

    for executor in w1.executors:
        print("\n id=", executor.id)

    print(w1.num_of_executors)

    w1.delete_executor("32423443")

    w2 = worker(4,6,5)

    print((w1+w2).num_of_executors)




