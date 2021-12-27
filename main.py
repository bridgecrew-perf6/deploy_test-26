from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#line傳給用戶
line_bot_api = LineBotApi('NQ8Ihq/Nb5Y3dVWADapsDO5xpzKzdysrFJfNz6IfPvWR+cFd7mCUgTFfF/+VAh+zYcqfxV10uSGcA7dJOY08x+p3uOS0rWv/ev73UNm875LHMvzIkNzJ+QR1Wgr4C5JfJLxAapjetCxjRXHn7y9etAdB04t89/1O/w1cDnyilFU=')
#line和主機的連接
handler = WebhookHandler('5edee00bac4ba1c19fd392928337f8e1')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
