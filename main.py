import os
import sys
import shlex

def parse_command(user_input):
    if user_input.strip() == "":
        return []

    try:
        tokens = shlex.split(user_input)
    except ValueError:
        print("ngawi-shell: error: unclosed quotation")
        return []

    return tokens

def main():
    while True:
        try:
            user = os.environ.get('USER', 'user')
            cwd = os.getcwd()
            prompt = f"{user}@ngawi-shell:{cwd}$ "
            
            raw_input = input(prompt)
            
            if raw_input.strip() == "exit":
                print(r"""   _____                 _ _                _ 
  / ____|               | | |              | |
 | |  __  ___   ___   __| | |__  _   _  ___| |
 | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ |
 | |__| | (_) | (_) | (_| | |_) | |_| |  __/_|
  \_____|\___/ \___/ \__,_|_.__/ \__, |\___(_)
                                  __/ |       
                                 |___/        """)
                print("\n")
                break
            
            if raw_input.strip() == "":
                continue

            args = parse_command(raw_input)

            if not args:
                continue

            command = args[0]
            arguments = args[1:]

            # Built-in Command: cd
            if command == "cd":
                if not arguments:
                    target_dir = os.path.expanduser("~")
                else:
                    target_dir = arguments[0]
                
                try:
                    os.chdir(target_dir)
                except FileNotFoundError:
                    print(f"ngawi-shell: cd: {target_dir}: No such file or directory")
                except NotADirectoryError:
                    print(f"ngawi-shell: cd: {target_dir}: Not a directory")
                except PermissionError:
                    print(f"ngawi-shell: cd: {target_dir}: Permission denied")
                continue

            # Built-in Command: pwd
            elif command == "pwd":
                print(os.getcwd())
                continue


            # ==========================================
            # Stage 5: Piping & I/O Redirection
            # ==========================================

            # Piping Implementation (|)
            if "|" in args:
                # TODO: Implement piping using os.pipe()
                
                print("ngawi-shell: piping feature not yet implemented")
                continue


            # I/O Redirection Implementation (< and >)
            input_file = None
            output_file = None
            clean_args = []
            
            # Parse redirection operators and target files
            i = 0
            while i < len(args):
                if args[i] == "<" and i + 1 < len(args):
                    input_file = args[i+1]
                    i += 2
                elif args[i] == ">" and i + 1 < len(args):
                    output_file = args[i+1]
                    i += 2
                else:
                    clean_args.append(args[i])
                    i += 1

            if not clean_args:
                continue

            command = clean_args[0]

            try:
                pid = os.fork()
            except OSError as e:
                print(f"ngawi-shell: fork failed: {e}")
                continue

            if pid == 0:
                # Child Process
                
                # Handle Input Redirection (<)
                if input_file:
                    try:
                        fd_in = os.open(input_file, os.O_RDONLY)
                        os.dup2(fd_in, 0) # Redirect stdin (0)
                        os.close(fd_in)
                    except FileNotFoundError:
                        print(f"ngawi-shell: {input_file}: No such file or directory")
                        os._exit(1)

                # Handle Output Redirection (>)
                if output_file:
                    fd_out = os.open(output_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
                    os.dup2(fd_out, 1) # Redirect stdout (1)
                    os.close(fd_out)

                # Execute target command
                try:
                    os.execvp(command, clean_args)
                except FileNotFoundError:
                    print(f"ngawi-shell: {command}: command not found")
                    os._exit(127)
                except PermissionError:
                    print(f"ngawi-shell: {command}: Permission denied")
                    os._exit(126)
                except Exception as e:
                    print(f"ngawi-shell: {command}: {e}")
                    os._exit(1)

            else:
                # Parent Process
                _, status = os.waitpid(pid, 0)
                 
                if os.WIFEXITED(status):
                    exit_code = os.WEXITSTATUS(status)
                    if exit_code != 0:
                        print(f"ngawi-shell: {command}: exited with status {exit_code}")

        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print()
            sys.exit(0)

if __name__ == "__main__":
    main()