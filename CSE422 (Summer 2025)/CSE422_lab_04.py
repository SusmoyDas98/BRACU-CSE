# Task 1

import random
import math

class Designer:
    def __init__(self, generation_count):

        self.generation_count = generation_count
        self.parent_limit = 6
        self.components = {"ALU":(5,5), "Cache":(7,4), "Control_Unit":(4,4), "Register_file":(6,6), "Decoder":(5,3), "Floating_Unit" : (5,5)}
        self.grid_size = 25

    def population_creator(self, number_of_chromosomes):

        position_array = []
        for i in range(number_of_chromosomes):
            chromosome = {}
            for k, v in self.components.items():
                left_from_y, top_from_x = random.randint(0, self.grid_size - v[0]), random.randint(0,self.grid_size - v[1])
                chromosome[k] = (left_from_y, top_from_x)
            position_array.append(chromosome)

        return position_array

    def wiring_distance_checker(self, comp1, comp2, components,chromosomes):
        center1_x, center1_y = chromosomes[comp1][0]+(self.components[comp1][0]/2), chromosomes[comp1][1]+(self.components[comp1][1]/2)
        center2_x, center2_y = chromosomes[comp2][0]+(self.components[comp2][0]/2), chromosomes[comp2][1]+(self.components[comp2][1]/2)
        distance = math.sqrt(math.pow((center1_x-center2_x), 2) + math.pow((center1_y-center2_y), 2))
        return distance

    def bounding_area_checker(self, chromosomes, components):

        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
        for k, v in chromosomes.items():
            x, y = v
            min_x = min(min_x, x)
            max_x = max(max_x, x + self.components[k][0])
            min_y = min(min_y, y)
            max_y = max(max_y, y + self.components[k][1])
        bounding_area = (max_x - min_x) * (max_y - min_y)

        return bounding_area

    def component_overlap_checker(self, chromosomes, components):

        element_list = list(self.components.keys())
        count = 0
        for i in range(len(element_list)):
            for j in range(i + 1, len(element_list)):
                A = element_list[i]
                B = element_list[j]
                A_x, A_y = chromosomes[A]
                A_width, A_height = self.components[A]
                B_x, B_y = chromosomes[B]
                B_width, B_height = self.components[B]
                if not (
                        A_x + A_width <= B_x or
                        B_x + B_width <= A_x or
                        A_y + A_height <= B_y or
                        B_y + B_height <= A_y
                ):
                    count += 1
        return count

    def fitness_checker(self, chromosomes, components):

        connections = [("Register_file", "ALU"), ("Control_Unit", "ALU"), ("ALU", "Cache"),   ("Register_file", "Floating_Unit"), ("Cache", "Decoder"), ("Decoder", "Floating_Unit")]
        wiring = 0

        for i in range(len(connections)):
            wiring += self.wiring_distance_checker(connections[i][0], connections[i][1], self.components, chromosomes)

        bounding_area = self.bounding_area_checker(chromosomes, self.components)
        overlap = self.component_overlap_checker(chromosomes, self.components)
        fitness_function = -(wiring * 1 + bounding_area * 2 + overlap * 1000)

        return fitness_function, wiring, bounding_area, overlap

    def crossover(self, p1, p2):

        point = random.randint(0, len(p1) - 1)
        final_p1, final_p2 = {}, {}

        for index, key in enumerate(p1.keys()):
            if index < point:
                final_p1[key] = p1[key]
                final_p2[key] = p2[key]
            else:
                final_p1[key] = p2[key]
                final_p2[key] = p1[key]

        return final_p1, final_p2

    def mutation(self, child1, child2):
        mutation_rate = 0.1
        for key, val in child1.items():
            random1 = random.random()

            if random1 < mutation_rate:
                width, height = self.components[key]
                new_width = random.randint(0, self.grid_size - width)
                new_height = random.randint(0, self.grid_size - height)
                child1[key] = (new_width, new_height)

        for key, val in child2.items():
            random2 = random.random()
            if random2 < mutation_rate:
                width, height = self.components[key]
                new_width = random.randint(0, self.grid_size - width)
                new_height = random.randint(0, self.grid_size - height)
                child2[key] = (new_width, new_height)

        return child1, child2

    def __call__(self):
        gen = 1
        parents = self.population_creator(self.parent_limit)
        final_fitness, wiring, bounding_area, overlap, best_layout = 0, 0, 0, 0, {}
        for gen in range(self.generation_count + 1):

            fitness_vals = []
            for i in range(len(parents)):
                chromosomes = parents[i]
                fitness, wiring, bounding_area, overlap = self.fitness_checker(chromosomes, self.components)
                fitness_vals.append((fitness, parents[i]))

            fitness_vals.sort()
            fitness_vals.reverse()
            new_generation = [fitness_vals[0][1], fitness_vals[1][1]]

            while len(new_generation) < self.parent_limit:
                parent1, parent2 = random.sample(fitness_vals[0:3], 2)
                crossovered_child_1, crossovered_child_2 = self.crossover(parent1[1], parent2[1])
                mutated_ch1, mutated_ch2 = self.mutation(crossovered_child_1, crossovered_child_2)
                new_generation.append(mutated_ch1)
                if len(new_generation) < self.parent_limit:
                    new_generation.append(mutated_ch2)
            parents = new_generation
            final_fitness = fitness_vals[0][0]

            best_layout = fitness_vals[0][1]
        print("Generation:", gen)
        print()
        print("Best Layout:")
        for k, v in best_layout.items():
            print(k, "-->", v, )
        print()

        print("Best Fitness Value:", final_fitness, "\n")

        print("Total wiring length:", wiring, "\n")
        print("The total bounding box area:", bounding_area, "\n")
        print("The total overlap counts:", overlap, "\n")


d = Designer(15)
d()




# Task 2 (Using two point crossover)

import random
import math

class Designer:
    def __init__(self, generation_count):

        self.generation_count = generation_count
        self.parent_limit = 6
        self.components = {"ALU":(5,5), "Cache":(7,4), "Control_Unit":(4,4), "Register_file":(6,6), "Decoder":(5,3), "Floating_Unit" : (5,5)}
        self.grid_size = 25

    def population_creator(self, number_of_chromosomes):

        position_array = []
        for i in range(number_of_chromosomes):
            chromosome = {}
            for k, v in self.components.items():
                left_from_y, top_from_x = random.randint(0, self.grid_size - v[0]), random.randint(0,self.grid_size - v[1])
                chromosome[k] = (left_from_y, top_from_x)
            position_array.append(chromosome)

        return position_array

    def wiring_distance_checker(self, comp1, comp2, components,chromosomes):
        center1_x, center1_y = chromosomes[comp1][0]+(self.components[comp1][0]/2), chromosomes[comp1][1]+(self.components[comp1][1]/2)
        center2_x, center2_y = chromosomes[comp2][0]+(self.components[comp2][0]/2), chromosomes[comp2][1]+(self.components[comp2][1]/2)
        distance = math.sqrt(math.pow((center1_x-center2_x), 2) + math.pow((center1_y-center2_y), 2))
        return distance

    def bounding_area_checker(self, chromosomes, components):

        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
        for k, v in chromosomes.items():
            x, y = v
            min_x = min(min_x, x)
            max_x = max(max_x, x + self.components[k][0])
            min_y = min(min_y, y)
            max_y = max(max_y, y + self.components[k][1])
        bounding_area = (max_x - min_x) * (max_y - min_y)

        return bounding_area

    def component_overlap_checker(self, chromosomes, components):

        element_list = list(self.components.keys())
        count = 0
        for i in range(len(element_list)):
            for j in range(i + 1, len(element_list)):
                A = element_list[i]
                B = element_list[j]
                A_x, A_y = chromosomes[A]
                A_width, A_height = self.components[A]
                B_x, B_y = chromosomes[B]
                B_width, B_height = self.components[B]
                if not (
                        A_x + A_width <= B_x or
                        B_x + B_width <= A_x or
                        A_y + A_height <= B_y or
                        B_y + B_height <= A_y
                ):
                    count += 1
        return count

    def fitness_checker(self, chromosomes, components):

        connections = [("Register_file", "ALU"), ("Control_Unit", "ALU"), ("ALU", "Cache"),   ("Register_file", "Floating_Unit"), ("Cache", "Decoder"), ("Decoder", "Floating_Unit")]
        wiring = 0

        for i in range(len(connections)):
            wiring += self.wiring_distance_checker(connections[i][0], connections[i][1], self.components, chromosomes)

        bounding_area = self.bounding_area_checker(chromosomes, self.components)
        overlap = self.component_overlap_checker(chromosomes, self.components)
        fitness_function = -(wiring * 1 + bounding_area * 2 + overlap * 1000)

        return fitness_function, wiring, bounding_area, overlap

    def crossover(self, p1, p2):

        point1 = random.randint(0, len(p1)-1)
        point2 = random.randint(point1, len(p1)-1)
        final_p1, final_p2 = {}, {}

        for index, key in enumerate(p1.keys()):
            if index < point1:
                final_p1[key] = p1[key]
                final_p2[key] = p2[key]
            elif index >= point1 and index <= point2:
                final_p1[key] = p2[key]
                final_p2[key] = p1[key]
            else:
                final_p1[key] = p1[key]
                final_p2[key] = p2[key]

        return final_p1, final_p2


    def mutation(self, child1, child2):
        mutation_rate = 0.1
        for key, val in child1.items():
            random1 = random.random()

            if random1 < mutation_rate:
                width, height = self.components[key]
                new_width = random.randint(0, self.grid_size - width)
                new_height = random.randint(0, self.grid_size - height)
                child1[key] = (new_width, new_height)

        for key, val in child2.items():
            random2 = random.random()
            if random2 < mutation_rate:
                width, height = self.components[key]
                new_width = random.randint(0, self.grid_size - width)
                new_height = random.randint(0, self.grid_size - height)
                child2[key] = (new_width, new_height)

        return child1, child2

    def __call__(self):
        gen = 1
        parents = self.population_creator(self.parent_limit)
        final_fitness, wiring, bounding_area, overlap, best_layout = 0, 0, 0, 0, {}
        for gen in range(self.generation_count + 1):

            fitness_vals = []
            for i in range(len(parents)):
                chromosomes = parents[i]
                fitness, wiring, bounding_area, overlap = self.fitness_checker(chromosomes, self.components)
                fitness_vals.append((fitness, parents[i]))

            fitness_vals.sort()
            fitness_vals.reverse()
            new_generation = [fitness_vals[0][1], fitness_vals[1][1]]

            while len(new_generation) < self.parent_limit:
                parent1, parent2 = random.sample(fitness_vals[0:3], 2)
                crossovered_child_1, crossovered_child_2 = self.crossover(parent1[1], parent2[1])
                mutated_ch1, mutated_ch2 = self.mutation(crossovered_child_1, crossovered_child_2)
                new_generation.append(mutated_ch1)
                if len(new_generation) < self.parent_limit:
                    new_generation.append(mutated_ch2)
            parents = new_generation
            final_fitness = fitness_vals[0][0]

            best_layout = fitness_vals[0][1]
        print("Generation:", gen)
        print()
        print("Best Layout:")
        for k, v in best_layout.items():
            print(k, "-->", v, )
        print()

        print("Best Fitness Value:", final_fitness, "\n")

        print("Total wiring length:", wiring, "\n")
        print("The total bounding box area:", bounding_area, "\n")
        print("The total overlap counts:", overlap, "\n")


d1 = Designer(15)
d1()
