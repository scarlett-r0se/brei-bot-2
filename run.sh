docker run \
    --name=Minecraft-Server \
    --rm \
    -it \
    -p 25565:25565 \
    -v /home/r0xanne/Documents/programming-projects/brei-bot-2/discordBot/server/:/server \
    bb2