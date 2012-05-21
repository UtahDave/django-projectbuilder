## TODO
- Write README
- Write Credits
- Write Quick Start docs
- Make it so everything can be relative rather than absolute
- Add '--domain' argparse flag
- Replace 'prototypemagic.com' in server-scripts/proto-new-virtualhost-subdomain.py with result of --domain
- Use stdin/out/err pipes to show output during `pip install -r requirements.txt`
- Fix `cpvirtualenv` bug in `virtualenvwrapper.sh` or create our own replacement
- Server should use something like `lynx -dump checkip.dyndns.org 2>&1 | awk '{print $4}' | grep ^[0-9]` in place of the generic `my-django-powerde-site.com`

## Final Stuff
- Use distutils to make a setup.py
- Get onto PyPI

## Completed
- Add Bootstrap and Non-Bootstrap options
- Make more files generic
- Clean up files
- Organize folders
- Write Contributors

## Possible TODO
- Take out '_site'
