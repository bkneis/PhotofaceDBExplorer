import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

def zero_to_nan(values):
    """Replace every 0 with 'nan' and return a copy."""
    return [np.nan if x==0 else x for x in values]

def plotPie(totals, legend=False):
    labels = totals.keys()
    fracs = totals.values()
    # Make square figures and axes
    the_grid = GridSpec(1, 1)
    plt.subplot(the_grid[0, 0], aspect=1)

    if not legend:
        plt.pie([float(v) for v in fracs], labels=[v for v in labels], autopct='%1.1f%%', shadow=False)
    else:
        patches, texts, autos = plt.pie([float(v) for v in fracs], autopct='%1.1f%%', shadow=False)
        plt.legend(patches, [v for v in labels], loc='best', fontsize=8)

    plt.show()

