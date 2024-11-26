import flet as ft
from flet import Text, Container, TextField, IconButton, Row

window_title = "Sistema de vestidos"
button_size = 20

def main(page: ft.Page) -> None:
    page.title = window_title
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    
    #Definindo Componentes da interface
    title: Text = Text(window_title, size=32, weight=ft.FontWeight.BOLD)
    title_container: Container = Container(
        content=title,
        alignment=ft.alignment.center
    )

    action_bar: TextField = TextField(label="Digite aqui para adicionar ou pesquisar...", width=500)
    add_button: IconButton = IconButton(icon=ft.icons.ADD, icon_size=button_size,tooltip="Adicionar no sistema")
    search_button: IconButton = IconButton(icon=ft.icons.SEARCH, icon_size=button_size,tooltip="Procurar no sistema")
    
    action_row: Row = Row(controls=[action_bar,search_button,add_button],alignment=ft.MainAxisAlignment.CENTER)
    

    categories_tab = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tab_alignment = ft.TabAlignment.CENTER,
        tabs=[
            ft.Tab(
                text="Clientes",
                icon=ft.icons.PERSON,
                content=ft.Container(
                    content=ft.DataTable( columns=[ ft.DataColumn(ft.Text("Name")), ft.DataColumn(ft.Text("Age")), ], rows=[ ft.DataRow( cells=[ ft.DataCell(ft.Text("Alice")), ft.DataCell(ft.Text("25")), ] ), ft.DataRow( cells=[ ft.DataCell(ft.Text("Bob")), ft.DataCell(ft.Text("30")), ] ), ] ), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text= "Fornecedores",
                icon=ft.icons.BUSINESS_ROUNDED,
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Stock de vestidos",
                icon=ft.icons.INBOX_OUTLINED,
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                text="Alugueis",
                icon=ft.icons.SHOPPING_CART,
                content=ft.Text("This is Tab 4"),
            ),
        ],
        expand=1,
    )


    page.add(title_container)
    page.add(action_row)
    page.add(categories_tab)

if __name__ == "__main__":
    ft.app(main)