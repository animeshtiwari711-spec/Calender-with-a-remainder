# import tkinter as tk
# from tkinter import messagebox
# from datetime import datetime
# from playsound import playsound
# import threading
# import time

# alarm_time = None
# snooze_minutes = 5

# def play_alarm():
#     playsound("alarm.mp3")

# def check_alarm():
#     global alarm_time

#     while True:
#         current_time = datetime.now().strftime("%H:%M")

#         if alarm_time == current_time:
#             messagebox.showinfo("Alarm", "Wake up!")
#             threading.Thread(target=play_alarm).start()
#             alarm_time = None

#         time.sleep(1)

# def set_alarm():
#     global alarm_time

#     hour = hour_entry.get()
#     minute = minute_entry.get()

#     if hour == "" or minute == "":
#         messagebox.showwarning("Warning", "Enter hour and minute")
#         return

#     alarm_time = f"{hour}:{minute}"
#     status_label.config(text=f"Alarm set for {alarm_time}")

# def snooze_alarm():
#     global alarm_time

#     now = datetime.now()
#     snooze_time = now.replace(minute=now.minute + snooze_minutes)
#     alarm_time = snooze_time.strftime("%H:%M")

#     status_label.config(text=f"Snoozed until {alarm_time}")

# root = tk.Tk()
# root.title("Alarm Clock")
# root.geometry("350x300")

# title = tk.Label(root, text="Alarm Clock", font=("Arial", 20, "bold"))
# title.pack(pady=10)

# hour_entry = tk.Entry(root, width=10)
# hour_entry.pack(pady=5)
# hour_entry.insert(0, "HH")

# minute_entry = tk.Entry(root, width=10)
# minute_entry.pack(pady=5)
# minute_entry.insert(0, "MM")

# set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
# set_button.pack(pady=10)

# snooze_button = tk.Button(root, text="Snooze 5 Minutes", command=snooze_alarm)
# snooze_button.pack(pady=10)

# status_label = tk.Label(root, text="No alarm set")
# status_label.pack(pady=10)

# threading.Thread(target=check_alarm, daemon=True).start()

# root.mainloop()

# import tkinter as tk
# from tkinter import filedialog, messagebox
# from datetime import datetime, timedelta
# from playsound import playsound
# import threading
# import time

# alarm_time = None
# alarm_tone = ""
# snooze_minutes = 5

# def choose_tone():
#     global alarm_tone

#     file = filedialog.askopenfilename(
#         title="Select Alarm Tone",
#         filetypes=[("MP3 Files", "*.mp3")]
#     )

#     if file:
#         alarm_tone = file
#         tone_label.config(text="Tone Selected")

# def play_alarm():
#     if alarm_tone:
#         playsound(alarm_tone)
#     else:
#         messagebox.showwarning("Warning", "Please select a tone")

# def check_alarm():
#     global alarm_time

#     while True:
#         current_time = datetime.now().strftime("%H:%M")

#         if alarm_time == current_time:
#             messagebox.showinfo("Alarm", "Wake Up!")

#             threading.Thread(target=play_alarm).start()

#             alarm_time = None

#         time.sleep(1)

# def set_alarm():
#     global alarm_time

#     hour = hour_entry.get()
#     minute = minute_entry.get()

#     if hour == "" or minute == "":
#         messagebox.showwarning("Warning", "Enter time")
#         return

#     alarm_time = f"{hour}:{minute}"

#     status_label.config(text=f"Alarm Set: {alarm_time}")

# def snooze_alarm():
#     global alarm_time

#     new_time = datetime.now() + timedelta(minutes=snooze_minutes)

#     alarm_time = new_time.strftime("%H:%M")

#     status_label.config(text=f"Snoozed Until {alarm_time}")

# root = tk.Tk()
# root.title("Alarm Clock")
# root.geometry("400x400")

# title = tk.Label(root, text="Alarm Clock", font=("Arial", 20, "bold"))
# title.pack(pady=10)

# hour_entry = tk.Entry(root, width=10)
# hour_entry.pack(pady=5)
# hour_entry.insert(0, "HH")

# minute_entry = tk.Entry(root, width=10)
# minute_entry.pack(pady=5)
# minute_entry.insert(0, "MM")

# set_btn = tk.Button(root, text="Set Alarm", command=set_alarm)
# set_btn.pack(pady=10)

# tone_btn = tk.Button(root, text="Choose Tone", command=choose_tone)
# tone_btn.pack(pady=10)

# tone_label = tk.Label(root, text="No Tone Selected")
# tone_label.pack()

# snooze_btn = tk.Button(root, text="Snooze 5 Minutes", command=snooze_alarm)
# snooze_btn.pack(pady=10)

# status_label = tk.Label(root, text="No Alarm Set")
# status_label.pack(pady=10)

# threading.Thread(target=check_alarm, daemon=True).start()

# root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from datetime import datetime, timedelta
from playsound import playsound
import threading
import time

alarm_time = None
alarm_tone = ""
snooze_minutes = 5

# ---------------- ALARM FUNCTIONS ---------------- #

def choose_tone():
    global alarm_tone

    file = filedialog.askopenfilename(
        title="Select Alarm Tone",
        filetypes=[("MP3 Files", "*.mp3")]
    )

    if file:
        alarm_tone = file
        tone_label.config(text="Tone Selected")

def play_alarm():
    if alarm_tone:
        playsound(alarm_tone)
    else:
        messagebox.showwarning("Warning", "Please select a tone")

def check_alarm():
    global alarm_time

    while True:
        current_time = datetime.now().strftime("%H:%M")

        if alarm_time == current_time:
            messagebox.showinfo("Alarm", "Wake Up!")

            threading.Thread(target=play_alarm).start()

            alarm_time = None

        time.sleep(1)

def set_alarm():
    global alarm_time

    hour = hour_entry.get()
    minute = minute_entry.get()

    if hour == "" or minute == "":
        messagebox.showwarning("Warning", "Enter Time")
        return

    alarm_time = f"{hour}:{minute}"

    status_label.config(text=f"Alarm Set For {alarm_time}")

def snooze_alarm():
    global alarm_time

    new_time = datetime.now() + timedelta(minutes=snooze_minutes)

    alarm_time = new_time.strftime("%H:%M")

    status_label.config(text=f"Snoozed Until {alarm_time}")

# ---------------- BACKGROUND FUNCTION ---------------- #

def change_background():
    color = colorchooser.askcolor()[1]

    if color:
        root.configure(bg=color)

        title.config(bg=color)
        tone_label.config(bg=color)
        status_label.config(bg=color)

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x450")
root.configure(bg="lightblue")

title = tk.Label(
    root,
    text="Alarm Clock",
    font=("Arial", 22, "bold"),
    bg="lightblue"
)
title.pack(pady=15)

hour_entry = tk.Entry(root, width=10, font=("Arial", 14))
hour_entry.pack(pady=5)
hour_entry.insert(0, "HH")

minute_entry = tk.Entry(root, width=10, font=("Arial", 14))
minute_entry.pack(pady=5)
minute_entry.insert(0, "MM")

set_btn = tk.Button(
    root,
    text="Set Alarm",
    command=set_alarm,
    width=20
)
set_btn.pack(pady=10)

tone_btn = tk.Button(
    root,
    text="Choose Tone",
    command=choose_tone,
    width=20
)
tone_btn.pack(pady=10)

tone_label = tk.Label(
    root,
    text="No Tone Selected",
    bg="lightblue"
)
tone_label.pack()

bg_btn = tk.Button(
    root,
    text="Change Background",
    command=change_background,
    width=20
)
bg_btn.pack(pady=10)

snooze_btn = tk.Button(
    root,
    text="Snooze 5 Minutes",
    command=snooze_alarm,
    width=20
)
snooze_btn.pack(pady=10)

status_label = tk.Label(
    root,
    text="No Alarm Set",
    bg="lightblue",
    font=("Arial", 12)
)
status_label.pack(pady=15)

threading.Thread(target=check_alarm, daemon=True).start()

root.mainloop()