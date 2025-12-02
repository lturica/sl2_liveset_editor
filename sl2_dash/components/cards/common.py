from dash import html


# General arguments for each slider
SLIDER_ARGS = {
    "tooltip": {"always_visible": True, "placement": "bottom"},
    "vertical": True,
    "verticalHeight": 200,
    "marks": None,
    "dots": False,
    # "persistence": True,
    "step": 1,
}


def make_tooltip(id):
    tt = html.A(
        id=id,
        className="bi bi-question-circle",
        style={"margin-left": "5px", "color": "info"},
    )
    return tt


def opts_from_enum(enum):
    return [{"label": e.name, "value": e.value} for e in enum]


# Get the number of slider groups

# The number of sliders per group
