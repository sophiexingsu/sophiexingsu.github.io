# Research Project Files

This directory contains papers, posters, supplementary materials, datasets, and **featured images** for research projects.

## Featured Project Images (Homepage & Portfolio)

These image files appear in the interactive cards on your homepage and portfolio page:

- **`gaze-mental-representations.gif`** - Mental Representations from Gaze project card
- **`predictive-looking.gif`** - Predictive Looking & Event Segmentation project card
- **`incremental-global-updating.gif`** - Incremental vs. Global Updating project card

### How to Swap Project Images

To replace any project image:

1. **Replace the file directly**:
   ```bash
   cp /path/to/your/new-visualization.gif gaze-mental-representations.gif
   ```

2. **Use a different format** (JPG, PNG, SVG are all supported):
   ```bash
   # Just rename your file to match the expected name
   cp /path/to/your/new-image.png gaze-mental-representations.gif
   ```

3. **Recommended specs**: 800x600px or 16:9 aspect ratio, under 2MB file size

## Directory Structure

- `gaze-entropy/` - Gaze entropy and event boundaries project
  - Papers, supplementary materials

- `predictive-looking/` - Predictive looking errors project
  - Published paper PDFs, supplementary figures

- `action-segmentation/` - Action segmentation and memory project
  - Analysis outputs, supplementary materials

- `gaze-clip/` - Mental representations (CLIP + Gaze) project
  - VSS 2025 poster, presentation materials

## Usage

To link to files in project pages:

```markdown
[Download Paper](/files/projects/project-name/paper.pdf)
```

Or in front matter:

```yaml
publications:
  - title: "Paper Title"
    url: /files/projects/project-name/paper.pdf
```

## File Guidelines

- Use descriptive filenames
- Keep file sizes reasonable for web delivery
- Include version numbers or dates for materials that may be updated
- For large datasets, consider using external hosting (OSF, GitHub releases)
