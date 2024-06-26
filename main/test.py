import yaml

text = 'вставь'

with open("C:/Users/User/Desktop/PROG/.vscode/voice_helper/main/user_com.yaml", "r") as user_com:
    read_data = yaml.safe_load(user_com)

if read_data["keyboard"]["keyboard_command1"]["voice_command"] in text:
    print(1)

elif read_data["keyboard"]["keyboard_command2"]["voice_command"] in text:
    print(2)




   






