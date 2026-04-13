# Hacker's Manifesto

A Python library written in Rust (PyO3) with two main features:

- Return the full Hacker's Manifesto text.
- Open the original manifesto in the browser: https://phrack.org/issues/7/3

## Exposed Functions

- `get_hackers_manifesto()`
- `open_manifesto_in_browser()`

## Usage in Python

```python
import hackers_manifesto as hm

print(hm.get_hackers_manifesto())
hm.open_manifesto_in_browser()
```

## Note

On PyPI/pip, package names are normalised, so `hackers_manifesto` may appear as `hackers-manifesto`. This is expected; the Python import remains `import hackers_manifesto`.
