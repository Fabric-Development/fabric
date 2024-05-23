"""dead simple desktop widget that shows the time and date."""
import fabric
import os
from loguru import logger
from fabric.widgets import Box, Window, DateTime
from fabric.utils import (
    set_stylesheet_from_file,
    monitor_file,
    get_relative_path,
)

PYWAL = False


class ClockWidget(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="bottom",
            anchor="left top right",
            margin="240px 0px 0px 0px",
            children=Box(
                children=[
                    DateTime(format_list=["%A. %d %B"], name="date", interval=10000),
                    DateTime(format_list=["%I:%M"], name="clock"),
                ],
                orientation="v",
            ),
            all_visible=True,
            exclusive=False,
        )


def apply_style(*args):
    logger.info("[Desktop Widget] CSS applied")
    return set_stylesheet_from_file(get_relative_path("desktop_widget.css"))


if __name__ == "__main__":
    desktop_widget = ClockWidget()

    if PYWAL is True:
        monitor = monitor_file(
            f"/home/{os.getlogin()}/.cache/wal/colors-widgets.css", "none"
        )
        monitor.connect("changed", apply_style)

    # initialize style
    apply_style()

    fabric.start()
