 
import complex_calc as cc
import real_calc as rc
import view
import logger as log



 

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text.split('/start ')
 
    if len(msg) <= 1:
        await update.message.reply_text("Пример: /start 5+6i + 4+6i")
        return
    value_a=msg[1].split(' ')[0]
    
    value_op=msg[1].split(' ')[1]
    value_b=msg[1].split(' ')[2]
 
    if 'i' in value_a or 'i' in value_b:
        try:
            value_a_lst = list(map(int, value_a.replace('i', '').split('+')))
            value_b_lst = list(map(int, value_b.replace('i', '').split('+')))
            cc.init(value_a_lst, value_b_lst)
            result = cc.do_it(value_op)
            log_res = view.view_data_lst(result, "result")
            await update.message.reply_text(log_res)  
            log_str = f'{value_a} {value_op} {value_b} = {log_res}'
        except:
            await update.message.reply_text('Error')  
    else:
        try:
            value_a = int(value_a)
            value_b = int(value_b)
            rc.init(value_a, value_b)
            result = rc.do_it(value_op)
            await update.message.reply_text(view.view_data(result, "result"))  
            log_str = f'{value_a} {value_op} {value_b} = {result}'
        except:
            await update.message.reply_text('Error')  
    log.log_operation(log_str)

 
def button_click():
    app = ApplicationBuilder().token('5749932159:AAFxbBj9agGbBEFOzSIifzIELxhKzDorXfE').build()
    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == '__main__':
    button_click()

