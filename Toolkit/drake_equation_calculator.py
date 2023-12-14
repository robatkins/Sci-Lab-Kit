#Drake Equation Calculator

def drake_equation(R_star, f_p, n_e, f_l, f_i, f_c, L):
    N = R_star * f_p * n_e * f_l * f_i * f_c * L
    return N

# Input values for the parameters
R_star = float(input("Average rate of star formation (R*): "))
f_p = float(input("Fraction of stars with planets (f_p): "))
n_e = float(input("Average number of planets that could support life per star with planets (n_e): "))
f_l = float(input("Fraction of planets where life develops (f_l): "))
f_i = float(input("Fraction of planets with intelligent life (f_i): "))
f_c = float(input("Fraction of planets with intelligent life that develop interstellar communication (f_c): "))
L = float(input("Average lifespan of a communicating civilization (L): "))

# Calculate and print the result
estimated_civilizations = drake_equation(R_star, f_p, n_e, f_l, f_i, f_c, L)
print(f"The estimated number of communicative civilizations in the Milky Way is approximately {estimated_civilizations:.2f}.")
