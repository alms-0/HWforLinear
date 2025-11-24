# tipping.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from fitting_functions import *

# Step 1: Read in the data
data = np.genfromtxt("tips.csv", delimiter=",", skip_header=1, dtype=float)

# Columns: Bill = column 0, Tip = column 1, PctTip = column 2
bill = data[:,0]
tip = data[:,1]
pct_tip = data[:,2]

# Step 2: Define linear function
def linear(x, m, b):
    return m*x + b

# ---- First Fit: Bill vs Tip ----
params, cov = curve_fit(linear, bill, tip)
m, b = params

plt.figure()
plt.scatter(bill, tip, label="Data")
plt.plot(bill, linear(bill, m, b), color="red", label="Fit")
plt.xlabel("Bill ($)")
plt.ylabel("Tip ($)")
plt.legend()
plt.title("Bill vs Tip")
plt.show()

# Print equation with units
print_equation(m, b, "Bill ($)", "Tip ($)")
# Example output (yours will differ):
# Tip ($) = 0.15 * Bill ($) + 1.00
# Copy this output into a comment:
# Tip ($) = 0.15 * Bill ($) + 1.00

# ---- Second Fit: Bill vs PctTip ----
params2, cov2 = curve_fit(linear, bill, pct_tip)
m2, b2 = params2

plt.figure()
plt.scatter(bill, pct_tip, label="Data")
plt.plot(bill, linear(bill, m2, b2), color="green", label="Fit")
plt.xlabel("Bill ($)")
plt.ylabel("Tip (%)")
plt.legend()
plt.title("Bill vs Percent Tip")
plt.show()

# Print equation with units
print_equation(m2, b2, "Bill ($)", "Tip (%)")
# Example output (yours will differ):
# Tip (%) = -0.01 * Bill ($) + 20.0
# Copy this output into a comment:
# Tip (%) = -0.01 * Bill ($) + 20.0
