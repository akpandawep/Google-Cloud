import os
from subprocess import Popen, PIPE

# Define the run_command function to execute shell commands
def run_command(command):
    process = Popen(command, stdout=PIPE, shell=True)
    output, _ = process.communicate()
    return output.decode('utf-8')

# Environment variables
env_vars = {
    'ADMIN': '6141937812',
    'API_HASH': 'c149386dcd58a40fa9fe60e632e161d4',
    'API_ID': '22287041',
    'BOT_TOKEN': '7116242057:AAE8gJtwFjLDtaBZ2y3AYhFqlex4ZWzh8wI',
    'DB_NAME': 'Cluster0',
    'DB_URL': 'mongodb+srv://filerenamebot:QEycfrD2yCwRHaPc@cluster0.zfr3afv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
    'FILE_STORE_CHANNEL': '-1001869105126',
    'FORCE_SUB': 'pandawep',
    'LOG_CHANNEL': '-1001869105126',
    'START_PIC': 'https://graph.org/file/b3125068739885e7109db.jpg',
    'WEBHOOK': 'False',
    'PORT' : '8070',
    'PYTHON_VERSION': '3.10.8'
}

# Setting environment variables
for key, value in env_vars.items():
    os.environ[key] = value

# netstat command to check port 8070
output = run_command('netstat -tuln | grep 8070')
print(output)

# Clone the GitHub repository
run_command('git clone https://github.com/akpandawep/RenameXbot')

# Change directory to the cloned repository
os.chdir('RenameXbot')

# Install requirements
run_command('pip install -r requirements.txt')

# Run the bot
run_command('python bot.py')
