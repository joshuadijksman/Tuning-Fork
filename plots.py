import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def heatmapPlot(
    fName: str,
    data: list[list[int | float]] | np.ndarray,
    xTickLabels: list[int | float] = [],
    yTickLabels: list[int | float] = [],
    title: str = "",
    xTicks: int = 10,
    yTicks: int = 10,
    xTickLabelRound: int = 4,
    yTickLabelRound: int = 4,
    figsize: tuple[int, int] = (9, 6),
) -> None:
    fig = plt.figure(None, figsize)

    ax = sns.heatmap(data)

    if len(xTickLabels) != 0:
        if len(xTickLabels) >= xTicks:
            xStep = int(len(data[0]) / xTicks)
            xSpots = list(range(0, len(data[0]) + 1, xStep))
            ax.set_xticks(ticks=np.array(xSpots) + 0.5)

            if len(xTickLabels) == xTicks:
                ax.set_xticklabels(xTickLabels)
            else:
                step = int(len(xTickLabels) / xTicks)
                for i, _ in enumerate(xSpots):
                    xSpots[i] = round(xTickLabels[i * step], xTickLabelRound)
                ax.set_xticklabels(xSpots)

    if len(yTickLabels) != 0:
        if len(yTickLabels) >= yTicks:
            yStep = int(len(data) / yTicks)
            ySpots = list(range(0, len(data) + 1, yStep))
            ax.set_yticks(np.array(ySpots) + 0.5)

            if len(yTickLabels) == yTicks:
                ax.set_yticklabels(yTickLabels)
            else:
                step = int(len(yTickLabels) / yTicks)
                for i, _ in enumerate(ySpots):
                    ySpots[i] = round(yTickLabels[i * step], yTickLabelRound)
                ax.set_yticklabels(ySpots)

    if title != "":
        ax.set_title(title)

    
    ax.set_xlabel("Shear Frequency (Hz)")
    ax.set_ylabel("Normal Frequency (Hz)")

    fig.axes.append(ax)
    fig.savefig(fName, bbox_inches="tight")


def linePlot(
    fName: str,
    x: list[int | float] | np.ndarray,
    y: list[int | float] | np.ndarray,
    xLabel="",
    yLabel="",
    xTickLabels: list[int | float] = [],
    yTickLabels: list[int | float] = [],
    title: str = "",
    xTicks: int = 10,
    yTicks: int = 10,
    xTickLabelRound: int = 4,
    yTickLabelRound: int = 4,
    figsize: tuple[int, int] = (9, 6),
):
    fig = plt.figure(None, figsize)
    ax = fig.add_subplot()
    ax.plot(x, y)

    if len(xTickLabels) != 0:
        if len(xTickLabels) >= xTicks:
            xStep = int(len(x) / xTicks)
            xSpots = list(range(0, len(x) + 1, xStep))
            ax.set_xticks(ticks=np.array(xSpots) + 0.5)

            if len(xTickLabels) == xTicks:
                ax.set_xticklabels(xTickLabels)
            else:
                step = int(len(xTickLabels) / xTicks)
                for i, _ in enumerate(xSpots):
                    xSpots[i] = round(xTickLabels[i * step], xTickLabelRound)
                ax.set_xticklabels(xSpots)

    if len(yTickLabels) != 0:
        if len(yTickLabels) >= yTicks:
            yStep = int(len(y) / yTicks)
            ySpots = list(range(0, len(y) + 1, yStep))
            ax.set_yticks(np.array(ySpots) + 0.5)

            if len(yTickLabels) == yTicks:
                ax.set_yticklabels(yTickLabels)
            else:
                step = int(len(yTickLabels) / yTicks)
                for i, _ in enumerate(ySpots):
                    ySpots[i] = round(yTickLabels[i * step], yTickLabelRound)
                ax.set_yticklabels(ySpots)

    if title != "":
        ax.set_title(title)
    if xLabel != "":
        ax.set_xlabel(xLabel)
    if yLabel != "":
        ax.set_ylabel(yLabel)

    fig.axes.append(ax)
    fig.savefig(fName, bbox_inches="tight")
