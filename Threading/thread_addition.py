import multiprocessing
import threading


lock = threading.Lock()
Super_sum = 0
NCPU = multiprocessing.cpu_count()
A = [i for i in range(1,103)]
N = len(A)
n = N/NCPU


def add_nums(i,j):
	global Super_sum
	sum = 0
	for k in range(i,j):
		sum += A[k]
	with lock:
		Super_sum += sum

if __name__ == "__main__":
    threads = []
    start = 0
    for i in range(NCPU):
    	if i == NCPU - 1:
    		t = threading.Thread(target = add_nums, args = (start,N))
    	else:
    		t = threading.Thread(target = add_nums, args = (start,start+n))
        start = start + n
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print Super_sum