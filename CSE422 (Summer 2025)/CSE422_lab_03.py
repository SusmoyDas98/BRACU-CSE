
#Task 1

class Gene_Designer:
    def __init__(self):

        pass

    def utility_checker(self, weights, gene, target):
        answer = 0
        i, j = 0, 0
        new_weight = []
        for i in range(1, len(target)+1):
            new_weight.append(weights[-i])
        weights = new_weight[-1::-1]

        for i in range(len(gene)):
            if i <= len(target) - 1:
                answer += weights[i]*abs(ord(gene[i]) - ord(target[i]))
            else:
                answer += 1*abs(ord(gene[i]))

        return -answer

    def minimax_algorithm(self, pool, gene, is_max, target, alpha, beta, weights):

        if not pool:
            utility = self.utility_checker(weights, gene, target)
            return gene, utility

        if is_max:
            max_val = float("-inf")
            selected_gene = None
            for i in range(len(pool)):

                nucleotide = pool[i]
                updated_pool = pool[:i] + pool[i+1:]

                new_gene = gene + nucleotide
                candidate, utility = self.minimax_algorithm( updated_pool, new_gene, False, target, alpha, beta, weights)
                if utility > max_val :
                    max_val = utility
                    selected_gene = candidate
                alpha = max(max_val, alpha)
                if beta<=alpha : break
            return selected_gene, max_val

        else:
            min_val = float("inf")
            selected_gene = None
            for i in range(len(pool)):
                nucleotide = pool[i]
                updated_pool = pool[:i] + pool[i+1:]

                new_gene = gene + nucleotide
                candidate, utility = self.minimax_algorithm( updated_pool, new_gene, True, target, alpha, beta, weights)
                if utility < min_val:
                    min_val = utility
                    selected_gene = candidate
                beta = min(min_val, beta)
                if alpha>beta  : break
            return selected_gene, min_val

    def __call__(self, pool, gene, is_max, target, alpha, beta, weights):

        selected_gene, utility = self.minimax_algorithm( pool, gene, is_max, target, alpha, beta, weights)


        return selected_gene, utility



with open('input1.txt', 'r') as file1, open('output1.txt', 'w') as file2 :
    pool = file1.readline().strip().split(",")
    target = file1.readline().strip()
    weights = file1.readline().strip().split(" ")
    weights = [int(i) for i in weights]
    gene = ''
    alpha = float("-inf")
    beta = float("inf")
    D = Gene_Designer()
    selected_gene, utility = D(  pool, gene, True, target, alpha, beta, weights)
    file2.write(f"Best gene sequence generated: {selected_gene} \nUtility score: {utility}")

#Task 2

class Gene_Designer:
    def __init__(self):

        pass

    def utility_checker(self, weights, gene, target):
        answer = 0
        i, j = 0, 0
        new_weight = []
        for i in range(1, len(target)+1):
            new_weight.append(weights[-i])
        new_weight = new_weight[-1::-1]

        for i in range(len(gene)):
            if i <= len(target) - 1:
                answer += new_weight[i]*abs(ord(gene[i]) - ord(target[i]))
            else:
                answer += 1*abs(ord(gene[i]))

        return -answer

    def minimax_algorithm(self, pool, gene, is_max, target, alpha, beta, weights, booster):

        if not pool:
            utility = self.utility_checker(weights, gene, target)
            return gene, utility

        if is_max:
            max_val = float("-inf")
            selected_gene = None
            for i in range(len(pool)):

                nucleotide = pool[i]
                updated_pool = pool[:i] + pool[i+1:]

                new_gene = gene + nucleotide
                if not booster and nucleotide == "S":
                        updated_weights = []
                        for m in range(len(weights)):
                            if m < len(gene):
                                updated_weights.append(weights[m])
                            else:

                                updated_weights.append(weights[m]*(self.mul))
                        candidate, utility = self.minimax_algorithm( updated_pool, new_gene, False, target, alpha, beta, updated_weights,True)
                else:
                        candidate, utility = self.minimax_algorithm( updated_pool, new_gene, False, target, alpha, beta, weights,booster)


                if utility > max_val :
                    max_val = utility
                    selected_gene = candidate
                alpha = max(max_val, alpha)
                if beta<=alpha : break
            return selected_gene, max_val

        else:
            min_val = float("inf")
            selected_gene = None
            for i in range(len(pool)):
                nucleotide = pool[i]
                updated_pool = pool[:i] + pool[i+1:]

                new_gene = gene + nucleotide
                candidate, utility = self.minimax_algorithm( updated_pool, new_gene, True, target, alpha, beta, weights,booster)
                if utility < min_val:
                    min_val = utility
                    selected_gene = candidate
                beta = min(min_val, beta)
                if alpha>beta  : break
            return selected_gene, min_val

    def __call__(self, pool, gene, is_max, target, alpha, beta, weights, booster,mul):
        self.mul = mul
        selected_gene, utility = self.minimax_algorithm( pool, gene, is_max, target, alpha, beta, weights, booster)


        return selected_gene, utility



with open('input1.txt', 'r') as file1, open('output1.txt', 'w') as file2 :
    pool = file1.readline().strip().split(",")
    target = file1.readline().strip()
    weights = file1.readline().strip().split(" ")
    weights = [int(i) for i in weights]
    gene = ''
    alpha = float("-inf")
    beta = float("inf")
    if len(weights) >= 2 :
        mul = int(str(weights[0]) + str(weights[1]))/100
    else :
        mul = 1


    D = Gene_Designer()
    selected_gene, utility = D(  pool, gene, True, target, alpha, beta, weights, False, mul)
    new_pool = pool + ["S"]

    selected_gene_boosted, utility_boosted = D(  new_pool, gene, True, target, alpha, beta, weights, False, mul)
    if utility_boosted > utility :
        file2.write(f"YES\nWith special nucleotide\nBest gene sequence generated: {selected_gene_boosted},\nUtility score: {utility_boosted}")
    else:
        file2.write(f"No\nWith special nucleotide\nBest gene sequence generated: {selected_gene_boosted},\nUtility score: {utility_boosted}")

