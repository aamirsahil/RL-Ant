import random as rd

class QLearn:
    def __init__(self,epsilon=0.1,alpha=0.2,lambd=0.5,epsilon_decay=0.01, decay_till=0) -> None:
        self.q = {}
        self.oldstate=None
        self.actions=None
        self.epsilon=epsilon
        self.alpha=alpha
        self.lambd=lambd
        self.epsilon_decay=epsilon_decay
        self.decay_till = decay_till
        self.reward = 0
        self.age = 0
    # initialize Q table
    def load(self, states, actions):
        self.setAction(actions)
        for state in states:
            for action in actions:
                value = 0.0
                self.setQ(state, action, value)
    # get q value foe (state,action) pair
    def getQ(self,state,action):
        return self.q.get((state,action), 0.0)
    # set q value for (state,action) pair
    def setQ(self,state,action,value):
        self.q[(state,action)]=value
    # set all available actions
    def setAction(self, actions):
        self.actions=actions
    # choose an action given the current state
    def decide(self,state):
        self.oldstate=state
        if rd.random()<self.epsilon:
            action=rd.choice(self.actions)
        else:
            q=[self.getQ(state,a) for a in self.actions]
            max_q=max(q)
            max_ind=[]
            for i in range(len(q)):
                if max_q == q[i]:
                    max_ind.append(i)
            i = rd.choice(max_ind)
            action=self.actions[i]    

        self.age += 1
        if(self.age % 100 == 0 and self.epsilon > self.decay_till):
            self.epsilon *= self.epsilon_decay
            self.age = 0
    
        self.oldaction=action
        return action
    # update q value with Bellmann equation
    def learn(self,newstate):
        if self.oldstate==None: 
            return
        oldq=self.getQ(self.oldstate,self.oldaction)
        maxqnew=max([self.getQ(newstate,a) for a in self.actions])
        self.setQ(self.oldstate,self.oldaction,oldq+self.alpha*(self.reward+self.lambd*maxqnew-oldq))