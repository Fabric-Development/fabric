"""dead simple desktop widget that shows the time and date."""
import fabric
import os
from loguru import logger
from fabric.widgets.box import Box
from fabric.widgets.wayland import Window
from fabric.widgets.date_time import DateTime
from fabric.utils.helpers import set_stylesheet_from_file, monitor_file

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


ClockWidget()


def apply_style(*args):
    logger.info("[Desktop Widget] CSS applied")
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    css_file_path = os.path.join(current_script_directory, "desktop_widget.css")

    return set_stylesheet_from_file(css_file_path)


if __name__ == "__main__":
    if PYWAL is True:
        monitor = monitor_file(
            f"/home/{os.getlogin()}/.cache/wal/colors-widgets.css", "none"
        )
        monitor.connect("changed", apply_style)

    # initlize style
    apply_style()

    fabric.start()
