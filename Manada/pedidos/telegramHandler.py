from os import environ
import telegram_send
import imgkit
def sendMessage(body, id):
    config = imgkit.config(wkhtmltoimage=('bin/wkhtmltoimage'))
    options = {'format':'jpg'}
    img = imgkit.from_url("http://www.manadafoodhouse.com.br/carrinho/detail/"+id, 'img-'+id+'.jpg', options=options, config=config)
    with open('img-'+id+'.jpg', "rb") as f:
        telegram_send.send(conf="telegramConf",messages=[body], images=[f])
