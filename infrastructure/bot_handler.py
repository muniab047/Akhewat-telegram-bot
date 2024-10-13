from telegram import Bot
from infrastructure.handlers.keyboard_button_handlers import KeyboardButtonHandlers
from infrastructure.state_action_map import state_actions
from data.dictionary.button_id_map import button_id_map
class BotHandlers:

    async def start(update, context):
        await KeyboardButtonHandlers.show_orginal_buttons(update,context)




    async def button_handler(update, context):
        text = update.message.text
        state = context.user_data.get('state', "state original")
        
        
        if state in state_actions:
            await state_actions[state](update, context, text)
        else:
            await update.message.reply_text(text='State not recognized')


    async def button_click(update, context):
        query = update.callback_query
        button_clicked= query.data
        user_name= "https://t.me/ASTUMJ_Academics_Course_Material"
        user_name2="https://t.me/amljheyuiodcji"
        chat_id= query.message.chat_id
        TOKEN = "6625557391:AAEVaxlCfuBsZCA_eLu2TH_kl5O6oL1fMVI"
        bot = bot=Bot(token=TOKEN)
        

        button_actions = button_id_map

        if button_clicked in button_actions:
            action = button_actions[button_clicked]
            if isinstance(action, list):
                await KeyboardButtonHandlers.retrive_data(query, action, user_name, chat_id, button_clicked, bot)
            elif isinstance(action, str):
                await bot.send_message(chat_id=chat_id, text=action)
            elif isinstance(action, list) and all(isinstance(item, str) for item in action):
                for link in action:
                    await bot.send_message(chat_id=chat_id, text=link)

