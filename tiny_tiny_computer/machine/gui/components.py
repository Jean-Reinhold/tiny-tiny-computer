import flet as ft


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


def create_assembly_code_input():
    """Create the assembly code input text field with a sample callback."""
    return ft.TextField(
        multiline=True,
        value=(
            "START    INP        ; Input a number\n"
            "         STA FIRST   ; Store it in FIRST\n"
            "         INP         ; Input another number\n"
            "         STA SECOND  ; Store it in SECOND\n"
            "         LDA FIRST   ; Load FIRST into accumulator\n"
            "         ADD SECOND  ; Add SECOND to accumulator\n"
            "         OUT         ; Output the result\n"
            "         HLT         ; Halt the program\n"
            "FIRST    DAT 0       ; Memory location for FIRST\n"
            "SECOND   DAT 0       ; Memory location for SECOND\n"
        ),
        width=460,
        height=645,
        label="Assembly Code",
        text_style=ft.TextStyle(size=14),
        min_lines=40,
        max_lines=40,
        on_change=lambda e: print(
            f"Assembly code changed: {e.control.value}"
        ),  # You could place your callback here
    )


def create_output_display():
    """Create the output display with a sample callback."""
    return ft.Container(
        content=ft.Text("Output: [Placeholder]", size=14),
        padding=10,
        border=ft.border.all(1, "black"),
        border_radius=5,
        bgcolor="#f9f9f9",
        width=460,
        height=200,
    )


def create_cpu_section():
    """Create the CPU section with placeholders."""
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("CPU Registers", size=16, weight="bold"),
                ft.Text("Program Counter: 00", size=14),
                ft.Text("Instruction Register: 00", size=14),
                ft.Text("Accumulator: 000", size=14),
            ],
            spacing=10,
        ),
        padding=10,
        border=ft.border.all(1, "black"),
        border_radius=5,
        bgcolor="#f9f9f9",
        width=400,
    )


def create_ram_section():
    """Create the RAM section with a sample callback."""
    ram_cells = [
        ft.Container(
            content=ft.Text(f"{i:03}", color="white"),
            bgcolor="black",
            alignment=ft.alignment.center,
            width=50,
            height=50,
            border_radius=5,
            on_click=lambda e, cell=i: print(
                f"RAM Cell {cell} clicked!"
            ),  # You could place your callback here
        )
        for i in range(64)  # 8x8
    ]
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("RAM (Memory)", size=16, weight="bold"),
                ft.GridView(
                    expand=1,
                    runs_count=8,
                    max_extent=60,
                    spacing=5,
                    run_spacing=5,
                    controls=ram_cells,
                ),
            ]
        ),
        padding=10,
        border=ft.border.all(1, "black"),
        border_radius=5,
        bgcolor="#f9f9f9",
        width=400,
    )
