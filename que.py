# -*- coding: utf-8 -*-
import  queue
import  threading
import  time

def worker(i):
    while True:
        item = q.get()
        if item is None:
            print("线程 %s 发现了一个None, 可以休息了 ^-^" % i)
            break
        time.sleep(0.5)
        print ("线程%s将任务<%s>完成了!" % (i, item))
        q.task_done()


if __name__ == '__main__':
    num_of_threads = 5
    source = [i for i in range(1,21)]
    q = queue.Queue();

    threads = []
    for i in range(1, num_of_threads+1):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for item in source:
        time.sleep(0.5)
        q.put(item)

    #阻塞队列
    q.join()

    print ('工作都完成了')
    for i in range(num_of_threads):
        q.put(None)
    #阻塞线程  相当于停止线程
    for t in threads:
        t.join()
    print(threads)