import flet as ft

from tiny_tiny_computer.machine.gui.components import (
    create_assembly_code_input,
    create_control_buttons,
    create_cpu_section,
    create_output_display,
    create_ram_section,
)


def machine_ui(page: ft.Page):
    """Main UI function to assemble all components."""
    page.title = "Little Man Computer (LMC) Simulator"
    page.scroll = "adaptive"
    page.padding = 20
    page.theme_mode = "light"

    control_buttons = create_control_buttons()
    assembly_code = create_assembly_code_input()
    output_display = create_output_display()
    cpu_section = create_cpu_section()
    ram_section = create_ram_section()

    left_column = ft.Column(
        [
            control_buttons,
            assembly_code,
            output_display,
        ],
        spacing=10,
    )

    right_column = ft.Column(
        [
            cpu_section,
            ram_section,
        ],
        spacing=10,
    )

    page.add(
        ft.Row(
            [
                left_column,
                right_column,
            ],
            spacing=20,
            vertical_alignment="start",
        )
    )
    page.update()
