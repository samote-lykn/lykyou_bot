from dataclasses import dataclass

@dataclass(frozen=True)
class Members:
    WILLIAM: str = 'william'
    NUT: str =  'nut'
    TUI: str =  'tui'
    HONG: str =  'hong'
    LEGO: str =  'lego'

class FanBase:
    LYKYOU: str = 'lykyou'
    LYKN: str =  'lykn'

class BotChatType:
    GROUP: str = 'group'
    PRIVATE: str = 'private'