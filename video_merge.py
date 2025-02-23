import os
import subprocess
from moviepy.editor import VideoFileClip, concatenate_videoclips
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to merge video with outro
def merge_videos(input_video_path, outro_video_path, output_video_path):
    try:
        input_clip = VideoFileClip(input_video_path)
        outro_clip = VideoFileClip(outro_video_path)
        final_clip = concatenate_videoclips([input_clip, outro_clip])
        final_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')
        return True
    except Exception as e:
        print(f"Error merging videos: {e}")
        return False

# Function to process videos
def process_videos(input_folder, outro_video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.mp4', '.mov', '.avi', '.mkv')):
            input_video_path = os.path.join(input_folder, filename)
            output_video_path = os.path.join(output_folder, f"output_{filename}")
            print(f"Processing {filename}...")
            success = merge_videos(input_video_path, outro_video_path, output_video_path)
            if success:
                print(f"Successfully processed: {filename}")
            else:
                print(f"Failed to process: {filename}")

# GUI for the app
def main():
    def select_input_folder():
        folder = filedialog.askdirectory()
        input_folder_entry.delete(0, tk.END)
        input_folder_entry.insert(0, folder)

    def select_outro_video():
        file = filedialog.askopenfilename()
        if file:
            outro_video_entry.delete(0, tk.END)
            outro_video_entry.insert(0, file)

    def select_output_folder():
        folder = filedialog.askdirectory()
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, folder)

    def start_processing():
        input_folder = input_folder_entry.get()
        outro_video_path = outro_video_entry.get()
        output_folder = output_folder_entry.get()

        if not input_folder or not outro_video_path or not output_folder:
            messagebox.showwarning("Missing Information", "Please fill in all fields.")
            return

        process_videos(input_folder, outro_video_path, output_folder)
        messagebox.showinfo("Success", "Processing completed successfully!")

    root = tk.Tk()
    root.title("Bulk Video Outro Adder")
    root.geometry("500x400")
    root.configure(bg="white")

    tk.Label(root, text="Input Folder (Videos):", bg="white", fg="black").pack(pady=5)
    input_folder_entry = tk.Entry(root, width=50)
    input_folder_entry.pack()
    tk.Button(root, text="Browse", command=select_input_folder).pack()

    tk.Label(root, text="Outro Video (Select File):", bg="white", fg="black").pack(pady=5)
    outro_video_entry = tk.Entry(root, width=50)
    outro_video_entry.pack()
    tk.Button(root, text="Browse", command=select_outro_video).pack()

    tk.Label(root, text="Output Folder:", bg="white", fg="black").pack(pady=5)
    output_folder_entry = tk.Entry(root, width=50)
    output_folder_entry.pack()
    tk.Button(root, text="Browse", command=select_output_folder).pack()

    tk.Button(root, text="Start Processing", command=start_processing, bg="green", fg="white").pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
