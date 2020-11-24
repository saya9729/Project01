import brain
import main

class seeker:
    dead = False
    caught=False
    best=False
    vision=[]
    fitness=0
    decision=[]
    step_to_go=100
    next_step=0
    movement=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,-1]]
    for i in range((2 * main.vision_radius + 1) ** 2 + 1):
        vision.append(-1)

    def __init__(this, x, y):
        this.location = [x, y]
        this.Brain=brain.neural_network((2 * main.vision_radius + 1) ** 2 + 1,25,8)
        this.step_to_go=100

    def mutate(this):
        this.Brain.mutate()

    def set_direction(this):
        this.decision=this.Brain.output(this.vision)

        max=0
        this.next_step=0
        for i in range(len(this.decision)):
            if max<this.decision[i]:
                max=this.decision[i]
                this.next_step=i

    def suicide(this,next_step):
        if this.location[0]+this.movement[next_step][0]<0 or this.location[0]+this.movement[next_step][0]>=main.n or this.location[1]+this.movement[next_step][1]<0 or this.location[1]+this.movement[next_step][1]>=main.m:
            return True
        if main.map[this.location[0]+this.movement[next_step][0]][this.location[1]+this.movement[next_step][1]]==1:
            return True

    def catch(this,next_step):
        if main.map[this.location[0]+this.movement[next_step][0]][this.location[1]+this.movement[next_step][1]]==3:
            return True

    def move(this):
        this.step_to_go-=1
        if this.step_to_go<0:
            this.dead=True
        if this.suicide(this.next_step):
            this.dead = True
        if this.catch(this.next_step):
            this.caught=True

