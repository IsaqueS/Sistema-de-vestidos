import flet as ft
from flet import Text, Container, TextField, IconButton, Row, ResponsiveRow, AppBar, TextButton

window_title = "Vestidos Essencia"
button_size = 20

def main(page: ft.Page) -> None:
    
    page.title = window_title
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode=ft.ThemeMode.DARK
    page.window.min_width = 600
    page.window.min_height = 500
    #fletpage.window.full_screen = True
    
    #Definindo Componentes da interface
    title: AppBar = AppBar(
        title=Text(window_title, weight=ft.FontWeight.BOLD,overflow=ft.TextOverflow.ELLIPSIS, size=28,),
        center_title=True,
        actions=[TextButton(
            icon=ft.icons.BOOK,
            text="Manual",
        ),
        TextButton(
            icon=ft.icons.FOLDER_SHARED,
            text="Gerenciar Backups"
        )
        ],
        leading=IconButton(icon=ft.icons.SETTINGS_ROUNDED, tooltip="Configurações do aplicativo"),
        #title_spacing=5.0
        
    )

    action_bar: TextField = TextField(
        label="Digite aqui para adicionar ou pesquisar...",
        border_radius=ft.border_radius.all(32)
        
    )
    
    

    add_button: IconButton = IconButton(icon=ft.icons.ADD, icon_size=button_size,tooltip="Adicionar no sistema", )
    search_button: IconButton = IconButton(icon=ft.icons.SEARCH, icon_size=button_size,tooltip="Procurar no sistema", )
    buttons_row: Row = Row(controls=[search_button,add_button])
    
    action_row: ResponsiveRow = ResponsiveRow(
        [Container(
            #controls=[action_bar,],
            content=action_bar,
            col={"sm": 5,"md": 4,"xl": 4},
            
            ),
        Container(
            #controls=[search_button,add_button],
            content= buttons_row,
            col={"sm": 1,"md": 1,"xl": 1},
            
            )
        ,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        columns=8,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        
    )
    

    categories_tab = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tab_alignment = ft.TabAlignment.CENTER,
        tabs=[
            ft.Tab(
                text="Clientes",
                icon=ft.icons.PEOPLE,
                content=ft.Container(
                    content=ft.DataTable( columns=[ ft.DataColumn(ft.Text("Name")), ft.DataColumn(ft.Text("Age")), ], rows=[ ft.DataRow( cells=[ ft.DataCell(ft.Text("Alice")), ft.DataCell(ft.Text("25")), ] ), ft.DataRow( cells=[ ft.DataCell(ft.Text("Bob")), ft.DataCell(ft.Text("30")), ] ), ] ), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text= "Fornecedores",
                icon=ft.icons.BUSINESS_ROUNDED,
                content=ft.Text("This is Tab 2!!!"),
            ),
            ft.Tab(
                text="Stock de vestidos",
                icon=ft.icons.INBOX_OUTLINED,
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                text="Alugueis",
                icon=ft.icons.CURRENCY_EXCHANGE_OUTLINED,
                content=ft.Text("This is Tab 4"),
            ),
        ],
        expand=1,
    )


    page.add(title)
    page.add(action_row)
    page.add(categories_tab)

if __name__ == "__main__":
    ft.app(main)