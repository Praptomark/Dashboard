import logging
# from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler("dashboard.log"),
        logging.StreamHandler()
    ]
)

def log_widget_usage(widget_name):
    logging.info(f"{widget_name}")

def on_button_click(button_name):
    log_widget_usage(f"'{button_name}' is pressed")

def on_entry_change(event, widget_name):
    log_widget_usage(f"'{event}' by '{widget_name}")

def on_checkbox_toggle(checkbox_name):
    log_widget_usage(f"'{checkbox_name}' is toggled")

def on_entry(entrybox_name, data):
    log_widget_usage(f"'{data}' entered in '{entrybox_name}'")

def on_tab_change(event):
    selected_tab = event.widget.tab(event.widget.index("current"), "text")
    log_widget_usage(selected_tab)