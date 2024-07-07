from pathlib import Path
from pages.BasePage import BasePage

# default ukuran window
DEFAULT_APP_VIEW_GEOMETRY = "1512x982"
DEFAULT_APP_CONTROL_GEOMETRY = "1133x744"
APP_TITLE = "Smart ENT"

def relative_to_assets(path: str) -> Path: #
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")
    return ASSETS_PATH / Path(path)

def goToPage(page:BasePage, data=None):
    if data is None:
        page.drawPage()
    else:
        page.drawPage(data)