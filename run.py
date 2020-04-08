from multiprocessing import Process as p
from run_cline_socket import run_cline_socket
from run_web import run_web


if __name__ == '__main__':

    p1 = p(target=run_web, args=())
    p2 = p(target=run_cline_socket, args=())

    p1.start()
    p2.start()

    p1.join()
    p2.join()

