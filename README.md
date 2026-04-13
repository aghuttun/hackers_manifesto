# Hacker's Manifesto

A Python library written in Rust (PyO3) with two main features:

- Return the full Hacker's Manifesto text.
- Open the original manifesto in the browser: https://phrack.org/issues/7/3

## Exposed Functions

- `get_hackers_manifesto()`
- `open_manifesto_in_browser()`

## Quick Build (Windows)

Build in release mode:

```powershell
cargo build --release
```

Create a local Python module from the DLL:

```powershell
Copy-Item .\target\release\hackers_manifesto.dll .\hackers_manifesto.pyd -Force
```

## Usage in Python

```python
import hackers_manifesto

print(hackers_manifesto.get_hackers_manifesto())
hackers_manifesto.open_manifesto_in_browser()
```

## Build a Wheel with Maturin

Install maturin in the active Python environment:

```powershell
python -m pip install maturin
```

Build the wheel:

```powershell
python -m maturin build --release
```

The generated wheel is placed in `target/wheels/`.

Install the wheel in the current environment:

```powershell
python -m pip install --force-reinstall .\target\wheels\hackers_manifesto-0.1.0-cp38-abi3-win_amd64.whl
```

## Smoke Test

Run a quick validation of the installed package:

```powershell
python .\scripts\smoke_test.py
```
