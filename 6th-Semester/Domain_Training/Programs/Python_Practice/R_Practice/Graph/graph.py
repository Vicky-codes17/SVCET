class graph:
    def __init__(self,n):
        self.Adjlist = [[] for i in range(n)]
    
    def addedge(self,u,v):
        self.Adjlist[u].append(v)
        self.Adjlist[v].append(u)

    def display(self):
        for i in range(len(self.Adjlist)):
            print("Adj List  {} : ".format(i),end = "")
            for j in self.Adjlist[i]:
                print("--> {}".format(j),end = " ")
            print()

if __name__ == "__main__":
    x  = graph(6)
    x.addedge(0,3)
    x.addedge(0,2)
    x.addedge(1,2)
    x.addedge(1,4)
    x.addedge(2,4)
    x.addedge(3,5)
    x.addedge(4,3)
    x.display()