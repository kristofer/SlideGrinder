# Examples

This directory contains example files for testing SlideGrinder.

## Sample PDF

The `sample.pdf` file contains a sample article about machine learning that can be used to test the tool.

## Usage

```bash
# Generate slides from the sample PDF
python slidegrinder.py examples/sample.pdf

# Generate slides with custom options
python slidegrinder.py examples/sample.pdf -o my_slides -n 8

# Generate only HTML output
python slidegrinder.py examples/sample.pdf -f html
```

## Expected Output

Running SlideGrinder on the sample PDF should generate approximately 5-8 slides covering:
- Introduction to Machine Learning
- Key Concepts (Supervised, Unsupervised, Reinforcement Learning)
- Applications (NLP, Computer Vision, Recommendations)
- Challenges (Data Quality, Overfitting, Resources)
- Future Trends (Deep Learning, AutoML)
