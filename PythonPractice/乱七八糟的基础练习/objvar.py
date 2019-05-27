class Robot:
    popuation = 0
    def __init__(self,name):
        self.name = name
        Robot.popuation+=1
        print("Name:{}".format(self.name))
    def __del__(self):
        print("{} was destoryed".format(self.name))
        Robot.popuation-=1
        if Robot.popuation == 0:
            print("{} is last one".format(self.name))
        else:
            print("still have {} robot".format(Robot.popuation))
    @classmethod
    def havemany(self):
        print("have {} robot".format(self.popuation))
    #havemany = staticmethod(havemany)

    def sayhi(self):
        print("{} saying hi".format(self.name))

droid1	=	Robot("R2-D2")
droid1.sayhi()
Robot.havemany()
droid2	=	Robot("C-3PO")
droid2.sayhi()
Robot.havemany()
print("\nRobots	can	do	some	work	here.\n")
print("Robots	have	finished	their	work.	So	let's	destroy	them.")
del droid1
del droid2
Robot.havemany()