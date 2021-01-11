import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from database import (
    get_sum_in_columns, get_winratio_columns, get_best_in_columns
)
from io import BytesIO


def round_bars(ax):
    new_patches = []
    for patch in reversed(ax.patches):
        if patch.get_width() != 0:
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


def get_description(player_wins, player_losses):
    player_wins = int(player_wins)
    player_losses = int(player_losses)
    if player_wins == 0 and player_losses == 0:
        return "Lack of data", 0
    ratio = round((player_wins/(player_wins + player_losses))*100, 2)
    return f"{player_wins}/{player_losses} ({int(ratio)}%)", ratio


def get_data(
    player1, player2, tourney_name, columns, best, min_date, max_date
):
    ax1_txt = []
    ax2_txt = []
    ax1_data = []
    ax2_data = []
    for column in columns.values():
        if column[0] == "winner_name":
            data = get_winratio_columns(
                player1, player2, tourney_name, column, min_date, max_date)
            player1_desc, player1_rato = get_description(
                data[0], data[1])
            player2_desc, player2_rato = get_description(
                data[2], data[3])
            ax1_txt.append(player1_desc)
            ax2_txt.append(player2_desc)
            ax1_data.append(player1_rato)
            ax2_data.append(player2_rato)
        else:
            if best or column[0] == "winner_ht":
                data = get_best_in_columns(
                    player1, player2, tourney_name, column, min_date, max_date)
            else:
                data = get_sum_in_columns(
                    player1, player2, tourney_name, column, min_date, max_date)
            player1_desc, player1_rato = get_description(
                data[0], data[1])
            player2_desc, player2_rato = get_description(
                data[1], data[0])
            ax1_txt.append(player1_desc)
            ax2_txt.append(player2_desc)
            ax1_data.append(player1_rato)
            ax2_data.append(player2_rato)
    return ax1_txt, ax1_data, ax2_txt, ax2_data


def get_plot(
    player1, player2, tourney_name, columns, best, min_date, max_date
):
    row_labels = columns
    row_count = np.arange(len(row_labels))
    ax1_txt, ax1_data, ax2_txt, ax2_data = get_data(
        player1, player2, tourney_name, columns, best, min_date, max_date)
    ax1_name = player1
    ax2_name = player2
    ax3_name = tourney_name
    bg = [100 for i in range(len(row_labels))]
    center = [1 for i in range(len(row_labels))]

    f, ax = plt.subplots(
        1, 3, gridspec_kw={'width_ratios': [5, 2, 5]},
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

    for pos_y, text in enumerate(row_labels):
        ax[1].text(
            0.5 * (left + right), pos_y, text,
            horizontalalignment='center',
            verticalalignment='center', wrap=True)

    for pos_y, text in enumerate(ax1_txt):
        ax[0].text(
            -105, pos_y, text,
            horizontalalignment='right',
            verticalalignment='center')

    for pos_y, text in enumerate(ax2_txt):
        ax[2].text(
            105, pos_y, text,
            horizontalalignment='left',
            verticalalignment='center')
    buffer = BytesIO()
    plt.savefig(buffer)
    plt.clf()
    return buffer.getvalue()


if __name__ == "__main__":
    get_plot(
        "Novak Djokovic", "Juan Martin Del Potro", "Us Open",
        {"Number of wins in ther": ['w_ace', 'l_ace']})
