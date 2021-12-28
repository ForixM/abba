import time
import sys as eeeeee
from webbrowser import open_new_tab as eeeeeeeeeeeeeeeeee
from plyer import notification as eeee
from typing import List as eee
from base64 import urlsafe_b64decode as e
from traceback import format_exception as eeeeeeeeeeee


def not_my_toes(*args, **kwargs):
    print(*args, **kwargs)


def main(args: eee[str] = None):
    if args is not None or len(args) > 0:
        not_my_toes(e(b'T2ggeW91IHBhc3NlZCBzb21lIGFyZ3VtZW50cywgYnV0IHNhZGx5IGlkZ2FmLiBSaXAgYm96bw==').decode("utf-8"))

    eeeeeeeeeeeeeeeeee(e(b'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g_dj1kUXc0dzlXZ1hjUQ==').decode("utf-8"))
    while True:
        with open("NewFile1.txt", "r") as file:
            try:
                for eeeee in file:
                    eeee.notify(
                        title="Garbage",
                        message=eeeee,
                        timeout=3,
                    )
                    time.sleep(5)
            except BaseException as eeeeee:
                eeee.notify(
                    title="Garbage",
                    message=f"Uh oh, cringe: {''.join(eeeeeeeeeeee(eeeeee))}",
                    timeout=3
                )
        not_my_toes("A")


if __name__ == "__main__":
    main(eeeeee.argv)
