import population
import seeker
import brain
class world:
    gen=0
    world_best_score=0
    best_brain=[]
    species=[]
    best_seeker=[]
    def __init__(this,species_no,pop_size):
        for i in range(species_no):
            this.species.append(population.population(pop_size))

        for i in range(5):
            this.best_seeker.append(seeker.seeker(0,0))#need changing
    def update(this):
        for i in this.species:
            i.update()

    def genetic_algorithm(this):
        for i in this.species:
            i.cal_fitness()
            i.natual_selection()
        this.gen+=1
        this.set_best_score()
        for i in range (len(this.species)):
            this.save_best_seeker()

    def load_best_seeker(this):
        for i in range (5):
            this.best_seeker[i]=this.best_seeker[i].load_seeker

    def done(this):
        for i in this.species:
            if not i.done():
                return False
        return True

    def set_best_score(this):
        max=0
        max_index=0
        for i in range(len(this.species)):
            if this.species[i].global_best_fitness>max:
                max=this.species[i].global_best_fitness
                max_index=i
        this.world_best_score=this.species[max_index].global_best
