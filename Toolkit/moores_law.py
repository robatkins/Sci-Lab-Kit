import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for Moore's Law
start_year = 1971
end_year = 2023
years = np.arange(start_year, end_year + 1, 1)
transistors = 2**(np.floor((years - start_year) / 2)) * 1e3


# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(1e3, 1e14)  # Adjust the y-axis limits as needed
ax.set_xlim(start_year, end_year)
ax.set_yscale('log')  # Use a logarithmic scale for better visualization
ax.set_xlabel('Year')
ax.set_ylabel('Number of Transistors')
ax.set_title("Moore's Law: Transistors vs. Year")

# Preallocate the line data to be updated
line_data = np.empty((len(years), 2))

# Animation function
# Animation function
def update(frame):
    interpolated_years = np.linspace(start_year, years[frame], num=len(line_data))
    interpolated_transistors = np.interp(interpolated_years, years, transistors)
    
    line_data[:, 0] = interpolated_years
    line_data[:, 1] = interpolated_transistors
    
    line.set_data(line_data[:, 0], line_data[:, 1])
    
    return line,





# Create the animation
ani = FuncAnimation(fig, update, frames=len(years), blit=True, interval=100)

# Show the plot
plt.show()
