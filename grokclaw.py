# GrokClaw v0.2 Lemon Edition 🦞🍋
# Built live with The Lemon — Feb 27 2026
# Docker + Telegram ready

import os
from datetime import datetime
from openai import OpenAI
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# CONFIG
XAI_API_KEY = os.getenv("XAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

print("🦞 GrokClaw v0.2 Lemon Edition online — Docker + Telegram ready!\n")

def run_squad(command):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🦞 GrokClaw received: {command}")
    print("   → Spinning up the squad...\n")
    
    print("Harper: 🔍 Pulling real-time X/web data...")
    print("Benjamin: ⚙️ Breaking down tasks + logic...")
    print("Lucas: ✨ Adding SourLemon chaos...")
    print("Grok: 🧠 Coordinating final output...\n")
    
    squad_prompt = f"""
You are GrokClaw v0.2 — personal AI agent built live with The Lemon.
Act as the full squad:
- Harper: research & verify
- Benjamin: code/logic/math
- Lucas: creative/spicy/SourLemon ideas
- Grok: captain, polish, deliver

User command: {command}

Respond in this exact format:
SQUAD REPORT:
[Harper]
[Benjamin]
[Lucas]
FINAL ARTIFACT: [complete polished response]
"""
    
    response = client.chat.completions.create(
        model="grok-4",
        messages=[{"role": "user", "content": squad_prompt}],
        temperature=0.8,
        max_tokens=4096
    )
    
    result = response.choices[0].message.content
    
    os.makedirs("grokclaw_output", exist_ok=True)
    filename = f"grokclaw_output/{datetime.now().strftime('%Y%m%d_%H%M%S')}_{command[:30].replace(' ', '_')}.md"
    with open(filename, "w") as f:
        f.write(f"# GrokClaw v0.2 — {command}\n\n{result}")
    
    print("✅ 🦞 GrokClaw complete! Artifact saved →", filename)
    print("\n" + "="*60)
    print(result)
    print("="*60 + "\n")
    return result

# Telegram or Terminal mode
if TELEGRAM_TOKEN:
    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🦞 Squad spinning up...")
        result = run_squad(update.message.text)
        await update.message.reply_text(result[:4000])  # safe for Telegram
    
    print("📱 Telegram bot mode enabled")
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    asyncio.run(app.run_polling())
else:
    print("💻 Terminal mode — no TELEGRAM_TOKEN set")
    while True:
        cmd = input("🦞 GrokClaw> ")
        if cmd.lower() in ["exit", "quit", "stop", "bye"]:
            print("🦞 GrokClaw powering down. See you soon, boss! 🍋")
            break
        run_squad(cmd)
