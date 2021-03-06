#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

from ax.plot.base import AxPlotConfig, AxPlotTypes
from ax.plot.render import _js_requires, _wrap_js, plot_config_to_html
from ax.utils.common.logger import get_logger
from IPython.display import display
from plotly.offline import init_notebook_mode, iplot


logger = get_logger("ipy_plotting")


def init_notebook_plotting(offline=False):
    """Initialize plotting in notebooks, either in online or offline mode."""
    display_bundle = {"text/html": _wrap_js(_js_requires(offline=offline))}
    display(display_bundle, raw=True)
    logger.info(
        "Injecting Plotly library into cell. " "Do not overwrite or delete cell."
    )
    init_notebook_mode()


def render(plot_config: AxPlotConfig, inject_helpers=False) -> None:
    """Render plot config."""
    if plot_config.plot_type == AxPlotTypes.GENERIC:
        iplot(plot_config.data)
    else:
        display_bundle = {
            "text/html": plot_config_to_html(plot_config, inject_helpers=inject_helpers)
        }
        display(display_bundle, raw=True)
