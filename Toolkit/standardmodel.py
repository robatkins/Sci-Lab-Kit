class Particle:
    def __init__(self, name, symbol, mass, charge, spin, particle_type):
        self.name = name
        self.symbol = symbol
        self.mass = mass  # in GeV/c^2
        self.charge = charge
        self.spin = spin
        self.particle_type = particle_type

    def __str__(self):
        return f"{self.name} ({self.symbol}): Mass = {self.mass} GeV/c^2, Charge = {self.charge}e, Spin = {self.spin}, Type = {self.particle_type}"

    def formatted_str(self):
        # Create a formatted string with left-aligned columns
        return f"{self.name.ljust(20)} {self.symbol.ljust(5)} {str(self.mass).ljust(10)} GeV/c^2 {str(self.charge).ljust(10)} {str(self.spin).ljust(5)} {self.particle_type}"

class CompositeParticle:
    def __init__(self, name, constituents, mass, charge, spin, type):
        self.name = name
        self.constituents = constituents  # List of Particle objects
        self.type = type
        self.charge = charge
        self.mass = mass
        self.spin = spin

    def __str__(self):
        return f"{self.name} - Constituents: {', '.join([particle.name for particle in self.constituents])}"

    def formatted_str(self):
        # Create a formatted string with left-aligned columns
        return f"{self.name.ljust(20)} {', '.join([particle.name for particle in self.constituents]).ljust(60)} {str(self.mass).ljust(16)}   MeV/c {str(self.charge).ljust(40)} {str(self.spin).ljust(40)}  {self.type.ljust(40)}"

class FundamentalForce:
    def __init__(self, name, description, mediator_particle, strength):
        self.name = name
        self.description = description
        self.mediator_particle = mediator_particle
        self.strength = strength  # Relative strength compared to the electromagnetic force

    def __str__(self):
        return f"{self.name} Force:\nDescription: {self.description}\nMediator Particle: {self.mediator_particle}\nStrength: {self.strength}"

    def formatted_str(self):
        return f"{self.name.ljust(20)} {self.description.ljust(60)} {self.mediator_particle.ljust(30)} {str(self.strength)}"

class Atom:
    def __init__(self, name, symbol, atomic_number, mass_number, electrons):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.mass_number = mass_number
        self.electrons = electrons

    def __str__(self):
        return f"{self.name} ({self.symbol}) - Atomic Number: {self.atomic_number}, Mass Number: {self.mass_number}, Electrons: {self.electrons}"

    def formatted_str(self):
        return f"{self.name.ljust(20)} {self.symbol.ljust(5)} {str(self.atomic_number).ljust(10)} {str(self.mass_number).ljust(10)} {str(self.electrons).ljust(5)}"


# Define the particles
electron = Particle("Electron", "e-", 0.000511, -1, 0.5, "Lepton")
positron = Particle("Positron", "e+", 0.000511, 1, 0.5, "Lepton")
muon = Particle("Muon", "μ-", 0.1057, -1, 0.5, "Lepton")
antimuon = Particle("Antimuon", "μ+", 0.1057, 1, 0.5, "Lepton")
tau = Particle("Tau", "τ-", 1.776, -1, 0.5, "Lepton")
antitau = Particle("Antitau", "τ+", 1.776, 1, 0.5, "Lepton")
electron_neutrino = Particle("Electron Neutrino", "νe", 0, 0, 0.5, "Lepton")
muon_neutrino = Particle("Muon Neutrino", "νμ", 0, 0, 0.5, "Lepton")
tau_neutrino = Particle("Tau Neutrino", "ντ", 0, 0, 0.5, "Lepton")
photon = Particle("Photon", "γ", 0, 0, 1, "Gauge Boson")

#Quarks
up_quark = Particle("Up Quark", "u", 0.002, .66, 0.5, "Quark")
down_quark = Particle("Down Quark", "d", 0.005, -0.33, 0.5, "Quark")
strange_quark = Particle("Strange Quark", "s", 0.095, -0.33, 0.5, "Quark")
charm_quark = Particle("Charm Quark", "c", 1.27, 0.66, 0.5, "Quark")
top_quark = Particle("Top Quark", "t", 172.76, .66, 0.5, "Quark")
bottom_quark = Particle("Bottom Quark", "b", 4.18, -0.33, 0.5, "Quark")

#Antiquarks
up_antiquark = Particle("Up Anti-Quark", "u̅", 0.002, -.66, 0.5, "Anti-Quark")
down_antiquark = Particle("Down Anti-Quark", "d̅", 0.005, .33, 0.5, "Anti-Quark")
strange_antiquark = Particle("Strange Anti-Quark", "s̅", 0.095, .33, 0.5, "Anti-Quark")
charm_antiquark = Particle("Charm Anti-Quark", "c̅", 1.27, -.66, 0.5, "Anti-Quark")
top_antiquark = Particle("Top Anti-Quark", "t̅", 172.76, -.66, 0.5, "Anti-Quark")
bottom_antiquark = Particle("Bottom Anti-Quark", "b̅", 4.18, .33, 0.5, "Anti-Quark")

positive_w_boson = Particle("W+ Boson", "W+", 80.39, 1, 1, "Gauge Boson")
negative_w_boson = Particle("W- Boson", "W-", 80.39, -1, 1, "Gauge Boson")
z_boson = Particle("Z Boson", "Z", 91.19, 0, 1, "Gauge Boson")
gluon = Particle("Gluon", "g", 0, 0, 1, "Gauge Boson")
higgs_boson = Particle("Higgs Boson", "H", 125.1, 0, 0, "Scalar Boson")

#Define the composite particles
proton = CompositeParticle("Proton", [up_quark, up_quark, down_quark], "938.27208816(29)", "1e", 0.5, "Baryon")
neutron = CompositeParticle("Neutron", [down_quark, down_quark, up_quark], "939.56542052(54)", 0, 0.5, "Baryon")

anti_proton = CompositeParticle("Anti-Proton", [up_antiquark, up_antiquark, down_antiquark], "938.27208816(29)", "-1e", 0.5, "Anti-Baryon")
anti_neutron = CompositeParticle("Anti-Neutron", [up_antiquark, down_antiquark, down_antiquark], "939.56542052(54)", "0", 0.5, "Anti-Baryon")

#Define the Kaon and Pion Mesons
positive_pion = CompositeParticle("Positive Pion", [up_quark, down_antiquark], "139.57039(18)", "1e", 0, "Meson")
neutral_pion = CompositeParticle("Neutral Pion", [up_quark, up_antiquark], "134.9768(5)", 0, 0, "Meson")
negative_pion = CompositeParticle("Negative Pion", [down_quark, up_antiquark], "139.57039(18)", "-1e", 0, "Meson")
positive_kaon = CompositeParticle("Positive Kaon", [up_quark, strange_antiquark], "493.677±0.016", "1e", 0, "Meson")
neutral_kaon = CompositeParticle("Neutral Kaon", [down_quark, strange_antiquark], "497.611±0.013", 0, 0, "Meson")
negative_kaon = CompositeParticle("Negative Kaon", [strange_quark, up_antiquark], "493.677±0.016", "-1e", 0, "Meson")
anti_neutral_kaon = CompositeParticle("Anti-Neutral Kaon", [strange_quark, down_antiquark], "497.611±0.013", 0, 0,"Meson")

#Define fundamental forces
electromagnetic_force = FundamentalForce(
    name="Electromagnetic",
    description="Responsible for electromagnetic interactions.                                        ",
    mediator_particle="Photon",
    strength=1
)

weak_nuclear_force = FundamentalForce(
    name="Weak Nuclear",
    description="Responsible for processes involving neutrinos and flavor-changing quark interactions.",
    mediator_particle="W+, W-, and Z Bosons",
    strength=1e-13  # Much weaker than electromagnetic force
)

strong_nuclear_force = FundamentalForce(
    name="Strong Nuclear",
    description="Responsible for binding quarks together to form protons, neutrons, and other hadrons.",
    mediator_particle="Gluon",
    strength=1e38  # Much stronger than electromagnetic force
)

gravitational_force = FundamentalForce(
    name="Gravitational",
    description="Gravity is described by the theory of general relativity.                            ",
    mediator_particle="Graviton (Hypothetical)",
    strength="Proportional to the product of the masses of the objects and inversely proportional to the square of the distance between them." #Dependent on the curvature of space-time
)



# Sortparticles and antiparticles
particles = [
    electron, positron, muon, antimuon, tau, antitau,
    electron_neutrino, muon_neutrino, tau_neutrino,
    photon, up_quark, down_quark, strange_quark,
    charm_quark, top_quark, bottom_quark,
    positive_w_boson, negative_w_boson, z_boson, gluon, higgs_boson,
	up_antiquark, down_antiquark, strange_antiquark, charm_antiquark,
	top_antiquark, bottom_antiquark,
]

forces = [
    electromagnetic_force, weak_nuclear_force, strong_nuclear_force, gravitational_force,
]

compositeparticles = [
    proton, anti_proton, neutron, anti_neutron, positive_pion, neutral_pion,
    negative_pion, positive_kaon, neutral_kaon, negative_kaon, anti_neutral_kaon,
]

particles.sort(key=lambda x: (x.particle_type, x.name))

# Print formatted information about the particles
print("=" * 275)
print("Fundamental Particle Information:")
print("=" * 275)
print("Name                Symbol Mass               Charge     Spin  Type")
print("-" * 275)
for particle in particles:
    print(particle.formatted_str())

print("=" * 275)
print("Fundamental Force Information:")
print("=" * 275)
print("Name                 Description                                                                           Mediator Particle              Strength")
print("-" * 275)
# Print formatted information about fundamental forces
for force in forces:
    print(force.formatted_str())
print("=" * 275)
# Print information about the composite particle
print("Composite Particle Information:")
print("=" * 275)
print("Name                 Constituents                                                 Mass                     Charge                                   Spin                                      Classification")
print("-" * 275)
for particle in compositeparticles:
    print(particle.formatted_str())
print("=" * 275)
