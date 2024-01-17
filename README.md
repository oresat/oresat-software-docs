# OreSat Software Docs

Documentation, resources, guides, and best practices for OreSat software development.

## Manual Build Docs

Clone the git repository

```bash
$ git clone https://github.com/oresat/oresat-software-docs
```

Change to the `oresat-software-docs` directory

```bash
$ cd oresat-software-docs
```

Install dependencies

**NOTE**: May need to replace `pip` with `pip3` on your system (it varies on
OS and distro).

```bash
$ pip install -r requirements.txt
```

Build the docs

```bash
$ make html -C docs
```

Open `docs/build/html/index.html` in a web browser.
