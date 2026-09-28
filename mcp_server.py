"""MCP stdio server for Log Barrier Solver."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import LogBarrierSolver

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "solve_log_barrier",
                        "description": "Solve linear-constrained problem via interior-point log-barrier annealing",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "c": {"type": "array", "items": {"type": "number"}},
                                "A": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}},
                                "b": {"type": "array", "items": {"type": "number"}},
                                "x0": {"type": "array", "items": {"type": "number"}}
                            },
                            "required": ["c", "A", "b", "x0"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "solve_log_barrier":
            c = args.get("c", [])
            A = args.get("A", [])
            b = args.get("b", [])
            x0 = args.get("x0", [])
            sol = LogBarrierSolver.solve_linear_constrained(c, A, b, x0)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"solution": sol}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
