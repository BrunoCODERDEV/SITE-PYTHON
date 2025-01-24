# Tela inicial:
    # botão: iniciar chat
         # quando clicar no botão:
         # abrir um popup/modal/alerda
               # Titulo: bem-vindo ao Brunoletters
               # caixa de texto: escreva seu nome no chat
               # botão: entrar no chat
                      # quando clicar no botão
                      # fechar o popup
                      # sumir com o título
                      # sumir com o botão iniciar chat
                             # carregar o chat
                             # carregar o campo de enviar mensagem: "digite sua mensagem"
                             # botão enviar
                                     # quando clicar no botão enviar
                                     # enviar a mensagem
                                     # limpar a caixa de mensagem


# Flet 

# pacote de codigos : blibioteca python
    # Flask     = para cria site 
    # Django    = para cria site
    # Kivy      = para cria app
    # Tkinter   = para cria telas pos programas
    # Flet      = para cria site , app e programas de computador

# logica sempre para cria um app ou site 

# importa o flet 
import flet as ft 

# criar uma função principal para rodar o seu aplicativo
def main(pagina):
    
    # titulo
    titulo = ft.Text("Brunoletters")

    # websocket - tunel de comunicacao entre 2 usuarios

    def enviar_mensagem_tunel(mensagem):
        # executar tudo o que eu quero que aconteça para
        # todos os usuarios que receberem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

        # criar tubo, comando "pagina.pubsub.subscribe(enviar_mensagem_tunel)"

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        # "f" antes do texto dizendo que quer formatar esse texto e coloca esses valores dinamicos dentro do texto e pra pegar colocar o {} no usuario         
        # limpar a caixa de mensagem
        # append vem de adicionar, ele adiciona um item no final
        campo_enviar_mensagem.value = ""
        pagina.update()
        

    campo_enviar_mensagem = ft.TextField(label="digite aqui suas palavras", on_submit=enviar_mensagem)
     # on_submit forma para fazer enviar ao invés de clicar no enviar, clicar no enter + envio
    botao_enviar = ft.ElevatedButton("enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    # ft.Column
    
    # ft.Row

    chat = ft.Column()

    def entrar_inferno(evento):
        # fechar o popup
        popup.open = False
        # sumir com o titulo
        pagina.remove(titulo)
        # sumir com o botão iniciar chat
        pagina.remove(botao)
        # carregar o chat
        pagina.add(chat)
        # carregar o campo de enviar mensagem
        # carregar o botao enviar
        pagina.add(linha_enviar)

        # adicionar no chat a mensagem "alguém entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

       # criar o popup
    titulo_popup = ft.Text("bem-vindo ao inferno")
    caixa_nome = ft.TextField(label="digite o seu nome", on_submit=entrar_inferno)
    botao_popup = ft.ElevatedButton("entrar no inferno", on_click=entrar_inferno)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])
       

       # botão inicial
    def abrir_popup(evento):
        
        pagina.dialog = popup

        popup.open = True

        pagina.update()

    botao = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup, color = ft.Colors.with_opacity(0.5, '#ff0000'))
       

       # colocar os elementos na pagina
    pagina.add(titulo)
    pagina.add(botao)

# executar essa função com o flet
ft.app(main, view= ft.WEB_BROWSER)
