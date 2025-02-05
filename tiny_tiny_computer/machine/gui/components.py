import flet as ft

from tiny_tiny_computer.machine.gui.actions import *
from tiny_tiny_computer.machine.gui.popup import Popup
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers

popup = Popup()


def create_control_buttons(page: ft.Page, sic, register_controls, memory_controls):
    """Create the control buttons for the LMC Simulator with sample callbacks."""
    return ft.Column(
        [
            popup,
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
                visible=False,
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
                on_click=lambda _: step_execution(
                    sic, page, register_controls, memory_controls
                ),
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


def create_memory_section(sic: SICMachine, page: ft.Page, memory_controls: dict):
    name_section = ft.Text(
        "Memória",
        size=22,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
        color="#102F44",
    )

    memory_table = create_memory_table(sic, page, memory_controls)

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


def create_memory_table(sic: SICMachine, page: ft.Page, memory_controls: dict):
    memory_list = ft.ListView(spacing=10)

    for i in range(len(sic.memory.memory)):
        address_text = ft.Text(
            f"{i:02} ", weight="bold", width=25, size=16, color="#5AB6F3"
        )

        instruction_input = ft.TextField(
            value=sic.memory.load(i),
            width=80,
            height=40,
            content_padding=ft.padding.symmetric(vertical=0, horizontal=10),
            border_color="#C7D7E1",
            focused_border_color="#5AB6F3",
            focused_border_width=2,
            border_radius=5,
            keyboard_type=ft.KeyboardType.NUMBER,
            on_change=lambda e, addr=i: update_memory(e, sic, addr, page),
        )

        # Armazena a referência do TextField no dicionário de controles
        memory_controls[i] = instruction_input

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


def create_main_section(page: ft.Page, sic, register_controls, memory_controls):
    registers = sic.registers
    calculator = create_calculator(page, sic, register_controls, memory_controls)
    others_registers = create_others_registers(registers, register_controls)
    output_value = 0
    # output_container = create_output_container(output_value)

    main_section = ft.Column(
        [calculator, others_registers],
        spacing=60,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return main_section


def create_output_container(output_value: int):
    output_container = ft.Container(
        ft.Text(
            value=output_value,
            weight="bold",
            size=16,
            color="#FFFFFF",
            text_align=ft.TextAlign.CENTER,
        ),
        width=350,
        bgcolor="#18212C",
        border_radius=ft.border_radius.all(12),
        padding=16,
    )

    name = ft.Text(
        "Saída",
        size=22,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
        color="#101925",
    )

    return ft.Column([name, output_container])


def create_others_registers(registers: Registers, register_controls: dict):
    # Label e valor do registrador PC
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

    value_pc = ft.Text(
        str(registers.PC),  # Valor inicial de PC
        size=16,
        color="#000000",
        text_align=ft.TextAlign.CENTER,
    )
    value_pc_container = ft.Container(
        value_pc,
        padding=16,
        border_radius=ft.border_radius.only(0, 0, 8, 0),
        bgcolor="#D9D9D9",
        width=80,
    )

    # Registrar PC no dicionário de controles
    register_controls["PC"] = value_pc

    # Label e valor do registrador SW
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

    value_sw = ft.Text(
        str(registers.SW),  # Valor inicial de SW
        size=16,
        color="#000000",
        text_align=ft.TextAlign.CENTER,
    )
    value_sw_container = ft.Container(
        value_sw,
        padding=16,
        border_radius=ft.border_radius.only(0, 0, 0, 8),
        bgcolor="#D9D9D9",
        width=80,
    )

    # Registrar SW no dicionário de controles
    register_controls["SW"] = value_sw

    # Combinar os dois registradores
    others_registers = ft.Row(
        [
            ft.Column([label_pc, value_pc_container], spacing=0),
            ft.Column([label_sw, value_sw_container], spacing=0),
        ],
        spacing=0,
    )

    return others_registers


def create_calculator(page: ft.Page, sic, register_controls, memory_controls):
    buttons = create_control_buttons(page, sic, register_controls, memory_controls)
    accumulator = sic.registers.A

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

    register_controls["A"] = display

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


def create_registers_section(registers: Registers, registers_controls: dict):
    """Create a section to display the registers in a layout similar to the memory table."""
    registers_table = create_registers_table(registers, registers_controls)

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


def create_registers_table(registers: Registers, register_controls: dict):
    """Cria a tabela de registradores e inicializa o dicionário de controle para atualização."""
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
                registers[register_name],  # Valor inicial do registrador
                size=16,
                color="#000000",
                text_align="right",
            ),
            padding=16,
            border_radius=ft.border_radius.only(0, 8, 0, 8),
            bgcolor="#F88443",
            width=40,
        )

        # Armazena o Text do value_text no dicionário para futura atualização
        register_controls[register_name] = value_text.content

        row = ft.Row(
            [register_text, value_text],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0,
        )

        registers_list.controls.append(row)

    return registers_list
