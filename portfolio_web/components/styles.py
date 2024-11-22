import reflex as rx
from enum import Enum


class Size(Enum):
    # Using instead of px, to fit the text size
    ZERO = "0px !important"
    TINY = "0.3em"
    SMALL = "0.5em"
    MEDIUM = "0.7em"
    DEFAULT = "1em"
    ABIT_BIG = "1.2em"
    LIGHT_BIG = "1.5em"
    BIG = "2em"
    VERY_BIG = "2.5em"
    HUGE = "4em"
    GARGANTUAL = "6em"
    COLOSAL = "8em"


class Color(Enum):
    FEATURED = "#0033CC"  # Sapphire Glitter
    PRIMARY = "#000000"  # Black
    SECONDARY = "#202020"  # Light Steel Blue
    TERTIARY = "#4682B4"  # Steel Blue
    ACCENT = "#0070f3"  # Pure (or mostly pure) blue
    HOVER = "#1a1a1a"  # Very dark gray (mostly black)


class TextColor(Enum):
    FEATURED = "#0033CC"  # Sapphire Glitter
    PRIMARY = "#ffffff"  # White
    SECONDARY = "#B0C4DE"  # Light Steel Blue
    TERTIARY = "#4682B4"  # Steel Blue
    HOVER = "#1a1a1a"  # Very dark gray (mostly black)


class Font(Enum):
    TITLES = "Dancing Script"
    TEXT = ""
    NOTES = "Taking a Chance on Love"


MAX_WIDTH = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    litle_width="1200px",
    max_width="1500px",
)


MAX_WIDTH_SKILLS = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    litle_width="1200px",
    max_width="1500px",
)


BASE_STYLE = {
    "font_family": Font.TEXT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.heading: {"color": TextColor.FEATURED.value},
    rx.link: {
        "text_decoration": "none",
        "_hover": {"color": TextColor.FEATURED.value, "text_decoration": "none"},
    },
    rx.button: {
        "background-color": Color.FEATURED.value,
        "variant": "solid",
        "margin_bottom": Size.DEFAULT.value,
        "height": Size.BIG.value,
        "color": TextColor.SECONDARY.value,
        "_hover": {"color": TextColor.TERTIARY.value},
    },
}


# Fonts and CSS animations
STYLE_SHEET = [
    # FONTS
    "https://fonts.googleapis.com/css?family=Qwitcher+Grypen&display=swap",
    "https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap"
    # CSS
    "https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/csshake/1.7.0/csshake.css",
    # Makes some icons/buttons jitter
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    # "Heartbeat" effect on title
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    # Brings the GitHub and LinkedIn icons from the footer
]
