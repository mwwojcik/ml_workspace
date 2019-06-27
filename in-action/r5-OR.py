from random import random
import numpy as np

sample_data = [ [0, 0],  # False, False
                [0, 1],  # False, True
                [1, 0],  # True, False
                [1, 1]]  # True, True


expected_results = [0,  # (False OR False) gives False
                    1,  # (False OR True ) gives True
                    1,  # (True  OR False) gives True
                    1]  # (True  OR True ) gives True

weights = np.random.random(2) / 1000  # Small random float 0 < w < .001

activation_threshold = 0.5

bias_weight = np.random.random() / 1000
bias_weight
for iteration_num in range(5):
    correct_answers = 0
    for idx, sample in enumerate(sample_data):
        input_vector = np.array(sample)
        weights = np.array(weights)
        activation_level = np.dot(input_vector, weights) +\
            (bias_weight * 1)
        if activation_level > activation_threshold:
            perceptron_output = 1
        else:
            perceptron_output = 0
        if perceptron_output == expected_results[idx]:
            correct_answers += 1
        new_weights = []
        for i, x in enumerate(sample):
            new_weights.append(weights[i] + (expected_results[idx] -\
                perceptron_output) * x)
        bias_weight = bias_weight + ((expected_results[idx] -\
            perceptron_output) * 1)
        weights = np.array(new_weights)
    print('{} correct answers out of 4, for iteration {}'\
        .format(correct_answers, iteration_num))



