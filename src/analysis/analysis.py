# Initial analyses
from scipy import stats
import numpy as np
import pylab


def entities_in_environment(e):
    p, n = 0
    for patch in e.children:
        p += 1
        n += patch.number_children()

    return p, n


def extract_data(results):
    data = {
        'number_patches': [],
        'total_entities': [],
        'total_remaining': [],
        'total_captured': []
        }

    for trial in range(len(results)):
        env = results[trial]['environment']
        pred = results[trial]['predator']

        n_patches, n_entities = entities_in_environment(env)

        data['number_patches'].append(n_patches)
        data['total_remaining'].append(n_entities)
        data['total_captured'].append(pred.total_captured())
        data['total_entities'].append(
            data['total_remaining'][trial] +
            data['total_captured'][trial])

    return data


def analyse_results(data):

    x = np.array(data['total_entities'])
    y = np.array(data['total_captured'])

    slope, intercept, r_value, p_value, \
        slope_std_error = stats.linregress(x, y)

    print("Slope, intercept:", slope, intercept)
    print("R-squared:", r_value**2)

    # Calculate some additional outputs
    predict_y = intercept + slope * x
    pred_error = y - predict_y
    degrees_of_freedom = len(x) - 2
    residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)
    print("Residual Std Error = ", residual_std_error)

    # Plotting
    pylab.plot(x, y, 'o')
    pylab.plot(x, predict_y, 'k-')
    pylab.title("Captured vs Total Entities")
    pylab.xlabel("No. Entity in Environment")
    pylab.ylabel("No. Entity Captured")
    pylab.show()
