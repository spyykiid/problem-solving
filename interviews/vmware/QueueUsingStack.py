instack = []
outstack = []

def enque(elem):
    instack.append(elem)
    

def deque():
    if not outstack:
        for _ range(len(instack)):
        outstack.append(instack.pop())
        
    outstack.pop()