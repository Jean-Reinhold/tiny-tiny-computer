import flet as ft

from tiny_tiny_computer.machine.instruction_mapper import InstructionMapper
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers
from tiny_tiny_computer.machine.sic import SICMachine

sic = SICMachine(Memory(), Registers(), InstructionMapper())
memory_controls = {}
register_controls = {}

from tiny_tiny_computer.machine.gui.components import (
    create_macro_section,
    create_main_section,
    create_memory_section,
    create_registers_section,
)


def machine_ui(page: ft.Page):
    """Main UI function to assemble all components."""
    global sic, memory_controls, register_controls

    page.title = "Little Man Computer (LMC) Simulator"
    page.scroll = "adaptive"
    page.padding = 20
    page.theme_mode = "light"
    page.bgcolor = "#000000"

    memory_section = create_memory_section(sic, page, memory_controls)
    main_section = create_main_section(page, sic, register_controls, memory_controls)
    registers_section = create_registers_section(sic.registers, register_controls)
    macro_section = create_macro_section(page)

    row = ft.Row(
        [memory_section, main_section, registers_section, macro_section],
        spacing=60,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    page.add(row)
    page.update()


# To run the app:
# ft.app(target=machine_ui)
