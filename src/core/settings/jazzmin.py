JAZZMIN_SETTINGS = {
    "site_title": "Kettik",

    "site_header": "Kettik",

    "site_brand": "Kettik",

    "site_logo": None,

    "login_logo": None,

    "login_logo_dark": None,

    "site_logo_classes": None,

    "site_icon": None,

    "welcome_sign": "Welcome to the Kettik",

    "copyright": "Acme Kettik Ltd",


    "search_model": ["auth.User", "auth.Group"],

    "user_avatar": None,



    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],



    "show_sidebar": True,

    "navigation_expanded": True,

    "hide_apps": [],

    "hide_models": [],

    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },


    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",


    "related_modal_active": False,


    "custom_css": None,
    "custom_js": None,

    "use_google_fonts_cdn": True,

    "show_ui_builder": True,


    "changeform_format": "horizontal_tabs",

    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},

}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-navy",
    "navbar": "navbar-success navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}