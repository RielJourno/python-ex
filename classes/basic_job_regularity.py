

def main():
    my_workers = workers_data()
    print(my_workers.add("A", 4))
    print(my_workers.add("A", 5))
    print(my_workers.add("B", 3))
    print(my_workers.add("C", 3))
    print(my_workers.get("A"))
    print(my_workers)

class workers_data():
    jobList = {}

    def __init__(self):
        pass

    def add(self, charJob, workerNumber):
        if workerNumber in self.jobList.values():
            return False
        else:
            self.jobList[charJob] = workerNumber
            return True

    def get(self, item):
        return self.jobList[item]

    def __str__(self):
        return "{}".format(self.jobList)



main()



