import flet as ft

from tiny_tiny_computer.machine.gui.components import *
from tiny_tiny_computer.machine.memory import Memory


def machine_ui(page: ft.Page):
    """Main UI function to assemble all components."""

    page.title = "Little Man Computer (LMC) Simulator"
    page.scroll = "adaptive"
    page.padding = 20
    page.theme_mode = "light"

    mem = Memory()

    memory_section = create_memory_section(mem, page)

    page.add(memory_section)
    page.update()


# To run the app:
# ft.app(target=machine_ui)
