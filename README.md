# Airbnb 2016
Turning homes into hotels continues to flourish in SF, despite controversies, legal battles and new laws. Top-line summaries of our data findings for Airbnb, HomeAway and FlipKey, including overall numbers of listings, types (homes, rooms, shared rooms), average price, YoY changes, guest frequency, multiple properties. 


## Includes:

- Livereload for fast development
- Grunt tasks for serving application
- Jinja2 for sane templating
- Frozen-Flask for creating static projects

### Requirements
- Python 2.7.x
- Node.js 0.12
  - uglifyjs (`npm install -g uglifyjs`)
  - clean-css (`npm install -g clean-css`)
  - Bower and Grunt (`$ npm install -g grunt-cli bower`)

### Installation
```bash
$ git clone git@github.com:sfchronicle/airbnb16_site.git airbnb16
$ cd airbnb16
$ mkvirtualenv airbnb16
$ pip install -r requirements.txt && npm install && bower install
$ grunt serve
```

### Build and deployment
Now run `build.py` and specify if its for `production` or `staging` to compress assets for upload.
```bash
$ python build.py production
```

## Contributing
1. Fork it.
2. Create a branch (`git checkout -b username-patch-n`)
3. Commit your changes (`git commit -am "Added support for MovableType"`)
4. Push to the branch (`git push origin username-patch-n`)
5. Open a [Pull Request](https://help.github.com/articles/creating-a-pull-request/)
6. Enjoy some [artisanal toast](https://www.eater.com/2014/5/30/6215971/artisanal-toast-is-taking-the-nation-by-storm)

## License
The MIT License (MIT)

Copyright The San Francisco Chronicle from '93 'til ...

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
