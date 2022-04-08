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
                name: 'screen 1'
                text: 'Home'
                icon: "home-outline"
                id: homeScreen
                on_tab_press: toolBar.title = homeScreen.text
    
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Transactions'
                icon: 'receipt-outline'
                id: transactionsScreen
                on_tab_press: toolBar.title = transactionsScreen.text
    
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Budgets'
                icon: 'calculator'
                id: budgetsScreen
                on_tab_press: toolBar.title = budgetsScreen.text
            
            MDBottomNavigationItem:
                name: 'screen4'
                text: 'Profile'
                icon: 'face-man-outline'
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
