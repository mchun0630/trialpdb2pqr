#
# This worked for me:
# - Verify Ruby is 1.9.3 or 2.0.0 or greater: ruby --version
# - sudo gem install bundler
# - https://developer.apple.com/downloads/index.action —> in the left toolbar, search for command line tools
# - ...and download + install the version for your Mac
# - From the directory in which you find this file, run: bundle install
# - And finally execute: jekyll serve --watch --baseurl=
# - The site is available at https://localhost:4000

source 'https://rubygems.org'

require 'json'
require 'open-uri'
versions = JSON.parse(open('https://pages.github.com/versions.json').read)

gem 'github-pages', versions['github-pages']
