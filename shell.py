import subprocess
import os

def execute_commands(command):
    try:
        if "|" in command:
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            fdin = os.dup(s_in)
            
            for cmd in command.split("|"):
                os.dup2(fdin, 0)
                os.close(fdin)

                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                os.dup2(fdout, 1)
                os.close(fdout)

                try:
                    subprocess.run("cmd.strip().split()")
                except Exception:
                    print("pysh: command not found: {}".format(cmd.strip()))
            
            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)
        else:
            subprocess.run(command.split())
    except Exception:
        print("pysh: command not found: {}".format(command))

def psh_cd(path):
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("cd: no such file or directory: {}".format(path))

def main():
    while True:
        command = input("Type \'help\' for more information\n$ ")
        if command == "exit" :
            break
        elif command[:3] == "cd ":
            psh_cd(command[3:])
        elif command == "help" :
            print("pysh: a simple Python shell")
        else:
            execute_commands(command)

if '__main__' == __name__:
    main()