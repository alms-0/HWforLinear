def linear(m, x, b):
    return m*x + b
def slope_units(x_units,y_units):
    x_stripped = x_units.rstrip('s')
    y_stripped = y_units.rstrip('s')
    return y_stripped + '/' + x_stripped
def print_equation(m,b,y_units,x_units):
    return 'The equation of the line is: ' + str(m) + slope_units(y_units,x_units) + '+' + str(b) + y_units
    
