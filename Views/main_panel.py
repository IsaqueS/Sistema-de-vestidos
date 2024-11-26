import flet as ft

class MainPanel:
    def __init__(self, page: ft.Page) -> None:
        self.__search_icon_size: int = 25

        self.__view: ft.View = ft.View(
            route="/"
        )

        self.current_page = page

        page.views.append(self.setup_view(self.__view))

        
    
    def setup_view(self, view: ft.View) -> ft.View:
        
        # Creating the Title Bar
        self.title: ft.Text = ft.Text(
            "Titulo",
            weight=ft.FontWeight.BOLD,
            overflow=ft.TextOverflow.ELLIPSIS,
            size=28
        )

        self.manual_button: ft.TextButton = ft.TextButton(
            icon=ft.icons.BOOK,
            text="Manual",
        )

        self.backup_button: ft.TextButton = ft.TextButton(
            icon=ft.icons.FOLDER_SHARED,
            text="Gerenciar Backups"
        )

        self.settings_button: ft.Icon = ft.Icon(
            name=ft.icons.MORE_VERT,
            tooltip="Configurações do aplicativo"
        )

        self.options_button:ft.PopupMenuButton = ft.PopupMenuButton(
            content = self.settings_button,
            items=[
                ft.PopupMenuItem(text= "Tela Cheia (F11)",icon=ft.icons.FULLSCREEN),
                ft.PopupMenuItem(text= "Sobre o aplicativo",icon=ft.icons.INFO),
                ft.PopupMenuItem(text= "Manual",icon=ft.icons.BOOK),
                ft.PopupMenuItem(text= "Configurações",icon=ft.icons.SETTINGS),
            ],
        )

        self.title_bar: ft.AppBar = ft.AppBar(
            title=self.title,
            center_title=True,
            actions=[
                self.manual_button,
                self.backup_button
            ],
            leading=self.options_button,
          
        )

        # Creating the Title Bar *END*

        # Creating Search Bar

        self.action_bar: ft.TextField = ft.TextField(
            label="Digite aqui para adicionar ou pesquisar...",
            border_radius=ft.border_radius.all(32)
        )

        self.add_button: ft.IconButton = ft.IconButton(
            icon=ft.icons.ADD,
            icon_size=self.__search_icon_size,
            tooltip="Adicionar no sistema"
        )
        
        self.search_button: ft.IconButton = ft.IconButton(
            icon=ft.icons.SEARCH,
            icon_size=self.__search_icon_size,
            tooltip="Procurar no sistema",
        )
        
        self.buttons_row: ft.ResponsiveRow = ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=self.search_button,
                    col={"sm": 1,"md": 1,"xl": 1},
                ),
                ft.Container(
                    content=self.add_button,
                    col={"sm": 1,"md": 1,"xl": 1},
                ),
                ],
            columns=2,
        )

        self.action_row: ft.ResponsiveRow = ft.ResponsiveRow(
            [ft.Container(
                #controls=[action_bar,],
                content=self.action_bar,
                col={"sm": 5,"md": 4,"xl": 4},
                
                ),
            ft.Container(
                #controls=[search_button,add_button],
                content= self.buttons_row,
                col={"sm": 1,"md": 1,"xl": 1},
                
                )
            ,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            columns=8,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            
        )

        # Creating Search Bar *END*

        # Creating Tabs

        self.categories_tab = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tab_alignment = ft.TabAlignment.CENTER,
            #adaptive=True,
            #scrollable=True,
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
                ft.Tab(
                    text="Analítica",
                    icon=ft.icons.DATA_THRESHOLDING_OUTLINED,
                    content=ft.Text("This is Tab 4"),
                ),
            ],
            expand=1,
        )

        view.controls.append(self.title_bar)
        view.controls.append(self.action_row)
        view.controls.append(self.categories_tab)

        return view
        

        