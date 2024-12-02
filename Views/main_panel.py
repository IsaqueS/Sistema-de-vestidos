import flet as ft
from Translations.translation_server import tr
from Views.view_template import ViewTemplate
from .MainPanelTabs.client_tab import ClientTab

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class MainPanel(ViewTemplate):
    def __init__(self, app: "App") -> None:
        super().__init__(app)
        
        self.__search_icon_size: int = 25

        self.view: ft.View = ft.View(
            route="/",
        )

        self.setup_view()

    # @property
    # def view(self) -> ft.View:
    #     return self.__view
        
    def change_to_full_screen(self, args: ft.ControlEvent) -> None:
        self.app.page.window.full_screen = not self.app.page.window.full_screen
        self.update_fullscreen_button()

        self.app.page.update()
    
    def update_fullscreen_button(self) -> None:
        if not self.app.page.window.full_screen:
            self.full_screen_item_button.icon = ft.Icons.FULLSCREEN
            self.full_screen_item_button.text = tr("fullscreen_button")
        else:
            self.full_screen_item_button.icon = ft.Icons.FULLSCREEN_EXIT
            self.full_screen_item_button.text = tr("exit_fullscreen_button")
    
    def open_more_options_menu_update(self, args: ft.ControlEvent) -> None:    
        self.update_fullscreen_button()
        self.app.page.update()



    def setup_view(self) -> ft.View:
        super().setup_view()

        # Creating the Title Bar
        self.title: ft.Text = ft.Text(
            tr("title"),
            weight=ft.FontWeight.BOLD,
            overflow=ft.TextOverflow.ELLIPSIS,
            size=self.app.title_size
        )

        self.manual_button: ft.TextButton = ft.TextButton(
            icon=ft.Icons.BOOK,
            text=tr("manual"),
            on_click = self.app.go_to_manual
        )

        self.backup_button: ft.TextButton = ft.TextButton(
            icon=ft.Icons.FOLDER_SHARED,
            text=tr("manage_backups")
        )

        self.settings_button: ft.Icon = ft.Icon(
            name=ft.Icons.MORE_VERT,
            tooltip=tr("more_options")
        )

        self.full_screen_item_button: ft.PopupMenuItem = ft.PopupMenuItem(
                    text= tr("fullscreen_button"),
                    icon=ft.Icons.FULLSCREEN,
                    on_click=self.change_to_full_screen
                )
        
        self.app_info_button: ft.PopupMenuItem = ft.PopupMenuItem(
            text= tr("app_info"),
            icon=ft.Icons.INFO,
            on_click= lambda x: print("Info Button was pressed, Functionalty needs to be done!"),
        )

        self.options_button:ft.PopupMenuButton = ft.PopupMenuButton(
            content = self.settings_button,
            items=[
                self.full_screen_item_button,
                self.app_info_button,
                ft.PopupMenuItem(text= tr("manual"),icon=ft.Icons.BOOK),
                ft.PopupMenuItem(text= tr("settings"),icon=ft.Icons.SETTINGS),
            ],
            on_open=self.open_more_options_menu_update,
            
            
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
            label=tr("search_bar_tip"),
            border_radius=ft.border_radius.all(32)
        )

        self.add_button: ft.IconButton = ft.IconButton(
            icon=ft.Icons.ADD,
            icon_size=self.__search_icon_size,
            tooltip=tr("add_button_tip")
        )
        
        self.search_button: ft.IconButton = ft.IconButton(
            icon=ft.Icons.SEARCH,
            icon_size=self.__search_icon_size,
            tooltip=tr("search_button_tip"),
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

        self.client_tab = ClientTab()


        self.categories_tab = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tab_alignment = ft.TabAlignment.CENTER,
            #adaptive=True,
            #scrollable=True,
            tabs=[
                self.client_tab.tab,
                ft.Tab(
                    text= tr("suppliers"),
                    icon=ft.Icons.BUSINESS_ROUNDED,
                    content=ft.Text("This is Tab 2!!!"),
                ),
                ft.Tab(
                    text=tr("stock"),
                    icon=ft.Icons.INBOX_OUTLINED,
                    content=ft.Text("This is Tab 3"),
                ),
                ft.Tab(
                    text=tr("rentals"),
                    icon=ft.Icons.CURRENCY_EXCHANGE_OUTLINED,
                    content=ft.Text("This is Tab 4"),
                ),
                ft.Tab(
                    text=tr("analytics"),
                    icon=ft.Icons.DATA_THRESHOLDING_OUTLINED,
                    content=ft.Text("This is Tab 4"),
                    
                ),
            ],
            expand=True,
        )

        self.gradient_container: ft.Container = ft.Container(
            content= self.action_row,
            # gradient=ft.LinearGradient(
            #     begin=ft.alignment.top_left,
            #     end=ft.Alignment(0.8, 1),
            #     colors=[
            #         "0xff1f005c",
            #         "0xff5b0060",
            #         "0xff870160",
            #         "0xffac255e",
            #         "0xffca485c",
            #         "0xffe16b5c",
            #         "0xfff39060",
            #         "0xffffb56b",
            #     ],
            #     tile_mode=ft.GradientTileMode.MIRROR,
            #     rotation=math.pi / 3,
            # ),
            margin=ft.Margin(left=-10,right=-10, top=0,bottom=0),

        )


        self.view.controls.append(self.title_bar)
        self.view.controls.append(self.gradient_container)
        self.view.controls.append(self.categories_tab)
        

        return self.view
        

        