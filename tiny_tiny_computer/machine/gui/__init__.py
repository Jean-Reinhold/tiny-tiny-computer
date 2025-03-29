import flet as ft

from tiny_tiny_computer.machine.gui.components import *
from tiny_tiny_computer.machine.instruction_mapper import InstructionMapper
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers
from tiny_tiny_computer.machine.sic import SICMachine

output_text_control = None


def machine_ui(page: ft.Page):
    """Main UI function to assemble all components."""

    page.title = "Little Man Computer (LMC) Simulator"
    page.scroll = "adaptive"
    page.padding = 20
    page.theme_mode = "light"
    page.bgcolor = "#000000"

    sic = SICMachine(Memory(), Registers(), InstructionMapper())
    register_controls = {}
    memory_controls = {}

    memory_section = create_memory_section(sic, page, memory_controls)
    main_section = create_main_section(page, sic, register_controls, memory_controls)
    registers_section = create_registers_section(sic.registers, register_controls)

    row = ft.Row(
        [memory_section, main_section, registers_section],
        spacing=60,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    page.add(row)
    page.update()


# To run the app:
# ft.app(target=machine_ui)
