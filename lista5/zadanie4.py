import numpy as np
from scipy.interpolate import lagrange

Re = np.array([0.2, 2, 20, 200, 2000, 20000], dtype = 'float') # Re
Cd = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433], dtype = 'float') # Cd

spl = lagrange(np.log(Re), np.log(Cd))

re_for_cp_to_find = np.array([5, 50, 5000])
cd_to_find = np.exp(spl(np.log(re_for_cp_to_find)))

result = dict(zip(re_for_cp_to_find, cd_to_find))

for key, value in result.items():
    print(f"Dla Re = {key} Cd = {value}")