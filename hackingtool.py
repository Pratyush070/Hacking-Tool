#!/usr/bin/env python3
# Version 1.1.0 (rich UI - purple theme)
import os
import sys
import webbrowser
from platform import system
from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.align import Align
from rich.text import Text
from rich import box
from rich.columns import Columns
from rich.rule import Rule
from rich.padding import Padding

from core import HackingToolsCollection
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phising_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_tools import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.webattack import WebAttackTools
from tools.wireless_attack_tools import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools

console = Console()

ASCII_LOGO = r"""
   ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄██████▄           ███      ▄██████▄   ▄██████▄   ▄█       
  ███    ███     ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███      ▀█████████▄ ███    ███ ███    ███ ███       
  ███    ███     ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀          ▀███▀▀██ ███    ███ ███    ███ ███       
 ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███                 ███   ▀ ███    ███ ███    ███ ███       
▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄           ███     ███    ███ ███    ███ ███       
  ███    ███     ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███          ███     ███    ███ ███    ███ ███       
  ███    ███     ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███          ███     ███    ███ ███    ███ ███▌    ▄ 
  ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀          ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ 
                                         ▀                                                                            ▀            
"""

tool_definitions = [
    ("Anonymously Hiding Tools", "🛡️"),
    ("Information gathering tools", "🔍"),
    ("Wordlist Generator", "📚"),
    ("Wireless attack tools", "📶"),
    ("SQL Injection Tools", "🧩"),
    ("Phishing attack tools", "🎣"),
    ("Web Attack tools", "🌐"),
    ("Post exploitation tools", "🔧"),
    ("Forensic tools", "🕵️"),
    ("Payload creation tools", "📦"),
    ("Exploit framework", "🧰"),
    ("Reverse engineering tools", "🔁"),
    ("DDOS Attack Tools", "⚡"),
    ("Remote Administrator Tools (RAT)", "🖥️"),
    ("XSS Attack Tools", "💥"),
    ("Steganograhy tools", "🖼️"),
    ("Other tools", "✨"),
    ("Update or Uninstall | Hackingtool", "♻️"),
]

all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager()
]


class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        header = Text()
        header.append(ASCII_LOGO, style="bold magenta")
        header.append("\n\n",)
        footer = Text.assemble(
            (" https://github.com/Z4nzu/hackingtool ", "bold bright_black"),
            (" | ",),
            ("Version 1.1.0", "bold green"),
        )
        warning = Text(" Please Don't Use For illegal Activity ", style="bold red")
        panel = Panel(
            Align.center(header + Text("\n") + footer + Text("\n") + warning),
            box=box.DOUBLE,
            padding=(1, 2),
            border_style="magenta"
        )
        console.print(panel)


def build_menu():
    table = Table.grid(expand=True)
    table.add_column("idx", width=6, justify="right")
    table.add_column("name", justify="left")

    for idx, (title, icon) in enumerate(tool_definitions):
        if idx == 17:
            label = "[bold magenta]99[/bold magenta]"
            name = f"[bold magenta]{icon} {title}[/bold magenta]"
        else:
            label = f"[bold magenta]{idx}[/bold magenta]"
            name = f"[white]{icon}[/white]  [magenta]{title}[/magenta]"
        table.add_row(label, name)

    top_panel = Panel(
        Align.center(Text("HackingTool — Main Menu", style="bold white on magenta"), vertical="middle"),
        style="magenta",
        padding=(0, 1),
        box=box.ROUNDED
    )
    menu_panel = Panel.fit(
        table,
        title="[bold magenta]Select a tool[/bold magenta]",
        border_style="bright_magenta",
        box=box.SQUARE
    )
    footer = Align.center(Text("Choose number and press Enter — 99 to exit", style="italic bright_black"))
    console.print(top_panel)
    console.print(menu_panel)
    console.print(Rule(style="bright_black"))
    console.print(footer)
    console.print("")


def choose_path():
    fpath = os.path.expanduser("~/hackingtoolpath.txt")
    if not os.path.exists(fpath):
        os.system("clear" if system() == "Linux" else "cls")
        build_menu()
        console.print(Panel("Setup path for tool installations", border_style="magenta"))
        choice = Prompt.ask("[magenta]Set Path[/magenta]", choices=["1", "2"], default="2")
        if choice == "1":
            inpath = Prompt.ask("[magenta]Enter Path (with Directory Name)[/magenta]")
            with open(fpath, "w") as f:
                f.write(inpath)
            console.print(f"[green]Successfully Set Path to:[/green] {inpath}")
        else:
            autopath = "/home/hackingtool/"
            with open(fpath, "w") as f:
                f.write(autopath)
            console.print(f"[green]Your Default Path Is:[/green] {autopath}")
            sleep(1)
    return fpath


def interact_menu():
    while True:
        try:
            build_menu()
            choice = IntPrompt.ask("[magenta]Choose a tool to proceed[/magenta]", default=0)
            if choice == 99:
                console.print(Panel("[bold white on magenta]Goodbye — Come Back Safely[/bold white on magenta]"))
                break
            if 0 <= choice < len(all_tools):
                tool = all_tools[choice]
                name = tool_definitions[choice][0]
                console.print(Panel(f"[bold magenta]{tool_definitions[choice][1]}  Selected:[/bold magenta] [white]{name}"))
                try:
                    fn = getattr(tool, "show_options", None)
                    if callable(fn):
                        fn()
                    else:
                        console.print(f"[yellow]Tool '{name}' has no interactive menu (show_options).[/yellow]")
                except Exception as e:
                    console.print(Panel(f"[red]Error while opening {name}[/red]\n{e}", border_style="red"))
                if not Confirm.ask("[magenta]Return to main menu?[/magenta]", default=True):
                    console.print(Panel("[bold white on magenta]Exiting...[/bold white on magenta]"))
                    break
            else:
                console.print("[red]Invalid selection. Pick a number from the menu.[/red]")
        except KeyboardInterrupt:
            console.print("\n[bold red]Interrupted by user — exiting[/bold red]")
            break

def main():
    try:
        if system() == "Linux":
            fpath = choose_path()
            with open(fpath) as f:
                archive = f.readline().strip()
                os.makedirs(archive, exist_ok=True)
                os.chdir(archive)
                AllTools().show_info()
                interact_menu()
        elif system() == "Windows":
            console.print(Panel("[bold red]Please run this tool on a Debian/Linux system for best results[/bold red]"))
            if Confirm.ask("Open guidance link in your browser?", default=True):
                webbrowser.open_new_tab("https://tinyurl.com/y522modc")
            sleep(2)
        else:
            console.print("[yellow]Please Check Your System or Open New Issue ...[/yellow]")
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting ..!!![/bold red]")
        sleep(1)


if __name__ == "__main__":
    main()
