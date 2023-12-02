# GMFF-Assistente-Virtual

Esse projeto utiliza uma biblioteca de reconhecimento de voz para automatizar as ações que estão no arquivo ```commands.json```, dessa forma, é possível adicionar mais comandos
de voz no arquivo e o assistente irá conseguir executar essas ações sem precisar alterar o código.

Módulos:
 - **OpenModule**: abre sites, videos, ou programas e arquivos estipulados.
 - **MusicModule**: toque música de forma que não fique visível para você, tendo a opção de parar ou encerrar a música.
 - **AlarmModule**: adicione lembretes e os informa para o usuário.

-  **SpeechRecognition** — Biblioteca de reconhecimento de fala, com suporte para diversos engines e APIs, online e offline.
- **pyttsx3** — Uma biblioteca de conversão de texto em fala com Python. Ao contrário das bibliotecas alternativas, funciona offline e é compatível com Python 2 e 3.
- **PyDub** — Manipule áudio com uma interface simples e fácil de alto nível.
- **Pytube** — Pytube é uma biblioteca leve, Pythonic, livre de dependência (e utilitário de linha de comando) para baixar vídeos do YouTube.
- **python-vlc** — Bindings para manipular o player de vídeo VLC.
- **keyboard** — Tenha controle total do seu teclado com essa biblioteca.

 Instale as bibliotecas: 
  &nbsp; &nbsp;<div>- ```pip install SpeechRecognition``` </div>
  &nbsp; &nbsp;<div>- ```pip install PyAudio``` </div>
  &nbsp; &nbsp;<div>- ```pip install pyttsx3``` </div>
  &nbsp; &nbsp;<div>- ```pip install pydub``` </div>
  &nbsp; &nbsp;<div>- ```pip install Pytube``` </div>
  &nbsp; &nbsp;<div>- ```pip install keyboard``` </div>
  &nbsp; &nbsp;<div>- Download e instale o VLC versão 64bit (https://www.videolan.org/vlc/) para o player do MusicModule </div>
  &nbsp; &nbsp;<div>- ```pip install python-vlc``` </div> <br>  
3. Para rodar o assistente sem mostrar uma janela do terminal, abre o terminal na pasta do projeto e rode ```pythonw main.py```. 
  Então, você pode fechar essa janela do terminal (o programa está rodando em background) 
