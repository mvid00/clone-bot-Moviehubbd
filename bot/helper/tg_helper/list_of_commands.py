from bot import CMD_INDEX

class _BotCommands:
    def __init__(self) -> None:
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f'mirror{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzipmirror{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipmirror{CMD_INDEX}'
        self.CancelMirror = f'cancel{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall{CMD_INDEX}'
        self.ListCommand = f'list{CMD_INDEX}'
        self.SearchCommand = f'search{CMD_INDEX}'
        self.StatusCommand = f'status{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'stats{CMD_INDEX}'
        self.HelpCommand = f'help{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.CloneCommand = f'clone{CMD_INDEX}'
        self.CountCommand = f'count{CMD_INDEX}'
        self.WatchCommand = f'watch{CMD_INDEX}'
        self.ZipWatchCommand = f'zipwatch{CMD_INDEX}'
        self.DeleteCommand = f'del{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'leechset0{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb{CMD_INDEX}'
        self.LeechCommand = f'leech0{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleech0{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleech0{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatch{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatch{CMD_INDEX}'
        
BotCommands = _BotCommands()
