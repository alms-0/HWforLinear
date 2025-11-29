# 1. Import everything from the fitting_functions file.
from fitting_functions import *

# 2. Import necessary libraries for numerical work, plotting, and fitting.
import numpy as np                     # Used for loading and manipulating data
import matplotlib.pyplot as plt        # Used for graphing
from scipy import stats                # Used for performing linear regression fits

# 3. Load the CSV data file into a NumPy array called "data".
data = np.genfromtxt("tips.csv", delimiter=",", names=True)

# 4. Extract Bill and Tip as x and y values.

x_bill = data['Bill']     # x-values (in dollars)
y_tip = data['Tip']       # y-values (in dollars)


# 5. Perform a linear fit using SciPy's stats.linregress().

fit1 = stats.linregress(x_bill, y_tip)

# 6. Create a scatter plot of the data.
plt.figure()
plt.scatter(x_bill, y_tip, color='blue', label='Data Points')
plt.xlabel("Bill (dollars)")            # Label x-axis WITH UNITS
plt.ylabel("Tip (dollars)")             # Label y-axis WITH UNITS
plt.title("Tip vs Bill")

# 7. Plot the best-fit line.
plt.plot(x_bill, fit1.intercept + fit1.slope*x_bill,
         color='red', label='Linear Fit')

plt.legend()
plt.grid(True)
plt.show()
print("Tip vs Bill linear fit:")
print_equation(fit1.slope, fit1.intercept, x_units="dollars", y_units="dollars")

# 9. Now repeat the process but use Percent Tip instead of Tip.

x_bill2 = data['Bill']         # x values stay the same
y_pct = data['PctTip']         # y-axis is percent_tip now (% units)

# 10. Perform a new regression for this relationship.
fit2 = stats.linregress(x_bill2, y_pct)

# 11. Scatter plot for Percent Tip vs Bill.
plt.figure()
plt.scatter(x_bill2, y_pct, color='green', label='Data Points')
plt.xlabel("Bill (dollars)")      # x-axis units stay the same
plt.ylabel("Percent Tip (%)")     # y-axis is now a percentage
plt.title("Percent Tip vs Bill")

# 12. Plot the new regression line.
plt.plot(x_bill2, fit2.intercept + fit2.slope*x_bill2,
         color='magenta', label='Linear Fit')
plt.legend()
plt.grid(True)
plt.show()

# 13. Print line equation for Percent Tip.
print("Percent Tip vs Bill linear fit:")
print_equation(fit2.slope, fit2.intercept, x_units="dollars", y_units="%")
