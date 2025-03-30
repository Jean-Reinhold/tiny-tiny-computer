import flet as ft

from tiny_tiny_computer.machine.gui import memory_controls, register_controls, sic
from tiny_tiny_computer.machine.gui.actions import (
    reset_execution,
    run_execution,
    step_execution,
    update_memory,
    update_memory_controls,
    update_registers_controls,
)
from tiny_tiny_computer.machine.gui.popup import Popup
from tiny_tiny_computer.machine.registers import Registers
from tiny_tiny_computer.machine.sic import (
    SICMachine,
    load_obj_file,
    macro_process_file,
    two_pass_assemble,
)


def process_file(path: str, destination: str, page: ft.Page):
    global output_text_control

    if destination == "assembler":
        success = two_pass_assemble(path)

        if success:
            lst_path = path.split(".")[0] + ".lst"
            with open(lst_path) as f:
                output = f.read()

            output_text_control.value = output
            page.update()

        else:
            print("Erro ao processar o arquivo: ${path}")

    elif destination == "macro":
        path_asm = macro_process_file(path)
        print("---------- Start no processamento da MACRO ----------")

        if path_asm:
            output_text_control.value = f"Sucesso\nArquivo processado em {path_asm}"
            page.update()
        else:
            print("Erro ao processar a macro")

    elif destination == "load":
        program, pc = load_obj_file("sample_flatenned.obj")

        print("Loaded program:")
        for i, instruction in enumerate(program):
            print(f"{i}: {instruction}")

        sic.load_program(program, 0)
        sic.registers.PC = pc

        update_memory_controls(sic.memory, memory_controls, page)
        update_registers_controls(sic.registers, register_controls, page)
        # page.update()


popup = Popup(on_confirm=process_file)


def create_control_buttons(page: ft.Page, sic, register_controls, memory_controls):
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
                on_click=lambda _: run_execution(
                    sic, page, register_controls, memory_controls
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
                on_click=lambda _: reset_execution(
                    page, sic, register_controls, memory_controls
                ),
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
        color="#FFFFFF",
    )

    memory_table = create_memory_table(sic, page, memory_controls)

    labels = ft.Row(
        [
            ft.Text("Endereço", size=16, weight=ft.FontWeight.W_600, color="#FFFFFF"),
            ft.Text("Valor", size=16, weight=ft.FontWeight.W_600, color="#FFFFFF"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    memory_section = ft.Column(
        [name_section, labels, memory_table],
        width=350,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return memory_section


def create_memory_table(sic: SICMachine, page: ft.Page, memory_controls: dict):
    memory_list = ft.ListView(spacing=10)

    for i in range(len(sic.memory.memory)):
        address_text = ft.Text(
            f"{i:02} ", weight="bold", width=25, size=16, color="#FFFFFF"
        )

        instruction_input = ft.TextField(
            value=sic.memory.load(i),
            width=80,
            height=40,
            content_padding=ft.padding.symmetric(vertical=0, horizontal=10),
            border_color="#2E303B",
            focused_border_color="#F88443",
            focused_border_width=2,
            border_radius=5,
            color="#FFFFFF",
            keyboard_type=ft.KeyboardType.NUMBER,
            on_change=lambda e, addr=i: update_memory(e, sic, addr, page),
        )

        # Armazena a referência do TextField no dicionário de controles
        memory_controls[i] = instruction_input

        row = ft.Row(
            [address_text, instruction_input],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            width=350,
        )

        container = ft.Container(
            content=row,
            padding=10,
            border=ft.border.all(1, "#282A36"),
            border_radius=5,
            bgcolor="#282A36",
            height=55,
            width=350,
        )

        memory_list.controls.append(container)

    return memory_list


def create_main_section(page: ft.Page, sic, register_controls, memory_controls):
    registers = sic.registers
    calculator = create_calculator(page, sic, register_controls, memory_controls)
    others_registers = create_others_registers(registers, register_controls)

    main_section = ft.Column(
        [others_registers, calculator],
        spacing=60,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return main_section


def create_macro_section(page: ft.Page):
    output_container = create_output_container()

    buttons = create_buttons_modal(page)

    return ft.Column(
        [buttons, output_container, popup],
        spacing=60,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=350,
    )


def create_buttons_modal(page: ft.Page):
    assembler_button = ft.Container(
        content=ft.Text(
            "Assembler Process",
            size=14,
            weight=ft.FontWeight.W_600,
            color="#FFFFFF",
            text_align=ft.TextAlign.CENTER,
        ),
        width=350,
        on_click=lambda _: popup.open(destination="assembler", page=page),
        padding=ft.padding.symmetric(vertical=10, horizontal=16),
        bgcolor="#F88443",
        border_radius=20,
    )

    macro_button = ft.Container(
        content=ft.Text(
            "Macro Process",
            size=14,
            weight=ft.FontWeight.W_600,
            color="#FFFFFF",
            text_align=ft.TextAlign.CENTER,
        ),
        width=350,
        on_click=lambda _: popup.open(destination="macro", page=page),
        padding=ft.padding.symmetric(vertical=10, horizontal=16),
        bgcolor="#F88443",
        border_radius=20,
    )

    load_button = ft.Container(
        content=ft.Text(
            "Load Object File",
            size=14,
            weight=ft.FontWeight.W_600,
            color="#FFFFFF",
            text_align=ft.TextAlign.CENTER,
        ),
        width=350,
        on_click=lambda _: popup.open(destination="load", page=page),
        padding=ft.padding.symmetric(vertical=10, horizontal=16),
        bgcolor="#F88443",
        border_radius=20,
    )

    return ft.Column([macro_button, assembler_button, load_button], spacing=20)


output_text_control = ft.Text(
    value="",
    weight="bold",
    size=16,
    color="#FFFFFF",
    text_align=ft.TextAlign.LEFT,
)


def create_output_container():
    global output_text_control

    output_container = ft.Container(
        content=output_text_control,
        width=350,
        bgcolor="#282A36",
        border_radius=ft.border_radius.all(12),
        padding=16,
    )

    label = ft.Text(
        "Saída",
        size=22,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
        color="#FFFFFF",
    )

    return ft.Column(
        [label, output_container],
    )


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
        bgcolor="#282A36",
        width=175,
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
        width=175,
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
        bgcolor="#282A36",
        width=175,
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
        width=175,
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
    accumulator = str(sic.registers.A)

    display = ft.TextField(
        value=accumulator,
        text_align=ft.TextAlign.RIGHT,
        read_only=True,
        border=ft.InputBorder.NONE,
        bgcolor="#2E303B",
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
        bgcolor="#282A36",
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
        color="#FFFFFF",
    )

    registers_section = ft.Column(
        [name_section, registers_table],
        width=166,
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
            bgcolor="#282A36",
            width=83,
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
            width=83,
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
