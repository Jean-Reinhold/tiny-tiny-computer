import flet as ft


class Popup(ft.Container):
    def __init__(self):
        super().__init__()

        self.visible = False
        self.text_field = ft.TextField(
            label="Digite a entrada",
            focused_border_color="#F88443",
            focused_color="#F88443",
        )

        self.content = ft.Column(
            [
                self.text_field,
                ft.Row(
                    [
                        ft.ElevatedButton(
                            content=ft.Text(
                                "Confirmar",
                                size=14,
                                weight=ft.FontWeight.W_500,
                                color="#101925",
                                text_align=ft.TextAlign.CENTER,
                            ),
                            bgcolor="#F88443",
                            on_click=self.confirm,
                        ),
                        ft.ElevatedButton(
                            content=ft.Text(
                                "Fechar",
                                size=14,
                                weight=ft.FontWeight.W_500,
                                color="#101925",
                                text_align=ft.TextAlign.CENTER,
                            ),
                            bgcolor="#D9D9D9",
                            on_click=self.close,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        self.alignment = ft.alignment.center
        self.padding = 20
        self.bgcolor = ft.colors.WHITE
        self.border_radius = 10
        self.width = 300

    def open(self, e=None):
        self.visible = True
        self.update()

    def close(self, e=None):
        self.visible = False
        self.update()

    def confirm(self, e=None):
        print(f"Usuário digitou: {self.text_field.value}")
        self.close()
