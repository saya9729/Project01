import matrix

class neural_network:
    def __init__(this, input, hidden, output):
        this.Input = input
        this.Hidden = hidden
        this.Output = output
        this.input_matrix = matrix.matrix(hidden, input + 1)
        this.hidden_matrix = matrix.matrix(hidden, hidden + 1)
        this.output_matrix = matrix.matrix(output, hidden + 1)

    def mutate(this, rate):
        this.input_matrix.mutate(rate)
        this.hidden_matrix.mutate(rate)
        this.output_matrix.mutate(rate)

    def output(this, array):
        this.input = this.input_matrix.array_to_matrix(array)
        this.input_bias = this.input.add_bias()

        this.hidden_input = this.hidden_matrix.dot(this.input_bias)
        this.hidden_ouput = this.hidden_input.activate()
        this.hidden_output_bias = this.hidden_ouput.add_bias()

        this.hidden_input_2 = this.hidden_matrix.dot(this.hidden_output_bias)
        this.hidden_ouput_2 = this.hidden_input_2.activate()
        this.hidden_output_bias_2 = this.hidden_ouput_2.add_bias()

        this.output_input = this.output_matrix.dot(this.hidden_output_bias_2)
        this.output = this.output_input.activate()

        return this.output.to_array()

    def crossover(this, partner):
        this.child = neural_network(this.Input, this.Hidden, this.Output)
        this.child.input_matrix = this.input_matrix.crossover(partner.input_matrix)
        this.child.hidden_matrix = this.hidden_matrix.crossover(partner.hidden_matrix)
        this.child.output_matrix = this.output_matrix.crossover(partner.output_matrix)
        return this.child

    def clone(this):
        this.clone = neural_network.(this.Input, this.Hidden, this.Output)
        this.clone.input_matrix = this.input_matrix.clone()
        this.clone.hidden_matrix = this.hidden_matrix.clone()
        this.clone.output_matrix = this.output_matrix.clone()
        return this.clone
