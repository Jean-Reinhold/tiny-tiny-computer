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
    main_section = create_main_section(page)

    row = ft.Row(
        [memory_section, main_section],
        spacing=60,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    page.add(row)
    page.update()


# To run the app:
# ft.app(target=machine_ui)
