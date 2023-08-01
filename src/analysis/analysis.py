# Initial analyses
from scipy import stats
import numpy as np
import pylab


def entities_in_environment(e):
    """Counts the number of patches and number of entities in all patches
    Input: environment e
    Returns: p number of patches and n total number of entities
    """
    p = n = 0
    for patch in e.children:
        p += 1
        n += patch.number_children()

    return p, n


def extract_data(results):
    """Extracts data from the given results dictionary.

    Parameters:
    - results (dict): A dictionary containing the results of a trial.

    Returns:
    - data (dict): A dictionary containing the extracted data. It has the following keys:
        - 'number_patches' (list): A list of the number of patches in each trial.
        - 'total_entities' (list): A list of the total number of entities in each trial.
        - 'total_remaining' (list): A list of the total number of remaining entities in each trial.
        - 'total_captured' (list): A list of the total number of captured entities in each trial.
    """
    data = {
        'number_patches': [],
        'total_entities': [],
        'total_remaining': [],
        'total_captured': []
        }

    for trial in range(len(results['environment'])):
        env = results['environment'][trial]
        pred = results['predator'][trial]

        n_patches, n_entities = entities_in_environment(env)

        data['number_patches'].append(n_patches)
        data['total_remaining'].append(n_entities)
        data['total_captured'].append(pred.total_captured())
        data['total_entities'].append(
            data['total_remaining'][trial] +
            data['total_captured'][trial])

    return data


def analyse_results(data):
    """Perform a linear regression analysis on the given data.

    Parameters:
    - data: a dictionary containing the 'total_entities' and 'total_captured' data arrays

    Returns:
    None
    """

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
