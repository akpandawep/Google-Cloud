# copyright 2023 © Xron Trix | https://github.com/Xrontrix10


# @title <font color=red> 🖥️ Main Colab Leech Code

# @title Main Code
# @markdown <div><center><img src="https://image.pandawep.in/logo2.jpg" height=80></center></div>
# @markdown <center><h4><a href="https://pandawep.in">READ</a><b> How to use</h4></b></center>
# @markdown <br><center><h2><font color=lime><strong>Fill all Credentials, Run The Cell and Start The Bot</strong></h2></center>
# @markdown <br><br>

API_ID = 20006068  # @param {type: "integer"}
API_HASH = "346becfc02417e50a2837a8d545b015e"  # @param {type: "string"}
BOT_TOKEN = "7006043771:AAGpxBrTV3Y2aA0uFDYYHwINJPy4BQHXHjY"  # @param {type: "string"}
USER_ID = 6141937812  # @param {type: "integer"}
DUMP_ID = -1002132886598  # @param {type: "integer"}


import subprocess, time, json, shutil, os
from IPython.display import clear_output, display, HTML
from threading import Thread

Working = True

banner = '''
𝐖𝖾ᥣ𝖼ⱺꭑ𝖾 𝐀𝗌ɦυ 𝚰 𝐌𝗂𝗌𝗌 𝐘ⱺυ 𝐕𝖾𝗋𝗒 𝐌υ𝖼ɦ

'''

print(banner)

def keep_alive(url):
    display(HTML(f'<audio src="{url}" controls autoplay style="display:none"></audio>'))

def Loading():
    white = 37
    black = 0
    while Working:
        print("\r" + "░"*white + "▒▒"+ "▓"*black + "▒▒" + "░"*white, end="")
        black = (black + 2) % 75
        white = (white -1) if white != 0 else 37
        time.sleep(2)
    clear_output()

audio_url    = "https://raw.githubusercontent.com/KoboldAI/KoboldAI-Client/main/colab/silence.m4a"
audio_thread = Thread(target=keep_alive, args=(audio_url,))
audio_thread.start()
_Thread = Thread(target=Loading, name="Prepare", args=())
_Thread.start()

if len(str(DUMP_ID)) == 10 and "-100" not in str(DUMP_ID):
    n_dump = "-100" + str(DUMP_ID)
    DUMP_ID = int(n_dump)

if os.path.exists("/content/sample_data"):
    shutil.rmtree("/content/sample_data")

cmd = "git clone https://github.com/ashutoshgoswami24/Telegram-Leecher && bash /content/Telegram-Leecher/setup.sh"
proc = subprocess.run(cmd, shell=True)
cmd = "apt update && apt install ffmpeg aria2 megatools"
proc = subprocess.run(cmd, shell=True)
cmd = "pip3 install -r /content/Telegram-Leecher/requirements.txt"
proc = subprocess.run(cmd, shell=True)

credentials = {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "USER_ID": USER_ID,
    "DUMP_ID": DUMP_ID,
}

with open('/content/Telegram-Leecher/credentials.json', 'w') as file:
    file.write(json.dumps(credentials))

Working = False

if os.path.exists("/content/Telegram-Leecher/my_bot.session"):
    os.remove("/content/Telegram-Leecher/my_bot.session") # Remove previous bot session
print("\rStarting Bot....")

!cd /content/Telegram-Leecher/ && python3 -m colab_leecher #type:ignore
