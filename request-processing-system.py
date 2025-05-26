import queue
import random
import time
from datetime import datetime

class RequestProcessingSystem:
    def __init__(self):
        self.request_queue = queue.Queue()
        self.request_counter = 1
        self.processed_requests = []
        
    def generate_request(self):
        request_id = f"REQ-{self.request_counter:04d}"
        request_types = ["Технічна підтримка", "Скарга", "Інформаційний запит", "Заміна обладнання", "Налаштування"]
        request_type = random.choice(request_types)
        
        request = {
            "id": request_id,
            "type": request_type,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "priority": random.choice(["Низький", "Середній", "Високий"])
        }
        
        self.request_queue.put(request)
        print(f"Нова заявка створена: {request_id} ({request_type}) - Пріоритет: {request['priority']}")
        
        self.request_counter += 1
        
    def process_request(self):
        if not self.request_queue.empty():
            request = self.request_queue.get()
            processing_time = random.uniform(1, 3)
            print(f"Обробляємо заявку {request['id']}... ({processing_time:.1f} сек)")
            time.sleep(processing_time)
            
            request["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request["status"] = "Оброблено"
            self.processed_requests.append(request)
            
            print(f"Заявка {request['id']} успішно оброблена")
        else:
            print("Черга заявок пуста - немає заявок для обробки")
            
    def show_queue_status(self):
        queue_size = self.request_queue.qsize()
        processed_count = len(self.processed_requests)
        
        print(f"\n Статус системи:")
        print(f"Заявки в черзі: {queue_size}")
        print(f"Оброблено заявок: {processed_count}")
        
        if queue_size > 0:
            print(f"Наступна заявка в черзі готова до обробки")
            
    def show_processed_requests(self):
        if self.processed_requests:
            print(f'\n Останні оброблені заявки:')
            for req in self.processed_requests[-5:]:
                print(f"{req['id']} - {req['type']} (оброблено: {req['processed_at']})")
        else:
            print("\n Поки що немає оброблених заявок")
            
def main():
    print("Система обробки заявок сервісного центру")
    print("=" * 50)
    
    system = RequestProcessingSystem()
    
    while True:
        print(f"\n{'='*50}")
        print("Виберіть дію:")
        print("1. Створити нову заявку")
        print("2. Обробити заявку з черги")
        print("3. Автоматичний режим (створення + обробка)")
        print("4. Показати статус черги")
        print("5. Показати оброблені заявки")
        print("6. Створити декілька заявок одразу")
        print("0. Вийти з програми")
        
        try:
            choice = input("\nВаш вибір (0-6): ").strip()
            
            if choice == "1":
                system.generate_request()
                
            elif choice == "2":
                system.process_request()
                
            elif choice == "3":
                print("\n Автоматичний режим активовано...")
                num_requests = random.randint(2, 3)
                for _ in range(num_requests):
                    system.generate_request()
                    time.sleep(0.5)
                    
                print(f"\n Обробляємо заявки...")
                
                while not system.request_queue.empty():
                    system.process_request()
                    time.sleep(0.5)
                    
            elif choice == "4":
                system.show_queue_status()
                
            elif choice == "5":
                system.show_processed_requests()
                
            elif choice == "6":
                try:
                    count = int(input("Скільки заявок створити (1-10)? "))
                    count = max(1, min(10, count))
                    for _ in range(count):
                        system.generate_request()
                        time.sleep(0.2)
                except ValueError:
                    print("Введіть правильне число")
                    
            elif choice == "0":
                print("\n Дякуємо за використання системи обробки заявок")
                system.show_queue_status()
                break
            
            else:
                print("Невірний вибір! Виберіть опцію від 0 до 6")
                
        except KeyboardInterrupt:
            print("\n\n Програма завершена користувачем")
            break
        except Exception as e:
            print("Виникла помилка: {e}")
            
if __name__ == "__main__":
    main()