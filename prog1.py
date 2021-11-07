import emoji
import spookify
import pyjoke
import subprocess

def joke():
    subprocess.run('pyjoke')
    return ":clown_face:"

def pun():
    print("Enter spooky, then enter the word you want spookified")
    subprocess.run('spookify')
    return ":angry_face_with_horns:"

print("Would you like a joke or a pun?")
choice = input()
if choice == "joke":
    print(emoji.emojize(joke()))
elif choice == "pun":
    print(emoji.emojize(pun()))
else:
    print(emoji.emojize('Bad input :confounded_face:'))




