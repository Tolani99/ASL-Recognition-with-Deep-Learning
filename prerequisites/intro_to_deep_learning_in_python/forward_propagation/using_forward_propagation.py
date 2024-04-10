import numpy as np
input_data = np.array([2, 3])
weights = {'node_0': np.array([1, 1]),
	   'node_1': np.array([-1, 1]),
	   'output': np.array([2, -1])}
node_0_value = (input_data * weights['node_0']).sum()
node_1_value = (input_data * weights['node_1']).sum()
