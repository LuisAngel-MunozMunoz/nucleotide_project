# Hardcoded sequence
dna_sequence = "ATAT"

#Condiciones en caso 0
if dna_sequence == "":
    print("La longitud es 0, dato erroneo en calculo")
else:
# Limpieza
    dna_sequence = dna_sequence.strip()
    dna_sequence = dna_sequence.upper()
    dna_sequence_sinesp = dna_sequence.replace(" ","")

# Conteos
    count_g = dna_sequence_sinesp.count("G")
    count_c = dna_sequence_sinesp.count("C")

# Longitud
    length = len(dna_sequence_sinesp)

# Cálculo GC
    gc_content = (count_g + count_c) / length * 100

# Output
    print(f"GC content: :{gc_content:.2f}%")