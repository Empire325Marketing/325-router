#!/usr/bin/env python3
"""325 Router — Smart prompt classification by Empire325Marketing. Open source MIT."""
import sys, time, statistics

TIERS = {
    "fast": "HTML, CSS, Shell, simple queries — lightweight models",
    "balanced": "Python, JavaScript, SQL, coding — mid-size models", 
    "ultra": "Research, analysis, complex reasoning — large models",
}

class SmartRouter:
    """Classifies prompts and recommends optimal model tier."""
    
    def classify(self, prompt: str) -> str:
        pl = prompt.lower()
        s = {"ultra": 0, "balanced": 0, "fast": 0}
        
        # Fast tier keywords
        for kw in ["html", "css", "bash", "shell", "docker", "git ", "find ", "grep"]:
            if kw in pl: s["fast"] += 4
        
        # Balanced tier keywords
        for kw in ["def ", "function", "class ", "python", "javascript", "sql", "code", "sort", "algorithm"]:
            if kw in pl: s["balanced"] += 4
        
        # Ultra tier keywords
        for kw in ["analyze", "research", "explain", "compare", "discuss"]:
            if kw in pl: s["ultra"] += 4
        
        # Short/simple → fast
        if len(pl) < 40 and "?" not in pl:
            s["fast"] += 3
        
        return max(s, key=s.get)

def benchmark(runs: int = 500) -> dict:
    r = SmartRouter()
    queries = ["Write HTML form","Python sort","What is capital","Analyze quantum","SQL JOIN","Bash find files","Explain AI","CSS grid","JavaScript debounce","Research fusion"]
    times = []
    for i in range(runs):
        q = queries[i % len(queries)]
        t0 = time.perf_counter()
        r.classify(q)
        times.append((time.perf_counter() - t0) * 1_000_000)
    return {"iterations": runs, "mean_us": round(statistics.mean(times), 2), "p99_us": round(sorted(times)[int(runs*0.99)], 2)}

def cli():
    import argparse
    p = argparse.ArgumentParser(description="325 Router — Smart AI model routing")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("classify").add_argument("prompt")
    sub.add_parser("benchmark")
    args = p.parse_args()
    r = SmartRouter()
    if args.cmd == "classify":
        tier = r.classify(args.prompt)
        print(f"Prompt: {args.prompt[:80]}\nTier:   {tier} — {TIERS[tier]}")
    elif args.cmd == "benchmark":
        b = benchmark()
        print(f"CPU Benchmark: {b['mean_us']}μs mean, {b['p99_us']}μs P99 ({b['iterations']} runs)")
    else:
        p.print_help()

if __name__ == "__main__":
    cli()
