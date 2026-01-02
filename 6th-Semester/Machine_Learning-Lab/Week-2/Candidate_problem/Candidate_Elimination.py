import csv
def load_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return [row for row in reader]
    
def candidate_elimination(data):
    num_attributes = len(data[0]) - 1
    S = ['0'] * num_attributes
    G = [['?'] * num_attributes]
    print("\nInitial S:", S, "\nInitial G:", G)
    for i, instance in enumerate(data):
        X, Y = instance[:-1], instance[-1]
        print(f"\nInstance {i+1}: {instance}")
        if Y == 'Yes':
            # Update S
            for j in range(num_attributes):
                if S[j] == '0':
                    S[j] = X[j]
                elif S[j] != X[j]:
                    S[j] = '?'
            # Remove inconsistent G
            G = [g for g in G if all(g[k] == '?' or g[k] == S[k] for k in range(num_attributes))]
        else:
            # Specialize G
            G = [h for g in G for j in range(num_attributes) 
                 if g[j] == '?' and S[j] not in ['?', '0'] 
                 for h in [g[:j] + [S[j]] + g[j+1:]]]
        
        print("S:", S, "\nG:", G)
    
    return S, G

# Main
data = load_csv("/home/vignesh/VS/GitHub/SVCET/6th-Semester/Machine_Learning-Lab/Week-2/Candidate_problem/data/temperature.csv")
S_final, G_final = candidate_elimination(data)
print("\n" + "="*30)
print("Final S:", S_final, "\nFinal G:", G_final)