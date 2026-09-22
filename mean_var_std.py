import numpy as np

def mathEquations(matrix, equation):
    np_func = getattr(np, equation)
    return [np_func(matrix, axis=0).tolist(), np_func(matrix, axis=1).tolist(), np_func(matrix).item()]

def calculate(list):
    if len(list) == 9:
        matrix = np.array(list).reshape(3, 3)
        calculations = {
            'mean': mathEquations(matrix, "mean"),
            'variance': mathEquations(matrix, "var"),
            'standard deviation': mathEquations(matrix, "std"),
            'max': mathEquations(matrix, "max"),
            'min': mathEquations(matrix, "min"),
            'sum': mathEquations(matrix, "sum")
        }

        return calculations
    else:
        raise ValueError('List must contain nine numbers.')