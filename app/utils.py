import base64
import json

class Color:
    red = '\033[91m'
    end = '\033[0m'


def save(solution):
    try:
        json_solution = json.dumps(solution)
        b64_solution = base64.b64encode(json_solution.encode('utf-8'))
        return str(b64_solution, encoding='utf-8')
    except Exception as e:
        print(f'Error: {e}')
        return None

def load(b64_solution):
    try:
        decoded_list = base64.b64decode(b64_solution)
        solution = json.loads(decoded_list.decode('utf-8'))
        return solution
    except Exception as e:
        print(f'Error: {e}')
        return None


def save_progress(solution, progress):
    try:
        solution_and_progress = [solution, progress]
        b64_soltution_and_progress = save(solution_and_progress)
        return b64_soltution_and_progress
    except Exception as e:
        print(f'Error: {e}')
        return None, None

def load_progress(b64_soltution_and_progress):
    try:
        solution_and_progress = load(b64_soltution_and_progress)
        solution = solution_and_progress[0]
        progress = solution_and_progress[1]
        return solution, progress
    except Exception as e:
        print(f'Error: {e}')
        return None, None