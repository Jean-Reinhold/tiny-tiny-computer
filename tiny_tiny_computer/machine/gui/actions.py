import flet as ft

from tiny_tiny_computer.machine.memory import Memory


def update_memory(e: ft.ControlEvent, mem: Memory, address: int, page: ft.Page):
    """Update memory when user edit one field."""

    new_value = e.control.value.upper()

    mem.store(address, new_value)

    page.update()


def open_popup(page, popup):
    popup.overlay.visible = True
    page.update()


def close_popup(page, popup, valor):
    print(f"Valor digitado: {valor}")
    popup.overlay.visible = False
    page.update()
