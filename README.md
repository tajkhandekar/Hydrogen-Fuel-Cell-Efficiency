# Hydrogen-Fuel-Cell-Efficiency
## Background
Hydrogen fuel cells are the future of energy. By combining water molecules, hydrogen fuel cells provide a sustainable method to obtain energy with only a byproduct of water. However, one disadvantage of hydrogen fuel cells is the high cost associated with their production. I wanted to improve the efficiency of energy storage in hydrogen fuel cells, so the benefits outweigh the price. 
## Data Collection
The model fuel cell created for the experiment consisted of two platinum coils (to separate and recombine the water molecules), a popsicle stick, and water. This cell was used to determine independent variables which influence the efficiency: ultrasonic waves, the water’s pH level, and the distance between the coils. Each variable was adjusted to specific values and I recorded the voltage at one-minute intervals for five minutes while it was discharging.  
## Analysis
To analyze the data, I developed a machine learning program with Python. Based on the factors present, multiple linear regression was the most suitable algorithm to determine the relationship between the x (independent variables) and y (voltage) values, if any.  
The regression coefficients generated by the analysis indicate that the distance between coils had no relationship to the output voltage. However, the analysis also indicated that a decrease in ultrasonic waves greatly influenced an increase in voltage. When the acidity of the water increased, it slightly increased the amount of voltage stored. In conclusion, to optimize the efficiency of hydrogen fuel cells, it is imperative to decrease ultrasonic waves and increase the acidity of the water. 
