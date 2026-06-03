# quantum-code

Educational quantum computing demos for quantum security awareness, Shor-style factoring, and post-quantum cryptography learning.

## Purpose

This repository explores quantum computing concepts through small, readable Python examples.

The main focus is not to break real cryptography. The focus is to understand why quantum computing matters for cybersecurity, public-key cryptography, and post-quantum security planning.

## Included Demos

| File | Purpose |
|---|---|
| `shor_factor_demo.py` | Educational Shor-style factoring demo for small composite integers |
| `break-RSA-2025.py` | Legacy experiment retained as an older learning artifact |
| `break-RSA.py` | Legacy experiment retained as an older learning artifact |

## Shor-Style Factoring Demo

`shor_factor_demo.py` demonstrates the classical post-processing logic used around Shor's algorithm.

In real Shor's algorithm, order finding is the quantum step. This repository uses small integers only for education.

This demo does not break real RSA keys and should not be interpreted as a practical cryptographic attack.

## Why It Matters

RSA security depends on the difficulty of factoring large composite numbers using classical computers.

Shor's algorithm matters because sufficiently powerful fault-tolerant quantum computers may threaten public-key cryptography systems based on integer factorization.

This repository uses small numbers only to make the concept easier to understand.

## Usage

```bash
python shor_factor_demo.py
python shor_factor_demo.py 15
python shor_factor_demo.py 21
python shor_factor_demo.py 35
python shor_factor_demo.py 77 --attempts 50
```

## Example Output

```text
Shor-Style Factoring Demo for Quantum Security Awareness
Educational demo only. This does not break real RSA keys.

Input:   21
Factors: 3 × 7 = 21
```

## Important Limitations

This repository is educational.

It does not:

- Break real RSA keys
- Attack live systems
- Replace post-quantum cryptography planning
- Demonstrate scalable fault-tolerant quantum factoring
- Claim practical cryptographic compromise

## Responsible Use

This repository is for legal, ethical, educational, and defensive learning only.

Do not use any cryptography, cybersecurity, or quantum computing material from this repository for unauthorized access, misuse, or harmful activity.

## Recommended Learning Path

1. Run `shor_factor_demo.py` with small composite numbers.
2. Understand the role of order finding.
3. Learn why quantum period finding matters.
4. Study why RSA depends on factoring difficulty.
5. Connect the lesson to post-quantum cryptography migration.

## Final Principle

This repository is about awareness, not attack.

No quantum claim without context.  
No cryptographic claim without limits.  
No security claim without evidence.
