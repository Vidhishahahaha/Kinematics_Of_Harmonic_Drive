import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the base circle and involute curve for gear 1
def gear_1(base_radius, theta, num_points=100):
    base_circle_x1 = base_radius * np.cos(theta)
    base_circle_y1 = base_radius * np.sin(theta)

    s3 = []
    v3 = []
    for i in np.linspace(0, 5 * np.pi / 9, 10):
        x3 = base_radius * (np.cos(i) + i * np.sin(i))
        y3 = base_radius * (np.sin(i) - i * np.cos(i))
        s3.append(x3)
        v3.append(y3)

    return base_circle_x1, base_circle_y1, s3, v3

# Define the base circle and involute curve for gear 2
def gear_2(base_radius, shift_x, shift_y, theta, num_points=100):
    base_circle_x2 = base_radius * np.cos(theta) + shift_x
    base_circle_y2 = base_radius * np.sin(theta) + shift_y

    s4 = []
    v4 = []
    for i in np.linspace(0, 5 * np.pi / 9, 10):
        x4 = -base_radius * (np.cos(i) + i * np.sin(i))
        y4 = -base_radius * (np.sin(i) - i * np.cos(i))
        s4.append(x4 + shift_x)
        v4.append(y4 + shift_y)

    return base_circle_x2, base_circle_y2, s4, v4

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid()
ax.set_xlim(-30, 60)
ax.set_ylim(-30, 60)

theta = np.linspace(0, 2 * np.pi, 100)
base_circle_1 = 10
base_circle_2 = 10
shift_x = 15.707 * 2
shift_y = 9.99 * 2

# Initialize the plot objects
base_circle_1_x, base_circle_1_y, s3, v3 = gear_1(base_circle_1, theta)
base_circle_2_x, base_circle_2_y, s4, v4 = gear_2(base_circle_2, shift_x, shift_y, theta)

line1, = ax.plot(base_circle_1_x, base_circle_1_y, 'b')
line2, = ax.plot(base_circle_2_x, base_circle_2_y, 'r')
involute1, = ax.plot(s3, v3, 'b')
involute2, = ax.plot(s4, v4, 'r')

# Animation update function
def update(frame):
    rotation_angle = frame * np.pi / 180
    rotation_matrix_1 = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                                  [np.sin(rotation_angle), np.cos(rotation_angle)]])
    rotation_matrix_2 = np.array([[np.cos(-rotation_angle), -np.sin(-rotation_angle)],
                                  [np.sin(-rotation_angle), np.cos(-rotation_angle)]])

    rotated_base_circle_1 = np.dot(rotation_matrix_1, np.array([base_circle_1_x, base_circle_1_y]))
    rotated_base_circle_2 = np.dot(rotation_matrix_2, np.array([base_circle_2_x - shift_x, base_circle_2_y - shift_y])) + np.array([[shift_x], [shift_y]])

    rotated_involute_1 = np.dot(rotation_matrix_1, np.array([s3, v3]))
    rotated_involute_2 = np.dot(rotation_matrix_2, np.array([np.array(s4) - shift_x, np.array(v4) - shift_y])) + np.array([[shift_x], [shift_y]])

    line1.set_data(rotated_base_circle_1[0], rotated_base_circle_1[1])
    line2.set_data(rotated_base_circle_2[0], rotated_base_circle_2[1])
    involute1.set_data(rotated_involute_1[0], rotated_involute_1[1])
    involute2.set_data(rotated_involute_2[0], rotated_involute_2[1])

    return line1, line2, involute1, involute2

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(-8, 8, 1), interval=50, blit=True)


# pitch circle
s5=[]
v5=[]

s6=[]
v6=[]
theta = np.linspace(0, 2*np.pi, 100)
base_circle_5 = 19
base_circle_x5 = base_circle_5 * np.cos(theta)
base_circle_y5 = base_circle_5 * np.sin(theta)

plt.plot(base_circle_x5,base_circle_y5)

theta = np.linspace(0,2*np.pi , 100)
base_circle_6 = 18.5

shift_x = 15.707*2
shift_y = 9.99*2
theta = np.linspace(0, 2*np.pi, 100)
base_circle_x6 = base_circle_6 * np.cos(theta) + shift_x
base_circle_y6 = base_circle_6 * np.sin(theta) + shift_y


plt.plot(base_circle_x6,base_circle_y6)




# for i in np.linspace(0,  np.pi/2, 10):
#     x3 = base_circle_1* (np.cos(i) + i * np.sin(i))
#     y3 = base_circle_1 * (np.sin(i) - i * np.cos(i))

#     s4.append(x3)
#     v4.append(y3)


x_values = [0, 15.707*2]
y_values = [0,9.99*2 ]

# Plot the line
# plt.plot(x_values, y_values, label='Line through points', marker='o')
center_x , center_y= 0,0
center_x2, center_y2 = shift_x,shift_y





# Define the two points
point1 = (0, 0)
point2 = (15.707*2,9.99*2 )

# Extract x and y coordinates
x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]





# Calculate the midpoint of the line segment
midpoint = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

# Calculate the slope of the original line
slope_original = (point2[1] - point1[1]) / (point2[0] - point1[0])

# Calculate the slope of the perpendicular line (negative reciprocal)
slope_perpendicular = -1 / slope_original

# Determine the endpoints of the perpendicular line segment for visualization
length = 20  # Length of the perpendicular line segment for visualization
delta_x = length / np.sqrt(1 + slope_perpendicular**2)
delta_y = slope_perpendicular * delta_x

# Endpoints of the perpendicular line segment
perp_point1 = (midpoint[0] - delta_x, midpoint[1] - delta_y)
perp_point2 = (midpoint[0] + delta_x, midpoint[1] + delta_y)

# Plot the original line
plt.plot(x_values, y_values, label='Original Line', marker='o')

# Mark the original points
plt.plot(point1[0], point1[1], 'ro')  # 'ro' means red color with circle marker
plt.plot(point2[0], point2[1], 'ro')

# Annotate the original points
plt.text(point1[0], point1[1], f'  Point 1 {point1}', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(point2[0], point2[1], f'  Point 2 {point2}', fontsize=12, verticalalignment='bottom', horizontalalignment='right')

# Plot the midpoint
plt.plot(midpoint[0], midpoint[1], 'go')  # 'go' means green color with circle marker
plt.text(midpoint[0], midpoint[1], '  Midpoint', fontsize=12, verticalalignment='bottom', horizontalalignment='right')

# Plot the perpendicular line
plt.plot([perp_point1[0], perp_point2[0]], [perp_point1[1], perp_point2[1]], label='Perpendicular Line', marker='x')

# Set aspect ratio to be equal
plt.axis('equal')

# Add grid
plt.grid(True)

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
# plt.title('Original Line and Perpendicular Line through Midpoint')

# Show the plot
plt.legend()
plt.show()

plt.show()



