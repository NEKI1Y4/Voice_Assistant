import psutil

class SystemInfo:
    @staticmethod
    def get_cpu_usage():
        return f"Загрузка процессора: {psutil.cpu_percent()}%"

    @staticmethod
    def get_memory_usage():
        memory = psutil.virtual_memory()
        return f"Используется памяти: {memory.percent}%"

    @staticmethod
    def get_disk_usage():
        disk = psutil.disk_usage('/')
        return f"Используется диска: {disk.percent}%"

    @staticmethod
    def get_system_name():
        return f"Имя системы: {psutil.users()[0].name}"

if __name__ == "__main__":
    print("Тест информации о системе:")
    try:
        print(SystemInfo.get_cpu_usage())
        print(SystemInfo.get_memory_usage())
        print(SystemInfo.get_disk_usage())
    except Exception as e:
        print(f"Ошибка в SystemInfo: {e}")
