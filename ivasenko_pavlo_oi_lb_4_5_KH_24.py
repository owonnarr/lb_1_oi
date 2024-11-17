import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

cargo_capacity = ctrl.Antecedent(np.arange(0, 11, 1), 'cargo_capacity')
dimensions = ctrl.Antecedent(np.arange(0, 11, 1), 'dimensions')
fuel_consumption = ctrl.Antecedent(np.arange(0, 11, 1), 'fuel_consumption')
vehicle_type = ctrl.Consequent(np.arange(0, 11, 1), 'vehicle_type')

cargo_capacity['low'] = fuzz.trimf(cargo_capacity.universe, [0, 0, 5])
cargo_capacity['high'] = fuzz.trimf(cargo_capacity.universe, [5, 10, 10])

dimensions['small'] = fuzz.trimf(dimensions.universe, [0, 0, 5])
dimensions['large'] = fuzz.trimf(dimensions.universe, [5, 10, 10])

fuel_consumption['low'] = fuzz.trimf(fuel_consumption.universe, [0, 0, 5])
fuel_consumption['high'] = fuzz.trimf(fuel_consumption.universe, [5, 10, 10])


vehicle_type['passenger'] = fuzz.trimf(vehicle_type.universe, [0, 0, 6])
vehicle_type['cargo'] = fuzz.trimf(vehicle_type.universe, [4, 10, 10])

rule1 = ctrl.Rule(
    (cargo_capacity['high'] & dimensions['large']) |
    (cargo_capacity['high'] & fuel_consumption['high']),
    vehicle_type['cargo']
)

rule2 = ctrl.Rule(
    (cargo_capacity['low'] & dimensions['small']) |
    (cargo_capacity['low'] & fuel_consumption['low']),
    vehicle_type['passenger']
)

vehicle_ctrl = ctrl.ControlSystem([rule1, rule2])
vehicle_simulation = ctrl.ControlSystemSimulation(vehicle_ctrl)

vehicle_simulation.input['cargo_capacity'] = 7
vehicle_simulation.input['dimensions'] = 6
vehicle_simulation.input['fuel_consumption'] = 7

vehicle_simulation.compute()
vehicle_type.view(sim=vehicle_simulation)
plt.show()

