"""
Simple plot functions for base data visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
from typing import overload
from os import PathLike
from datetime import datetime


def heatmapPlot(
    fName: str,
    data: list[list[int | float]] | np.ndarray,
    xTickLabels: list[int | float] = [],
    yTickLabels: list[int | float] = [],
    title: str = "",
    xLabel: str = "",
    yLabel: str = "",
    xTicks: int = 10,
    yTicks: int = 10,
    figsize: tuple[int, int] = (9, 6),
    **kwargs,
) -> None:
    fig = plt.figure(None, figsize)

    ax = sns.heatmap(data)

    xDecimals: int = kwargs.get("xDecimals", 3)
    xticks = np.linspace(data[0][0], data[0][-1], xTicks, endpoint=True)
    if len(xTickLabels) != 0:
        if len(xTickLabels) >= xTicks:
            ax.set_xticks(ticks=xticks)

            if len(xTickLabels) == xTicks:
                ax.set_xticklabels([str(label) for label in xTickLabels])
            else:
                step = int(len(xTickLabels) / xTicks)
                for i, _ in enumerate(xticks):
                    xticks[i] = xTickLabels[i * step]
                ax.set_xticklabels(xticks)
                ax.xaxis.set_major_formatter(FormatStrFormatter(f"%.{xDecimals}f"))
    elif xTicks != 0:
        ax.set_xticks(ticks=xticks, labels=xticks)
        ax.xaxis.set_major_formatter(formatter=FormatStrFormatter(f"%.{xDecimals}f"))
        ax.tick_params(axis="x", rotation=30)
    else:
        ax.tick_params(axis="x", which="both", bottom=False, labelbottom=False)

    yDecimals: int = kwargs.get("yDecimals", 3)
    yticks = np.round(
        np.linspace(min(data[1]), max(data[1]), yTicks, endpoint=True),
        decimals=yDecimals,
    )
    if len(yTickLabels) != 0:
        if len(yTickLabels) >= yTicks:
            ax.set_yticks(yticks)

            if len(yTickLabels) == yTicks:
                ax.set_yticklabels([str(label) for label in yTickLabels])
            else:
                step = int(len(yTickLabels) / yTicks)
                for i, _ in enumerate(yticks):
                    yticks[i] = round(yTickLabels[i * step], yDecimals)
                ax.set_yticklabels(yticks)
                ax.yaxis.set_major_formatter(FormatStrFormatter(f"%.{yDecimals}f"))
    elif yTicks != 0:
        ax.set_yticks(ticks=yticks, labels=yticks)
        ax.yaxis.set_major_formatter(FormatStrFormatter(f"%.{yDecimals}f"))
    else:
        ax.tick_params(
            axis="y",
            which="both",
            left=False,
            labelleft=False,
            right=False,
            labelright=False,
        )

    if title != "":
        ax.set_title(title)

    if xLabel != "":
        ax.set_xlabel(xLabel)
    else:
        ax.set_xlabel("Shear Frequency (Hz)")

    if yLabel != "":
        ax.set_ylabel(yLabel)
    else:
        ax.set_ylabel("Normal Frequency (Hz)")

    fig.axes.append(ax)
    fig.savefig(fName, bbox_inches="tight")


@overload
def linePlot(
    fName: str | PathLike,
    x: list[int | float] | np.ndarray,
    y: list[int | float] | np.ndarray,
) -> None: ...
@overload
def linePlot(
    fName: str | PathLike,
    x: list[int | float] | np.ndarray,
    y: list[int | float] | np.ndarray,
    time: list[int | float] | np.ndarray,
) -> None: ...
@overload
def linePlot(
    fName: str | PathLike,
    x: list[int | float] | np.ndarray,
    y: list[int | float] | np.ndarray,
    *,
    title: str = "",
    xLabel: str = "",
    yLabel: str = "",
    xTickLabels: list[int | float] = [],
    yTickLabels: list[int | float] = [],
    xTicks: int = 10,
    yTicks: int = 10,
    xTickLabelRound: int = 4,
    yTickLabelRound: int = 4,
    figsize: tuple[int, int] = (9, 6),
    linestyle: str = "-",
    transparent: bool = False,
    dpi: float | None = None,
) -> None: ...
@overload
def linePlot(
    fName: str | PathLike,
    x: list[int | float] | np.ndarray,
    y: list[int | float] | np.ndarray,
    time: list[int | float] | np.ndarray,
    *,
    title: str = "",
    xLabel: str = "",
    yLabel: str = "",
    xTickLabels: list[int | float] = [],
    yTickLabels: list[int | float] = [],
    xTicks: int = 10,
    yTicks: int = 10,
    figsize: tuple[int, int] = (9, 6),
    linestyle: str = "-",
    transparent: bool = False,
    dpi: float | None = None,
) -> None: ...


def linePlot(
    fName: str | PathLike,
    x: list[int | float] | np.ndarray,
    y: list[int | float] | np.ndarray,
    time: list[int | float] | np.ndarray = [],
    *,
    title: str = "",
    xLabel: str = "",
    yLabel: str = "",
    xTickLabels: list[int | float] = [],
    yTickLabels: list[int | float] = [],
    xTicks: int = 10,
    yTicks: int = 10,
    figsize: tuple[int, int] = (9, 6),
    **kwargs,
) -> None:
    """
    Creates a line plot figure with basic settings

    TODO add params

    :param fName: filename for output
    :type fName: str

    :param x: x axis data points
    :type x: list[int | float] | ndarray

    :param y: y axis data points
    :type y: list[int | float] | ndarray

    :param time: time data for x axis
    :type time: list[int | float] | ndarray

    :param title: plot title
    :type title: str

    :param xLabel: x label text
    :type xLabel: str

    :param yLabel: y label text
    :type yLabel: str

    :param xDecimal: Amount of decimal points on the bottom X-axis
    :type xDecimal: int

    :param yDecimal: Amount of decimal points on the Y-axis
    :type yDecimal: int

    :param fmt: plot line format, string of options \"[marker][line][colour]\"
    :type fmt: str
    """
    fig = plt.figure(None, figsize, dpi=kwargs.get("dpi", None))
    ax = fig.add_subplot()
    ax.plot(x, y, kwargs.get("fmt", ""))
    ax.grid(visible=True)

    xDecimals: int = kwargs.get("xDecimals", 3)
    xticks = np.linspace(x[0], x[-1], xTicks, endpoint=True)
    if len(xTickLabels) != 0:
        if len(xTickLabels) >= xTicks:
            ax.set_xticks(ticks=xticks)

            if len(xTickLabels) == xTicks:
                ax.set_xticklabels([str(label) for label in xTickLabels])
            else:
                step = int(len(xTickLabels) / xTicks)
                for i, _ in enumerate(xticks):
                    xticks[i] = xTickLabels[i * step]
                ax.set_xticklabels(xticks)
                ax.xaxis.set_major_formatter(FormatStrFormatter(f"%.{xDecimals}f"))
    elif xTicks != 0:
        ax.set_xticks(ticks=xticks, labels=xticks)
        ax.xaxis.set_major_formatter(formatter=FormatStrFormatter(f"%.{xDecimals}f"))
        ax.tick_params(axis="x", rotation=30)
    else:
        ax.tick_params(axis="x", which="both", bottom=False, labelbottom=False)

    yDecimals: int = kwargs.get("yDecimals", 3)
    yticks = np.round(
        np.linspace(min(y), max(y), yTicks, endpoint=True), decimals=yDecimals
    )
    if len(yTickLabels) != 0:
        if len(yTickLabels) >= yTicks:
            ax.set_yticks(yticks)

            if len(yTickLabels) == yTicks:
                ax.set_yticklabels([str(label) for label in yTickLabels])
            else:
                step = int(len(yTickLabels) / yTicks)
                for i, _ in enumerate(yticks):
                    yticks[i] = round(yTickLabels[i * step], yDecimals)
                ax.set_yticklabels(yticks)
                ax.yaxis.set_major_formatter(FormatStrFormatter(f"%.{yDecimals}f"))
    elif yTicks != 0:
        ax.set_yticks(ticks=yticks, labels=yticks)
        ax.yaxis.set_major_formatter(FormatStrFormatter(f"%.{yDecimals}f"))
    else:
        ax.tick_params(
            axis="y",
            which="both",
            left=False,
            labelleft=False,
            right=False,
            labelright=False,
        )

    if title != "":
        ax.set_title(title)
    if xLabel != "":
        ax.set_xlabel(xLabel)
    if yLabel != "":
        ax.set_ylabel(yLabel)

    fig.axes.append(ax)

    if len(time) == len(x) and len(time) > 0:
        ax2 = ax.twiny()
        ax2.set_xlim(ax.get_xlim())
        if xTicks != 0:
            ax2.set_xticks(ax.get_xticks())

        if datetime.fromtimestamp(time[-1]).day == datetime.fromtimestamp(time[0]).day:
            if x[-1] > x[0]:
                labels = [
                    datetime.fromtimestamp(t).strftime("%H:%M")
                    for t in np.interp(ax.get_xticks(), x, time)
                ]
            else:
                labels = [
                    datetime.fromtimestamp(t).strftime("%H:%M")
                    for t in np.interp(ax.get_xticks(), np.flip(x), np.flip(time))
                ]
            ax2.set_xticklabels(labels)
            ax2.set_xlabel("Time (HH:MM)")
        else:
            if x[-1] > x[0]:
                labels = [
                    datetime.fromtimestamp(t).strftime("%H:%M (%d/%m)")
                    for t in np.interp(ax.get_xticks(), x, time)
                ]
            else:
                labels = [
                    datetime.fromtimestamp(t).strftime("%H:%M (%d/%m)")
                    for t in np.interp(ax.get_xticks(), np.flip(x), np.flip(time))
                ]
            ax2.set_xticklabels(labels)
            ax2.set_xlabel("Time (HH:MM (dd/mm))")

        ax2.tick_params("x", rotation=30)
        fig.axes.append(ax2)

    fig.savefig(
        fName, bbox_inches="tight", transparent=kwargs.get("transparent", False)
    )
