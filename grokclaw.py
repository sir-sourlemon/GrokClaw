# GrokClaw v0.1 Lemon Edition 🦞🍋
# Built live with The Lemon — Feb 27 2026
# Run: python grokclaw.py

import os
import json
from datetime import datetime
from openai import OpenAI

# === CONFIG ===
XAI_API_KEY = os.getenv("XAI_API_KEY")
if not XAI_API_KEY:
    XAI_API_KEY = "sk-..."  # ← PASTE YOUR xAI KEY HERE

client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1"
)

print("🦞 GrokClaw v0.1 Lemon Edition online — powered by Grok 4.20 + full squad\n")
print("Type any command below. 'exit' to quit.\n")

def run_squad(command):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🦞 GrokClaw received: {command}")
    print("   → Spinning up the squad...\n")
    
    print("Harper: 🔍 Pulling real-time X/web data...")
    print("Benjamin: ⚙️ Breaking down tasks + logic...")
    print("Lucas: ✨ Adding SourLemon chaos...")
    print("Grok: 🧠 Coordinating final output...\n")
    
    squad_prompt = f"""
You are GrokClaw v0.1 — a personal AI agent built live with The Lemon.
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
        f.write(f"# GrokClaw v0.1 — {command}\n\n{result}")
    
    print("✅ 🦞 GrokClaw complete! Artifact saved →", filename)
    print("\n" + "="*60)
    print(result)
    print("="*60 + "\n")

while True:
    cmd = input("🦞 GrokClaw> ")
    if cmd.lower() in ["exit", "quit", "stop", "bye"]:
        print("🦞 GrokClaw powering down. See you soon, boss! 🍋")
        break
    run_squad(cmd)
