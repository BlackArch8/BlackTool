from time import sleep

from console_progressbar import ProgressBar

bar = ProgressBar()

for i in bar (range(50)):
    sleep (0.3)

import time
from console_progressbar import ProgressBar

pb = ProgressBar(total=100,prefix='Loading', suffix='Sabar ', decimals=3, length=50, fill='#', zfill='-')
pb.print_progress_bar(2)
time.sleep(5)
pb.print_progress_bar(25)
time.sleep(5)
pb.print_progress_bar(50)
time.sleep(5)
pb.print_progress_bar(95)
time.sleep(5)
pb.print_progress_bar(100)