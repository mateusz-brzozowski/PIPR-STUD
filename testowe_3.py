import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


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
ax1_txt = [
    "1",
    "3",
    "28/53 (53%)",
    "19/28 (68%)",
    "12/25 (52%)",
    "6/7 (86%)",
    "6/9 (67%)",
    "33/54 (61%)",
    "25",
    "17",
    "65"
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

ax2_txt = [
    "1",
    "3",
    "37/54 (69%)",
    "17/37 (46%)",
    "4/17 (24%)",
    "2/7 (29%)",
    "3/3 (100%)",
    "21/53 (40%)",
    "25",
    "17",
    "65"
]

ax3_name = "STATISTICS"
bg = [100 for i in range(len(row_labels))]
center = [1 for i in range(len(row_labels))]
# code


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


f, ax = plt.subplots(
    1, 3, gridspec_kw={'width_ratios': [5, 1, 5]},
    figsize=(13.33, 7.5), dpi=96)

ax1_colors = ["#daa382", "#c85a19"]
ax2_colors = ["#769e94", "#00503c"]

ax[0].barh(row_count, np.negative(ax1_data), align='center', color=ax1_colors)
ax[0].barh(row_count, np.negative(bg), align='center', color='#ececec')
ax[2].barh(row_count, ax2_data, align='center', color=ax2_colors)
ax[2].barh(row_count, bg, align='center', color='#ececec')
ax[1].barh(row_count, center, align='center', color='#ffffff')

ax[0].invert_yaxis()
ax[1].invert_yaxis()
ax[2].invert_yaxis()

ax[0] = round_bars(ax[0])
ax[2] = round_bars(ax[2])

ax[0].set_title(ax1_name, fontsize=13, fontweight='bold')
ax[1].set_title(ax3_name, fontsize=20, fontweight='bold')
ax[2].set_title(ax2_name, fontsize=13, fontweight='bold')

ax[0].set_axis_off()
ax[1].set_axis_off()
ax[2].set_axis_off()

# build a rectangle in axes coords
left, width = 0.25, 0.5
bottom, height = 0.25, 0.5
right = left + width
top = bottom + height

# add text
for i, v in enumerate(row_labels):
    ax[1].text(
        0.5 * (left + right), i, v,
        horizontalalignment='center',
        verticalalignment='center')

for i, v in enumerate(ax1_txt):
    ax[0].text(
        -105, i, v,
        horizontalalignment='right',
        verticalalignment='center')

for i, v in enumerate(ax2_txt):
    ax[2].text(
        105, i, v,
        horizontalalignment='left',
        verticalalignment='center')


# f.tight_layout()
# plt.savefig("wykres.png", bbox_inches='tight')
plt.show()
