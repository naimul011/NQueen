
# coding: utf-8

# In[131]:


import random

n = 8

class problem():
    
    board = list()
    neighbor = list()
    neigh_piecs = []
    pieces = []
    
    h = 0
    neighborh = 0
    
    def attacking(self,board,pieces,i,j):
        
        if i == j:
            return True
        elif pieces[i]==pieces[j] and (pieces[i] == 'Q' or pieces[i] == 'R'):
            return i != j and (board[i] == board[j] or abs(board[i] - board[j])) == abs(i-j)
        elif pieces[i]==pieces[j] and pieces[i] == 'R':
            return i != j and board[i] == board[j]
        
    def __init__(self):
        self.board = random.sample(range(n), n)
        self.neighbor = list(self.board)
        

        pos = random.sample(range(8), 4)

        for i in range(8):
            if i in pos :
                self.pieces.append('R')
            else:
                self.pieces.append('Q')
        self.neigh_piecs = list(self.pieces)
        
    def calValue(self,board,pieces):
        h = 0
        for i in range(len(board)):
            
            for j in range(len(board)):
                
                if self.attacking(board,pieces,i,j):
                        h += 1
                        #print('abs(board[',i,'] - board[',j,'])) == abs(',i,'-',j,')')
        self.h = h//2
            

        return int(h//2)
    
    
    def selectNeighbor(self,q):
        
        self.neighbor = list(self.board)
        neigh_piecs = list(self.pieces)
        
        board = list(self.board)
        pieces = list(self.pieces)

        for pos in range(len(self.board)):
            self.neighbor = list(board)
            self.neigh_piecs = list(neigh_piecs)
            
            if (pos != board[q]):
                self.neighbor[q] = pos

            p = random.sample(range(8), 4)
            
            for i in range(8):
                if i in p :
                    self.pieces[i] = 'R'
                else:
                    self.pieces[i] = 'Q'
                    
            self.neigh_piecs = list(self.pieces)
                                    
                
            #print('c ',board,' ',self.calValue(board,pieces),'  ',self.neighbor,' ',self.calValue(self.neighbor,self.neigh_piecs))
            if self.calValue(board,pieces) > self.calValue(self.neighbor,self.neigh_piecs):
                print(self.calValue(board,pieces),' >= ',self.calValue(self.neighbor,self.neigh_piecs))
                board = list(self.neighbor)
                    
                    
                    
                
                
        return list(board)
               
    def hillclimbing(self):
        
        while 1:
            
            for q in range(len(self.board)):
                self.neighbor = self.selectNeighbor(q)
                
                print(self.calValue(self.board,self.pieces),' ',self.calValue(self.neighbor,self.neigh_piecs))
                if self.calValue(self.board,self.pieces) <= self.calValue(self.neighbor,self.neigh_piecs):
                    
                    print ('Optimal solution value ',problem.calValue(self.board,self.pieces))
                    return list(self.board)
                
                
                self.board = list(self.neighbor)

                    
problem = problem()

print ('Chess board: ',problem.pieces)
print ('Current position: ',problem.board)
print ('H value ',problem.calValue(problem.board,problem.pieces))
print ('Result ',problem.hillclimbing())
print ('Pieces ',problem.pieces)



def hillclimbing (problem):
    current = problem.intial_state()
    neighbor = problem.height()
    while neighbor.calValue() > current.calValue :
        neighbor = problem.height()
        
        if neighbor.calValue() <= current.calValue() :
            return current.board

