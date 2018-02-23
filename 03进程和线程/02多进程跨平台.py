from multiprocessing import Process
import os


'''多进程'''
# 子进程执行的代码 getpid()获取当前进程pid getppid()获取父进程pid
def run_proc(name):
    print('Run child process, name: %s , pid: %s , parent: %s' % (name, os.getpid(), os.getppid()))

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
if __name__ == '__main__':
    print('Parent process, pid: %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


'''进程池Pool'''
print('\r\r\r')
from multiprocessing import Pool
import os,random,time

def proc_pool(args):
    print('process (%s) start --> pid: %s, ppid: %s' % (args, os.getpid(), os.getppid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('process (%s) used %0.2f seconds --> pid: %s, ppid: %s' % (args, (end-start), os.getpid(), os.getppid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(proc_pool, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

