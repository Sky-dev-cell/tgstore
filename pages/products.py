import flet as ft
from storage import sm

def product_page(page: ft.Page):
    def see_more(e, product):
        sm.current_product = product
        page.go("/details")

    products = [
            {"Category": "Gamepass", "name": "Criminality, BoomBox Gamepass", "description":" Make your day with music", "price": 130, "image": "https://www.google.com/search?sca_esv=8f02ab89f9e48a59&sxsrf=AHTn8zo3mMzN-CxyxeWlbwbC1Gn1qYnA7g:1745156232550&q=boombox+roblox&udm=2&fbs=ABzOT_CQmnVa6uw0NyNnWWoC7jZB2NtLn_3mYTWEZJidaMPoLR4sWngjUAZeoIpuv9MiRxTnY3vDU5x6mCMlKGq0gC2sWSlYAEUy4dZCMoYcanSp2c38ocH4qyXOYTf6kdaGHUgfLg9HN8rDHhL9qwYTafYxIX57EPaGQ8lQNcYp2bZ4JUQeFrf3UkfTxXmw43tqwiX3gUNsbzCJbabhuhq1tqCN_cIdPza47v_x--Ft2w0NwoAmfBZH8E85X9cI5q8u21Cg9DEslVCccg8rM-F6aT8-mSJdFA&sa=X&ved=2ahUKEwjcicbK3eaMAxWFEBAIHfFVA8oQtKgLegQIExAB&biw=1280&bih=593&dpr=1.5#vhid=kh89L1XSbY6WbM&vssid=mosaic"},
            {"Category": "Subscribe", "name": "Discord Nitro", "description":"Special Nitro for Extra price", "price": 455, "image": "https://www.google.com/search?sca_esv=8f02ab89f9e48a59&sxsrf=AHTn8zotDsjlGoSaRzVAsLXQ-DJ7KGpJ_w:1745156457139&q=%D0%B4%D0%B8%D1%81%D0%BA%D0%BE%D1%80%D0%B4+%D0%BD%D0%B8%D1%82%D1%80%D0%BE+%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE+%D1%81%D1%82%D0%BE%D0%B8%D1%82&udm=2&fbs=ABzOT_D2k6MNEmHCczqZM6bKks6bouq3sYx8xTOo-uO2nwKVnAZCSISYNV69r3NE8TOeuZbavZ94sekV5kNFBBf7hnyXbDJqiF_UCkj5ZDZ60xnJ3ixYnW1Q8y4Zv5lUrbl7StNavjo4GRKkuX3NwkZEqeE-SvcvIWFGuqpgSwZ5xw08oKKHmAx-ZZMigguymy2HJ0-RgtVb5Mo9N6eJBjBD9x0i45x33FaaIsmOqu1vAWsWvw_Wj2N3h-mvBB9v8IuQLfcRbFSSQeTuL0cN2r1MtlWOJT2cHA&sa=X&ved=2ahUKEwij-dG13uaMAxXnFhAIHf6EB5oQtKgLegQIEhAB&biw=1280&bih=593&dpr=1.5#vhid=joeY38A4Jofx5M&vssid=mosaic"},
            {"Category": "Subscribe", "name": "Подписка на Яндекс музыку", "description":"Слушай музыку бесплатно целый месяц", "price": 289, "image": "https://www.google.com/search?q=%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+%D0%BC%D1%83%D0%B7%D1%8B%D0%BA%D0%B0&sca_esv=d3e47f5c41dad28e&udm=2&biw=1280&bih=593&sxsrf=AHTn8zoOAI4QlC4UTrZKTdHqi75tNynliQ%3A1745156751532&ei=j_oEaOSYIMqtwPAPuPzHoA0&ved=0ahUKEwiknILC3-aMAxXKFhAIHTj-EdQQ4dUDCBE&uact=5&oq=%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+%D0%BC%D1%83%D0%B7%D1%8B%D0%BA%D0%B0&gs_lp=EgNpbWciGdCv0L3QtNC10LrRgSDQvNGD0LfRi9C60LAyCxAAGIAEGLEDGIMBMg0QABiABBixAxhDGIoFMggQABiABBixAzIIEAAYgAQYsQMyCBAAGIAEGLEDMgsQABiABBixAxiDATIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEAAYgARI_RFQAFitEHAAeACQAQCYAT2gAYoFqgECMTO4AQPIAQD4AQGYAg2gAtcFwgIHECMYJxjJAsICEBAAGIAEGLEDGEMYgwEYigXCAgoQABiABBhDGIoFmAMAkgcCMTOgB-1gsgcCMTO4B9cF&sclient=img#vhid=YOHSsra8qy-uwM&vssid=mosaic"},
            {"Category": "Gamepass", "name": "Criminality, Extra Income", "description":"incoming cash will be x2 more", "price": 249, "image": "https://www.google.com/search?q=Extra+income+criminality&sca_esv=8f02ab89f9e48a59&udm=2&biw=1280&bih=593&sxsrf=AHTn8zqS-rGfcqOMveHGzrB1oBEBRcn_ag%3A1745156234754&ei=ivgEaITqLbmnwPAP4sPP0A8&ved=0ahUKEwiE18zL3eaMAxW5ExAIHeLhE_oQ4dUDCBE&uact=5&oq=Extra+income+criminality&gs_lp=EgNpbWciGEV4dHJhIGluY29tZSBjcmltaW5hbGl0eTIFEAAYgARI_TRQhgVY8zJwAngAkAEBmAFVoAHtDqoBAjM3uAEDyAEA-AEBmAIboALiCqgCCsICBxAjGCcYyQLCAgYQABgHGB7CAggQABgHGAoYHsICChAAGIAEGEMYigXCAgoQIxgnGMkCGOoCwgIIEAAYgAQYsQPCAg4QABiABBixAxiDARiKBcICDBAAGIAEGEMYigUYCsICCxAAGIAEGLEDGIMBwgIQEAAYgAQYsQMYQxiDARiKBcICBBAAGB7CAgYQABgFGB7CAgYQABgIGB6YAwmIBgGSBwIyN6AHz6gBsgcCMjW4B8wK&sclient=img#vhid=54fwgb7kCRGh8M&vssid=mosaic"}
        
        ]   
    products_cards = []
    for product in products:
        card = ft.Card(
            content=ft.Column(
                [
                    ft.Image(src=product["image"], width=320, height=150),
                    ft.Text(product["name"], size=16, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            ft.Text(f"{product["price"]} ₽", size=18),
                            ft.ElevatedButton("See more", on_click=lambda e, product: see_more(e, product))
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            width=320,
            height=250,
        )
        products_cards.append(card)

    return ft.GridView(
        controls=products_cards,
        expand=1,
        runs_count=5,
        max_extent=320,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )