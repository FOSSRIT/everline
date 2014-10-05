Everline
========

Project for HackUpstate utilizing the Evernote API to build Civic Hacking Data
Visualizations

Clone The Repo
---

<code>git clone https://github.com/FOSSRIT/nethervote.git</code>

Install the Python Things
----
  <code>python setup.py develop</code>

Install the Javascript-y Things
----

## Linux

### NPM

Make sure you have npm and node. The best way to do this is using [nvm](https://github.com/creationix/nvm)
Getting nvm is easy. Simply run:
`curl https://raw.githubusercontent.com/creationix/nvm/v0.17.2/install.sh | bash`

*The script clones the nvm repository to `~/.nvm` and adds the source line to your profile (`~/.bash_profile`, `~/.zshrc` or `~/.profile`).*

You can customize the install source, directory and profile using the `NVM_SOURCE`, `NVM_DIR` and `PROFILE` variables. Eg: 
`curl ... | NVM_DIR=/usr/local/nvm bash` for a global install.

Once you have nvm, install the latest version of node 

`nvm install v0.10.24`

### Bower

To install bower (our front end javascript package manager) run `npm install -g bower`

*This installs the bower package manager globally on your box.*

### Gulp

To install gulp:

<code>npm install gulp</code>

<em>linux hack</em>
---
If you don't want to install gulp globally, you can run manually like so:
<code>./node_modules/gulp/bin/gulp.js</code>

<em>Windows hack</em>
---
If you cannot just run `gulp`:

`node .\node_modules\gulp\bin\gulp.js`

Run the server
----
 <code>python app.py</code>


