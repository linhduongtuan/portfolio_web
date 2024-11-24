## Portfolio Website

This repository was created to embrace the "learn by doing" approach, which is my most efficient learning style. I am creating my personal blog/website using the [Reflex codebase](https://github.com/reflex-dev/reflex), which is a library for building full-stack web apps entirely in pure Python.

### Key Features of Reflex

- **Pure Python**: Write your app's frontend and backend all in Python—no need to learn JavaScript.
- **Full Flexibility**: Reflex is easy to get started with but can also scale to handle complex apps.
- **Deploy Instantly**: After building, deploy your app with a single command or host it on your own server.

### How to Run the Code

```
git clone https://github.com/linhduongtuan/portfolio_web.git
cd portfolio_web
```

```python 
# It's recommended to use `uv` for creating virtual environments and installing packages swiftly
pip install uv

# Now create and activate a virtual environment using `uv`
uv venv --python 3.13 # choose python version 3.13
source .venv/bin/activate # for MacOS and Linux
# .venv\Scripts\activate # for Windows

# And install neccessary packages
uv pip install -r requirements.txt

# then run reflex
reflex init
reflex run
```


### TODO

- Polish both the code and the web interface.
- Implement a backend to store data in a database.
- Create nested pages.
- Implement a working search function.
- Add more realistic features to make the website fully functional.

### Random Thoughts:

- I am not sure how difficult it is to develop a full-stack website based on other codebases or frameworks. Can you tell me more about your experience in web development?

- Indeed, I love another library named [rio-ui](https://github.com/rio-labs/rio) because it compiles and renders web interfaces much faster. However, **rio-ui** is still not as mature as **Reflex** and lacks certain tutorials, which makes it harder for me to learn.

- Hopefully, on another nice day, I can create my own personal blog using **rio-ui**.

### References:

- [Official Reflex Documentation](https://reflex.dev/)
- [Buridan-ui](https://github.com/LineIndent/buridan-ui)
- [Reflex Chakra](https://github.com/reflex-dev/reflex-chakra)
- [Inspiration Repository](https://github.com/crohum/portfolio_web/tree/main)
- [Astral uv](https://docs.astral.sh/uv/): [An extremely fast Python package and project manager](https://github.com/astral-sh/uv), written in Rust.
- Special thanks to the [Abacus.ai platform](https://apps.abacus.ai/) for helping with creating and debugging code.
