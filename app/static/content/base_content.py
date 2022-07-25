class NavItem:
    def __init__(self, url, display_text):
        self.url = url
        self.display_text = display_text

navigation_items = [
    NavItem('', 'Home'),
    NavItem('professionalinfo', 'Education & Experience'),
    NavItem('hobbies', 'Hobbies'),
    NavItem('timeline', 'Timeline'),
    NavItem('#contact', 'Contact'),
    NavItem('about', 'About This Site')
]
copyright_text = 'Template originally created by Luis Fernando Carnales, Lin Jing Liu & Marcela Ixchel Gomez Wuotto for MLH Fellowship in Summer 2022. Current version built by Lin Jing Liu @2022.'
copyright = {
    'text': copyright_text,
    'timestamp': 'MLH Fellowship Summer 2022'
}

base_info = {
    'navigation': navigation_items,
    'copyright': copyright
}