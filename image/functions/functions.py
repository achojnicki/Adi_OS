from time import sleep
from termcolor import colored

import subprocess
import sys

def system(cmd, raise_exception=True):
    try:
        msg="Executing: {cmd} ...".format(cmd=cmd)
        msg=colored(msg,'cyan')
        print(msg,end=" ")
        sys.stdout.flush()

        process=subprocess.Popen(cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
        

        (stdout,stderr)=process.communicate()

        if process.returncode!=0:
            raise RuntimeError()

        msg='Success'
        msg=colored(msg,'green')
        print(msg)

    except RuntimeError:
        msg='Failed'
        msg=colored(msg, 'red')
        print(msg)

        msg='executing {cmd} failed.\n\nreturn code: {status}\n---\nstdout: {stdout}\n---\nstderr: {stderr}'.format(
            cmd=cmd, 
            status=process.returncode,
            stdout=stdout.decode(),
            stderr=stderr.decode()
            )
        if raise_exception:
            raise Exception(msg)
    except:
        msg='Failed'
        msg=colored(msg, 'red')
        print(msg)

        raise