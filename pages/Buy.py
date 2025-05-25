import flet as ft
class Verif:
    storage = None
def details_page(page: ft.Page, product):
    
    def go_back(e):
        page.go("/storage")
    
    def buy(e):
        pass

    return ft.Column(
        [
            ft.Image(src=product["image"], width=640, height=300),
            ft.Text(product["name"], size=24, weight="bold"),
            ft.Row(
                [
                    ft.ElevatedButton("Купить", on_click=buy),  
                    ft.Text(f"Price: {product['price']} ₽", size=18),  
                    ft.ElevatedButton("Go back", on_click=go_back),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text(product["description"], size=14),
        ],
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        scroll=ft.ScrollMode.ALWAYS
    )
