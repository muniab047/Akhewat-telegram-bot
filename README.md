## Project Title
**Akhewat Telegram Bot**

## Description
Akhewat Telegram Bot is a smart Telegram bot designed to enhance students' learning experiences by providing easy access to a wide range of educational materials. From course outlines to textbooks and lecture videos, this bot serves as a comprehensive resource hub for students, helping them manage their studies effectively. To optimize data retrieval, the bot uses a Telegram channel as a database for file storage, allowing for faster access to resources by forwarding files rather than uploading them and PostgreSQL for persistent state managment.

## Installation Instructions

### Prerequisites
- Python 3.8 or higher
- A Telegram bot token (can be obtained by talking to [BotFather](https://t.me/botfather) on Telegram)
- PostgreSQL for the database
- Virtual environment tool (optional but recommended)

### Project Structure
```markdown
Akhewat-telegram-bot/  
├── core/  
    ├──const.py  
├── data/
    ├── button_id_map.py
├── infrastructure/  
    ├──handlers  
       ├── keyboaed_button_handlers.py  
       ├── state_handlers.py  
    ├── bot_handlers.py  
    ├── state_action_map.py  
├── main.py              
├── postgres.py        
├── requirements.txt   
├── vercel.json         
└── README.md 

```        


### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Akhewat-telegram-bot.git
    cd Akhewat-telegram-bot
    ```

2. Set up a virtual environment (optional):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables by configuring the `.env` file with your bot's `TOKEN` and other necessary credentials (like the database).

5. Start the bot:
    ```bash
    python main.py
    ```

## Usage

### Bot Commands
- **/start**: Starts interaction with the bot.

The bot also responds to keyboard buttons and inline button clicks, facilitating access to course material.

### Example Command
Start the bot and interact with it by typing `/start` in your Telegram client.

## Features
- **Comprehensive Course Access**: Quickly retrieve course outlines, lecture notes, textbooks, exams, and video resources across various subjects.
- **User-Friendly Interface**: Simple and intuitive commands for users to easily navigate and access materials.
- **Real-Time Updates**: Leverages webhook integration with Telegram for instant notifications and responses.
- **Persistent Data Storage**: Utilizes PostgreSQL for secure and reliable data management, ensuring users' access to the latest content.
- **Multi-Subject Support**: Covers a wide range of subjects, catering to diverse academic needs and preferences.
