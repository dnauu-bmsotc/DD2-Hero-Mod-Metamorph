import itertools

def print_party_combinations(required_heroes, nonfocus_heroes):
    names = list(generate_party_combinations(required_heroes, nonfocus_heroes))
    names.sort(key=lambda x: tuple(x.index(kw) for kw in required_heroes))
    print_party_names(names)

def generate_party_combinations(required_heroes, nonfocus_heroes):
    n_free_slots = 4 - len(required_heroes)
    secondary_combinations = list(itertools.combinations(nonfocus_heroes, n_free_slots))
    for comb in secondary_combinations:
        four_heroes = required_heroes + list(comb)
        permutations = list(itertools.permutations(four_heroes))
        for perm in permutations:
            yield list(perm)

def print_party_names(combinations):
    loc_line = "party_name_{}_{}_{}_{}="
    for comb in combinations:
        print(loc_line.format(*comb))


print_party_combinations(["mmd","grave_robber"], ["plague_doctor", "man_at_arms", "highwayman"])
# print_party_combinations(["mmd"], ["grave_robber", "plague_doctor", "man_at_arms", "highwayman"])

# print_party_combinations(["mmd", "omen_seeker"], ["grave_robber", "plague_doctor", "man_at_arms", "highwayman"])

# print_party_combinations(["mmd", "monk"], ["grave_robber", "plague_doctor", "man_at_arms", "highwayman"])

# print_party_combinations(["mmd", "omen_seeker", "monk"], ["grave_robber", "plague_doctor", "man_at_arms", "highwayman"])
