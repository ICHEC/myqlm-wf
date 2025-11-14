import numpy as np

class RadialEncoding:
    """
    `max_feature` is the largest feature in the training set. 
    The radii are scaled so that they are all between `shift*scaling` and `(1+shift)*scaling`.
    E.g. choosing `shift=1` and `scaling=5` so that all the radii are between 5 and 10.
    """
    def __init__(self, max_feature, shift, scaling, n_features):
        self.shift = shift * scaling
        self.scaling = scaling / max_feature
        
        angles = np.linspace(0, 2 * np.pi, n_features, endpoint=False)
        self.unit_circle = np.array([np.cos(angles), np.sin(angles)]).T

    def encode(self, x):
        """
        Enode a data point into a set of qubit coordinates.

        Parameters
        ----------
        x : np.ndarray
            The feature vector to be encoded.

        Returns
        -------
        np.ndarray
            The qubit coordinates.
        """
        radius = x * self.scaling + self.shift
        return radius[:, None] * self.unit_circle
