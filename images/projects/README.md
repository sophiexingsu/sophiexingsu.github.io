# Research Project Images

This directory contains images and visualizations for research project pages.

## Directory Structure

- `gaze-entropy/` - Gaze entropy and event boundaries project
  - Hero images, entropy plots, timeline visualizations

- `predictive-looking/` - Predictive looking errors project
  - Gaze heatmaps, density maps, segmentation probability curves

- `action-segmentation/` - Action segmentation and memory project
  - Video stimuli thumbnails, performance metrics plots

- `gaze-clip/` - Mental representations (CLIP + Gaze) project
  - Gaze heatmaps, CLIP embedding visualizations

- `sem-model/` - SEM2 computational model project
  - Architecture diagrams, model output visualizations

## Usage

To use images in project pages, reference them with relative paths:

```markdown
![Description](../images/projects/project-name/image.png)
```

Or in front matter:

```yaml
header:
  teaser: /images/projects/project-name/teaser.jpg
```

## Image Guidelines

- Use descriptive filenames (e.g., `entropy-plot-01.png`, not `image1.png`)
- Optimize images for web (compress, reasonable dimensions)
- Include hero images (~1200x400px) for project banners
- Include teaser images (~500x300px) for archive cards
