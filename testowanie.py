import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

# Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = (
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
y_pos = np.arange(len(people))
right_performance = [
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
left_performance = [
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


ax.barh(y_pos, right_performance, align='center', color='orangered')
ax.barh(y_pos, bg, align='center', color='lightgrey')
ax.barh(y_pos, np.negative(left_performance),
        align='center', color='deepskyblue')
ax.barh(y_pos, np.negative(bg),
        align='center', color='lightgrey')

# ax.figure.set_size_inches(6, 6)
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

ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.set_xticklabels("")
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
left_name = "Iga Swiatek"
rigth_name = "Sofia Kenin"
ax.set_title(f'{left_name:<50}{rigth_name:>50}')

# ax.spines["left"].set_position(("data", 0))
# ax.spines["bottom"].set_visible(False)
# # Hide the top and right spines.
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
# plt.tight_layout()

plt.show()
