class bonus():
    def __init__(self,incentive):
        self.incentive=incentive
    def totalsal(self,basesal):
        print("Total Salary is {}".format(basesal+self.incentive))