# Hardcoded sequence
dna_sequence = " atg cga tta "

# Limpieza
dna_sequence = dna_sequence.strip()
dna_sequence = dna_sequence.upper()

# Conteos
count_a = dna_sequence.count("A")
count_t = dna_sequence.count("T")
count_g = dna_sequence.count("G")
count_c = dna_sequence.count("C")

# Longitud
length = count_a + count_t + count_c + count_g

# Output
print(f"Length:", {length})