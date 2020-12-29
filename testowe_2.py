import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


def round_bars(ax):
    new_patches = []
    for patch in reversed(ax.patches):
        bb = patch.get_bbox()
        color = patch.get_facecolor()
        p_bbox = FancyBboxPatch(
            (bb.xmin, bb.ymin),
            abs(bb.width), abs(bb.height),
            boxstyle="round,pad=-0.1,rounding_size=1",
            ec="none", fc=color,
            mutation_aspect=0.5
        )
        patch.remove()
        new_patches.append(p_bbox)

    for patch in new_patches:
        ax.add_patch(patch)
    return ax


# define pyplot
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# fig, (ax1, ax3, ax2) = plt.subplots(1, 3)

# Sample data
row_labels = (
    'ACES',
    'DOUBLE FAULTS',
    'FIRST SERVE',
    'WIN ON 1ST SERVE',
    'WIN ON 2ND SERVE',
    'NET POINTS WON',
    'BREAK POINTS WON',
    'RECEIVING POINTS WON',
    'WINNERS',
    'UNFORCED ERRORS',
    'TOTAL POINTS WON'
)
row_count = np.arange(len(row_labels))

ax1_name = "Iga Swiatek"
ax1_data = [
    50,
    50,
    53,
    68,
    52,
    86,
    67,
    61,
    71,
    42.5,
    61
]

ax2_name = "Sofia Kenin"
ax2_data = [
    50,
    50,
    69,
    46,
    24,
    29,
    100,
    40,
    29,
    57.5,
    39
]

bg = [
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100
]

ax1.barh(row_count, np.negative(ax1_data), align='center', color='deepskyblue')
ax1.barh(row_count, np.negative(bg), align='center', color='lightgrey')
ax2.barh(row_count, ax2_data, align='center', color='orangered')
ax2.barh(row_count, bg, align='center', color='lightgrey')

ax1 = round_bars(ax1)
ax2 = round_bars(ax2)

ax1.set_title(ax1_name)
ax2.set_title(ax2_name)

ax2.set_yticks(row_count)
ax2.set_yticklabels(row_labels)

ax1.set_axis_off()
ax2.set_axis_off()

fig.tight_layout()
plt.show()
