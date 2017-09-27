import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def plotPie(totals):
    labels = totals.keys()
    fracs = totals.values()
    # Make square figures and axes
    the_grid = GridSpec(1, 1)
    plt.subplot(the_grid[0, 0], aspect=1)
    plt.pie([float(v) for v in fracs], labels=[v for v in labels], autopct='%1.1f%%', shadow=True)
    plt.show()

