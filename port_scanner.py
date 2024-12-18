import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor


def verifica_porta(ip, porta):
    """
    Verifica se uma porta específica está aberta em um IP.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, porta)) == 0:
                print(f"[+] Porta {porta} aberta em {ip}")
    except Exception as e:
        print(f"[-] Erro ao verificar a porta {porta} em {ip}: {e}")


def scan_alvo(ip, portas):
    """
    Realiza o scan das portas de um IP.
    """
    print(f"[*] Iniciando o scan em {ip} nas portas: {portas}")
    with ThreadPoolExecutor(max_workers=10) as executor:
        for porta in portas:
            executor.submit(verifica_porta, ip, porta)


def main():
    """
    Menu principal do scanner de portas.
    """
    print("=== Scanner de Portas ===")
    alvo = input("Digite o IP ou a rede (ex.: 192.168.0.1 ou 192.168.0.0/24): ")
    try:
        ips = list(ipaddress.IPv4Network(alvo, strict=False)) if '/' in alvo else [ipaddress.IPv4Address(alvo)]
    except ValueError:
        print("[-] IP ou rede inválida!")
        return

    portas_input = input("Digite as portas (ex.: 22, 80, 443 ou 1-1024): ")
    portas = list(range(*map(int, portas_input.split('-')))) if '-' in portas_input else [int(p) for p in portas_input.split(',')]

    for ip in ips:
        scan_alvo(str(ip), portas)


if __name__ == "__main__":
    main()
