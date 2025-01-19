import dearpygui.dearpygui as dpg

class initial:
    def __init__(self):
        dpg.create_context()
        dpg.create_viewport(title=f"Node Editor - {dpg.get_dearpygui_version()}", width=1000, height=600)
        dpg.setup_dearpygui()

    def run(self):
        """Builds the UI and runs the Dear PyGui application."""
        # Add the menu bar
        with dpg.viewport_menu_bar(tag="menubar"):
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Exit", callback=lambda: dpg.stop_dearpygui())
            with dpg.menu(label="Tools"):
                dpg.add_menu_item(label="Show About", callback=lambda: dpg.show_tool(dpg.mvTool_About))
                dpg.add_menu_item(label="Show Metrics", callback=lambda: dpg.show_tool(dpg.mvTool_Metrics))
                dpg.add_menu_item(label="Show Documentation", callback=lambda: dpg.show_tool(dpg.mvTool_Doc))
                dpg.add_menu_item(label="Show Debug", callback=lambda: dpg.show_tool(dpg.mvTool_Debug))
                dpg.add_menu_item(label="Show Style Editor", callback=lambda: dpg.show_tool(dpg.mvTool_Style))
                dpg.add_menu_item(label="Show Font Manager", callback=lambda: dpg.show_tool(dpg.mvTool_Font))
                dpg.add_menu_item(label="Show Item Registry", callback=lambda: dpg.show_tool(dpg.mvTool_ItemRegistry))
        dpg.add_window(
            tag="main_window",
            no_scrollbar=True,
            no_title_bar=True,
            no_resize=True,
            no_move=True,
            pos=[0, dpg.get_item_height("menubar")]
        )
        dpg.set_primary_window("main_window",True)

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

if __name__ == '__main__':
    app = initial()
    app.run()

