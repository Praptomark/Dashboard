# Imported Modules
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.tableview import Tableview
from PIL import Image, ImageTk

# For Dubug purpose
from dummy_data import *
from logger import on_button_click, on_entry_change, on_checkbox_toggle, on_tab_change, on_entry

#===================================================================================================#

'''Initializing Window'''

root = ttk.Window(themename="litera", title="CRBC TOLL v0.1")

#===================================================================================================#

'''Variables'''

font_family = "Arial 10 bold"
colors = root.style.colors
image = Image.open("cat.png")
img_size = (600, 450)

#===================================================================================================#

'''Root Configurations '''

root.iconbitmap(r"logo.ico")

height = root.winfo_screenheight() # Screen Height
width = root.winfo_screenwidth() # Screen Width

root.geometry(f"{width}x{height}") # Full Window

#===================================================================================================#

'''Main Frame'''

# Main notebook
notebook = ttk.Notebook(root, bootstyle="info")
notebook.pack(expand=1, fill="both")

# Creating Frame and ScrolledFrames
home = ScrolledFrame(notebook, autohide=True, bootstyle="round")
audit = ttk.Frame(notebook)
users = ttk.Frame(notebook)
support = ScrolledFrame(notebook, autohide=True, bootstyle="round")

# Inserting Frames and Scrolledframes in notebook as tabs
notebook.add(home.container, text="Home")
notebook.add(audit, text="Audit")
notebook.add(users, text="Users")
notebook.add(support.container, text="Support")

# Notebook log
notebook.bind("<<NotebookTabChanged>>", on_tab_change)

#===================================================================================================#

'''Home'''

# Report main Frame
report_box_frame = ttk.Labelframe(home, bootstyle="success", text="Report")
report_box_frame.pack(expand=True, fill="y", side="left", pady=10, padx=20, ipadx=10, anchor="w")

# Report child frames
report_box_child_frame = ttk.Frame(report_box_frame)
report_box_child_frame.pack(expand=True, fill="both")

report_box_left_frame = ttk.Frame(report_box_child_frame)
report_box_left_frame.pack(expand=True, fill="both", side="left", pady=10, padx=20)

report_box_right_frame = ttk.Frame(report_box_child_frame)
report_box_right_frame.pack(expand=True, fill="both", side="left", pady=10, padx=20)

# Plaza
report_plaza_lebel_frame = ttk.LabelFrame(report_box_left_frame, bootstyle="info", text="PLAZA")
report_plaza_lebel_frame.pack(ipadx=5, ipady=3, fill="x", padx=10)

report_plaza_choice_input = ttk.Combobox(report_plaza_lebel_frame,bootstyle="secondary", foreground="grey", values=["EAST", "WEST", "BOTH"], state="readonly")
report_plaza_choice_input.bind("<<ComboboxSelected>>", lambda event: on_entry_change(report_plaza_choice_input.get(), "report_plaza_choice_input"))
report_plaza_choice_input.pack()

# Date
report_date_frame = ttk.LabelFrame(report_box_left_frame, bootstyle="info", text="DATE")
report_date_frame.pack(expand=True, fill="x", ipady=3, padx=10)

report_date_checkbox = ttk.DateEntry(report_date_frame, bootstyle="primary")
report_date_checkbox.pack(anchor="w", padx=10, pady=3)

# Shift
report_shift_lebel_frame = ttk.LabelFrame(report_box_left_frame, bootstyle="info", text="SHIFT")
report_shift_lebel_frame.pack(expand=True, fill="x", ipady=3, padx=10)

report_first_shift_checkbox = ttk.Checkbutton(report_shift_lebel_frame, command= lambda: on_checkbox_toggle("report_first_shift_checkbox"), bootstyle="info-square-toggle", text="1st Shift",)
report_first_shift_checkbox.pack(anchor="w", padx=10, pady=3)

report_second_shift_checkbox = ttk.Checkbutton(report_shift_lebel_frame, command= lambda: on_checkbox_toggle("report_second_shift_checkbox"), bootstyle="info-square-toggle", text="2nd Shift")
report_second_shift_checkbox.pack(anchor="w", padx=10, pady=3)

report_third_shift_checkbox = ttk.Checkbutton(report_shift_lebel_frame, command= lambda: on_checkbox_toggle("report_third_shift_checkbox"), bootstyle="info-square-toggle", text="3rd Shift")
report_third_shift_checkbox.pack(anchor="w", padx=10, pady=3)

# Export
report_export_lebel_frame = ttk.LabelFrame(report_box_left_frame, bootstyle="info", text="EXPORT")
report_export_lebel_frame.pack(expand=True, fill="x", ipady=3, padx=10)

report_export_pdf = ttk.Button(report_export_lebel_frame, command= lambda: on_button_click("report_export_pdf"), bootstyle="primary", text="PDF", width=20)
report_export_pdf.pack(pady=5)

report_export_excel = ttk.Button(report_export_lebel_frame, command= lambda: on_button_click("report_export_excel"), bootstyle="primary", text="EXCEL", width=20)
report_export_excel.pack(pady=5)

report_export_print = ttk.Button(report_export_lebel_frame, command= lambda: on_button_click("report_export_print"), bootstyle="primary", text="PRINT", width=20)
report_export_print.pack(pady=5)

# Vehical class
report_vehical_class_lebel_frame = ttk.LabelFrame(report_box_right_frame, bootstyle="info", text="VEH CLASS")
report_vehical_class_lebel_frame.pack(expand=True, fill="x", ipady=3, padx=10)

report_unregistered_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_unregistered_checkbox"), bootstyle="info-round-toggle", text="Unregistered",)
report_unregistered_checkbox.pack(anchor="w", padx=10, pady=3)

report_motorcycle_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_motorcycle_checkbox"), bootstyle="info-round-toggle", text="Motorcycle")
report_motorcycle_checkbox.pack(anchor="w", padx=10, pady=3)

report_car_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_car_checkbox"), bootstyle="info-round-toggle", text="Car")
report_car_checkbox.pack(anchor="w", padx=10, pady=3)

report_microbus_and_pickup_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_microbus_and_pickup_checkbox"), bootstyle="info-round-toggle", text="Microbus/Pickup")
report_microbus_and_pickup_checkbox.pack(anchor="w", padx=10, pady=3)

report_mini_bus_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_mini_bus_checkbox"), bootstyle="info-round-toggle", text="Mini Bus")
report_mini_bus_checkbox.pack(anchor="w", padx=10, pady=3)

report_bus_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_bus_checkbox"), bootstyle="info-round-toggle", text="Bus")
report_bus_checkbox.pack(anchor="w", padx=10, pady=3)

report_small_truck_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_small_truck_checkbox"), bootstyle="info-round-toggle", text="Small Truck")
report_small_truck_checkbox.pack(anchor="w", padx=10, pady=3)

report_medium_truck_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_medium_truck_checkbox"), bootstyle="info-round-toggle", text="Medium Truck (5-8)")
report_medium_truck_checkbox.pack(anchor="w", padx=10, pady=3)

report_large_truck_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_large_truck_checkbox"), bootstyle="info-round-toggle", text="Large Truck (8-11)")
report_large_truck_checkbox.pack(anchor="w", padx=10, pady=3)

report_large_truck_3_axel_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_large_truck_3_axel_checkbox"), bootstyle="info-round-toggle", text="Large Truck 3xl")
report_large_truck_3_axel_checkbox.pack(anchor="w", padx=10, pady=3)

report_large_truck_4_axel_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_large_truck_4_axel_checkbox"), bootstyle="info-round-toggle", text="Large Truck 4xl")
report_large_truck_4_axel_checkbox.pack(anchor="w", padx=10, pady=3)

report_large_truck_over_4_axel_checkbox = ttk.Checkbutton(report_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("report_large_truck_over_4_axel_checkbox"), bootstyle="info-round-toggle", text="Large Truck >4xl")
report_large_truck_over_4_axel_checkbox.pack(anchor="w", padx=10, pady=3)

# Vechical type
report_vehical_type_lebel_frame = ttk.LabelFrame(report_box_right_frame, bootstyle="info", text="VEH TYPE")
report_vehical_type_lebel_frame.pack(expand=True, fill="x", ipady=3, padx=10)

report_cash_checkbox = ttk.Checkbutton(report_vehical_type_lebel_frame, command= lambda: on_checkbox_toggle("report_cash_checkbox"), bootstyle="info-square-toggle", text="Cash",)
report_cash_checkbox.pack(anchor="w", padx=10, pady=3)

report_credit_checkbox = ttk.Checkbutton(report_vehical_type_lebel_frame, command= lambda: on_checkbox_toggle("report_credit_checkbox"), bootstyle="info-square-toggle", text="Credit")
report_credit_checkbox.pack(anchor="w", padx=10, pady=3)

report_exampt_checkbox = ttk.Checkbutton(report_vehical_type_lebel_frame, command= lambda: on_checkbox_toggle("report_exampt_checkbox"), bootstyle="info-square-toggle", text="Exampt")
report_exampt_checkbox.pack(anchor="w", padx=10, pady=3)

# Report preview button
report_preview_button = ttk.Button(report_box_frame, command= lambda: on_button_click("report_preview_button"), bootstyle="primary", text="PREVIEW REPORT", width=20)
report_preview_button.pack(pady=5)

# Shortage
shortage = ttk.Labelframe(home, bootstyle="success", text="Shortage")
shortage.pack(expand=True, padx=20, pady=20, ipadx=10, ipady=10)

# Registration No Imput
reg_frame = ttk.Frame(shortage)
reg_frame.pack(side='left', fill='x', expand=True, padx=10)

reg_label = ttk.Label(reg_frame, text="Reg No", font=font_family)
reg_label.pack(side="left", padx=2)

reg_no_entry = ttk.Entry(reg_frame, bootstyle="primary")
on_entry("reg_no_entry", reg_no_entry.get())
reg_no_entry.pack(side="left", padx=2)

# TC Imput
tc_name_frame = ttk.Frame(shortage)
tc_name_frame.pack(side='left', fill='x', expand=True, padx=10)

tc_name_label = ttk.Label(tc_name_frame, text="TC", font=font_family)
tc_name_label.pack(side="left", padx=2)

tc_name_entry = ttk.Combobox(tc_name_frame, values=tc_names, font=font_family, state="readonly")
tc_name_entry.bind("<<ComboboxSelected>>", lambda event: on_entry_change(tc_name_entry.get(), "tc_name_entry"))
tc_name_entry.pack(side="left", padx=2)

# cash Imput
cash_frame = ttk.Frame(shortage)
cash_frame.pack(side='left', fill='x', expand=True, padx=10)

cash_label = ttk.Label(cash_frame, text="Cash Amount", font=font_family)
cash_label.pack(side="left", padx=2)

cash_amount_entry = ttk.Entry(cash_frame, bootstyle="primary")
on_entry("cash_amount_entry", cash_amount_entry.get())
cash_amount_entry.pack(side="left", padx=2)

# Submit
shortage_entry_button = ttk.Button(shortage, command= lambda: on_button_click("shortage_entry_button"), bootstyle="primary", text="ADD", width=20)
shortage_entry_button.pack(side="left", padx=10, pady=10)

#===================================================================================================#

'''AUDIT''' 

# Control box mainframe
audit_control_ui_frame = ttk.Labelframe(audit, bootstyle="success", text="Control Box")
audit_control_ui_frame.pack(expand=True, fill="y", side="left", pady=10, padx=20, ipadx=10, anchor="w")

# Vehical audit frame
audit_vehical_and_tc_frame = ttk.Frame(audit)
audit_vehical_and_tc_frame.pack(expand=True, fill="both", side="left", pady=10, padx=20)

# Tc info and vehical image frame
audit_image_and_tc_frame = ttk.Frame(audit_vehical_and_tc_frame)
audit_image_and_tc_frame.pack(fill="both")

# Tc info and vehical image
audit_tc_audit_info = ttk.LabelFrame(audit_image_and_tc_frame, bootstyle="info", text="TC INFO")
audit_tc_audit_info.pack(side="left", expand=True, fill="both")

# Username
audit_tc_username_frame = ttk.Frame(audit_tc_audit_info)
audit_tc_username_frame.pack()

audit_tc_username_pointer = ttk.Label(audit_tc_username_frame, text="Username :", font="Arial 10 bold").pack(side="left",padx=3)
audit_tc_username = ttk.Label(audit_tc_username_frame, text="CRBC", font="Arial 10 bold").pack(side="left", padx=3)

# Shift
audit_tc_shift_frame = ttk.Frame(audit_tc_audit_info)
audit_tc_shift_frame.pack()

audit_tc_shift_pointer = ttk.Label(audit_tc_shift_frame, text="Shift :", font="Arial 10 bold").pack(side="left",padx=3)
audit_tc_shift = ttk.Label(audit_tc_shift_frame, text="All", font="Arial 10 bold").pack(side="left", padx=3)

# Vehical Image
resized_image = image.resize(img_size)
tk_image = ImageTk.PhotoImage(resized_image)
audit_img_lebel = ttk.Label(audit_image_and_tc_frame, image=tk_image)
audit_img_lebel.image = tk_image
audit_img_lebel.pack()

# Vehical data table
audit_vehical_data = Tableview(
    audit_vehical_and_tc_frame, 
    coldata=coldata, 
    rowdata=rowdata,
    searchable=True,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, None),
    autoalign=False,
    autofit=True
    )
audit_vehical_data.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Control box ui

# Plaza
audit_plaza_lebel_frame = ttk.LabelFrame(audit_control_ui_frame, bootstyle="info", text="PLAZA")
audit_plaza_lebel_frame.pack(ipadx=5, ipady=3, fill="x", padx=10)

audit_plaza_choice_input = ttk.Combobox(audit_plaza_lebel_frame, bootstyle="secondary", foreground="grey", values=["EAST", "WEST", "BOTH"], state="readonly")
audit_plaza_choice_input.bind("<<ComboboxSelected>>", lambda event: on_entry_change(audit_plaza_choice_input.get(), "audit_plaza_choice_input"))
audit_plaza_choice_input.pack()

# Date
audit_date_frame = ttk.LabelFrame(audit_control_ui_frame, bootstyle="info", text="DATE")
audit_date_frame.pack(expand=True, fill="x", ipady=3, padx=10)

audit_date_checkbox = ttk.DateEntry(audit_date_frame, bootstyle="primary")
audit_date_checkbox.pack(anchor="w", padx=10, pady=3)

# Shift
audit_shift_lebel_frame = ttk.LabelFrame(audit_control_ui_frame, bootstyle="info", text="SHIFT")
audit_shift_lebel_frame.pack(expand=True, fill="x", ipady=3, padx=10)

audit_first_shift_checkbox = ttk.Checkbutton(audit_shift_lebel_frame, command= lambda: on_checkbox_toggle("audit_first_shift_checkbox"), bootstyle="info-square-toggle", text="1st Shift",)
audit_first_shift_checkbox.pack(anchor="w", padx=10, pady=3)

audit_second_shift_checkbox = ttk.Checkbutton(audit_shift_lebel_frame, command= lambda: on_checkbox_toggle("audit_second_shift_checkbox"), bootstyle="info-square-toggle", text="2nd Shift")
audit_second_shift_checkbox.pack(anchor="w", padx=10, pady=3)

audit_third_shift_checkbox = ttk.Checkbutton(audit_shift_lebel_frame, command= lambda: on_checkbox_toggle("audit_third_shift_checkbox"), bootstyle="info-square-toggle", text="3rd Shift")
audit_third_shift_checkbox.pack(anchor="w", padx=10, pady=3)

# Vehical class
audit_vehical_class_lebel_frame = ttk.LabelFrame(audit_control_ui_frame, bootstyle="info", text="VEH CLASS")
audit_vehical_class_lebel_frame.pack(expand=True, fill="x", ipady=3, padx=10)

audit_unregistered_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_unregistered_checkbox"), bootstyle="info-round-toggle", text="Unregistered",)
audit_unregistered_checkbox.pack(anchor="w", padx=10, pady=3)

audit_motorcycle_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_motorcycle_checkbox"), bootstyle="info-round-toggle", text="Motorcycle")
audit_motorcycle_checkbox.pack(anchor="w", padx=10, pady=3)

audit_car_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_car_checkbox"), bootstyle="info-round-toggle", text="Car")
audit_car_checkbox.pack(anchor="w", padx=10, pady=3)

audit_microbus_and_pickup_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_microbus_and_pickup_checkbox"), bootstyle="info-round-toggle", text="Microbus/Pickup")
audit_microbus_and_pickup_checkbox.pack(anchor="w", padx=10, pady=3)

audit_mini_bus_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_mini_bus_checkbox"), bootstyle="info-round-toggle", text="Mini Bus")
audit_mini_bus_checkbox.pack(anchor="w", padx=10, pady=3)

audit_bus_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_bus_checkbox"), bootstyle="info-round-toggle", text="Bus")
audit_bus_checkbox.pack(anchor="w", padx=10, pady=3)

audit_small_truck_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_small_truck_checkbox"), bootstyle="info-round-toggle", text="Small Truck")
audit_small_truck_checkbox.pack(anchor="w", padx=10, pady=3)

audit_medium_truck_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_medium_truck_checkbox"), bootstyle="info-round-toggle", text="Medium Truck (5-8)")
audit_medium_truck_checkbox.pack(anchor="w", padx=10, pady=3)

audit_large_truck_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_large_truck_checkbox"), bootstyle="info-round-toggle", text="Large Truck (8-11)")
audit_large_truck_checkbox.pack(anchor="w", padx=10, pady=3)

audit_large_truck_3_axel_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_large_truck_3_axel_checkbox"), bootstyle="info-round-toggle", text="Large Truck 3xl")
audit_large_truck_3_axel_checkbox.pack(anchor="w", padx=10, pady=3)

audit_large_truck_4_axel_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_large_truck_4_axel_checkbox"), bootstyle="info-round-toggle", text="Large Truck 4xl")
audit_large_truck_4_axel_checkbox.pack(anchor="w", padx=10, pady=3)

audit_large_truck_over_4_axel_checkbox = ttk.Checkbutton(audit_vehical_class_lebel_frame, command= lambda: on_checkbox_toggle("audit_large_truck_over_4_axel_checkbox"), bootstyle="info-round-toggle", text="Large Truck >4xl")
audit_large_truck_over_4_axel_checkbox.pack(anchor="w", padx=10, pady=3)

# Vehical type
audit_vehical_type_lebel_frame = ttk.LabelFrame(audit_control_ui_frame, bootstyle="info", text="VEH TYPE")
audit_vehical_type_lebel_frame.pack(expand=True, fill="x", ipady=3, padx=10)

audit_cash_checkbox = ttk.Checkbutton(audit_vehical_type_lebel_frame, command= lambda: on_checkbox_toggle("audit_cash_checkbox"), bootstyle="info-square-toggle", text="Cash",)
audit_cash_checkbox.pack(anchor="w", padx=10, pady=3)

audit_credit_checkbox = ttk.Checkbutton(audit_vehical_type_lebel_frame, command= lambda: on_checkbox_toggle("audit_credit_checkbox"), bootstyle="info-square-toggle", text="Credit")
audit_credit_checkbox.pack(anchor="w", padx=10, pady=3)

audit_exampt_checkbox = ttk.Checkbutton(audit_vehical_type_lebel_frame, command= lambda: on_checkbox_toggle("audit_exampt_checkbox"), bootstyle="info-square-toggle", text="Exampt")
audit_exampt_checkbox.pack(anchor="w", padx=10, pady=3)

# Query button
audit_query_button = ttk.Button(audit_control_ui_frame, command= lambda: on_button_click("audit_query_button"), bootstyle="primary", text="QUERY", width=20)
audit_query_button.pack(pady=5)

#===================================================================================================#

'''USERS'''

# User main frame
user_frame = ttk.Labelframe(users, bootstyle="success", text="User")
user_frame.pack(expand=True, padx=10, pady=10, ipadx=10, ipady=10)

# User Create
user_create_frame = ttk.Labelframe(user_frame, bootstyle="success", text="User Create")
user_create_frame.pack(expand=True, ipadx=10, ipady=10)

# Username
username_frame = ttk.Frame(user_create_frame)
username_frame.pack(side='left', fill='x', expand=True, padx=10)

username_lebel = ttk.Label(username_frame, text="Username", font=font_family)
username_lebel.pack(side="left", padx=2)

username_entry = ttk.Entry(username_frame, bootstyle="primary")
on_entry("username_entry", username_entry.get())
username_entry.pack(side="left", padx=2)

# Password
password_frame = ttk.Frame(user_create_frame)
password_frame.pack(side='left', fill='x', expand=True, padx=10)

password_lebel = ttk.Label(password_frame, text="Password", font=font_family)
password_lebel.pack(side="left", padx=2)

password_entry = ttk.Entry(password_frame, bootstyle="primary")
on_entry("password_entry", password_entry.get())
password_entry.pack(side="left", padx=2)

# User type
user_type_frame = ttk.Frame(user_create_frame)
user_type_frame.pack(side='left', fill='x', expand=True, padx=10)

user_type_lebel = ttk.Label(user_type_frame, text="Type", font=font_family)
user_type_lebel.pack(side="left", padx=2)

user_type_box_entry = ttk.Combobox(user_type_frame, values=["TC", "SI"], font=font_family, state="readonly")
user_type_box_entry.bind("<<ComboboxSelected>>", lambda event: on_entry_change(user_type_box_entry.get(), "user_type_box_entry"))
user_type_box_entry.pack(side="left", padx=2)

# Create button
user_create_button = ttk.Button(user_create_frame, command= lambda: on_button_click("user_create_button"), bootstyle="success", text="CREATE", width=20)
user_create_button.pack(side='left', fill='x', expand=True, padx=10)

####
# User Update
user_update_frame = ttk.Labelframe(user_frame, bootstyle="success", text="User Update")
user_update_frame.pack(expand=True, ipadx=10, ipady=10)

# Username Finder
username_finder_frame = ttk.Frame(user_update_frame)
username_finder_frame.pack(side='left', fill='x', expand=True, padx=10)

username_finder_lebel = ttk.Label(username_finder_frame, text="Users", font=font_family)
username_finder_lebel.pack(side="left", padx=2)

username_finder_box_entry = ttk.Combobox(username_finder_frame, values=tc_names, font=font_family, state="readonly")
username_finder_box_entry.bind("<<ComboboxSelected>>", lambda event: on_entry_change(username_finder_box_entry.get(), "username_finder_box_entry"))
username_finder_box_entry.pack(side="left", padx=2)

# Username Update
username_update_frame = ttk.Frame(user_update_frame)
username_update_frame.pack(side='left', fill='x', expand=True, padx=10)

username_update_lebel = ttk.Label(username_update_frame, text="Username", font=font_family)
username_update_lebel.pack(side="left", padx=2)

username_update_entry = ttk.Entry(username_update_frame, bootstyle="primary")
on_entry("username_update_entry", username_update_entry.get())
username_update_entry.pack(side="left", padx=2)

# Password Update
password_frame = ttk.Frame(user_update_frame)
password_frame.pack(side='left', fill='x', expand=True, padx=10)

password_lebel = ttk.Label(password_frame, text="Password", font=font_family)
password_lebel.pack(side="left", padx=2)

password_update_entry = ttk.Entry(password_frame, bootstyle="primary")
on_entry("password_update_entry", password_update_entry.get())
password_update_entry.pack(side="left", padx=2)

# Update button
user_update_button = ttk.Button(user_update_frame, command= lambda: on_button_click("user_update_button"), bootstyle="success", text="UPDATE", width=20)
user_update_button.pack(side='left', fill='x', expand=True, padx=10)

#===================================================================================================#

'''SUPPORT'''

# Clearance Main Frame
clearance_box_frame = ttk.Labelframe(support, bootstyle="success", text="Clearence")
clearance_box_frame.pack(expand=True, fill="y", side="left", pady=10, padx=20, ipadx=10, anchor="w")

# Clearance child frames
clearance_box_east_frame = ttk.LabelFrame(clearance_box_frame, bootstyle="success", text="EAST")
clearance_box_east_frame.pack(expand=True, fill="both", side="left", pady=10, padx=20, ipadx=5, ipady=5)

clearance_box_west_frame = ttk.LabelFrame(clearance_box_frame, bootstyle="success", text="WEST")
clearance_box_west_frame.pack(expand=True, fill="both", side="left", pady=10, padx=20, ipadx=5, ipady=5)

# Toll Booths East Side
east_booth_1 = ttk.Button(clearance_box_east_frame, command= lambda: on_button_click("east_booth_1"), text="East Booth 1", bootstyle="warning").pack(pady=3)
east_booth_2 = ttk.Button(clearance_box_east_frame, command= lambda: on_button_click("east_booth_2"), text="East Booth 2", bootstyle="warning").pack(pady=3)
east_booth_3 = ttk.Button(clearance_box_east_frame, command= lambda: on_button_click("east_booth_3"), text="East Booth 3", bootstyle="warning").pack(pady=3)
east_booth_4 = ttk.Button(clearance_box_east_frame, command= lambda: on_button_click("east_booth_4"), text="East Booth 4", bootstyle="warning").pack(pady=3)
east_booth_5 = ttk.Button(clearance_box_east_frame, command= lambda: on_button_click("east_booth_5"), text="East Booth 5", bootstyle="warning").pack(pady=3)
east_booth_6 = ttk.Button(clearance_box_east_frame, command= lambda: on_button_click("east_booth_6"), text="East Booth 6", bootstyle="warning").pack(pady=3)
east_booth_7 = ttk.Button(clearance_box_east_frame, command= lambda: on_button_click("east_booth_7"), text="East Booth 7", bootstyle="warning").pack(pady=3)

# Toll Booths West Side
west_booth_1 = ttk.Button(clearance_box_west_frame, command= lambda: on_button_click("west_booth_1"), text="West Booth 1", bootstyle="warning").pack(pady=3)
west_booth_2 = ttk.Button(clearance_box_west_frame, command= lambda: on_button_click("west_booth_2"), text="West Booth 2", bootstyle="warning").pack(pady=3)
west_booth_3 = ttk.Button(clearance_box_west_frame, command= lambda: on_button_click("west_booth_3"), text="West Booth 3", bootstyle="warning").pack(pady=3)
west_booth_4 = ttk.Button(clearance_box_west_frame, command= lambda: on_button_click("west_booth_4"), text="West Booth 4", bootstyle="warning").pack(pady=3)
west_booth_5 = ttk.Button(clearance_box_west_frame, command= lambda: on_button_click("west_booth_5"), text="West Booth 5", bootstyle="warning").pack(pady=3)
west_booth_6 = ttk.Button(clearance_box_west_frame, command= lambda: on_button_click("west_booth_6"), text="West Booth 6", bootstyle="warning").pack(pady=3)
west_booth_7 = ttk.Button(clearance_box_west_frame, command= lambda: on_button_click("west_booth_7"), text="West Booth 7", bootstyle="warning").pack(pady=3)

#===================================================================================================#

# Debug Codes
# ttk.Label(shortage, text="Hello world").pack()


root.mainloop() # Main Loop