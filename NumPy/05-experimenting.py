# import matplotlib.pyplot as plt
# import numpy as np

# # Create a figure and axis
# fig, ax = plt.subplots(figsize=(10, 6))

# # Draw the body of the car (rectangular shape)
# car_body = plt.Rectangle((0.2, 0.3), 0.6, 0.2, color='silver', ec='black', lw=2)
# ax.add_patch(car_body)

# # Draw the roof of the car (smaller rectangle)
# car_roof = plt.Rectangle((0.3, 0.5), 0.4, 0.15, color='silver', ec='black', lw=2)
# ax.add_patch(car_roof)

# # Draw the wheels (circles)
# front_wheel = plt.Circle((0.3, 0.25), 0.07, color='black', lw=3)
# rear_wheel = plt.Circle((0.7, 0.25), 0.07, color='black', lw=3)
# ax.add_patch(front_wheel)
# ax.add_patch(rear_wheel)

# # Draw the windows (rectangles)
# front_window = plt.Rectangle((0.31, 0.51), 0.18, 0.12, color='lightblue', ec='black', lw=1)
# rear_window = plt.Rectangle((0.51, 0.51), 0.18, 0.12, color='lightblue', ec='black', lw=1)
# ax.add_patch(front_window)
# ax.add_patch(rear_window)

# # Draw the front grill (rectangle)
# front_grill = plt.Rectangle((0.43, 0.35), 0.14, 0.05, color='black', ec='black', lw=2)
# ax.add_patch(front_grill)

# # Draw the headlights (circles)
# headlight1 = plt.Circle((0.25, 0.43), 0.04, color='yellow')
# headlight2 = plt.Circle((0.75, 0.43), 0.04, color='yellow')
# ax.add_patch(headlight1)
# ax.add_patch(headlight2)

# # Draw the emblem (circle in the center for the Mercedes-Benz logo)
# emblem = plt.Circle((0.5, 0.58), 0.05, color='black', lw=2)
# ax.add_patch(emblem)

# # Customize the plot
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 0.7)
# ax.set_aspect('equal')
# ax.axis('off')  # Turn off axes

# # Display the Mercedes-Benz inspired car
# plt.title("Mercedes-Benz Inspired Car", fontsize=16, fontweight='bold')
# plt.show()




# import matplotlib.pyplot as plt
# # Time points representing the trading day
# times = ['Open', 'High', 'Low', 'Close']
# # Corresponding Nifty 50 index values
# values = [23783.00, 23877.00, 23751.55, 23862.30]

# # Create the plot
# plt.figure(figsize=(10, 5))
# plt.plot(times, values, marker='o', linestyle='-', color='b')

# # Add titles and labels
# plt.title('Nifty 50 Index Performance on January 2, 2025')
# plt.xlabel('Time of Day')
# plt.ylabel('Index Value')

# # Display the plot
# plt.grid(True)
# plt.show()










# import matplotlib.pyplot as plt
# import pandas as pd
# import datetime

# # Sample data: Date and Closing Prices for the past month
# data = {
#     'Date': pd.date_range(end=datetime.date(2025, 1, 2), periods=30),
#     'Close': [
#         500.00, 505.50, 510.00, 515.00, 520.50, 525.00, 530.50, 535.00, 540.50, 545.00,
#         550.50, 555.00, 560.50, 565.00, 570.50, 575.00, 580.50, 585.00, 590.50, 595.00,
#         600.50, 605.00, 610.50, 615.00, 620.50, 625.00, 630.50, 635.00, 640.50, 645.00
#     ]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Plotting
# plt.figure(figsize=(10, 5))
# plt.plot(df['Date'], df['Close'], marker='o', linestyle='-', color='b')

# # Adding titles and labels
# plt.title('Swiggy Limited Stock Performance - Last 30 Days')
# plt.xlabel('Date')
# plt.ylabel('Closing Price (INR)')
# plt.grid(True)

# # Display the plot
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()






import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Bird head (circle)
head = plt.Circle((0.5, 0.5), 0.4, color='red', ec='black', lw=3)
ax.add_patch(head)

# Beak (triangle)
beak_x = [0.5, 0.6, 0.4]
beak_y = [0.5, 0.6, 0.6]
ax.fill(beak_x, beak_y, color='orange', lw=2, ec='black')

# Eyes (white circles)
eye_left = plt.Circle((0.35, 0.65), 0.08, color='white', ec='black', lw=3)
eye_right = plt.Circle((0.65, 0.65), 0.08, color='white', ec='black', lw=3)
ax.add_patch(eye_left)
ax.add_patch(eye_right)

# Pupils (black circles)
pupil_left = plt.Circle((0.35, 0.67), 0.03, color='black')
pupil_right = plt.Circle((0.65, 0.67), 0.03, color='black')
ax.add_patch(pupil_left)
ax.add_patch(pupil_right)

# Eyebrows (lines above the eyes)
ax.plot([0.28, 0.42], [0.75, 0.77], color='black', lw=5)
ax.plot([0.58, 0.72], [0.75, 0.77], color='black', lw=5)

# Angry face (mouth) - curved line
theta = np.linspace(np.pi, 2 * np.pi, 100)
x = 0.5 + 0.2 * np.cos(theta)
y = 0.35 + 0.1 * np.sin(theta)
ax.plot(x, y, color='black', lw=3)

# Customize the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')  # Turn off axes

# Display the Angry Bird face
plt.title("Simplified Angry Bird Face", fontsize=16, fontweight='bold')
plt.show()


















#ANIMATIONS------------------------------------------------------------------------
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import numpy as np

# # Initialize the figure and axis
# fig, ax = plt.subplots(figsize=(6, 6))
# ax.set_xlim(-2, 2)
# ax.set_ylim(-2, 2)
# ax.set_aspect('equal')
# ax.axis('off')

# # Circle parameters
# circle_radius = 0.2
# circle, = ax.plot([], [], lw=2)

# # Precession and movement parameters
# t = np.linspace(0, 2 * np.pi, 100)  # Circle points
# angle = 0
# center_radius = 1  # Radius of the circular path

# def init():
#     """Initialize the animation frame."""
#     circle.set_data([], [])
#     return circle,

# def update(frame):
#     """Update function for the animation."""
#     global angle
#     # Update the center of the circle (precession motion)
#     cx = center_radius * np.cos(angle)
#     cy = center_radius * np.sin(angle)
#     angle += 0.05  # Increment angle for precession

#     # Compute the circle points around the center
#     x = cx + circle_radius * np.cos(t)
#     y = cy + circle_radius * np.sin(t)
#     circle.set_data(x, y)
#     return circle,

# # Create animation
# ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True)

# # Show the animation
# plt.show()
