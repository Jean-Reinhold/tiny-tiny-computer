import flet as ft

from tiny_tiny_computer.machine.gui.actions import *
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def create_control_buttons():
    """Create the control buttons for the LMC Simulator with sample callbacks."""
    return ft.Column(
        [
            ft.Container(
                content=ft.Text(
                    "Run",
                    size=14,
                    weight=ft.FontWeight.W_600,
                    color="#FFFFFF",
                    text_align=ft.TextAlign.CENTER,
                ),
                width=318,
                padding=ft.padding.symmetric(vertical=10, horizontal=16),
                bgcolor="#F88443",
                border_radius=20,
            ),
            ft.Container(
                content=ft.Text(
                    "Step",
                    size=14,
                    weight=ft.FontWeight.W_600,
                    color="#FFFFFF",
                    text_align=ft.TextAlign.CENTER,
                ),
                width=318,
                padding=ft.padding.symmetric(vertical=10, horizontal=16),
                bgcolor="#F88443",
                border_radius=20,
            ),
            ft.Container(
                content=ft.Text(
                    "Reset",
                    size=14,
                    weight=ft.FontWeight.W_600,
                    color="#FFFFFF",
                    text_align=ft.TextAlign.CENTER,
                ),
                width=318,
                padding=ft.padding.symmetric(vertical=10, horizontal=16),
                bgcolor="#D9D9D9",
                border_radius=20,
            ),
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


def create_memory_section(mem: Memory, page: ft.Page):
    name_section = ft.Text(
        "Memória",
        size=22,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
        color="#102F44",
    )

    memory_table = create_memory_table(mem, page)

    labels = ft.Row(
        [
            ft.Text("Endereço", size=16, weight=ft.FontWeight.W_600, color="#102F44"),
            ft.Text("Valor", size=16, weight=ft.FontWeight.W_600, color="#102F44"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    memory_section = ft.Column(
        [name_section, labels, memory_table],
        width=200,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return memory_section


def create_memory_table(mem: Memory, page: ft.Page):
    memory_list = ft.ListView(spacing=10)

    for i in range(len(mem.memory)):
        address_text = ft.Text(
            f"{i:02} ", weight="bold", width=25, size=16, color="#5AB6F3"
        )

        instruction_input = ft.TextField(
            value=mem.load(i),
            width=80,
            height=40,
            content_padding=ft.padding.symmetric(vertical=0, horizontal=10),
            border_color="#C7D7E1",
            focused_border_color="#5AB6F3",
            focused_border_width=2,
            border_radius=5,
            keyboard_type=ft.KeyboardType.NUMBER,
            on_change=lambda e, addr=1: update_memory(e, mem, addr, page),
        )

        row = ft.Row(
            [address_text, instruction_input],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        container = ft.Container(
            content=row,
            padding=10,
            border=ft.border.all(1, "#C7D7E1"),
            border_radius=5,
            bgcolor="lightgray",
            height=55,
        )

        memory_list.controls.append(container)

    return memory_list


def create_main_section(page: ft.Page, registers: Registers):
    accumulator = registers.A
    calculator = create_calculator(accumulator)
    others_registers = create_others_registers(registers)

    main_section = ft.Column(
        [calculator, others_registers],
        spacing=60,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return main_section


def create_others_registers(registers: Registers):
    label_pc = ft.Container(
        ft.Text(
            "PC",
            weight="bold",
            size=16,
            color="#FFFFFF",
            text_align=ft.TextAlign.CENTER,
        ),
        padding=16,
        border_radius=ft.border_radius.only(8, 0, 0, 0),
        bgcolor="#18212C",
        width=80,
    )

    pc = registers.PC
    value_pc = ft.Container(
        ft.Text(pc, size=16, color="#000000", text_align=ft.TextAlign.CENTER),
        padding=16,
        border_radius=ft.border_radius.only(0, 0, 8, 0),
        bgcolor="#D9D9D9",
        width=80,
    )

    register_pc = ft.Column([label_pc, value_pc], spacing=0)

    label_sw = ft.Container(
        ft.Text(
            "SW",
            weight="bold",
            size=16,
            color="#FFFFFF",
            text_align=ft.TextAlign.CENTER,
        ),
        padding=16,
        border_radius=ft.border_radius.only(0, 8, 0, 0),
        bgcolor="#18212C",
        width=80,
    )

    sw = registers.SW
    value_sw = ft.Container(
        ft.Text(sw, size=16, color="#000000", text_align=ft.TextAlign.CENTER),
        padding=16,
        border_radius=ft.border_radius.only(0, 0, 0, 8),
        bgcolor="#D9D9D9",
        width=80,
    )

    register_sw = ft.Column([label_sw, value_sw], spacing=0)

    others_registers = ft.Row([register_pc, register_sw], spacing=0)

    return others_registers


def create_calculator(accumulator: int):
    buttons = create_control_buttons()

    display = ft.TextField(
        value=accumulator,
        text_align=ft.TextAlign.RIGHT,
        read_only=True,
        border=ft.InputBorder.NONE,
        bgcolor="#18212C",
        color="#FFFFFF",
        text_size=32,
        width=300,
        height=80,
    )

    calculator = ft.Container(
        content=ft.Column(
            [display, buttons],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor="#101925",
        border_radius=10,
        width=350,
    )

    return calculator


def create_registers_section(registers: Registers):
    """Create a section to display the registers in a layout similar to the memory table."""
    registers_table = create_registers_table(registers)

    name_section = ft.Text(
        "Registradores",
        size=22,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
        color="#101925",
    )

    registers_section = ft.Column(
        [name_section, registers_table],
        width=200,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return registers_section


def create_registers_table(registers: Registers):
    registers_list = ft.ListView(spacing=10, width=200)

    for code in range(1, 7):
        register_name = registers.register_from_code(code)
        register_text = ft.Container(
            ft.Text(
                register_name,
                weight="bold",
                size=16,
                color="#FFFFFF",
            ),
            padding=16,
            border_radius=ft.border_radius.only(8, 0, 8, 0),
            bgcolor="#18212C",
            width=40,
        )

        value_text = ft.Container(
            ft.Text(
                registers[register_name],
                size=16,
                color="#000000",
                text_align="right",
            ),
            padding=16,
            border_radius=ft.border_radius.only(0, 8, 0, 8),
            bgcolor="#F88443",
            width=40,
        )

        # Row to hold the register name and value
        row = ft.Row(
            [register_text, value_text],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0,
        )

        # Add the container to the list
        registers_list.controls.append(row)

    return registers_list
