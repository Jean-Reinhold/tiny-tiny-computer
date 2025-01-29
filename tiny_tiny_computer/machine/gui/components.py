import flet as ft

from tiny_tiny_computer.machine.gui.actions import *
from tiny_tiny_computer.machine.memory import Memory


def create_control_buttons():
    """Create the control buttons for the LMC Simulator with sample callbacks."""
    return ft.Row(
        [
            ft.ElevatedButton(
                "Assemble",
                width=120,
                on_click=lambda e: print(
                    "Assemble button clicked!"
                ),  # You could place your callback here
            ),
            ft.ElevatedButton(
                "Run",
                width=100,
                on_click=lambda e: print(
                    "Run button clicked!"
                ),  # You could place your callback here
            ),
            ft.ElevatedButton(
                "Step",
                width=100,
                on_click=lambda e: print(
                    "Step button clicked!"
                ),  # You could place your callback here
            ),
            ft.ElevatedButton(
                "Reset",
                width=100,
                on_click=lambda e: print(
                    "Reset button clicked!"
                ),  # You could place your callback here
            ),
        ],
        spacing=10,
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
            border_color="#1F5E87",
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
