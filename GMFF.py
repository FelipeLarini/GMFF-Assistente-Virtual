import speech_recognition as sr 
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
import json
from module import OpenModule
from module import MusicModule
from module import AlarmModule

recognizer = sr.Recognizer()
LISTENING_SOUND = AudioSegment.from_wav("bip.wav")
tts_engine = pyttsx3.init()
VOICE_COMMANDS = []

def read_commands_file():
  global VOICE_COMMANDS
  with open('commands.json', 'rb') as commands_file:
    commands = json.load(commands_file)
    VOICE_COMMANDS = commands['commands']

read_commands_file()


def speak(text):
  if tts_engine._inLoop:
    tts_engine.endLoop()
  tts_engine.say(text)
  tts_engine.runAndWait()

def listen():
  play(LISTENING_SOUND)
  with sr.Microphone() as source: 
    audio = recognizer.listen(source, None, 5)  
    voice_data = ''
    try:
      voice_data = recognizer.recognize_google(audio, language="pt-BR").lower()  
    except sr.UnknownValueError: 
      speak("Desculpe, não entendi")
    except sr.RequestError:
      speak("Desculpe, o serviço está offline")

    print("GMFF>> ", voice_data.lower()) 
    if voice_data:
      success = check_commands(voice_data)
      if not success:
        speak("Não consegui entender o comando")

def check_command_matching(term, command):
  if term.strip() == command.strip():
    return True
  return False

def run_commands(command_type, command_action, argument, when):
  if (command_type=="abrir" or command_type=="fechar"):
    OpenModule.parse_command(command_action, argument)
    return True
  if command_type=="musica":
    MusicModule.parse_command(command_action, argument)
    return True
  if command_type=="alarme":
    AlarmModule.parse_command(command_action, argument, when)
    return True

  return False
  
def extract_argument(command_text, voice_command):
  splitted_text = command_text.split(voice_command.replace('*', '') , 1)
  
  argument = ''
  if len(splitted_text) > 1:
    argument = splitted_text[1]
  else:
    argument = splitted_text[0]

  return argument

def check_commands(command_text):
  for command_section_list in VOICE_COMMANDS:
    for command_section, commands in command_section_list.items():
      for index, command in enumerate(commands): 
        for voice_command, command_action in command.items():
          argument = ''
          when = ''
          if '#' in voice_command: 
            argument, when = AlarmModule.extract_argument_with_time(
              command_text, voice_command, command_action['time_indicator'])
          elif '*' in voice_command: 
            argument = extract_argument(command_text, voice_command)
          voice_command = voice_command.replace('*', argument).replace('#', when) 
          found_action = check_command_matching(voice_command, command_text)
         
          if found_action:
            try:
              return run_commands(command_section, command_action, argument, when)
            except:
              speak(f"Ocorreu um problema no comando {voice_command}. Tente de novo")
              return False
  return False