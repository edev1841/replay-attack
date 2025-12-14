from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient("127.0.0.1", port=502)
client.connect()

# Old sensor values (replayed)
replayed_values = [45, 46, 47, 48]

for value in replayed_values:
    client.write_register(0, value)   # 40001 → address 0
    print(f"Replayed Tank Level: {value}")
    time.sleep(1)

client.close()
