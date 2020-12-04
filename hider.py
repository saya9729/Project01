import math
import random
class Hider:
    anno=[0,0]
    def __init__(this, x, y):
        this.pos = [x, y]
    def announce(this,n,m):
        this.anno[0]=this.pos[0]+math.floor(random.uniform(-3,4))
        this.anno[1] = this.pos[1] + math.floor(random.uniform(-3, 4))
        if this.anno[0]<0:
            this.anno[0]=0
        elif this.anno[0]>=n:
            this.anno[0] = n-1
        if this.anno[1]<0:
            this.anno[1]=0
        elif this.anno[1]>=m:
            this.anno[1] = m-1
