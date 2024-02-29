from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

name = input("Enter the name by which you want to call the translator: ")
visible = tk.Tk()
visible.title(name)
visible.geometry('550x250')
visible.maxsize(550, 550)
visible.minsize(250, 250)

def translate():
    lang_1 = t1.get("1.0", "end-1c")
    cl = choose_language.get()
    if lang_1 == '':
        messagebox.showerror('Error', 'Please fill the box with valid input')
    else:
        try:
            translator = Translator()
            output = translator.translate(lang_1, dest=cl)
            translated_text = output.text
            t2.delete(1.0, END)  # Clear the existing text
            t2.insert(END, translated_text)  # Insert translated text into t2
        except Exception as e:
            messagebox.showerror('Translation Error', f'An error occurred during translation: {str(e)}')

def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

a = tk.StringVar()
auto_detect = ttk.Combobox(visible, width=20, textvariable=a, state='readonly', font=('Lucida Calligraphy', 11, 'bold'))
auto_detect['values'] = ('Auto-Detect')
auto_detect.place(x=10, y=25)
auto_detect.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(visible, width=20, textvariable=l, state='readonly', font=('Lucida Calligraphy', 11, 'bold'))
choose_language['values'] = (
    'Afrikaans','Albanian', 'Amharic', 'Arabic', 'Armenian','Azerbaijani','Basque', 'Belarusian', 'Bosnian', 'Bulgarian','Catalan',
    'Cebuano','Corsican', 'Croatian', 'Czech', 'Danish','Dutch', 'English', 'Esperanto', 'Estonian','Filipino', 'Finnish', 'French', 
    'Frisian','Georgian', 'German', 'Greek','Gujarati', 'Haitian Creole', 'Hausa','Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 
    'Icelandic', 'Igbo','Indonesian', 'Irish','Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer','Korean','Kyrgyz', 
    'Lao', 'Latin', 'Latvian','Lithuanian', 'Luxembourgish', 'Macedonian','Malagasy', 'Malay', 'Malayalam', 'Maltese',
    'Marathi','Mongolian', 'Nepali', 'Norwegian','Odia','Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi','Romanian','Russian', 
    'Samoan','Serbian', 'Shona', 'Sindhi', 'Sinhala', 'Slovak','Slovenian', 'Somali','Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik',
    'Tamil','Telugu', 'Thai','Turkish','Ukrainian', 'Urdu', 'Uyghur', 'Uzbek','Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')
choose_language.place(x=260, y=25)
choose_language.current(0)

t1 = Text(visible, width=30, height=10, borderwidth=5, relief=RIDGE)
t1.place(x=10, y=70)

t2 = Text(visible, width=30, height=10, borderwidth=5, relief=RIDGE)
t2.place(x=260, y=70)

button = Button(visible, text="Translate", relief=RIDGE, borderwidth=3, font=('Lucida Calligraphy', 11, 'bold'), cursor="hand2",
                command=translate)
button.place(x=150, y=280)

clear_button = Button(visible, text="Clear", relief=RIDGE, borderwidth=3, font=('Lucida Calligraphy', 11, 'bold'), cursor="hand2",
                      command=clear)
clear_button.place(x=280, y=280)

visible.mainloop()
