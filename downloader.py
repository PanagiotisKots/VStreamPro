import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import webbrowser

import yt_dlp




# Function to handle video download (placeholder)
def download_video():
    global download_directory
    primary_url = primary_url_entry.get().strip()
    additional_urls = additional_urls_text.get("1.0", tk.END).strip()
    
    if not primary_url and not additional_urls:
        messagebox.showerror("Input Error", "Please enter at least one URL.")
        return
    
    if not download_directory:
        messagebox.showerror("Directory Error", "Please select a download directory.")
        return
    
    # Simulate a loading process
    for i in range(101):
        root.after(i * 20, lambda i=i: update_progress(i, "Downloading Video..."))  # Update progress bar
    messagebox.showinfo("Info", f"Video download functionality is not yet implemented. Files will be saved to {download_directory}.")







def download_youtube_video_from_input():
    def update_progress(value, message):
        progress_var.set(value)
        progress_bar.update_idletasks()
        percentage_label.config(text=f"{int(value)}%")
        status_label.config(text=message)

    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
            root.after(0, update_progress, percent, f"Downloading: {d.get('filename', 'Unknown')}")
        elif d['status'] == 'finished':
            root.after(0, update_progress, 100, f"Finished: {d.get('filename', 'Unknown')}")

    def download_youtube_video(url, output_path='.'):
        try:
            # yt-dlp options to format output and download the best quality
            ydl_opts = {
                'outtmpl': f'{output_path}/%(title)s.%(ext)s',
                'format': 'best',
                'progress_hooks': [progress_hook],  # Set the progress hook
            }

            # Download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                print(f"Downloaded: {info_dict.get('title', 'Unknown Title')}")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            root.after(0, messagebox.showerror, "Download Error", f"An error occurred: {e}")

    # Reset progress before starting downloads
    root.after(0, update_progress, 0, "Ready")

    # Fetch the URLs from the GUI input fields
    primary_url = primary_url_entry.get().strip()
    additional_urls = additional_urls_text.get("1.0", tk.END).strip().split('\n')

    if not primary_url and not additional_urls:
        root.after(0, messagebox.showerror, "Input Error", "Please enter at least one URL.")
        return
    
    # Fetch the download path
    download_path = directory_entry.get().strip()
    
    # Default to the current directory if the download path is left empty
    if not download_path:
        download_path = '.'

    # Download the primary URL
    if primary_url:
        download_youtube_video(primary_url, download_path)

    # Download additional URLs
    for url in additional_urls:
        url = url.strip()
        if url:
            download_youtube_video(url, download_path)

    # Notify user that downloads are complete
    root.after(0, messagebox.showinfo, "Info", "Download process completed.")
    root.after(0, update_progress, 100, "All downloads completed.")







# Function to handle audio download (placeholder)
def download_audio():
    global download_directory
    primary_url = primary_url_entry.get().strip()
    additional_urls = additional_urls_text.get("1.0", tk.END).strip()
    
    if not primary_url and not additional_urls:
        messagebox.showerror("Input Error", "Please enter at least one URL.")
        return
    
    if not download_directory:
        messagebox.showerror("Directory Error", "Please select a download directory.")
        return
    
    # Simulate a loading process
    for i in range(101):
        root.after(i * 20, lambda i=i: update_progress(i, "Downloading Audio..."))  # Update progress bar
    messagebox.showinfo("Info", f"Audio download functionality is not yet implemented. Files will be saved to {download_directory}.")














# Function to handle OK action (placeholder)
def ok_action():
    primary_url = primary_url_entry.get().strip()
    additional_urls = additional_urls_text.get("1.0", tk.END).strip()
    
    if not primary_url and not additional_urls:
        messagebox.showerror("Input Error", "Please enter at least one URL.")
        return
    
    # Add functionality for OK action
    messagebox.showinfo("Info", "OK action is not yet implemented.")















# Function to update progress bar
def update_progress(value, message):
    progress_var.set(value)
    progress_bar.update_idletasks()
    percentage_label.config(text=f"{value}%")
    status_label.config(text=message)












# Function to handle file menu actions
def open_file():
    messagebox.showinfo("Info", "Open File functionality is not yet implemented.")

def save_file():
    messagebox.showinfo("Info", "Save File functionality is not yet implemented.")

def save_as():
    messagebox.showinfo("Info", "Save As functionality is not yet implemented.")

def print_file():
    messagebox.showinfo("Info", "Print functionality is not yet implemented.")

def recent_files():
    messagebox.showinfo("Info", "Recent Files functionality is not yet implemented.")

# Function to handle help menu actions
def show_help():
    messagebox.showinfo("Help", "Help information is not yet implemented.")

def show_tutorial():
    webbrowser.open("https://example.com/tutorial")

def show_faq():
    webbrowser.open("https://example.com/faq")

def show_feedback():
    webbrowser.open("https://example.com/feedback")

def show_about():
    messagebox.showinfo("About", "Video & Audio Downloader v1.0")













def apply_light_theme():
    root.config(bg='#f0f0f0')
    
    # Configure standard Tkinter widgets
    primary_url_label.config(bg='#f0f0f0', fg='#333')
    additional_urls_label.config(bg='#f0f0f0', fg='#333')
    additional_urls_text.config(bg='#ffffff', fg='#333', borderwidth=2, relief=tk.SOLID)
    directory_label.config(bg='#f0f0f0', fg='#333')
    directory_entry.config(bg='#ffffff', fg='#333', borderwidth=2, relief=tk.SOLID)
    text_display.config(bg='#ffffff', fg='#333', borderwidth=2, relief=tk.SOLID)
    progress_bar.config(style='gray.Horizontal.TProgressbar')
    percentage_label.config(bg='#f0f0f0', fg='#333')
    status_label.config(bg='#f0f0f0', fg='#333')
    
    # Configure buttons with a modern look
    for button in [download_video_button, download_audio_button, ok_button, cancel_button, exit_button, directory_browse_button, settings_button]:
        button.config(bg='#007bff', fg='#ffffff', relief=tk.FLAT)
        button.bind("<Enter>", lambda e: e.widget.config(bg='#0056b3'))
        button.bind("<Leave>", lambda e: e.widget.config(bg='#007bff'))
    
    # Configure menu
    menu_bar.config(bg='#007bff', fg='#ffffff')











def apply_dark_theme():
    root.config(bg='#2e2e2e')
    
    # Configure standard Tkinter widgets
    primary_url_label.config(bg='#2e2e2e', fg='#ffffff')
    additional_urls_label.config(bg='#2e2e2e', fg='#ffffff')
    additional_urls_text.config(bg='#3e3e3e', fg='#ffffff', borderwidth=2, relief=tk.SOLID)
    directory_label.config(bg='#2e2e2e', fg='#ffffff')
    directory_entry.config(bg='#3e3e3e', fg='#ffffff', borderwidth=2, relief=tk.SOLID)
    text_display.config(bg='#3e3e3e', fg='#ffffff', borderwidth=2, relief=tk.SOLID)
    progress_bar.config(style='blue.Horizontal.TProgressbar')
    percentage_label.config(bg='#2e2e2e', fg='#ffffff')
    status_label.config(bg='#2e2e2e', fg='#ffffff')
    
    # Configure buttons with a modern look
    for button in [download_video_button, download_audio_button, ok_button, cancel_button, exit_button, directory_browse_button, settings_button]:
        button.config(bg='#007bff', fg='#ffffff', relief=tk.FLAT)
        button.bind("<Enter>", lambda e: e.widget.config(bg='#0056b3'))
        button.bind("<Leave>", lambda e: e.widget.config(bg='#007bff'))
    
    # Configure menu
    menu_bar.config(bg='#007bff', fg='#ffffff')














# Function to handle theme menu actions
def switch_to_light_theme():
    apply_light_theme()

def switch_to_dark_theme():
    apply_dark_theme()

def switch_to_system_theme():
    # Add functionality for system default theme
    pass

def apply_custom_theme():
    # Add functionality to apply a custom theme
    pass

def reset_theme():
    # Reset to default theme
    apply_light_theme()

# Function to handle directory menu actions
def browse_directory():
    global download_directory
    download_directory = filedialog.askdirectory()
    if download_directory:
        directory_entry.delete(0, tk.END)  # Clear the entry field
        directory_entry.insert(0, download_directory)  # Insert the selected directory path

def clear_directory():
    global download_directory
    download_directory = None
    directory_entry.delete(0, tk.END)

def set_default_directory():
    # Set default directory functionality
    messagebox.showinfo("Default Directory", "Set default directory functionality is not yet implemented.")

def recent_directories():
    # Show recent directories functionality
    messagebox.showinfo("Recent Directories", "Recent Directories functionality is not yet implemented.")

# Function to handle donate actions
def donate():
    webbrowser.open("https://example.com/donate")

def sponsor():
    webbrowser.open("https://example.com/sponsor")

def support():
    webbrowser.open("https://example.com/support")

def contribute():
    webbrowser.open("https://example.com/contribute")

# Function to handle preferences actions
def open_preferences():
    messagebox.showinfo("Preferences", "Preferences functionality is not yet implemented.")

def configure_settings():
    messagebox.showinfo("Settings", "Settings configuration is not yet implemented.")

def set_language():
    messagebox.showinfo("Language", "Language settings functionality is not yet implemented.")

def manage_plugins():
    messagebox.showinfo("Plugins", "Plugin management functionality is not yet implemented.")

# Create the main window
root = tk.Tk()
root.title("Video & Audio Downloader")
root.geometry("1000x750")  # Increased window size to accommodate the new layout

# Create the menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save As...", command=save_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Print", command=print_file)
file_menu.add_command(label="Recent Files", command=recent_files)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help", command=show_help)
help_menu.add_command(label="Tutorial", command=show_tutorial)
help_menu.add_command(label="FAQ", command=show_faq)
help_menu.add_command(label="Feedback", command=show_feedback)
help_menu.add_command(label="About", command=show_about)

# Add Theme menu
theme_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Light Theme", command=switch_to_light_theme)
theme_menu.add_command(label="Dark Theme", command=switch_to_dark_theme)
theme_menu.add_command(label="System Default", command=switch_to_system_theme)
theme_menu.add_command(label="Custom Theme", command=apply_custom_theme)
theme_menu.add_command(label="Reset Theme", command=reset_theme)

# Add Directory menu
directory_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Directory", menu=directory_menu)
directory_menu.add_command(label="Browse...", command=browse_directory)
directory_menu.add_command(label="Clear Directory", command=clear_directory)
directory_menu.add_command(label="Set Default Directory", command=set_default_directory)
directory_menu.add_command(label="Recent Directories", command=recent_directories)

# Add Donate menu
donate_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Donate", menu=donate_menu)
donate_menu.add_command(label="Donate", command=donate)
donate_menu.add_command(label="Sponsor", command=sponsor)
donate_menu.add_command(label="Support", command=support)
donate_menu.add_command(label="Contribute", command=contribute)

# Add Preferences menu
preferences_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Preferences", menu=preferences_menu)
preferences_menu.add_command(label="Configure Settings", command=configure_settings)
preferences_menu.add_command(label="Set Language", command=set_language)
preferences_menu.add_command(label="Manage Plugins", command=manage_plugins)

# Create a frame for the left side text display
left_frame = tk.Frame(root, width=300, bg='#f0f0f0')
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Create a text widget for displaying large text
text_display = tk.Text(left_frame, wrap=tk.WORD, height=30, width=40, bg='#ffffff', fg='#333', borderwidth=2, relief=tk.SOLID)
text_display.pack(expand=True, fill=tk.BOTH)

# Create a frame for the main content area
main_frame = tk.Frame(root)
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create a label and entry for primary URL
primary_url_label = tk.Label(main_frame, text="Primary YouTube URL:")
primary_url_label.pack(pady=10)

primary_url_entry = tk.Entry(main_frame, width=80)
primary_url_entry.pack(pady=5)

# Create a label for additional URLs
additional_urls_label = tk.Label(main_frame, text="Additional YouTube URLs (one per line):")
additional_urls_label.pack(pady=10)

# Create a text area for additional URLs
additional_urls_text = tk.Text(main_frame, height=10, width=80)
additional_urls_text.pack(pady=5)

# Create a label and entry for download directory
directory_label = tk.Label(main_frame, text="Download Directory:")
directory_label.pack(pady=10)

directory_frame = tk.Frame(main_frame)
directory_frame.pack(pady=5)

directory_entry = tk.Entry(directory_frame, width=60)
directory_entry.pack(side=tk.LEFT, padx=5)

directory_browse_button = tk.Button(directory_frame, text="Browse", command=browse_directory)
directory_browse_button.pack(side=tk.LEFT, padx=5)

# Create a frame to hold buttons
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=15)

# Create a download video button
download_video_button = tk.Button(button_frame, text="Download Video", command=download_youtube_video_from_input)
download_video_button.pack(side=tk.LEFT, padx=5)







# Create a download audio button
download_audio_button = tk.Button(button_frame, text="Download Audio", command=download_audio)
download_audio_button.pack(side=tk.LEFT, padx=5)

# Create an OK button
ok_button = tk.Button(button_frame, text="OK", command=ok_action)
ok_button.pack(side=tk.LEFT, padx=5)

# Create a Cancel button
cancel_button = tk.Button(button_frame, text="Cancel", command=root.quit)
cancel_button.pack(side=tk.LEFT, padx=5)

# Create an Exit button
exit_button = tk.Button(button_frame, text="Exit", command=root.quit)
exit_button.pack(side=tk.LEFT, padx=5)

# Create a settings button
settings_button = tk.Button(button_frame, text="Settings", command=open_preferences)
settings_button.pack(side=tk.LEFT, padx=5)

# Create a frame for progress bar at the bottom
progress_frame = tk.Frame(root, bg='#f0f0f0')
progress_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Create a progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, length=800, mode='determinate', variable=progress_var)
progress_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Create a label for percentage
percentage_label = tk.Label(progress_frame, text="0%", bg='#f0f0f0')
percentage_label.pack(side=tk.RIGHT, padx=10)

# Create a status bar
status_label = tk.Label(root, text="Ready", bg='#f0f0f0', anchor='w')
status_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# Apply default theme
apply_light_theme()

# Start the GUI event loop
root.mainloop()
