class Messages:
    BOT_NAME = ""
    def victim_discord_message(self, victim):
        return {
            "content": None,
            "username": "Abigail",
            "avatar_url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/06590cce-eec1-4e12-98f6-d1bbebfe434a/original=true,quality=90/54334921.jpeg",
            "embeds": [
                {
                    "title": "New ransomware attack claimed!",
                    "color": 5827583,
                    "fields": [
                        {
                            "name": "👔 Name:",
                            "value": f"`{victim.name}`"
                        },
                        {
                            "name": "💼 Sector:",
                            "value": f"`{victim.activity}`",
                            "inline": True
                        },
                        {
                            "name": "🌎 Country:",
                            "value": f"`{victim.country} {victim.country_flag}`",
                            "inline": True
                        },
                        {
                            "name": "🗂️ Additional data:",
                            "value": f"`{victim.description}`"
                        },
                        {
                            "name": "🖥️ Website:",
                            "value": f"`{victim.website}`"
                        },
                        {
                            "name": "😈 Ransomware gang:",
                            "value": f"`{victim.group_name}`"
                        },
                        {
                            "name": "🖥️ Post URL:",
                            "value": f"`{victim.group_post_url}`"
                        },
                        {
                            "name": "📅 Published date:",
                            "value": f"`{victim.published_date}`"
                        }
                    ],
                    "author": {
                        "name": "ransomware_live_discord_bot"
                    },
                    "footer": {
                        "text": "Powered by: ransomware.live",
                        "icon_url": "https://i.imgur.com/s9pA2vD.png"

                    },
                    "image": {
                        "url": victim.screenshot_url
                    }
                }
            ],
            "attachments": []
        }