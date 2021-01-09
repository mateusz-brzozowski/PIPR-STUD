import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
# from database import get_total_w_l, get_better, get_w_l_on_surface, get_surface

from io import BytesIO


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


# def get_data(player1, player2, tourney_name):
#     ax1_w, ax1_l = get_total_w_l(player1)
#     ax1_wl = round((ax1_w/(ax1_w + ax1_l))*100, 2)
#     ax2_w, ax2_l = get_total_w_l(player2)
#     ax2_wl = round((ax2_w/(ax2_w + ax2_l))*100, 2)
#     ax1_wbtw, ax2_wbtw = get_better(player1, player2)
#     ax1_wbtwp = round((ax1_wbtw/(ax1_wbtw + ax2_wbtw))*100, 0)
#     ax2_wbtwp = round((ax2_wbtw/(ax1_wbtw + ax2_wbtw))*100, 0)

#     ax1_ws, ax1_ls = get_w_l_on_surface(player1, tourney_name)
#     ax1_wls = round((ax1_ws/(ax1_ws + ax1_ls))*100, 2)
#     ax2_ws, ax2_ls = get_w_l_on_surface(player2, tourney_name)
#     ax2_wls = round((ax2_ws/(ax2_ws + ax2_ls))*100, 2)

#     ax1_txt = [
#         f"{ax1_w}/{ax1_l} ({int(ax1_wl)}%)",
#         f"{ax1_wbtw}/{ax2_wbtw} ({int(ax1_wbtwp)}%)",
#         f"{ax1_ws}/{ax1_ls} ({int(ax1_wls)}%)"
#     ]
#     ax2_txt = [
#         f"{ax2_w}/{ax2_l} ({int(ax2_wl)}%)",
#         f"{ax2_wbtw}/{ax1_wbtw} ({int(ax2_wbtwp)}%)",
#         f"{ax2_ws}/{ax2_ls} ({int(ax2_wls)}%)"
#     ]
#     ax1_data = [
#         ax1_wl,
#         ax1_wbtwp,
#         ax1_wls
#     ]
#     ax2_data = [
#         ax2_wl,
#         ax2_wbtwp,
#         ax2_wls
#     ]
#     return ax1_txt, ax1_data, ax2_txt, ax2_data


def get_data(player1, player2, tourney_name, values):
    ax1_txt = []

    ax2_txt = []

    ax1_data = [data for data in ax1_win_to_loss]

    ax2_data = [data for data in ax2_win_to_loss]

    return ax1_txt, ax1_data, ax2_txt, ax2_data


def get_plot(player1, player2, tourney_name, values):
    row_labels = values
    row_count = np.arange(len(row_labels))
    ax1_txt, ax1_data, ax2_txt, ax2_data = get_data(
        player1, player2, tourney_name, values)
    ax1_name = player1
    ax2_name = player2
    ax3_name = tourney_name
    bg = [100 for i in range(len(row_labels))]
    center = [1 for i in range(len(row_labels))]

    f, ax = plt.subplots(
        1, 3, gridspec_kw={'width_ratios': [5, 1, 5]},
        figsize=(13.33, 7.5), dpi=96)

    ax1_colors = ["#daa382", "#c85a19"]
    ax2_colors = ["#769e94", "#00503c"]

    ax[0].barh(
        row_count, np.negative(ax1_data),
        align='center', color=ax1_colors)
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
    ax[1].set_title(ax3_name, fontsize=13, fontweight='bold')
    ax[2].set_title(ax2_name, fontsize=13, fontweight='bold')

    ax[0].set_axis_off()
    ax[1].set_axis_off()
    ax[2].set_axis_off()

    left, width = 0.25, 0.5
    right = left + width

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
    buffer = BytesIO()
    plt.savefig(buffer)
    plt.clf()
    return buffer.getvalue()


if __name__ == "__main__":
    get_plot("Novak Djokovic", "Juan Martin Del Potro", "Us Open")
