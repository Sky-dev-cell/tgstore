import flet as ft
from pages.storage import sm

def details_page(page: ft.Page, product):
    success_alert = ft.AlertDialog(
        title=ft.Text("Success"),
        content=ft.Text("product Added to Cart"),
        alignment=ft.alignment.center,
        actions=[
            ft.TextButton("close", on_click=lambda e: page.close(success_alert))
        ],
    ) 
    def go_back(e):
        page.go("/products")

    def buy(e, product):
        sm.cart = product
        page.open(success_alert)

    return ft.Column(
        [
            ft.Image(src=product["image"], width=640, height=300),
            ft.Text(product["name"], size=24, weight="bold"),
            ft.Row(
                [
                    ft.ElevatedButton("Купить", on_click=lambda e, product=product: buy(e,product)),  
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
