# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an academic personal website built with Jekyll and hosted on GitHub Pages. It's forked from the [Academic Pages template](https://github.com/academicpages/academicpages.github.io), which is based on the Minimal Mistakes theme.

## Development Commands

### Local Development
- **Start local server**: `bundle exec jekyll serve` or `bundle exec jekyll liveserve` (auto-rebuilds on changes)
- **Install dependencies**: `bundle install`
- **Clean directory**: `bundle clean`

### Asset Building
- **Build JavaScript**: `npm run build:js` or `npm run uglify`
- **Watch JavaScript changes**: `npm run watch:js`

## Site Architecture

### Content Structure
- `_pages/`: Main site pages (about, CV, publications, etc.)
- `_posts/`: Blog posts with date-based naming (YYYY-MM-DD-title.md)
- `_publications/`: Academic publications with metadata
- `_talks/`: Conference talks and presentations
- `_teaching/`: Teaching experience entries
- `_portfolio/`: Portfolio items
- `files/`: Static files (PDFs, images, etc.) served at `/files/`
- `images/`: Site images and media assets

### Configuration
- `_config.yml`: Main Jekyll configuration with site metadata, author info, and build settings
- `_config.dev.yml`: Development-specific overrides
- `_data/`: Site data files (navigation, UI text, author info)

### Styling and Assets
- `_sass/`: SCSS stylesheets organized by component
- `assets/`: Compiled CSS, JavaScript, and fonts
- Theme uses Minimal Mistakes with academic customizations

### Content Generation
- `markdown_generator/`: Python scripts and Jupyter notebooks for generating markdown from TSV data
  - Publications can be generated from BibTeX or TSV
  - Talks can be batch-generated from structured data
  - Use these scripts when adding multiple entries at once

## Key Features

### Collections
The site uses Jekyll collections for different content types:
- Publications with custom permalinks and metadata
- Talks with location mapping capabilities
- Teaching entries with course information
- Portfolio items for project showcases

### Academic Features
- Author profile with social links and institutional affiliation
- Citation and publication management
- Talk mapping (when `talkmap_link: true` in config)
- CV generation from structured data

## Development Notes

- Site uses GitHub Pages compatible plugins only
- Ruby dependencies managed via Bundler
- JavaScript assets are uglified for production
- Markdown processing via Kramdown with GFM input
- Future posts enabled for scheduling content

## Common File Patterns

- Blog posts: `_posts/YYYY-MM-DD-title.md`
- Publications: `_publications/YYYY-MM-DD-title.md`
- Static files: Place in `files/` directory for public access
- Images: Use `images/` directory with descriptive names