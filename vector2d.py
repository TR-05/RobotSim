import numpy as np

class V(np.ndarray):
    def __new__(cls, x, y):
        obj = np.asarray([x, y], dtype=np.float64).view(cls)
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return

    def __add__(self, other):
        return self + other

    def __sub__(self, other):
        return self - other

    def __mul__(self, scaler):
        return self
    def __div__(self, scaler):
        return self / scaler
    def dot(self, other):
        return np.dot(self, other)

    def cross(self, other):
        return np.cross(self, other)

    def length(self):
        return np.linalg.norm(self)

    def unit(self):
        return self / self.length()

    def angle(self, other):
        return np.arccos(self.dot(other) / (self.length() * other.length()))