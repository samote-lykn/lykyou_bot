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

class MembersLink:
    WIKI_LINKS = {
        Members.WILLIAM: 'https://tpop.fandom.com/wiki/William',
        Members.TUI: 'https://tpop.fandom.com/wiki/Tui_(LYKN)',
        Members.NUT: 'https://tpop.fandom.com/wiki/Nut_(LYKN)',
        Members.HONG: 'https://tpop.fandom.com/wiki/Hong_(LYKN)',
        Members.LEGO: 'https://tpop.fandom.com/wiki/Lego'
    }
    INSTAGRAM_LINKS = {
        Members.WILLIAM: 'https://www.instagram.com/williamjkp/',
        Members.TUI: 'https://www.instagram.com/m.tuiiii/',
        Members.NUT: 'https://www.instagram.com/nnutdan/',
        Members.HONG: 'https://www.instagram.com/hongshihoshi/',
        Members.LEGO: 'https://www.instagram.com/le_tsgo_eating/'
    }
    TWITTER_LINKS = {
        Members.WILLIAM: 'https://www.x.com/williamjkp1',
        Members.TUI: 'https://www.x.com/TuiChayatorn',
        Members.NUT: 'https://www.x.com/nnutdan',
        Members.HONG: 'https://www.x.com/hongshihoshi03',
        Members.LEGO: 'https://www.x.com/realxlg/'
    }
    TIKTOK_LINKS = {
        Members.WILLIAM: 'https://www.tiktok.com/@jkpwilliam',
        Members.TUI: 'https://www.tiktok.com/@m.tuiiii',
        Members.NUT: 'https://www.tiktok.com/@nnutdan',
        Members.HONG: 'https://www.tiktok.com/@hongshihoshi',
        Members.LEGO: 'https://www.tiktok.com/@lgeat'
    }
# Example Usage print(MembersLink.LINKS[Members.WILLIAM])

class BotChatType:
    GROUP: str = 'group'
    PRIVATE: str = 'private'

