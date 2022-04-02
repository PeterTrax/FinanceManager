screens = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

MDScreen:
    
    MDBottomNavigation:
        panel_color: get_color_from_hex("#eeeaea")
        selected_color_background: get_color_from_hex("#97ecf8")
        text_color_active: 0, 0, 0, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: "icons/home.png"

            MDLabel:
                text: 'Home coming soon...'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Transactions'
            icon: 'icons/document.png'

            MDLabel:
                text: 'Transactions coming soon...'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Budgets'
            icon: 'calculator'

            MDLabel:
                text: 'Budgets coming soon...'
                halign: 'center'
        
        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Profile'
            icon: 'icons/user.png'

            MDLabel:
                text: 'Profile coming soon...'
                halign: 'center'
"""
