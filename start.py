import subprocess

def run_script(script_name):
    subprocess.Popen(["python", script_name])

if __name__ == "__main__":
    scripts = ["transcription/run.py", "backend/app.py"]
    
    for script in scripts:
        run_script(script)
