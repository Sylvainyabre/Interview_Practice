from queue import PriorityQueue
import random
import math


class GeneticAlgorithm:
    def __init__(self, generations=5) -> None:
        self.pop_size = 8
        self.generations = generations
        self.population = [[1, 1, 1, 1, 1, 1, 1, 1]
                           [2, 2, 2, 2, 2, 2, 2, 2]
                           [3, 3, 3, 3, 3, 3, 3, 3]
                           [4, 4, 4, 4, 4, 4, 4, 4]
                           [1, 2, 3, 4, 1, 2, 3, 4]
                           [4, 3, 2, 1, 4, 3, 2, 1]
                           [1, 2, 1, 2, 1, 2, 1, 2]
                           [3, 4, 3, 4, 3, 4, 3, 4]]
        self.variables = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.domains = [[1, 2, 3, 4],
                        [1, 2, 3, 4],
                        [1, 2, 3, 4],
                        [1, 2, 3, 4],
                        [1, 2, 3, 4],
                        [1, 2, 3, 4],
                        [1, 2, 3, 4],
                        [1, 2, 3, 4]]
        self.solution_set = set()

    def set_generations(self, gen):
        self.generations = gen

    def set_population(self, pop):
        # for this problem, we do not change the pop size when we call this
        self.population = pop

    def crossover(self, first_parent, second_parent):
        crossover_point = random.randint(1, len(first_parent))
        print(f"------parent 1: {first_parent}, parent2: {second_parent}")
        print("------crossover point: ", crossover_point)
        offspring1 = first_parent[:crossover_point] + \
            second_parent[crossover_point:]
        offspring2 = second_parent[:crossover_point] + \
            first_parent[crossover_point:]
        print(f"------offspring 1: {offspring1}, offspring 2: {offspring2}")
        return (offspring1, offspring2)

    def mutate(self, individual, chance=0.3,):
        mutation_chance = random.random()
        mutated_individual = individual
        can_mutate = mutation_chance <= chance
        if can_mutate:
            mutation_point = random.randint(len(individual))
            domain = self.domains[0]
            new_value_index = random.randint(len(individual))
            print(f"------mutating index {mutation_point} in {individual}")
            print(f"------changing the value to {domain[new_value_index]}")
            mutated_individual[mutation_point] = domain[new_value_index]
        return mutated_individual

    def select_parents(self, pop):
        scores = self.get_fitness_scores(pop)
        random1 = random.random()
        parents = []
        cumulative_probability = 0
        for idx in range(self.pop_size):
            cumulative_probability += scores[idx]
            if random1 <= cumulative_probability:
                parents[0] = pop[idx]
                break
        cumulative_probability = 0
        random2 = random.random()
        for idx in range(self.pop_size):
            cumulative_probability += scores[idx]
            if random2 <= cumulative_probability and parents[idx] != pop[idx]:
                parents[1] = pop[idx]
                break
        return parents

    def get_fitness_score(self, individual):
        "Returns the number of constraints satisfied by this individual"
        max_violations = 17
        violations = self.get_violation_count(individual)
        return max_violations-violations

    def get_fitness_scores(self, pop):
        """Fitness is proportional to the number of satisfied constraints
        """
        scores = []
        for idx, individual in enumerate(pop):
            scores[idx] = self.get_fitness_score(individual)
        return scores

    def get_selection_probability(self, individual, pop):
        fitness_score = self.get_fitness_score(individual)
        fitness_scores = self.get_fitness_scores(pop)
        prob = fitness_score/sum(fitness_scores)
        return prob

    def get_selection_probabilities(self, pop):
        probs = []
        for idx, ind in enumerate(pop):
            probs[idx] = self.get_selection_probability(ind, pop)
        return probs

    def get_violation_count(self, individual):
        A, B, C, D, E, F, G, F, G, H = individual

        conflict_map = {}
        conflict_map["A>G"] = 1 if A <= G else 0
        conflict_map["|G-C|=1"] = 1 if abs(G-C) != 1 else 0
        conflict_map["D!=C"] = 1 if D == C else 0
        conflict_map["G!=F"] = 1 if G == F != 1 else 0
        conflict_map["|E-F| is odd"] = 1 if abs(E-F) % 2 == 0 else 0
        conflict_map["A<=H"] = 1 if A > H else 0
        conflict_map["|H-C| is even"] = 1 if abs(H-C) % 2 == 1 else 0
        conflict_map["E != C"] = 1 if E == C else 0
        conflict_map["H != F"] = 1 if H == F else 0
        conflict_map["|F-B|=1"] = 1 if abs(F-B) != 1 else 0
        conflict_map["H !=D"] = 1 if H == D else 0
        conflict_map["E< D-1"] = 1 if E-D+1 >= 0 else 0
        conflict_map["C!=F"] = 1 if C == F else 0
        conflict_map["G < H"] = 1 if G-H >= 0 else 0
        conflict_map["D>=G"] = 1 if D < G else 0
        conflict_map["E!=H-2"] = 1 if E == H-2 else 0
        conflict_map["D!=F-1"] = 1 if F-1 == D else 0
        conflict_map["G < H"] = 1 if G-H >= 0 else 0

        violations = list(conflict_map.values())
        violations = sum(violations)
        return violations

    def is_solution(self, individual):
        fitness = self.get_fitness_score(individual)
        max_fitness = 17  # a solution satisfies all 17 constraints
        return fitness == max_fitness

    def solve(self, gen_count: int):
        generation = 0
        info = {"generation": generation,
                "population": self.population,
                "fitness_score": self.get_fitness_scores(self.population),
                "parent_likelihood": self.get_selection_probabilities(self.population)}
        print(info)
        while generation < gen_count:
            for individual in self.population:
                if self.is_solution(individual):
                    self.solution_set.add(individual)
            for i in range(self.pop_size//2):
                new_population = []
                print(f"------crossover {i}")
                parent1 = self.select_randomly(self.population)
                parent2 = self.select_randomly(self.population)

                offspring1, offspring2 = self.crossover(parent1, parent2)
                mutated_offspring1 = self.mutate(offspring1)
                mutated_offspring2 = self.mutate(offspring2)
                new_population.append(mutated_offspring1)
                new_population.append(mutated_offspring2)
            print("---------------------------------------------------------------")
            print("---------------------------------------------------------------")
            self.population = new_population

            generation += 1

        return self.solution_set
