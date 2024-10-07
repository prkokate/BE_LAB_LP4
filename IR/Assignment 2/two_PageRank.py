import numpy as np

class TwoPageRank:
    def __init__(self):
        self.path = np.zeros((10, 10))
        self.pagerank = np.zeros(10)

    def calc(self, totalNodes):
        InitialPageRank = 1 / totalNodes
        DampingFactor = 0.85
        TempPageRank = np.zeros(10)

        print(f"Total Number of Nodes: {totalNodes}\t Initial PageRank of All Nodes: {InitialPageRank}\n")

        # Initialize PageRank values
        for k in range(1, int(totalNodes) + 1):
            self.pagerank[k] = InitialPageRank

        print("\nInitial PageRank Values, 0th Step\n")
        for k in range(1, int(totalNodes) + 1):
            print(f"Page Rank of {k} is :\t{self.pagerank[k]}")

        # Perform 2 iterations
        ITERATION_STEP = 1
        while ITERATION_STEP <= 2:
            # Copy current PageRank values to TempPageRank and reset pagerank
            for k in range(1, int(totalNodes) + 1):
                TempPageRank[k] = self.pagerank[k]
                self.pagerank[k] = 0

            for InternalNodeNumber in range(1, int(totalNodes) + 1):
                for ExternalNodeNumber in range(1, int(totalNodes) + 1):
                    if self.path[ExternalNodeNumber][InternalNodeNumber] == 1:
                        # Count the number of outgoing links from ExternalNodeNumber
                        OutgoingLinks = sum(self.path[ExternalNodeNumber][1:int(totalNodes) + 1])
                        self.pagerank[InternalNodeNumber] += TempPageRank[ExternalNodeNumber] * (1 / OutgoingLinks)

            print(f"\nAfter {ITERATION_STEP}th Step")
            for k in range(1, int(totalNodes) + 1):
                print(f"Page Rank of {k} is :\t{self.pagerank[k]}")

            ITERATION_STEP += 1

        # Apply Damping Factor
        for k in range(1, int(totalNodes) + 1):
            self.pagerank[k] = (1 - DampingFactor) + DampingFactor * self.pagerank[k]

        print("\nFinal Page Rank:")
        for k in range(1, int(totalNodes) + 1):
            print(f"Page Rank of {k} is :\t{self.pagerank[k]}")

def main():
    nodes = int(input("Enter the Number of WebPages \n"))
    p = TwoPageRank()

    print("Enter the Adjacency Matrix with 1->PATH & 0->NO PATH Between two WebPages: \n")
    for i in range(1, nodes + 1):
        for j in range(1, nodes + 1):
            p.path[i][j] = int(input())
            if j == i:
                p.path[i][j] = 0

    p.calc(nodes)

if __name__ == "__main__":
    main()


# OUTPUT

# Enter the Number of WebPages 

# 4
# Enter the Adjacency Matrix with 1->PATH & 0->NO PATH Between two WebPages: 

# 0 1 0 1
# 1 2 3 0
# 2 1 0 1
# 0 2 1 1
#  Total Number of Nodes :4.0      Initial PageRank  of All Nodes :0.25

#  Initial PageRank Values , 0th Step
#  Page Rank of 1 is :    0.25
#  Page Rank of 2 is :    0.25
#  Page Rank of 3 is :    0.25
#  Page Rank of 4 is :    0.25

#  After 1th Step
#  Page Rank of 1 is :    0.25
#  Page Rank of 2 is :    0.25
#  Page Rank of 3 is :    0.25
#  Page Rank of 4 is :    0.25

#  After 2th Step
#  Page Rank of 1 is :    0.25
#  Page Rank of 2 is :    0.25
#  Page Rank of 3 is :    0.25
#  Page Rank of 4 is :    0.25

#  Final Page Rank :
#  Page Rank of 1 is :    0.36250000000000004
#  Page Rank of 2 is :    0.36250000000000004
#  Page Rank of 3 is :    0.36250000000000004
#  Page Rank of 4 is :    0.36250000000000004