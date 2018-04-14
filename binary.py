#! python3
# March 10, 2018
# Denniel Luis Saway Sadian
# https://denniel-sadian.github.io

from tkinter import *
from tkinter import ttk, messagebox
from about_dialog import AboutDialog


class BinaryTranslator(ttk.Frame):

    def __init__(self, master, **kw):
        ttk.Frame.__init__(self, master, **kw)
        self.master = master
        # objects
        self.alpha = Text(self, width=40, height=8, wrap='word')
        self.binary = Text(self, width=40, height=8, wrap='word')
        self.one = ttk.Scrollbar(self, orient=VERTICAL,
                                 command=self.alpha.yview)
        self.two = ttk.Scrollbar(self, orient=VERTICAL,
                                 command=self.binary.yview)
        self.alpha['yscrollcommand'] = self.one.set
        self.binary['yscrollcommand'] = self.two.set
        # geometry
        for i in range(3):
            if i != 2:
                self.columnconfigure(i, weight=1)
        for i in range(12):
            self.rowconfigure(i, weight=1)
        # events
        self.alpha.bind('<Return>', self.encode_with_spaces)
        self.binary.bind('<Return>', self.decode)
        self.master.bind('<F1>', self.show_about_dialog)

        self.create_widgets()

    def encode_with_spaces(self, *args):
        self.binary.delete(0.1, 'end')
        text = self.alpha.get(0.1, 'end').strip()
        if text:
            self.binary.insert('end', encode(text))
        return args

    def encode_with_no_spaces(self):
        self.binary.delete(0.1, 'end')
        text = self.alpha.get(0.1, 'end').strip()
        if text:
            self.binary.insert('end', encode(text, False))

    def decode(self, *args):
        self.alpha.delete(0.1, 'end')
        binary = self.binary.get(0.1, 'end').strip()
        if binary:
            try:
                self.alpha.insert('end', decode(binary))
            except ValueError:
                messagebox.showerror(
                    'Error', 'Binaries must only contain ones, zeros or spaces.')
        return args

    def show_about_dialog(self, *args):
        d = AboutDialog(
            self, window_title='About Binary Code Translator',
            about_title='Binary Code Translator',
            content='Developed and written by:\n'
                    '\tDenniel Luis Saway Sadian '
                    '(https://denniel-sadian.github.io)\n\n'
                    'Date of creation:\n'
                    '\tMarch 10, 2018\n\n'
                    'Description:\n'
                    '\tThis app can translate text to binary and '
                    'binary to text.',
            image='binary.png')
        d.wm_iconbitmap('binary.ico')
        d.mainloop()
        return args

    def create_widgets(self):
        ttk.Label(self, text='Translator', font=('courier', 24, 'bold')).grid(
            column=0, row=0, columnspan=3)
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='NEW', columnspan=3, pady='0 10')
        ttk.Label(self, text='Text').grid(column=0, row=2, columnspan=3)
        self.alpha.grid(column=0, row=3, sticky='NEWS', columnspan=2, rowspan=2)
        self.one.grid(column=2, row=3, sticky='NSW', rowspan=2)
        ttk.Button(self, text='Encode with spaces',
                   command=self.encode_with_spaces).grid(
            column=0, row=5, sticky='NEWS', pady='5 0', columnspan=3)
        ttk.Button(self, text='Encode with no spaces',
                   command=self.encode_with_no_spaces).grid(
            column=0, row=6, sticky='NEWS', pady='5 0', columnspan=3)
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=0, row=7, sticky='NEW', columnspan=3, pady=10)
        ttk.Label(self, text='Binary').grid(column=0, row=8, columnspan=3)
        self.binary.grid(column=0, row=9, sticky='NEWS', columnspan=2, rowspan=2)
        self.two.grid(column=2, row=9, rowspan=2, sticky='NSW')
        ttk.Button(self, text='Decode', command=self.decode).grid(
            column=0, row=11, sticky='NEWS', columnspan=3, pady='5 0')


CAP = {'A': '01000001', 'B': '01000010', 'C': '01000011',
       'D': "01000100", 'E': "01000101", 'F': "01000110",
       'G': "01000111", 'H': "01001000", 'I': "01001001",
       'J': "01001010", 'K': "01001011", 'L': "01001100",
       'M': "01001101", 'N': "01001110", 'O': "01001111",
       'P': "01010000", 'Q': "01010001", 'R': "01010010",
       'S': "01010011", 'T': "01010100", 'U': "01010101",
       'V': "01010110", 'W': "01010111", 'X': "01011000",
       'Y': "01011001", 'Z': "01011010"}

LOW = {'a': "01100001", 'b': "01100010", 'c': "01100011",
       'd': "01100100", 'e': "01100101", 'f': "01100110",
       'g': "01100111", 'h': "01101000", 'i': "01101001",
       'j': "01101010", 'k': "01101011", 'l': "01101100",
       'm': "01101101", 'n': "01101110", 'o': "01101111",
       'p': "01110000", 'q': "01110001", 'r': "01110010",
       's': "01110011", 't': "01110100", 'u': "01110101",
       'v': "01110110", 'w': "01110111", 'x': "01111000",
       'y': "01111001", 'z': "01111010"}

NUM = {'0': '00110000', '1': '00110001', '2': '00110010',
       '3': '00110011', '4': '00110100', '5': '00110100',
       '6': '00110101', '7': '00110110', '8': '00110111',
       '9': '00111000'}

META = {'!': '00100001', '@': '01000000', '#': '00100011',
        '$': '00100100', '%': '00100101', '^': '01011110',
        '&': '00100110', '*': '00101010', '(': '00101000',
        ')': '00101001', '-': '00101101', '_': '01011111',
        '=': '00111101', '+': '00101011', '[': '01011011',
        '{': '01111011', ']': '01011101', '}': '01111101',
        '|': '01111100', ':': '00111010', ';': '00111011',
        "'": '00100111', '"': '00100010', ',': '00101100',
        '<': '00111100', '.': '00101110', '>': '00111110',
        '/': '00101111', '?': '00111111', ' ': '00100000',
        '\\': '01011100', '~': '01111110', '`': '01100000',
        '\n': '00001010'}


def encode(string: str, with_space=True) -> str:
    encoded = ''
    for character in string.strip():
        for dictionary in [CAP, LOW, NUM, META]:
            if character in dictionary:
                if with_space:
                    encoded += dictionary[character] + ' '
                else:
                    encoded += dictionary[character]
                break
    return encoded.strip()


def decode(string: str) -> str:
    string = string.strip()
    decoded = ''
    it_has_spaces = True
    binaries = []
    for character in string:
        if character not in '0 1':
            raise ValueError('The string to be decoded must only contain 1s, 0s '
                             'or spaces.')
    if ' ' not in string:
        it_has_spaces = False
    if it_has_spaces:
        binaries = string.split()
    else:
        for i in range(int(len(string) / 8)):
            binary = string[:8]
            binaries.append(binary)
            string = string[8:]
    for binary in binaries:
        for dictionary in [CAP, LOW, NUM, META]:
            for character in dictionary:
                if dictionary[character] == binary:
                    decoded += character
                    break
    return decoded if decoded else None


if __name__ == '__main__':
    root = Tk()
    app = BinaryTranslator(root, relief='flat', padding='8')
    app.grid(column=0, row=0, sticky='NEWS')
    root.wm_iconbitmap('binary.ico')
    root.title('Binary Code Translator')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    ttk.Style().configure('TLabel', background='lightgreen')
    ttk.Style().configure('TLabel', font=('courier', 14, 'bold'))
    ttk.Style().configure('TButton', font=('courier', 12, 'bold'))
    ttk.Style().configure('TFrame', background='lightgreen')
    root.mainloop()
