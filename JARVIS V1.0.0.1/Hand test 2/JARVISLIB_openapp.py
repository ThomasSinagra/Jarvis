import subprocess

def openapp(name):
    if name=="Minecraft":
        subprocess.call(
            ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Minecraft.app"]
            )
    if name=='Discord':
        subprocess.call(
            ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Discord.app"]
            )


