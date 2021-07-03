# Instala biblitecas
def Bibliotecas():
    import os
    os.system('pip3 install keyboard')
    print('Biblioteca keyboard instalada com sucesso')
    os.system('pip3 install time')
    print('Biblioteca time instalada com sucesso')
    os.system('pip3 install tkinter')
    print('biblioteca tkinter instalada com sucesso')
    os.system('pip3 install bs4')
    os.system('pip3 install beautifulsoup')
    print('Biblioteca BeautifulSoup instalado com sucesso')
    os.system('pip3 install webdrive')
    print('Biblioteca Webdriver instalado com sucesso')
    os.system('pip3 install selenium')
    print('Biblioteca Selenium instalado com sucesso')
    os.system('pip3 install pathlib')
    print('Biblioteca Pathlib instalado com sucesso')
    os.system('pip3 install Path')
    print('Biblioteca Path instalado com sucesso')
    os.system('pip3 install PIL')
    os.system('pip3 install Image')
    os.system('pip3 install ImageTk')
    os.system('pip3 install paramiko')
    os.system('pip3 install SSHClient')


import os
#Bibliotecas()

import paramiko
from paramiko import SSHClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import keyboard as kb
import time
import tkinter as tk
from PIL import Image, ImageTk

url = ''


# Encerrar alguns processos do windows
def Encerrar_Processos():
    os.system("taskkill /f /im Spotify.exe")
    os.system("taskkill /f /im MicrosoftEdge.exe")
    os.system("taskkill /f /im MicrosoftEdgeCP.exe")
    os.system("taskkill /f /im MicrosoftEdgeSH.exe")
    os.system("taskkill /f /im GoogleCrashHandler.exe")
    os.system("taskkill /f /im GoogleCrashHandler64.exe")
    os.system("taskkill /f /im ReviverSoft Service Smart Monitor.exe")
    os.system("taskkill /f /im ReviverSoftSmartMonitor.exe")
    os.system("taskkill /f /im mqsvc.exe")
    os.system("taskkill /f /im helper.exe")
    os.system("taskkill /f /im Micdisrosoft.Photos.exe")
    os.system("taskkill /f /im YourPhone.exe")
    os.system("taskkill /f /im ApplicantionFrame.exe")
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im spoolsv.exe")
    os.system("taskkill /f /im SecurityHealthService.exe")
    os.system("taskkill /f /im SecurityHealthSystray.exe")
    os.system("taskkill /f /im ctfmon.exe")
    os.system("taskkill /f /im RuntimeBroker.exe")
    os.system("taskkill /f /im utweb.exe")
    os.system("taskkill /f /im svchost.exe")
    os.system("taskkill /f /im TextInputHost.exe")
    os.system("taskkill /f /im winStore.App.exe")
    os.system("taskkill /f /im video.UI.App.exe")
    os.system("taskkill /f /im taskhostw.exe")
    os.system("taskkill /f /im SearchApp.exe")
    os.system("taskkill /f /im dllhost.exe")
    os.system("taskkill /f /im MicrosoftEdgeCP.exe")
    os.system("taskkill /f /im browser_broker.exe")
    os.system("taskkill /f /im Cortana")
    os.system("taskkill /f /im AnyDesk.exe")
    os.system("taskkill /f /im RvRvpnGui.exe")
    os.system("taskkill /f /im hamachi-2-ui.exe")

    result = input('Deseja manter o discord? s/n ')

    if result == 'n':
        os.system("taskkill /f /im Discord.exe")

# Abre o google chrome
def Navegador():

    os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe" ' + url)
    os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" ' + url)

    # option = Options()
    # option.headless = True
    # driver = webdriver.Chrome()

    # driver.get(url)


# Abrir piano e tocar o arpejo de "Pra ser Sincero"
def Piano():
    global url
    url = 'https://www.musicca.com/pt/piano'

    # Encerrar_Processos()  # Chama a função que encerrar alguns processos
    Navegador() # Chama a função qu abre o navegador

    time.sleep(10)
    print('Começando a tocar')

    # Arpejo da musica "Pra ser sincero"
    kb.press_and_release('x'), time.sleep(0.4), kb.press_and_release('e'), time.sleep(0.4), kb.press_and_release('y'), time.sleep(0.4)
    kb.press_and_release('u'), time.sleep(0.4), kb.press_and_release('9'), time.sleep(0.4), kb.press_and_release('u'), time.sleep(0.4)
    kb.press_and_release('y'), time.sleep(0.4), kb.press_and_release('e'), time.sleep(0.4), kb.press_and_release('r'), time.sleep(0.4)
    kb.press_and_release('w'), time.sleep(0.4), kb.press_and_release('r'), time.sleep(0.4), kb.press_and_release('y'), time.sleep(0.4)
    kb.press_and_release('6')
    time.sleep(2)
    kb.press_and_release('´'), time.sleep(0.4), kb.press_and_release('9'), time.sleep(0.4), kb.press_and_release('´'), time.sleep(0.4)
    kb.press_and_release('f'), time.sleep(0.4), kb.press_and_release('v'), time.sleep(0.4), kb.press_and_release('f'), time.sleep(0.4)
    kb.press_and_release('´'), time.sleep(0.4), kb.press_and_release('p'), time.sleep(0.4), kb.press_and_release('´'), time.sleep(0.4)
    kb.press_and_release('p'), time.sleep(0.4), kb.press_and_release('o'), time.sleep(0.4), kb.press_and_release('9'), time.sleep(0.4)
    kb.press_and_release('u')


# abre o site fast.com
def SpeedTeste():
    global url
    url = 'https://www.fast.com'

    Navegador(), time.sleep(15)


# tirar print
def Print():
    print = input('Qual o nome da imagem? ')
    kb.press_and_release('Print Screen'), time.sleep(3)
    kb.press_and_release('win'), time.sleep(7)
    kb.write('paint'), time.sleep(7)
    kb.press_and_release('enter'), time.sleep(15)
    kb.press_and_release('ctrl+v'), time.sleep(0.5),
    kb.press_and_release('ctrl+s'), time.sleep(15)
    kb.write(print)
    kb.press_and_release('ctrl+l')
    kb.write('desktop'), time.sleep(3)
    kb.press_and_release('enter')
    kb.press_and_release('enter')
    kb.press_and_release('enter'), time.sleep(0.5)
    kb.press_and_release('enter')
    kb.press_and_release('enter')

# Função que troca a saída de áudio

# Abre o overwatch (Não pode mexer no pc quando chamar a função)
def Overwatch():
    # os.popen('"C:\Program Files (x86)\Overwatch\Overwatch Launcher.exe" --productcode=pro"')
    os.popen('"C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe"')

    print('Encerrando processos')
    Encerrar_Processos()
    
    os.popen('"C:/Program Files\Realtek\Audio\HDA\RAVCpl64.exe"')
    
    print('Em 60 segundo os proximo comando será executado!')
    
    


# Tocar Fátima
def Fatima():
    global url
    url = 'https://www.youtube.com/watch?v=4uBjd6HfCI4'

    class Fatima(tk.Frame):
        def __init__(self, fatima=None):
            super().__init__(fatima)
            self.fatima = fatima
            self.pack()
            self.Widget_Fatima()

        def Widget_Fatima(self):
            self.letra = tk.Button(self)
            self.letra['text'] = '''Vocês esperam uma intervenção divina
                                    Mas não sabem que o tempo agora está contra vocês
                                    Vocês se perdem no meio de tanto medo
                                    De não conseguir dinheiro pra comprar sem se vender
                                    E vocês armam seus esquemas ilusórios
                                    Continuam só fingindo que o mundo ninguém fez
                                    Mas acontece que tudo tem começo
                                    E se começa um dia acaba, eu tenho pena de vocês
                                    E as ameaças de ataque nuclear
                                    Bombas de nêutrons não foi Deus quem fez
                                    Alguém, alguém um dia vai se vingar
                                    Vocês são vermes, pensam que são reis
                                    Não quero ser como vocês
                                    Eu não preciso mais, mais mais mais
                                    Eu já sei o que eu tenho que saber
                                    E agora tanto faz
                                    Três crianças sem dinheiro e sem moral
                                    Não ouviram a voz suave que era uma lágrima
                                    E se esqueceram de avisar pra todo mundo
                                    Ela talvez tivesse um nome e era Fátima
                                    E de repente o vinho virou água
                                    E a ferida não cicatrizou
                                    E o limpo se sujou
                                    E no terceiro dia ninguém ressuscitou
                                    E no terceiro dia ninguém ressuscitou
                                    E no terceiro dia ninguém ressuscitou'''
            self.letra.pack(side='top')

    Navegador()

    rot = tk.Tk()
    ap = Fatima(fatima=rot)
    ap.mainloop()


# Pacotes do chrome
def Pacotes():
    i = 0
    while i == 0:

        so = input(str('Escolha o S.O. \nlinux64 \nmac64 \nwin32\n'))

        if so == 'linux64' or so == 'mac64' or so == 'win32':

            os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe" https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_'+ so + '.zip')
            os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_'+ so +'.zip')

            i = 1
        else:
            print('Voce digitou um S.O. que não corresponde com o pedido acima')

        if so == 'Fundo':
            Fundo()

    def Button_Hey():
        hi_there = tk.Button('')
        hi_there["text"] = "Hello World\n(click me)"
        hi_there["command"] = print('Oi')
        hi_there.pack()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        image = ImageTk.PhotoImage(Image.open("background.png"))
        #image = image.subsample(1, 1)

        label_image = tk.Label(image=image)
        label_image.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        tk.Label(form, text="Konnichiwaaaaaaaaaaa", bg='gray', fg='white').place(x=460, y=400)
        self.create_widgets()
        self.master = master
        self.pack()


    def create_widgets(self):

        self.hi_there = tk.Button(text="Hello World ", command=self.say_hi).place(x=80, y=20)

        self.Piano = tk.Button(text="      Piano      ", command=Piano).place(x=80, y=70)

        self.Servidor = tk.Button(text=" Abrir a Kali  ", command=self.Servidor).place(x=80, y=120)

        self.Conexao = tk.Button(text='Teste de conexão', command=SpeedTeste).place(x=220, y=20)

        self.Fatima = tk.Button(text='Fátima', command=Fatima).place(x=220, y=70)

        self.Overwatch = tk.Button(text='Overwatch', command=Overwatch).place(x=220, y=120)

        self.Encerrar_Processos = tk.Button(text='Encerrar processos', command=Encerrar_Processos).place(x=80, y=170)

        self.Biblitecas = tk.Button(text='Install bibiliotecas', command=Bibliotecas).place(x=220, y=170)

        self.quit = tk.Button(text="QUIT", fg="red", command=self.master.destroy).place(x=500, y=440)

        #self.Resultados = tk.Label(text='Oi', pady=20).place(x=550, y=20)

        form.mainloop()

    def say_hi(self):
        print("hi there, everyone!")

    # Abrir cmd e conecta com a Kalli
    def Servidor(self):
        class SSH:  # Conecta com o servidor via SSH
            def __init__(self):
                self.ssh = SSHClient()
                self.ssh.load_system_host_keys()
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect(hostname='192.168.1.16', port='1337', username='root', password='')

            def exec_cmd(self, cmd):
                stdin, stdout, stderr = self.ssh.exec_command(cmd)
                if stderr.channel.recv_exit_status() != 0:
                    print(stderr.read(), 'Conectado')
                else:
                    print(stdout.read(), 'Não conectou')

        if __name__ == '__main__':
            ssh = SSH()
            # comando = ssh.exec_cmd('ls')
            # comando = ssh.exec_cmd('python /root/luciano/rsync_recebe.py')
            log = ssh.exec_cmd('python3 /root/luciano/rsync_recebe.py')
            str(log)
            print(log)

        global Results  # Esta variavel é para mostrar o resultados na insteface gráfica (Label results)

'''
        Results = ssh.exec_cmd('ls')
        #type(Results)
        #print(Results, 'MEEEEEEEERDA')

        mostrar = ''
        for i in range(Results):
            mostrar = mostrar + Results


        self.Resultados = tk.Label(height=15, width=48, text='Oi').place(x=550, y=20), time.sleep(3)
        #self.Resultados = tk.Label(text=Results).place(x=550, y=20), time.sleep(5)
        #ssh.exec_cmd('rsync --version')'''


form = tk.Tk()
form.title("My amazing world")
form.geometry('1000x500')
form.configure(background='gray')
form = Application(master=form)
form.mainloop()

def Fundo():
    for i in range(0, 1):
        Funcao = globals()
        fazer = input('O que deseja fazer meu caro? ')

        Funcao[fazer]()

        i = 0


Fundo()
