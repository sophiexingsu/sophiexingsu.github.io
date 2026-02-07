# Human Movement Analysis Dashboard

A static web dashboard for visualizing pose estimation and movement analysis data. This dashboard runs entirely in the browser and can be hosted on GitHub Pages.

## Live Demo

Once deployed, the dashboard will be available at:
`https://sophiexingsu.github.io/files/projects/movement-dashboard/`

## Features

- **Skeleton Visualization**: Animated playback of body joint positions
- **Joint Position Charts**: Track joint movements over time with Plotly.js
- **Movement Timeline**: Visualize movement intensity throughout the action
- **Trajectory Plots**: See how joints move through 2D space

## Files

```
movement-dashboard/
├── index.html              # Main dashboard (static HTML/JS)
├── data/                   # Pre-processed JSON data
│   ├── index.json          # Data structure index
│   └── study2/             # Study data
│       └── [participant]/  # Participant folders
│           └── [action].json
├── preprocess_simple.py    # Script to generate JSON from CSVs
├── preprocess_data.py      # Full preprocessing (requires pandas)
└── README.md
```

## How It Works

The original Python Dash dashboard required a server to run. This version:

1. **Pre-processes data**: Converts CSV pose data to JSON files
2. **Runs in browser**: Uses Plotly.js (same charts as Dash, but client-side)
3. **No server needed**: Works on static hosting like GitHub Pages

## Adding More Data

To add more data to the dashboard:

1. Run the preprocessing script locally:
   ```bash
   python3 preprocess_simple.py
   ```

2. Or use the full script (requires pandas):
   ```bash
   python3 preprocess_data.py --max-participants 10 --max-actions 10
   ```

3. The scripts will read from the original data location and create JSON files in `./data/`

4. Commit the new JSON files and push to GitHub

## Customization

### Adding More Studies

Edit `preprocess_simple.py` to include additional studies:

```python
for study in ['study1', 'study2', 'study3', 'study4']:
```

### Changing Data Limits

Adjust the slicing in the preprocessing script:
- `[:3]` for participants
- `[:5]` for actions per participant
- `[:50]` for frames per action

## Deployment to GitHub Pages

The files are already in the correct location. To deploy:

1. Commit all files including the `data/` folder:
   ```bash
   git add files/projects/movement-dashboard/
   git commit -m "Add movement analysis dashboard"
   git push
   ```

2. Ensure GitHub Pages is enabled in your repository settings

3. The dashboard will be available at your GitHub Pages URL

## Technical Notes

- Data is sampled (every 5th frame) to reduce file sizes
- JSON files are limited to 50 time points for performance
- Plotly.js is loaded from CDN for faster page loads
- Bootstrap 5 is used for styling

## Original Dashboard

The original Dash-based dashboard (`movement-analysis-dashboard-python.py`) requires:
- Python with Dash, Plotly, OpenCV, MediaPipe
- Local access to video files and CSV data
- A running Python server

This static version provides the same visualizations without those requirements.
