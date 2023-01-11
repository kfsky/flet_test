import flet as ft
import time

def main(page):
    first_name = ft.TextField(label="First name")
    last_name = ft.TextField(label="Last name")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = "" # 初期値
        last_name.value = "" # 初期値
        page.update()
        first_name.forcus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say Hello!", on_click=btn_click),
        greetings
    )


ft.app(target=main)