import random
import random
import string


class Executor:
    def __init__(self, core, memory):
        self.core = core
        self.memory = memory
        self.id = ''.join(random.sample(list(set(string.printable) - set(['\n', '\t', '\r', '\x0b', '\x0c', '\\'])), 9))

    def __repr__(self):
        return f"Core:{self.core} Memory:{self.memory} Id: {self.id}"


class worker:
    def __init__(self, num_of_executors=None, core_per_executor=None, memory_per_executor=None, non_uniform=False,
                 non_uniform_executors=None):
        self.non_uniform = non_uniform

        if non_uniform == True:
            self.executors = non_uniform_executors
            self.num_of_executors = len(self.executors)
            self.cores_in_executors = [e.core for e in self.executors]
            self.memory_in_executors = [e.memory for e in self.executors]

        else:
            self.num_of_executors = num_of_executors
            self.core_per_executor = core_per_executor
            self.memory_per_executor = memory_per_executor
            self.create_uniform_executors()

    def create_uniform_executors(self):
        self.executors = [Executor(self.core_per_executor, self.memory_per_executor) for i in
                          range(self.num_of_executors)]

    def add_executor(self, c, m):
        new_exe = Executor(c, m)
        self.executors.append(new_exe)
        self.num_of_executors += 1
        return new_exe.id

    def __add__(self, other):
        return worker(non_uniform=True, non_uniform_executors=self.executors + other.executors)

    def __repr__(self) -> str:
        if self.non_uniform == True:
            return f'worker object is created {self.num_of_executors}, core per. executor {self.cores_in_executors}, memory: {self.memory_in_executors}'

        else:
            return f'worker object is created {self.num_of_executors}, core per. executor {self.core_per_executor}, memory: {self.memory_per_executor}'

    def __delitem__(self, id):
        self.executors = [executor for executor in self.executors if executor.id != id]
        self.num_of_executors -= 1

    def __getitem__(self, executor_id):
        return [executor for executor in self.executors if executor.id == executor_id][0]




