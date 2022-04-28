sourcecode = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: homeScreen.text
            right_action_items: [["plus", lambda x: app.callback()], ["qrcode-scan", lambda x: qrscancode()]]
            elevation:5
            id: toolBar
            
        MDBottomNavigation:

            MDBottomNavigationItem:
                name: 'screen1'
                text: 'Home'
                icon: 'receipt'
                id: homeScreen
                on_tab_press: toolBar.title = homeScreen.text

                MDLabel
                    text: 'MONTHLY'
                    theme_text_color: "Primary"
                    font_style: 'H6'
                    pos_hint: { "x": .1, "y": .435}
                MDLabel
                    text: 'PROCEEDS'
                    theme_text_color: "Primary"
                    font_style: 'H6'
                    pos_hint: { "x": .1, "y": .4}
                MDLabel
                    id: monthlyProceeds
                    theme_text_color: "Secondary"
                    text: '1000'
                    font_style: 'H4'
                    pos_hint: { "x": .1, "y": .325}
                MDLabel
                    text: 'MONTHLY'
                    theme_text_color: "Primary"
                    font_style: 'H6'
                    pos_hint: { "x": .65, "y": .435}
                MDLabel
                    text: 'EXPENSES'
                    theme_text_color: "Primary"
                    font_style: 'H6'
                    pos_hint: { "x": .65, "y": .4}
                MDLabel
                    id: monthlyExpenses
                    text: '1000'
                    theme_text_color: "Secondary"
                    font_style: 'H4'
                    pos_hint: { "x": .65, "y": .325}
                
                MDFloatingActionButtonSpeedDial:
                    data: app.TransanctionSearchData
                    root_button_anim: True
                    icon: 'magnify-plus'

            MDBottomNavigationItem:
                name: 'screen2'
                text: 'Budgets'
                icon: 'calculator'
                id: budgetsScreen
                on_tab_press: toolBar.title = budgetsScreen.text
            
            MDBottomNavigationItem:
                name: 'screen3'
                text: 'Profile'
                icon: 'face-recognition'
                id: profileScreen
                on_tab_press: toolBar.title = profileScreen.text
                
                MDRectangleFlatButton:
                    text: "Security Settings"
                    disabled: True
                    disabled_color: 0, 0, 1, 1
                    pos_hint: {"center_x": 0.5, "center_y": 0.45}
                MDFlatButton:
                    text: "Change username-picture"
                    text_color: 0, 0, 1, 1
                    pos_hint: {"center_x": 0.5, "center_y": 0.365}
              
              MDFlatButton:
                    text: "Change password"
                    text_color: 0, 0, 1, 1
                    pos_hint: {"center_x": 0.5, "center_y": 0.3}
                MDFlatButton:
                    text: "Change fingerprint"
                    text_color: 0, 0, 1, 1
                    pos_hint: {"center_x": 0.5, "center_y": 0.235}
"""
