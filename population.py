import seeker
import math
import random
import main


class population:
    Seeker = []

    gen = 1
    global_best = 0
    global_best_fitness = 0
    current_best_index = 0
    current_best_fitness = 0

    global_best_seeker = seeker.seeker(0, 0)
    population_id = math.floor(random.uniform(0, 1000000))

    def __init__(this, size):
        for i in range(size):
            this.Seeker.append(seeker.seeker(0, 0))
        this.global_best_seeker = this.Seeker[0].clone()

    def update(this):
        for i in range(len(this.Seeker)):
            if not this.Seeker[i].dead:
                this.Seeker[i].look()
                this.Seeker[i].set_direction()
                this.Seeker[i].move()
        this.set_best_seeker()

    def cal_fitness(this):
        for i in range(len(this.Seeker)):
            this.Seeker[i].cal_fitness()

    def natual_selection(this):
        this.new = []
        this.set_best_seeker()
        this.new.append(this.global_best_seeker.clone())
        for i in range(1, len(this.Seeker)):
            this.parent_1 = this.select_seeker()
            this.parent_2 = this.select_seeker()

            this.child = this.parent_1.crossover(this.parent_2)

            this.child.mutate(main.global_mutation_rate)

            this.new.append(this.child)
        this.Seeker = this.new

        this.gen += 1
        this.current_best_fitness = 0

    def select_seeker(this):
        fitness_sum = 0
        for i in this.Seeker:
            fitness_sum += i.fitness

        rand = math.floor(random.uniform(0, fitness_sum))

        running_sum = 0

        for i in this.Seeker:
            running_sum += i.fitness
            if running_sum > rand:
                return i

        return this.Seeker[0]

    def set_best_seeker(this):
        max = 0
        max_index = 0
        for i in range(len(this.Seeker)):
            if this.Seeker[i].fitness > max:
                max = this.Seeker[i].fitness
                max_index = i
        if max > this.global_best_fitness:
            this.global_best_fitness = max
            this.global_best_seeker = this.Seeker[max_index].clone()
