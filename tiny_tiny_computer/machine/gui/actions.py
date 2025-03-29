import flet as ft

from tiny_tiny_computer.machine.registers import Registers
from tiny_tiny_computer.machine.sic import SICMachine, two_pass_assemble

output = []


def update_memory(e: ft.ControlEvent, sic: SICMachine, address: int, page: ft.Page):
    """Update memory when user edit one field."""

    value = e.control.value.upper()
    sic.memory.store(address, value)

    page.update()


def step_execution(
    sic: SICMachine, page: ft.Page, register_controls: dict, memory_controls: dict
):
    """Executes a single step of the SICMachine and updates the UI."""

    try:
        pc: int = sic.registers.PC
        memory_line: str = sic.memory.load(pc)

        if memory_line == "000000":  # HALT instruction
            page.snack_bar = ft.SnackBar(
                ft.Text("A simulação terminou (INSTRUÇÃO HALT)!"), open=True
            )
        else:
            sic.step()
            page.snack_bar = ft.SnackBar(
                ft.Text("Step executed successfully!"), open=True
            )
    except Exception as e:
        page.snack_bar = ft.SnackBar(
            ft.Text(f"Error during step execution: {e}"), open=True
        )

    update_registers_controls(sic.registers, register_controls, page)
    update_memory_controls(sic.memory, memory_controls, page)


def update_registers_controls(
    registers: Registers, register_controls: dict, page: ft.Page
):
    for reg_name, text_component in register_controls.items():
        text_component.value = registers[reg_name]

    page.update()


def update_memory_controls(memory, memory_controls: dict, page: ft.Page):
    for address, control in memory_controls.items():
        control.value = memory.load(address)

    page.update()


def reset_execution(
    page: ft.Page, sic: SICMachine, register_controls: dict, memory_controls: dict
):
    sic.reset()

    update_registers_controls(sic.registers, register_controls, page)

    update_memory_controls(sic.memory, memory_controls, page)

    page.update()


def process_file(path: str, destination: str, page: ft.Page):
    global output

    if destination == "assembler":
        sucess = two_pass_assemble(path)

        if sucess:
            lst_path = path.split(".")[0] + ".lst"
            with open(lst_path) as f:
                output = f.read()

            print(output)
            page.controls[4].content.value = output
            page.update()

        else:
            print("Erro ao processar o arquivo: ${path}")
