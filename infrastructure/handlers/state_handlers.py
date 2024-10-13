from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from infrastructure.handlers.keyboard_button_handlers import *
from core.const import *

class StateHandlers:
    
    async def handle_state_original(update, context, text):
        if text== "📚 Course Materials":
            updatedState= "department type"
            await KeyboardButtonHandlers.show_department_type(update, context, updatedState)
        elif text == '💡 Get information':
            updatedState='information'
            buttons=['ASTU Freshman Book','Instructor Info','Akhewat Advisors', 'Internship Info']
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState,)
        elif text=="✏️📊 GPA & CGPA calculator":
            await update.message.reply_text(text='under development')
        elif text=="🎉 Entertainment":
            await update.message.reply_text(text='under development')
        elif text=="🌱💪 Skill Development":
            updatedState='skills'
            buttons=[ "🔭🌌 Astronomy","🚙 Auto", '💻🏆 Competitive Programming', "🚀 Physics", "🤖🔧 Robotics", "💻🔨 Software Development"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState)
        elif text=="🎓📝 Exit exam":
            updatedState='exit exam department'
            buttons=['Engineering','Applied']
            await KeyboardButtonHandlers.show_keyboard_button(update,context,buttons,updatedState)
        elif text=="📚🔍 Data gathering":
            await update.message.reply_text(text='under development')
        elif text=='🌐 Usefull Sites':
            buttons=[[InlineKeyboardButton("To get Paid Books For Free", web_app=WebAppInfo(url="https://libgen.li/"))],
                    [InlineKeyboardButton("E-student", web_app=WebAppInfo(url="https://estudent.astu.edu.et/"))],
                    [InlineKeyboardButton("Chatgpt", web_app=WebAppInfo(url="https://poe.com/ChatGPT"))],
                    [InlineKeyboardButton("To get Paid Apps For Free", web_app=WebAppInfo(url="https://getintopc.com/?id=000444159142"))]]
                    
            reply_markup=InlineKeyboardMarkup(buttons)
            await update.message.reply_photo(photo='https://t.me/amljheyuiodcji/60',reply_markup=reply_markup)


    # Define other handler functions similarly...
    async def handle_exit_exam_department(update, context, text):
        if text == 'Engineering':
            updatedState = 'engineering exit exam'
            departments = ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        elif text == 'Applied':
            updatedState = 'applied exit exam'
            departments = APPLIED_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        elif text == '⬅️ Back':
            await KeyboardButtonHandlers.show_orginal_buttons(update, context)

    async def handle_engineering_exit_exam(update, context, text):
        if text=="⬅️ Back":
            updatedState='exit exam department'
            buttons=['Engineering','Applied']
            await KeyboardButtonHandlers.show_keyboard_button(update,context,buttons,updatedState)
        else:
            await update.message.reply_text('Under Development')


    async def handle_applied_exit_exam(update, context, text):
        if text=="⬅️ Back":
            updatedState='exit exam department'
            buttons=['Engineering','Applied']
            await KeyboardButtonHandlers.show_keyboard_button(update,context,buttons,updatedState)
        else:
            await update.message.reply_text('Under Development')

    async def handle_skills(update, context, text):
        if text == '💻🏆 Competitive Programming':
            await KeyboardButtonHandlers.show_skill_inlinekeyboard(update, 'competitive programming', 'https://t.me/amljheyuiodcji/61')
        elif text == '⬅️ Back':
            await KeyboardButtonHandlers.show_orginal_buttons(update, context)
        else:
            await update.message.reply_text(text='under development')

    async def handle_information(update, context, text):
        if text=='Instructor Info':
                updatedState='department catagory instructor'
                buttons=['Engineering', 'Applied']
                await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState)
        elif text=='Akhewat Advisors':
            await update.message.reply_text(text='Click the link Below \n\n https://docs.google.com/document/d/1zx-Tq7xSqVauDoYfYYgT8EZWpCRLdVDFxAOC_dMwEuU/edit?usp=sharing')
        elif text=='Internship Info':
            updatedState='department catagory internship'
            buttons=['Engineering', 'Applied']
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState)
        elif text=='ASTU Freshman Book':
            updatedState="freshman book language"
            buttons=['Amharic', 'Afaan Oromoo']
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState)
        elif text=="⬅️ Back":
            await KeyboardButtonHandlers.show_orginal_buttons(update,context)

    async def handle_freshman_book_language(update, context, text):
        if text=="Amharic":
                id=''
                await context.message.bot.send_document(chat_id=update.effective_chat.user.id , document=id)
        elif text==text=="Afaan Oromoo":
            id=''
            await context.message.bot.send_document(chat_id=update.effective_chat.user.id , document=id)
        elif text=="⬅️ Back":
            updatedState='information'
            buttons=['ASTU Freshman Book','Instructor Info','Akhewat Advisors', 'Internship Info']
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState,)

    async def handle_department_catagory_internship(update, context, text):
        if text == 'Engineering':
            updatedState = 'engineering department internship'
            departments = ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        elif text == 'Applied':
            updatedState = 'applied department internship'
            departments = APPLIED_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        elif text == '⬅️ Back':
            await KeyboardButtonHandlers.show_orginal_buttons(update, context)

    async def handle_engineering_department_internship(update, context, text):
        if text== "Architecture":
                await update.message.reply_text('https://drive.google.com/drive/folders/15pvDC_Ki3Gihaa9ej3gegnVbt1C5jFxR?usp=sharing')
        elif text== "Chemical Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1WdIN0u8nGUH1zz_J5wxfXKRtJs6KVBBP?usp=sharing')
        elif text== "Civil Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1Sng-ittuDqv-DuMzjScjZLm5Jm3Cxx7v?usp=sharing')
        elif text== "Computer Science Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1OIW9vrYP03Caq2mxE48Quh2COZzs5jHc?usp=sharing')
        elif text== "Electronics and Communication":
            await update.message.reply_text('https://drive.google.com/drive/folders/1M2QaN0QSuRoeCEU9cQvUzbYT67_NbBXj?usp=sharing')
        elif text== "Hydrolics":
            await update.message.reply_text('https://drive.google.com/drive/folders/1JOKrvN1VmGIppzN4As-VT-M_aYwfc4qq?usp=sharing')
        elif text== "Material Science Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1JDVYefW_SH0bTGlKzM5pNTGOohI0dMmx?usp=sharing')
        elif text== "Mechanical Enginnering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1A3VFTPImsV12529BlHonb9fx-xQgsFwJ?usp=sharing')
        elif text== "Power and Control Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/18VFgT437pdKUq9x_8s4rL_L4hPMt5eqT?usp=sharing')
        elif text== "Software Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1Z1zaXLQcrw7VZH1lMFgSwPIiGWonlzMI?usp=sharing')
        elif text=="⬅️ Back":
            updatedState='department catagory internship'
            buttons=['Engineering', 'Applied']
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState)

    async def handle_applied_department_internship(update, context, text):
        if text== "Pharmacy":
                await update.message.reply_text('https://drive.google.com/drive/folders/1w-E0p2mxWtLDeQEQo_73jcX56Eqz0uwe?usp=sharing')
        elif text== "Applied Biology":
            await update.message.reply_text('https://drive.google.com/drive/folders/1tk_AtA1vPVQFjTfCNz-wsKg29s-VjrTl?usp=sharing')
        elif text== "Applied Chemistry":
            await update.message.reply_text('https://drive.google.com/drive/folders/1ZkkLArn1dwgU-TK0GpQe3bQW4brxayK5?usp=sharing')
        elif text== "Applied Physics":
            await update.message.reply_text('https://drive.google.com/drive/folders/1au3ZIYHLcMyki20hKnfqwQ7GkZwJT7rV?usp=sharing')
        elif text== "Applied Mathematics":
            await update.message.reply_text('https://drive.google.com/drive/folders/1iDiGHeSAlPx1xuBD_efbjPeqbFiWUpwH?usp=sharing')
        elif text== "Industrial Chemistry":
            await update.message.reply_text('https://drive.google.com/drive/folders/1o9RAoi9YcNV3mj1QDvrHzQ7nqW1vw28C?usp=sharing')
        elif text=="⬅️ Back":
            updatedState='department catagory internship'
            buttons=['Engineering', 'Applied']
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState)


    async def handle_department_catagory_instructor(update, context, text):
        if text == 'Engineering':
                updatedState="engineering department instructor"
                buttons= ENGINEERING_DEPARTMENTS
                await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState)
        elif text=="Applied":
            updatedState="applied department instructor"
            buttons= APPLIED_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState)
        elif text=="⬅️ Back":
            updatedState='information'
            buttons=['Instructor Info','Akhewat Advisors', 'Internship Info']
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState,)

    async def handle_engineering_department_instructor(update, context, text):
        if text== "Architecture":
                await update.message.reply_text('https://drive.google.com/drive/folders/1ZvKxQs34o8blWSk2Qx7e8HRnnfPOrjNT?usp=sharing')
        elif text== "Chemical Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1eBPaTbjHpvvTfVshLPpej7fgSo6mu_Qv?usp=sharing')
        elif text== "Civil Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1Th8ZenI2BzUrRn3fSF8ArzSVieu7hWh-?usp=sharing')
        elif text== "Computer Science Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1DfMwHgzS7J2l7FiSr78YqiUpr7NYUAp6?usp=sharing')
        elif text== "Electronics and Communication":
            await update.message.reply_text('https://drive.google.com/drive/folders/11G1gwstcl2yhChWsUD-acthIywrOlcV_?usp=sharing')
        elif text== "Hydrolics":
            await update.message.reply_text('https://drive.google.com/drive/folders/1wSHbGItDcdq41YsRIRC4zC8tpx8omaHZ?usp=sharing')
        elif text== "Material Science Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1isyUwBJLKxi-yJMqOavyVdfFAMZprjz7?usp=sharing')
        elif text== "Mechanical Enginnering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1c3NC6H6rvNT2KIP4akK8cNZp87GHl9nZ?usp=sharing')
        elif text== "Power and Control Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1FQFtm-NX8cnQf-UT150ayKetXhALPAV9?usp=sharing')
        elif text== "Software Engineering":
            await update.message.reply_text('https://drive.google.com/drive/folders/1ripUB-Op4cZsN0_7uDDpkmkfiidKJNtd?usp=sharing')
        elif text=="⬅️ Back":
            updatedState='department catagory instructor'
            buttons=['Engineering', 'Applied']
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState)

    async def handle_applied_department_instructor(update, context, text):
        if text== "Pharmacy":
                await update.message.reply_text('https://drive.google.com/drive/folders/1kTHIqcRPLRza2Xb8oFxCLmx4C5682wO1?usp=sharing')
        elif text== "Applied Biology":
            await update.message.reply_text('https://drive.google.com/drive/folders/1EcQZwM_SKM8fx-g9w8ZB1cIotRqXHDeu?usp=sharing')
        elif text== "Applied Chemistry":
            await update.message.reply_text('https://drive.google.com/drive/folders/1Hv6WfMuQbhIv-5QVA2cW-KgcMLEdLtGx?usp=sharing')
        elif text== "Applied Physics":
            await update.message.reply_text('https://drive.google.com/drive/folders/14eLK3dkiOSJLpu7s1FjUazSGUDs9x17A?usp=sharing')
        elif text== "Applied Mathematics":
            await update.message.reply_text('https://drive.google.com/drive/folders/19HTAYpeRhg9_XbLFiMFdrfRuqoyjeBR1?usp=sharing')
        elif text== "Industrial Chemistry":
            await update.message.reply_text('https://drive.google.com/drive/folders/1djYT9gCiE0igfNVAOcN5L-fnXq16N7Un?usp=sharing')
        elif text=="⬅️ Back":
            updatedState='department catagory instructor'
            buttons=['Engineering', 'Applied']
            await KeyboardButtonHandlers.show_keyboard_button(update, context, buttons, updatedState)

    async def handle_department_type(update, context, text):
        if text == "Pre":
                updatedState='pre'
                await KeyboardButtonHandlers.show_semester(update, context, updatedState)
        elif text == "Engineering":
            updatedState= "engineering"
            catagory= ["School", "Department"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, catagory, updatedState)
        elif text == "Applied Science":
            updatedState= "applied"
            departments= APPLIED_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        elif text == '⬅️ Back':
            await KeyboardButtonHandlers.show_orginal_buttons(update, context)

    async def handle_applied(update, context, text):
        if text=="⬅️ Back":
            updatedState= "department type"
            await KeyboardButtonHandlers.show_department_type(update, context, updatedState)
        else:
            await update.message.reply_text(text='under development')


    async def handle_pre(update, context, text):
        if text == '☝🏼📅 First':
            updatedState= 'freshman first semester'
            courses= ['Applied I', "General Physics","Civics & Ethics","General Chemistry","Communicative English", "Introduction to computing"   ]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, courses, updatedState)

        elif text == '✌🏼📅 Second':
            updatedState='freshman second semester catagory'
            departmentType= ["Applied", "Engineering"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departmentType, updatedState)
        elif text=="⬅️ Back":
            updatedState= "department type"
            await KeyboardButtonHandlers.show_department_type(update, context, updatedState)


    async def handle_freshman_second_semester_catagory(update, context, text):
        if text=="Applied":
                updatedState= 'freshman second semester applied'
                courses=["Applied II", 
                        "Logic and Critical Thinking", 
                        "Introduction to Emerging Technology", 
                        "General Biology", 
                        'Basic Statistics']
                await KeyboardButtonHandlers.show_keyboard_button(update, context, courses, updatedState)
        elif text == "Engineering":
            updatedState= 'freshman second semester engineering'
            courses=["Applied II", 
                    "Fundamentals of programming",
                    "Introduction to Emerging Technology", 
                    "Basic Writing Skill", 
                    "Logic and Critical Thinking",
                    'Engineering Drawing' ]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, courses, updatedState)
        elif text== "⬅️ Back":
            updatedState= 'pre'
            await KeyboardButtonHandlers.show_semester(update, context, updatedState)

    async def handle_engineering(update, context, text):
        if text== "School":
                updatedState= "school"
                schools= ['Electrical and Computing', 'Civil and Architectural', 'Mechanical Material and Chemical'] 
                await KeyboardButtonHandlers.show_keyboard_button(update, context, schools, updatedState) 
        elif text =='Department':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        elif text ==  "⬅️ Back":
            updatedState= "department type"
            await KeyboardButtonHandlers.show_department_type(update, context, updatedState)

    async def handle_school(update, context, text):
        if text== 'Electrical and Computing':
                # updatedState= 'electrical school'
                # courses=['Applied III', 'Fundamental', 'Data Structure and Algorithm']
                # await KeyboardButtonHandlers.show_keyboard_button(update, context, courses, updatedState )
                await update.message.reply_text(text='under development')
        elif text == 'Civil and Architectural':
            # updatedState= 'civil school'
            # courses=['civil school courses']
            # await KeyboardButtonHandlers.show_keyboard_button(update, context, courses, updatedState )
            await update.message.reply_text(text='under development')
        elif text == 'Mechanical Material and Chemical':
            # updatedState= 'mechanical school'
            # courses = ['mechanical school courses']
            # await KeyboardButtonHandlers.show_keyboard_button(update, context, courses, updatedState )
            await update.message.reply_text(text='under development')
        elif text=="⬅️ Back":
            updatedState= "engineering"
            catagory= ["School", "Department"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, catagory, updatedState)

    async def handle_department(update, context, text):
        if text == "Architecture":
                updatedState= 'architecture'
                years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
                await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
        elif text == "Chemical Engineering" :
            updatedState= 'chemical'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
        elif text == "Civil Engineering" :
            updatedState= 'civil'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
        elif text == "Computer Science Engineering" :
            updatedState= 'computer science'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
        elif text == "Electronics and Communication" :
            updatedState= 'communication'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
        elif text == "Hydrolics" :
            updatedState= 'hydrolics'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
        elif text == "Material Science Engineering" :
            updatedState= 'material'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
        elif text == "Mechanical Enginnering" :
            updatedState= 'mechanical'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
        elif text == "Power and Control Engineering" :
            updatedState= 'power'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
        elif text == "Software Engineering" :
            updatedState= 'software'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
        elif text == '⬅️ Back':
            updatedState= "engineering"
            catagory= ["School", "Department"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, catagory, updatedState) 


    async def handle_architecture(update, context, text):
        # courses=['archtecture sophomore courses']
        # await department_year_choice(update, context, state, courses, text)
        if text=='⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        else:
            await update.message.reply_text(text='under development')


    async def handle_chemical(update, context, text):
        # courses=['archtecture sophomore courses']
        # await department_year_choice(update, context, state, courses, text)
        if text=='⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        else:
            await update.message.reply_text(text='under development')


    async def handle_civil(update, context, text):
        # courses=['archtecture sophomore courses']
        # await department_year_choice(update, context, state, courses, text)
        if text=='⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        else:
            await update.message.reply_text(text='under development')

    async def handle_computer_science(update, context, text):
        # courses=['archtecture sophomore courses']
        # await department_year_choice(update, context, state, courses, text)
        if text=='⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        else:
            await update.message.reply_text(text='under development')

    async def handle_communication(update, context, text):
        # courses=['archtecture sophomore courses']
        # await department_year_choice(update, context, state, courses, text)
        if text=='⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        else:
            await update.message.reply_text(text='under development')

    async def handle_hydrolics(update, context, text):
        # courses=['archtecture sophomore courses']
        # await department_year_choice(update, context, state, courses, text)
        if text=='⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        else:
            await update.message.reply_text(text='under development')

    async def handle_material(update, context, text):
        # courses=['archtecture sophomore courses']
        # await department_year_choice(update, context, state, courses, text)
        if text=='⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        else:
            await update.message.reply_text(text='under development')

    async def handle_mechanical(update, context, text):
        # courses=['archtecture sophomore courses']
        # await department_year_choice(update, context, state, courses, text)
        if text=='⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        else:
            await update.message.reply_text(text='under development')

    async def handle_power(update, context, text):
        # courses=['archtecture sophomore courses']
        # await department_year_choice(update, context, state, courses, text)
        if text=='⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        else:
            await update.message.reply_text(text='under development')

    async def handle_software(update, context, text):
        # courses=['archtecture sophomore courses']
        # await department_year_choice(update, context, state, courses, text)
        if text=='⬅️ Back':
            updatedState= 'department'
            departments= ENGINEERING_DEPARTMENTS
            await KeyboardButtonHandlers.show_keyboard_button(update, context, departments, updatedState)
        else:
            await update.message.reply_text(text='under development')

    async def handle_architecture_junior(update, context, text):
        if text== '☝🏼📅 First':
            # updatedState='architecture junior first semester'
            # courses= [ 'architecture junior first semester courses']
            # await KeyboardButtonHandlers.show_keyboard_button(update, context, courses,updatedState)
            await update.message.reply_text(text='under development')


        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'architecture'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)


    async def handle_chemical_junior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'chemical'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)


    async def handle_civil_junior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'civil'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_computer_science_junior(update, context, text):
        if text== '☝🏼📅 First':
                await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'computer science'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_communication_junior(update, context, text):
        if text== '☝🏼📅 First':
                await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'communication'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_hydrolics_junior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'hydrolics'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_material_junior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'material'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_mechanical_junior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'mechanical'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_power_junior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'power'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_software_junior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'software'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)
    async def handle_architecture_senior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'architecture'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_chemical_senior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'chemical'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_civil_senior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'civil'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_computer_science_senior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'computer science'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_communication_senior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'communication'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_hydrolics_senior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'hydrolics'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_material_senior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'material'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_mechanical_senior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'mechanical'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_power_senior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'power'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_software_senior(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'software'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_architecture_gc(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'architecture'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_chemical_gc(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'chemical'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_civil_gc(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'civil'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_computer_science_gc(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'computer science'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_communication_gc(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'communication'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_hydrolics_gc(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'hydrolics'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_material_gc(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'material'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_mechanical_gc(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'mechanical'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_power_gc(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'power'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_software_gc(update, context, text):
        if text== '☝🏼📅 First':
            await update.message.reply_text(text='under development')
        elif text== '✌🏼📅 Second':
            await update.message.reply_text(text='under development')
        elif text == '⬅️ Back':
            updatedState= 'software'
            years =["✌🏼 Sophomore Year","🔮 Junior Year","🎉 Senior Year", "🎓 GC"]
            await KeyboardButtonHandlers.show_keyboard_button(update, context, years, updatedState)

    async def handle_freshman_first_semester(update, context, text):
        if text== "⬅️ Back" :
                updatedState= 'pre'
                await KeyboardButtonHandlers.show_semester(update,context, updatedState) 
        elif text == 'Applied I':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'Applied_I','https://t.me/ASTUMJ_Academics_Course_Material/5')
        elif text == 'General Physics':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'General_Physics',"https://t.me/ASTUMJ_Academics_Course_Material/103" )
        elif text == 'Civics & Ethics':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'Civics_&_Ethics', 'https://t.me/ASTUMJ_Academics_Course_Material/299' )
        elif text == 'General Chemistry':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'General_Chemistry','https://t.me/ASTUMJ_Academics_Course_Material/235' )
        elif text == 'Communicative English':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'Communicative_English','https://t.me/ASTUMJ_Academics_Course_Material/355' )
        elif text == 'Introduction to computing':
            await KeyboardButton.show_inlinekeyboard2(update, 'Introduction_to_computing','https://t.me/ASTUMJ_Academics_Course_Material/174' )
        else:
            pass

    async def handle_freshman_second_semester_applied(update, context, text):
        if text== "⬅️ Back" :
            updatedState= 'pre'
            await KeyboardButtonHandlers.show_semester(update,context, updatedState) 
        elif text == 'Applied II':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'Applied_II','https://t.me/amljheyuiodcji/13')
        elif text == 'Introduction to Emerging Technology':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'emerging', 'https://t.me/amljheyuiodcji/15' )
        elif text == 'Logic and Critical Thinking':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'logic','https://t.me/amljheyuiodcji/17' )
        elif text == 'General Biology':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'biology','https://t.me/amljheyuiodcji/19' )
        elif text == 'Basic Statistics':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'statistics','https://t.me/amljheyuiodcji/20' )
        else:
            pass
    async def handle_freshman_second_semester_engineering(update, context, text):
        if text== "⬅️ Back" :
            updatedState= 'pre'
            await KeyboardButtonHandlers.show_semester(update,context, updatedState) 
        elif text == 'Applied II':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'engineering Applied_II','https://t.me/amljheyuiodcji/13')
        elif text == 'Fundamentals of programming':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'c++',"https://t.me/amljheyuiodcji/14" )
        elif text == 'Introduction to Emerging Technology':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'emerging', 'https://t.me/amljheyuiodcji/15' )
        elif text == 'Basic Writing Skill':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'writing','https://t.me/amljheyuiodcji/16' )
        elif text == 'Logic and Critical Thinking':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'logic','https://t.me/amljheyuiodcji/17' )
        elif text == 'Engineering Drawing':
            await KeyboardButtonHandlers.show_inlinekeyboard(update, 'drawing','https://t.me/amljheyuiodcji/18' )
        else:
            pass