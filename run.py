import logging

import flet as ft

from tiny_tiny_computer.machine.gui import machine_ui

logging.basicConfig(level=logging.DEBUG)


def main():
    ft.app(target=machine_ui, host="0.0.0.0", port=5000, view=ft.WEB_BROWSER)


if __name__ == "__main__":
    main()
