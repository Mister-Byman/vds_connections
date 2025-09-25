import subprocess
import psutil
import time

# Функция для отображения всех подключений, связанных с портом 22
def show_ssh_connections():
    # Получаем все текущие сетевые подключения
    connections = psutil.net_connections(kind='inet')
    
    # Фильтруем только те, которые используют порт 22
    ssh_connections = [conn for conn in connections if conn.laddr.port == 22]
    
    if ssh_connections:
        print("Подключения на порт 22:")
        for conn in ssh_connections:
            print(f"Локальный адрес: {conn.laddr}, Удаленный адрес: {conn.raddr}, Статус: {conn.status}")
    else:
        print("Нет активных подключений на порт 22")

# Функция для отслеживания трафика с помощью tcpdump
def capture_traffic():
    print("Запуск tcpdump для захвата трафика на порту 22...")
    command = ["sudo", "tcpdump", "-i", "any", "port", "22", "-nn", "-l"]
    
    # Запуск tcpdump для захвата трафика
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    try:
        while True:
            # Чтение вывода tcpdump и вывод его на экран
            output = process.stdout.readline().decode('utf-8')
            if output:
                print(output.strip())
            time.sleep(1)
    except KeyboardInterrupt:
        print("Завершение мониторинга.")
        process.terminate()

if __name__ == "__main__":
    # Сначала отобразим текущие соединения на порту 22
    show_ssh_connections()
    
    # Затем начнем захват трафика
    capture_traffic()
