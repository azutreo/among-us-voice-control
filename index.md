# Among Us Voice Control
Discord bot that aids server managers during games of Among Us by automating the muting and unmuting of members in a voice channel.

This bot is currently deployed on Heroku, hence the requirements.txt file.

### Prefix
**`a!`**

### Required Permission to Use Commands
**`Manage Channels`**

### Commands
`a!help` - Shows the list of commands (exception to the permission rule).

`a!mutechannel` - Overrides the speak permission to *`false`* for the @everyone role for the channel the user is in.

`a!unmutechannel` - Overrides the speak permission to *`none`* for the @everyone role for the channel the user is in.
