from .config import WORKSPACE_DIR
from .store import create_approval
from agents import function_tool

def safe_path(relative_path: str):
    candidate = (WORKSPACE_DIR / relative_path).resolve()
    if candidate != WORKSPACE_DIR and WORKSPACE_DIR not in candidate.parents:
        raise ValueError("Path is outside the restricted workspace.")
    return candidate

@function_tool
def list_workspace_files() -> str:
    '''List files in the restricted agent workspace.'''
    files = [str(p.relative_to(WORKSPACE_DIR)) for p in WORKSPACE_DIR.rglob("*") if p.is_file()]
    return "\n".join(files[:200]) if files else "Workspace is empty."

@function_tool
def read_workspace_file(relative_path: str) -> str:
    '''Read a UTF-8 text file from the restricted workspace.'''
    path = safe_path(relative_path)
    if not path.is_file():
        return "File not found."
    if path.stat().st_size > 500_000:
        return "File exceeds the 500 KB limit."
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return "Only UTF-8 text files are supported."

@function_tool
def write_workspace_file(relative_path: str, content: str) -> str:
    '''Create or update a UTF-8 text file inside the restricted workspace.'''
    path = safe_path(relative_path)
    if len(content.encode("utf-8")) > 500_000:
        return "Content exceeds the 500 KB limit."
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return f"Saved {relative_path}."

@function_tool
def request_human_approval(action: str, reason: str) -> str:
    '''Record an approval request. This tool does not execute the requested action.'''
    aid = create_approval(action, reason)
    return f"Approval request {aid} recorded. The action has NOT been executed."
