@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("You don't have the permissions to do that")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You can't do that")
    else:
        print('Ignoring exception in command {}:'.format(ctx.command),
              file=sys.stderr)
        traceback.print_exception(type(error),
                                  error,
                                  error.__traceback__,
                                  file=sys.stderr)
    if isinstance(error, commands.CommandOnCooldown):
        msg = "Woah! Slow down! You have to wait {:.2f} seconds before you can do that again".format(
            error.retry_after)
        await ctx.reply(msg)
