app_name = "palim"
app_title = "Palim"
app_publisher = "Palim Ltda"
app_description = "Customizações upgrade-safe do sistema de tickets Palim"
app_email = "suporte@palim.com.br"
app_license = "MIT"

# Fixtures para preservar customizações entre upgrades
fixtures = [
    "Custom Field",
    "Property Setter", 
    "Client Script",
    "Server Script",
    "Notification",
    "Email Template",
    "Print Format"
]

# Hooks para estender DocTypes do Helpdesk (upgrade-safe)
# Usar extend_doctype_class em vez de override para evitar conflitos
# extend_doctype_class = {
#     "HD Ticket": ["palim.overrides.ticket.TicketExtension"]
# }

# JavaScript customizado para DocTypes
# doctype_js = {
#     "HD Ticket": "public/js/ticket_custom.js"
# }

# Eventos de documentos
# doc_events = {
#     "HD Ticket": {
#         "before_save": "palim.overrides.ticket.before_save",
#         "after_insert": "palim.overrides.ticket.after_insert"
#     }
# }

# Scheduler events
# scheduler_events = {
#     "daily": [
#         "palim.tasks.daily_cleanup"
#     ]
# }

# Jinja template methods
# jinja = {
#     "methods": [
#         "palim.utils.jinja_methods"
#     ]
# }
