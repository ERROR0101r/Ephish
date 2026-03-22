#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'

clear

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║   ███████╗██████╗ ██╗  ██╗██╗███████╗██╗  ██╗              ║"
echo "║   ██╔════╝██╔══██╗██║  ██║██║██╔════╝██║  ██║              ║"
echo "║   █████╗  ██████╔╝███████║██║███████╗███████║              ║"
echo "║   ██╔══╝  ██╔═══╝ ██╔══██║██║╚════██║██╔══██║              ║"
echo "║   ███████╗██║     ██║  ██║██║███████║██║  ██║              ║"
echo "║   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝              ║"
echo "║                                                              ║"
echo "║           E P H I S H   -   T E R M U X   S E T U P          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${YELLOW}[!] EDUCATIONAL PURPOSE ONLY - Use responsibly${NC}"
echo ""

echo -e "${CYAN}[*] Updating Termux packages...${NC}"
pkg update -y && pkg upgrade -y

echo -e "${CYAN}[*] Installing Python...${NC}"
pkg install python -y

echo -e "${CYAN}[*] Installing pip...${NC}"
pkg install python-pip -y

echo -e "${CYAN}[*] Installing required Python packages...${NC}"
pip install flask requests colorama

echo -e "${CYAN}[*] Installing additional tools...${NC}"
pkg install openssl-tool -y
pkg install termux-api -y

echo -e "${GREEN}[+] All requirements installed successfully!${NC}"
echo ""

read -p "Do you want to run Ephish.py now? (y/n): " run_tool

if [[ $run_tool == "y" || $run_tool == "Y" ]]; then
    if [ -f "Ephish.py" ]; then
        chmod +x Ephish.py
        echo -e "${CYAN}[*] Running Ephish.py...${NC}"
        python Ephish.py
    else
        echo -e "${RED}[!] Ephish.py not found in current directory!${NC}"
        echo -e "${YELLOW}[!] Please place Ephish.py in this folder and run again${NC}"
    fi
else
    echo -e "${GREEN}[+] Setup complete!${NC}"
    echo -e "${YELLOW}To run tool: python Ephish.py${NC}"
fi