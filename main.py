import flet as ft
from pages.login import auth_page
from pages.products import product_page
from pages.Details import details_page
from pages.Cart import cart_page
from pages.storage import StateManager


def main(page:ft.Page):
    page.title = 'Store'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 320
    page.window.min_width = 320

    def set_page(e):
        ind = e.control.selected_index
        if ind == 0:
            page.go("/home")
        elif ind == 1:
            page.go("/cart")
        elif ind ==2:
            page.go("/home")


    menu = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.Home_OUTLINED, label="Home"),
            ft.NavigationBarDestination(icon=ft.icons.SHOPPING_CART_OUTLINED, label="Cart"),
            ft.NavigationBarDestination(icon=ft.icons.LOGOUT, label="Logout"),
        ],
        on_change=lambda e: set_page(e)
    )


    def route_change(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(
                ft.View(
                    '/',
                    [product_page(page), menu],
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        elif page.route == "/details":
            page.views.append(
                ft.View(
                    "/details",
                    [product_page(page, sm.current_product), menu],
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        elif page.route == "/cart":
            page.views.append(
                ft.View(
                    "/cart",
                    [cart_page(page)],
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go('/storage')

if __name__ == '__main__':
    ft.app(target=main)