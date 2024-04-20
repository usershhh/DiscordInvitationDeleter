import discord
import time

TOKEN = "" # token for your bot
SERVER_ID = 123456789 # server id

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

        guild = self.get_guild(SERVER_ID)
        if guild is None:
            print(f"The server with ID {SERVER_ID} cannot be found.")
            return

        invitations = await guild.invites()
        if not invitations:
            print("No invitation to delete.")
            return

        print(f"Delete {len(invitations)} invitations...")
        for invite in invitations:
            time.sleep(1)
            try:
                await invite.delete()
                print(f"The {invite.code} invitation has been removed.")
            except discord.HTTPException as e:
                print(f"Unable to delete invitation {invite.code}: {e}")

        print("All invitations have been deleted.")

client = MyClient(intents=discord.Intents.all())
client.run(TOKEN)