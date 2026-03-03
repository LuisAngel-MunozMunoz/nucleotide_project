# Hardcoded sequence
dna_sequence = "aaaa"

# Limpieza
dna_sequence = dna_sequence.strip()
dna_sequence = dna_sequence.upper()
dna_sequence_sinesp = dna_sequence.replace(" ","")

# Conteos
count_a = dna_sequence_sinesp.count("A")
count_t = dna_sequence_sinesp.count("T")
count_g = dna_sequence_sinesp.count("G")
count_c = dna_sequence_sinesp.count("C")

# Longitud
length = count_a + count_t + count_c + count_g

# Output
print(f"La longitud de la secuencia es de:", {length})
print(dna_sequence_sinesp)