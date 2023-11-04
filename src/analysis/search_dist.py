# Present the search area as a 2 dimensional rectange
import pylab

def extract_search_paths(results):
    """
    Extracts the x and y coordinates from the given results.

    Parameters:
    - results (dict): A dictionary containing the results of the trials.

    Returns:
    - x (list): A list of x coordinates.
    - y (list): A list of y coordinates.
    """
    # Set up arrays to sum the x and y coordinates for all trials
    x = []
    y = []

    pred = results['predator']

    # Add the steps for each predator from each trial
    for trial in range(len(pred)):
        for step in range(len(pred[trial].X)):
            x.append(pred[trial].X[step])
            y.append(pred[trial].Y[step])

    return x, y

def plot_search_dist(x, y):
    #TODO more work needed here
    """
    Plot the search distribution.
    
    Parameters:
        x (list): The x-coordinates of the points to plot.
        y (list): The y-coordinates of the points to plot.
    """
    pylab.plot(x, y)
    pylab.show()

