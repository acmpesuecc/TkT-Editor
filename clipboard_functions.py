from tkinter import TclError, Toplevel, Listbox, Scrollbar, END
from widget_registry import get_widget

# Local clipboard list (session-only)
local_clipboard = []

def copy_text(event=None):
    """Copy selected text into local clipboard without duplicate at the top."""
    T = get_widget('text_widget')
    try:
        selected = T.get("sel.first", "sel.last").strip()
        if selected:
            if not local_clipboard or local_clipboard[0] != selected:
                local_clipboard.insert(0, selected)
            # Keep only last 10 items
            if len(local_clipboard) > 10:
                local_clipboard.pop()
    except TclError:
        pass  # nothing selected
    return "break"

def cut_text(event=None):
    """Cut selected text into local clipboard without duplicate at the top."""
    T = get_widget('text_widget')
    try:
        selected = T.get("sel.first", "sel.last").strip()
        if selected:
            if not local_clipboard or local_clipboard[0] != selected:
                local_clipboard.insert(0, selected)
            # Keep only last 10 items
            if len(local_clipboard) > 10:
                local_clipboard.pop()
            T.delete("sel.first", "sel.last")
    except TclError:
        pass  # nothing selected
    return "break"


def paste_text(event=None, item=None):
    """Paste most recent or a chosen clipboard item."""
    T = get_widget('text_widget')
    if item is None:
        if local_clipboard:
            T.insert("insert", local_clipboard[0])
    else:
        T.insert("insert", item)
    return "break"

# def show_clipboard_popup(root):
#     """Open a scrollable popup window showing all clipboard items for selection."""
#     from tkinter import Toplevel, Listbox, Scrollbar, END

#     if not local_clipboard:
#         return  # nothing to show

#     popup = Toplevel(root)
#     popup.title("Clipboard")
#     popup.geometry("400x250")
#     popup.transient(root)
#     popup.grab_set()  # modal behavior

#     # Scrollbar
#     scrollbar = Scrollbar(popup)
#     scrollbar.pack(side="right", fill="y")

#     # Listbox for clipboard items
#     listbox = Listbox(popup, yscrollcommand=scrollbar.set, font=("Arial", 12))
#     listbox.pack(side="left", fill="both", expand=True)

#     # Add items (replace newlines with spaces for display)
#     for item in local_clipboard:
#         display = item.replace("\n", " ")
#         listbox.insert(END, display)

#     scrollbar.config(command=listbox.yview)

#     def on_select(event):
#         """Paste the selected clipboard item into the text editor."""
#         selection = listbox.curselection()
#         if selection:
#             idx = selection[0]
#             paste_text(item=local_clipboard[idx])  # paste that specific item
#             popup.destroy()  # close popup after pasting

#     listbox.bind("<Double-Button-1>", on_select)  # double-click to paste
