import webbrowser
import subprocess
import GMFF

def parse_command(command_action, argument=""):

  if command_action[0:4]=="web!":
    open_link(command_action[5:])
  elif command_action[0:4]=="web?":
    open_link_with_search(command_action[5:], argument)
    GMFF.speak("Pesquisando " + argument)
  elif command_action[0:4]=="path":
    open_program(command_action[5:])
    GMFF.speak("Abrindo " + argument)
  elif command_action=='commands':
    reload_commands()
    GMFF.speak("Atualizado")


def open_link_with_search(link, argument=""):
  print(f'{link}/search?q={argument}')
  webbrowser.get('windows-default').open_new(f'{link}/search?q={argument}')

def open_link(link):
  webbrowser.get('windows-default').open_new(f'{link}')

def open_program(path):
  subprocess.Popen([path, '-new-tab'])

def reload_commands():
  GMFF.read_commands_file()