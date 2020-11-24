import random
import math

class matrix:
    def __init__(this, row, col):
        this.Row = row
        this.Col = col
        this.Matrix = [[0 for i in range(col)] for j in range(row)]

    def randomize(this):
        for i in range(this.Row):
            for j in range(this.Col):
                this.Matrix[i][j] = random.uniform(-1, 1)

    def mutate(this, rate):
        for i in range(this.Row):
            for j in range(this.Col):
                rand = random.random()
                if rand < rate:
                    this.Matrix[i][j] += random.normalvariate(0, 1) / 5
                    if this.Matrix[i][j] > 1:
                        this.Matrix[i][j] = 1
                    if this.Matrix[i][j] < -1:
                        this.Matrix[i][j] = -1

    def array_to_matrix(this, array):
        this.new = matrix(len(array), 1)
        for i in range(len(array)):
            this.new.Matrix[i][0] = array[i]
        return this.new

    def add_bias(this):
        this.new=matrix(this.Row+1,1)
        for i in range (this.Row):
            this.new.Matrix[i][0]= this.Matrix[i][0]
        this.new.Matrix[this.Row][0]=1
        return this.new

    def activate(this):
        this.new=matrix(this.Row,this.Col)
        for i in range(this.Row):
            for j in range (this.Col):
                this.new.Matrix[i][j]=this.sigmoid(this.Matrix[i][j])
        return this.new

    def sigmoid(this,x):
        y=1.0/(1+math.exp(-x))
        return y

    def crossover(this,partner):
        this.child=matrix(this.Row,this.Col)

        rand_col=math.floor(random.uniform(0,this.Col))
        rand_row=math.floor(random.uniform(0,this.Row))

        for i in range(this.Row):
            for j in range(this.Col):
                if i<rand_row or i==rand_row and j<=rand_col:
                    this.child.Matrix[i][j]=this.Matrix[i][j]
                else:
                    this.child.Matrix[i][j] = partner.Matrix[i][j]
        return this.child

    def clone(this):
        this.clone=matrix(this.Row,this.Col)
        for i in range (this.Row):
            for j in range(this.Col):
                this.clone.Matrix[i][j]=this.Matrix[i][j]
        return this.clone

    def dot(this,n):
        this.result=matrix(this.Row,n.Col)

        if this.Col==n.Row:
            for i in range(this.Row):
                for j in range(n.Col):
                    sum=0
                    for k in range (this.Col):
                        sum+=this.Matrix[i][k]*n.Matrix[k][j]
                    this.result.Matrix[i][j]=sum
        return this.result

    def to_array(this):
        this.array=[]
        for i in range(this.Row):
            for j in range(this.Col):
                this.array.append(this.Matrix[i][j])
        return this.array