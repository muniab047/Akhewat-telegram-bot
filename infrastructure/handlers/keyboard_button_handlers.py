import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from core.const import ENGINEERING_DEPARTMENTS


class KeyboardButtonHandlers:

    

    async def show_orginal_buttons(update, context):
        buttons =[
            [KeyboardButton("📚 Course Materials"), KeyboardButton("💡 Get information")],
            [KeyboardButton("✏️📊 GPA & CGPA calculator"), KeyboardButton("🎉 Entertainment")],
            [KeyboardButton("🌱💪 Skill Development"), KeyboardButton("🎓📝 Exit exam")],
            [KeyboardButton("📚🔍 Data gathering"), KeyboardButton("🌐 Usefull Sites")]
            
        ]
        reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True )
        await update.message.reply_text('choose an option: ', reply_markup= reply_markup)
        context.user_data['state']= "state original"

    async def show_year(update, context):
        buttons=[
            [KeyboardButton("✌🏼 Sophomore Year")],
            [KeyboardButton("🔮 Junior Year")],
            [KeyboardButton("🎉 Senior Year")],
            [KeyboardButton("🎓 GC")],
            [KeyboardButton("⬅️ Back")]
        ]
        reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True )
        await update.message.reply_text('choose an option: ', reply_markup= reply_markup)
        context.user_data['state']= "years"


    async def show_yearsd(update, context):
        buttons=[
            [KeyboardButton("☝🏼📅 First"), KeyboardButton("✌🏼📅 Second")],
            [KeyboardButton("⬅️ Back")]
        ]

        reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True)
        await update.message.reply_text('choose a semester', reply_markup= reply_markup)
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
    
    async def show_semester(update, context, state):
        buttons=[
            [KeyboardButton("☝🏼📅 First"), KeyboardButton("✌🏼📅 Second")],
            [KeyboardButton("⬅️ Back")]
        ]

        reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True)
        await update.message.reply_text('choose a semester', reply_markup= reply_markup)
        context.user_data['state']= state
        


    async def show_keyboard_button(update, context, courses, states):
        buttons=[]
        for course in courses:        
            buttons.append([KeyboardButton(course)])

        buttons.append([KeyboardButton("⬅️ Back")])

        reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True)
        await update.message.reply_text("choose a course", reply_markup=reply_markup)
        context.user_data['state']= states

    async def show_department_type(update, context, state):
        buttons=[
            [KeyboardButton('Pre')],
            [KeyboardButton("Applied Science")], 
            [KeyboardButton("Engineering")],
            [KeyboardButton("⬅️ Back")]
        ]
        reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard= True)
        await update.message.reply_text("choose", reply_markup=reply_markup)
        context.user_data['state']= state

    async def show_department_courses(update, context, text, year, course, semester,courses):
        if text == "Pharmacy":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context, courses, updatedState)
        elif text == "Applied Biology":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Applied Chemistry":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Industrial Chemistry":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Applied Physics":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Applied Mathematics":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Arcitecture":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Chemical Engineering":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Civil Engineering":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Computer Science Engineering":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Electronics and Communication":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Hydrolics":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Material Science Engineering":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Mechanical Enginnering":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Power and Control Engineering":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)
        elif text == "Software Engineering":
            updatedState =f'{year} {semester} semester {course}'
            await KeyboardButtonHandlers.show_keyboard_button(update, context,courses, updatedState)


    async def show_inlinekeyboard(update,course, photo ):
        
        keyboard=[
            [InlineKeyboardButton("📚🎯Course outline", callback_data= f'{course}_course_outline')],
            [InlineKeyboardButton("🎙️🖥️Lecture", callback_data= f'{course}_lecture')],
            [InlineKeyboardButton("📖Reference", callback_data= f'{course}_text_book')],
            [InlineKeyboardButton("📝🧠Questions", callback_data= f'{course}_exam')],
            #[InlineKeyboardButton("📓✍️Assignment", callback_data= f'{course}_assignment')],
            [InlineKeyboardButton("🎥Video", callback_data= f'{course}_video')],

        ]
        reply_markup= InlineKeyboardMarkup(keyboard)
        await update.message.reply_photo(photo= photo, reply_markup=reply_markup)


    async def show_skill_inlinekeyboard(update,course, photo ):
        
        keyboard=[
            [InlineKeyboardButton("📝 Description", callback_data= f'{course} description')],
            [InlineKeyboardButton("📚 Books", callback_data= f'{course} book')],
            [InlineKeyboardButton("👥 Clubs", callback_data= f'{course} club')],
            [InlineKeyboardButton("🌐 Sites", callback_data= f'{course} site')],
            [InlineKeyboardButton("🤔 Advisors", callback_data= f'{course} advisor')],
            [InlineKeyboardButton("🔄 Other", callback_data= f'{course} other')],

        ]
        reply_markup= InlineKeyboardMarkup(keyboard)
        await update.message.reply_photo(photo= photo, reply_markup=reply_markup)

    async def show_inlinekeyboard2(update,course, photo ):
        
        keyboard=[
            [InlineKeyboardButton("📚🎯Course outline", callback_data= f'{course}_course_outline')],
            [InlineKeyboardButton("🎙️🖥️Lecture", callback_data= f'{course}_lecture')],
            [InlineKeyboardButton("📖Reference", callback_data= f'{course}_text_book')],
            [InlineKeyboardButton("📝🧠 Questions", callback_data= f'{course}_exam')],
            #[InlineKeyboardButton("📓✍️Assignment", callback_data= f'{course}_assignment')],
            [InlineKeyboardButton("🎥Video", callback_data= f'{course}_video')],
            [InlineKeyboardButton("🛠️ Required Tool", callback_data= f'{course}_tool')],
            [InlineKeyboardButton("📝🔬Lab Exercise", callback_data= f'{course}_lab')],
            [InlineKeyboardButton("🚧 Project", callback_data= f'{course}_project')],
        

        ]
        reply_markup= InlineKeyboardMarkup(keyboard)
        await update.message.reply_photo(photo= photo, reply_markup=reply_markup)

    
    async def department_year_choice(update, context, department, courses, text):
        if text== "✌🏼 Sophomore Year":
            updatedState= f'{department} sophomore'               
            await KeyboardButtonHandlers.show_keyboard_button(update, context, courses, updatedState)
        elif text == "🔮 Junior Year":
            updatedState=f'{department} junior'
            await KeyboardButtonHandlers.show_semester(update, context, updatedState)
        elif text == "🎉 Senior Year":
            updatedState= f'{department} senior'
            await KeyboardButtonHandlers.show_semester(update, context, updatedState)
        elif text == "🎓 GC":
            updatedState= f'{department} gc'
            await KeyboardButtonHandlers.show_semester(update, context, updatedState)
        elif text == '⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState) 



    async def retrive_data(query, id, user_name, chat_id, file_name, bot):
        
        if id:
            await bot.send_message(chat_id=chat_id, text=f'here are {file_name}')
        else:
            await bot.send_message(chat_id=chat_id, text=f'coming soon')

        for i in id:
            file_path = f'{user_name}/{i}'
            try:
                await bot.send_document(chat_id=chat_id, document=file_path)
            except:
                try:
                    await bot.send_document(chat_id=chat_id, document=f'{file_path}?single')
                    
                except:
                    try:
                        await bot.send_photo(chat_id=chat_id, photo=file_path)
                        
                    except:
                        try:
                            await bot.send_photo(chat_id=chat_id, photo=f'{file_path}?single')
                        except:
                            try:
                                await bot.send_audio(chat_id=chat_id, audio=file_path)
                            except:
                                try:
                                    await bot.send_audio(chat_id=chat_id, audio=f'{file_path}?single')
                                except:
                                    try:
                                        await bot.send_video(chat_id=chat_id, video=file_path)
                                    except:
                                        try:
                                            await bot.send_video(chat_id=chat_id, video=f'{file_path}?single')
                                        except:
                                            try:
                                                await bot.send_message(chat_id=chat_id, text=file_path)
            
                                            except:
                                                    await bot.send_message(chat_id=chat_id, text=f'pass {i}')
                                                    continue

                    

        await bot.send_message(chat_id=chat_id, text=f'DONE')

