from threading import Thread, Timer

import services.dht as tmp 
thread_dht = Thread(target=tmp.getData, name="dht")
thread_dht.start()