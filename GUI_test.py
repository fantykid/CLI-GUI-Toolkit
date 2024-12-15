import PySimpleGUI as sg

text = sg.Text('test')
hello = sg.Button('hello',key='test') 
clear = sg.Button('clear')

layout =[[text],[hello,clear]]
window = sg.Window('My GUI',layout)

while True:
    event , value = window.read()
    print(event)
    if event == sg.WIN_CLOSED : break
window.close()