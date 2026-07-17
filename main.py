import flet as ft
import time

def main(page: ft.Page):
    page.title = "مهتز"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def vibrate(e):
        try:
            count = int(number_field.value)
            for i in range(count):
                page.haptic_feedback()
                time.sleep(0.6)
            page.snack_bar = ft.SnackBar(ft.Text(f"تم {count} هزات ✅"))
            page.snack_bar.open = True
            page.update()
        except:
            page.snack_bar = ft.SnackBar(ft.Text("اكتب رقم صحيح"))
            page.snack_bar.open = True
            page.update()

    number_field = ft.TextField(label="اكتب عدد الهزات", width=200, keyboard_type=ft.KeyboardType.NUMBER)
    
    page.add(
        ft.Text("تطبيق الهزاز 😂", size=25),
        number_field,
        ft.ElevatedButton("اهتز", on_click=vibrate, bgcolor="red", color="white")
    )

ft.app(target=main)
