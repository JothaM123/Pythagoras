# Imports
from rich import print

#Functions
def add(n1,n2):
    print(n1+n2)
    print("")    

def subtract(n1,n2):
    print(n1-n2)
    print("")

def multiply(n1,n2):
    print(n1*n2)
    print("")

def divide(n1,n2):
    print(n1/n2)
    print("")

def power(n1,n2):
    print(n1**n2)
    print("")

def help():
    print("""
[medium_spring_green]
╭─COMMANDS : ─────────╮                                                               
│ [turquoise2]add(n1,n2)[/turquoise2]          │
│                     │ 
│ [turquoise2]subtract(n1,n2)[/turquoise2]     │
│                     │
│ [turquoise2]multiply(n1,n2)[/turquoise2]     │
│                     │
│ [turquoise2]divide(n1,n2)[/turquoise2]       │
│                     │
│ [turquoise2]power(n1,n2)[/turquoise2]        │
│                     │
│ [turquoise2]help()[/turquoise2]              │                                                               
╰─────────────────────╯   
[/medium_spring_green]   
    """)

# Welcome text
print("[purple]Pythagoras v1.0[/purple]")
print("[cyan1]Pythagoras is a very simple scripting language built with Python for doing basic math[/cyan1]\n")

# Scripting area

while 1:
    try:
        
        command = input("@pythagoras>Pythagoras$")
        exec(command)
    
    except:
        print("[red]Error, please try again![/red]\n")