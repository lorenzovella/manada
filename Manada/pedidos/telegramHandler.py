from os import environ
import telegram_send
import imgkit
def sendMessage(body, id):
    config = imgkit.config('bin/wkhtmltopdf-linux-amd64')
    options = {'format':'png'}
    img = imgkit.from_url("http://www.manadafoodhouse.com/carrinho/detail/"+id, 'img-'+id+'.png', options=options, config=config)
    with open('img-'+id+'.png', "rb") as f:
        telegram_send.send(conf="telegramConf",messages=[body], images=[f])
