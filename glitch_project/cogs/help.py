import discord
from discord.ext import commands
from discord import app_commands

HELP_TEXT = """
**📚 قائمة الأوامر:**

**/stream `<رابط أو كلمات>`**
➤ أضف مقطع يوتيوب أو فيسبوك أو ابحث باسم القارئ أو السورة.

**/queue**
➤ عرض قائمة التشغيل الحالية.

**/play**
➤ بدء التشغيل أو استئناف المقطع الحالي.

**/pause**
➤ إيقاف مؤقت للمقطع الجاري.

**/skip**
➤ تخطي المقطع الحالي وتشغيل التالي.

**/stop**
➤ إيقاف التشغيل ومسح الطابور تمامًا.

**/jump `<رقم>`**
➤ الانتقال لمقطع معيّن في الطابور.

**/restart**
➤ العودة إلى المقطع الأول في الطابور.

---

**💡 نصائح متقدّمة:**
• يدعم الروابط من: **YouTube, Facebook, SoundCloud** وغيرهم.
• البوت يحمّل مسبقًا المقطع التالي لتشغيل بلا انقطاع.
• يمكنك استخدام البحث باسم القارئ أو السورة (مثال: عبد الباسط الفاتحة).
• في حال حدوث مشكلة في التشغيل، جرّب إعادة إضافة المقطع أو التحقق من الرابط.

---

**🔗 ملاحظات عامة:**
- تأكد من وجودك في قناة صوتية عند استخدام أوامر التشغيل.
- سيتم حذف الطابور إذا خرجت البوت من القناة الصوتية أو استخدمت /stop.
- كل مقطع يُشغل منفصل عن الآخرين لتسهيل التحكم.

__تم تطوير هذا البوت لخدمة بث التلاوات بشكل احترافي وسهل الاستخدام. جزاكم الله خيرًا.__
"""

class HelpCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="help", description="دليل استخدام البوت")
    async def help_cmd(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🟢 **دليل الاستخدام الكامل**",
            description=HELP_TEXT,
            color=0x3498db
        )
        embed.set_footer(text="بوت تلاوات القرآن - By AbuNawas")
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(HelpCog(bot))
