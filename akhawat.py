from telegram import KeyboardButton , ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import requests

TOKEN = "6625557391:AAEVaxlCfuBsZCA_eLu2TH_kl5O6oL1fMVI"


def start(update, context):
    show_orginal_buttons(update, context)


def show_orginal_buttons(update, context):
    buttons =[
        [KeyboardButton("📚 Course Materials"), KeyboardButton("💡 Get information")],
        [KeyboardButton("✏️📊 GPA & CGPA calculator"), KeyboardButton("🎉 Entertainment")],
        [KeyboardButton("🌱💪 Skill Development"), KeyboardButton("🎓📝 Exit exam")],
        [KeyboardButton("📚🔍 Data gathering"), KeyboardButton("E-student")]
        
    ]
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True )
    update.message.reply_text('choose an option: ', reply_markup= reply_markup)
    context.user_data['state']= "state original"

def show_course_materials(update, context):
    buttons=[
        [KeyboardButton("🆕 Freshman year")],
        [KeyboardButton("✌🏼 Sophomore Year")],
        [KeyboardButton("🔮 Junior Year")],
        [KeyboardButton("🎉 Senior Year")],
        [KeyboardButton("🎓 GC")],
        [KeyboardButton("⬅️ Back")]
    ]
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True )
    update.message.reply_text('choose an option: ', reply_markup= reply_markup)
    context.user_data['state']= "course materials"

def show_year(update, context):
    buttons=[
        [KeyboardButton("☝🏼📅 First"), KeyboardButton("📅✌🏼 Second")],
        [KeyboardButton("⬅️ Back")]
    ]

    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    update.message.reply_text('choose a semester', reply_markup= reply_markup)
    text= update.message.text
    if text== "🆕 Freshman year":
        context.user_data['state']= "freshman"
    elif text=="✌🏼 Sophomore Year":
        context.user_data['state']= "sophomore"
    elif text=="🔮 Junior Year":
        context.user_data['state']= 'junior'
    elif text=="🎉 Senior Year":
        context.user_data['state']= 'senior'
    elif text=="🎓 GC":
        context.user_data['state']= 'gc'
    else:
        pass
   
    
def show_freshman_first_semester(update, context):
     buttons=[
         [KeyboardButton("Applied I")],
         [KeyboardButton("General Physics")],
         [KeyboardButton("Civics & Ethics")],
         [KeyboardButton("General Chemistry")],
         [KeyboardButton("Communicative English")],
         [KeyboardButton("Introduction to computing")],
         [KeyboardButton("🔙 Back")]

     ]
     reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True)
     update.message.reply_text("choose a course", reply_markup=reply_markup)
     context.user_data['state']= "freshman first semester"


def show_appliedI(update, context):
    keyboard=[
        [InlineKeyboardButton("📚🎯Course outline", callback_data="applied_I_course_outline")],
        [InlineKeyboardButton("🎙️🖥️Lecture", callback_data='applied_I_lecture')],
        [InlineKeyboardButton("📖Text Book", callback_data="applied_I_course_outline")],
        [InlineKeyboardButton("📝🧠Exam", callback_data="applied_I_course_outline")],
        [InlineKeyboardButton("📓✍️Assignment", callback_data="applied_I_course_outline")],
        [InlineKeyboardButton("🎥Video", callback_data="applied_I_course_outline")],

    ]
    reply_markup= InlineKeyboardMarkup(keyboard)
    update.message.reply_photo(photo="https://t.me/andelus_database/4", reply_markup=reply_markup)

     


     
    


def button_click(update, context):
    query = update.callback_query
    button_clicked= query.data
    user_name= "https://t.me/andelus_database"

    message ='https://t.me/andelus_database/6'
    
    

    if button_clicked == 'applied_I_course_outline':
        id = [2,3,4,5,6]
        user_name = "https://t.me/andelus_database"  # Replace with the actual username
        chat_id= query.message.chat_id
        for i in id:
            file_path = f'{user_name}/{i}'

            try:
                query.message.bot.send_document(chat_id=chat_id, document=file_path)
            except:
                query.message.bot.send_photo(chat_id=chat_id, photo=file_path)
        
        






   
       
            
   
       

      


def button_handler(update, context):
    text = update.message.text
    state= context.user_data.get('state', "state original")

    if state == 'state original':
        if text== "📚 Course Materials":
            show_course_materials(update, context)
    if state == "course materials":
        if text== "🆕 Freshman year" or text=="✌🏼 Sophomore Year" or text=="🔮 Junior Year" or text=="🎉 Senior Year" or text=="🎓 GC" :
            show_year(update, context)
        else:
            show_orginal_buttons(update, context)
    if state == "sophomore" or state =="freshman" or state =='junior' or state =='senior' or state =='gc':
        if text=="⬅️ Back":
            show_course_materials(update,context)
        else:
            if state== "freshman":
                if text== "☝🏼📅 First":
                    show_freshman_first_semester(update, context)
                elif text == "⬅️ Back":
                    show_course_materials(update, context)
                else:
                    pass;
    else:
        pass

    if state== "freshman first semester":
        if text== "🔙 Back" :
            show_year(update,context) 
        else:
            show_appliedI(update, context)

            
        


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, button_handler))
    dp.add_handler(CallbackQueryHandler(button_click))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()